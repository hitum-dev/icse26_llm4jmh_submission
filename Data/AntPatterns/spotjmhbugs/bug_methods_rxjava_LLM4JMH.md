## JMH IGNORED METHOD RETURN - Method return not used or consumed by a Blackhole.

### Method 1

```java
/* --------------------------------------------------------------------- */
/*  Multi‑threaded benchmarks (multiple producers, single consumer)      */
/* --------------------------------------------------------------------- */
@Benchmark
// 3 producers + 1 consumer
@Threads(4)
public void multiProducerSingleConsumer(SharedState state, Blackhole bh) {
    // Thread 0 acts as the consumer, others as producers.
    int threadId = (int) Thread.currentThread().getId();
    if (threadId % 4 == 0) {
        // Consumer
        Integer v = state.queue.poll();
        if (v != null) {
            bh.consume(v);
        }
    } else {
        // Producer
        state.queue.offer(threadId);
    }
}
```

### Method 2

```java
/* --------------------------------------------------------------------- */
/*  Single‑threaded benchmarks                                            */
/* --------------------------------------------------------------------- */
@Benchmark
@Threads(1)
public void singleThreadOffer(ThreadState state) {
    state.queue.offer(state.nextValue());
}
```

### Method 3

```java
/* --------------------------------------------------------------------- */
/* Helper benchmark that repeatedly schedules a batch of tasks.         */
/* This mimics a realistic usage pattern where many tasks are queued.   */
/* --------------------------------------------------------------------- */
@Benchmark
public void scheduleBatchOfTasks(Blackhole bh) {
    // Schedule a small batch (e.g., 10 tasks) to amortize loop overhead.
    for (int i = 0; i < 10; i++) {
        worker.schedule(() -> bh.consume(counter.incrementAndGet()));
    }
}
```

### Method 4

```java
/**
 * Baseline benchmark without the scan operator to help isolate its overhead.
 */
@Benchmark
public void baselineThroughput(Blackhole bh) {
    source.subscribe(bh::consume);
}
```

### Method 5

```java
/**
 * Benchmark method that pushes a batch of items through the {@code onBackpressureDrop}
 * operator and consumes them via {@link Blackhole}.
 *
 * @param state shared benchmark state
 * @param bh    Blackhole to consume items and prevent dead‑code elimination
 */
@Benchmark
public void backpressureDropThroughput(BenchmarkState state, Blackhole bh) {
    // Emit a batch of items; the operator will drop none because the subscriber
    // requests Long.MAX_VALUE.
    state.emitBatch();
    // Drain the subscriber's internal queue by consuming all items that have arrived.
    // Since the subscriber does not store items, we rely on the fact that the
    // Flowable's internal mechanisms will deliver items to the Blackhole via the
    // onNext hook we set up in the subscriber.
    // To make the consumption visible to JMH, we subscribe a temporary consumer
    // that forwards to Blackhole.
    state.source.subscribe(bh::consume);
}
```

### Method 6

```java
/**
 * Benchmark method that replays the cached sequence to a new subscriber.
 * The {@link TestObserver} waits until the sequence terminates, ensuring that
 * the whole replay path is exercised.
 */
@Benchmark
public void replayThroughput() throws Exception {
    TestObserver<Integer> testObserver = new TestObserver<>();
    cache.subscribe(testObserver);
    // Await completion; the timeout is generous to avoid false failures.
    testObserver.awaitDone(1, TimeUnit.MINUTES);
}
```

### Method 7

```java
/**
 * Benchmark method that schedules a delayed action (1 ms) on the SchedulerWhen.
 */
@Benchmark
public Disposable scheduleDelayed(Blackhole bh) {
    SchedulerWhen.Worker worker = schedulerWhen.createWorker();
    Disposable d = worker.schedule(NOOP, 1, TimeUnit.MILLISECONDS);
    counter.incrementAndGet();
    bh.consume(d);
    worker.dispose();
    return d;
}
```

### Method 8

```java
/**
 * Benchmark method that schedules an immediate no‑op action on the SchedulerWhen.
 */
@Benchmark
public Disposable scheduleImmediate(Blackhole bh) {
    SchedulerWhen.Worker worker = schedulerWhen.createWorker();
    Disposable d = worker.schedule(NOOP);
    counter.incrementAndGet();
    bh.consume(d);
    worker.dispose();
    return d;
}
```

### Method 9

```java
/**
 * Benchmark method that subscribes to the Flowable and consumes all items.
 *
 * @param bh Blackhole to consume values and avoid dead‑code elimination.
 */
@Benchmark
public void concatAndConsume(Blackhole bh) {
    // Use TestSubscriber to request all items and await completion.
    TestSubscriber<Integer> ts = new TestSubscriber<>(Long.MAX_VALUE);
    flowable.subscribe(ts);
    // Ensure the subscription has completed before returning.
    ts.awaitDone(5, TimeUnit.SECONDS);
    // Consume the received items via Blackhole.
    for (Integer v : ts.values()) {
        bh.consume(v);
    }
}
```

### Method 10

```java
/**
 * Benchmark method that subscribes to the FlowableMapOptional,
 * consumes all emitted items, and blocks until completion.
 *
 * @param bh Blackhole to consume emitted items and avoid dead‑code elimination.
 */
@Benchmark
public void mapOptionalThroughput(Blackhole bh) {
    flowableUnderTest.subscribe(bh::consume);
    // The subscription is synchronous for the range source, so no explicit
    // blocking is required. If an asynchronous source were used, one would
    // need to block (e.g., using blockingSubscribe()).
}
```

### Method 11

```java
/**
 * Benchmark method that subscribes to the filtered Observable and consumes all items.
 *
 * @param bh Blackhole to consume the emitted items and avoid dead‑code elimination.
 */
@Benchmark
public void filterAndConsume(Blackhole bh) {
    source.filter(predicate).subscribe(bh::consume);
}
```

### Method 12

```java
/**
 * Benchmark that applies the {@code window} operator and then flattens the
 * windows back into a single stream, consuming each element with a Blackhole.
 *
 * The flattening step ensures that the benchmark measures the full cost of
 * window creation, emission, and completion.
 */
@Benchmark
public void windowAndFlatten(Blackhole bh) {
    source.window(count, skip, capacityHint).flatMap(w -> w).subscribe(bh::consume, bh::consume, () -> {
    });
}
```

### Method 13

```java
/**
 * Benchmark that creates a fresh {@link Stream}, wraps it into an {@link ObservableFromStream},
 * subscribes with a {@link TestObserver}, and blocks until completion.
 *
 * The use of a fresh Stream per invocation ensures that the benchmark measures the
 * full cost of stream creation, iterator acquisition, emission, and resource cleanup.
 *
 * @return a {@link TestObserver} that has completed the subscription.
 */
@Benchmark
public TestObserver<Integer> subscribeAndConsume() {
    // Create a new Stream for each benchmark iteration.
    Stream<Integer> stream = sourceList.stream();
    // Wrap the Stream into the Observable under test.
    Observable<Integer> observable = new ObservableFromStream<>(stream);
    // Use TestObserver to subscribe and await terminal event.
    TestObserver<Integer> observer = new TestObserver<>();
    observable.subscribe(observer);
    observer.awaitDone(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
    // The observer now holds the consumed items; returning it prevents dead‑code elimination.
    return observer;
}
```

### Method 14

```java
/**
 * Benchmark that measures the combined latency of a single offer‑followed‑by‑poll
 * pair executed by the same thread. Useful for single‑threaded baseline.
 */
@Benchmark
@GroupThreads(1)
@Group("singleThread")
public Integer offerAndPoll() {
    queue.offer(ELEMENT);
    return queue.poll();
}
```

### Method 15

```java
/**
 * Benchmark that repeatedly adds and removes observers.
 * The subject is kept in a terminated state to avoid the cost of emission.
 */
@Benchmark
public void addRemoveObservers() {
    // Create a fresh observer for each iteration to simulate realistic usage
    NoOpObserver<Integer> tempObserver = new NoOpObserver<>();
    MaybeSubject.MaybeDisposable<Integer> md = new MaybeSubject.MaybeDisposable<>(tempObserver, subject);
    // Directly add without going through subscribeActual to isolate add/remove cost
    subject.add(md);
    // Immediately remove
    subject.remove(md);
}
```

### Method 16

```java
/**
 * Benchmark that subscribes to the scanned Observable and consumes all emitted items.
 * The subscription runs synchronously because the source is a cold, non‑async Observable.
 */
@Benchmark
public void scanThroughput(Blackhole bh) {
    source.scan(accumulator).subscribe(bh::consume);
}
```

### Method 17

```java
/**
 * Benchmark the concatMap operator in its default (IMMEDIATE error) mode.
 *
 * @param bh Blackhole to consume the emitted items and avoid dead‑code elimination.
 */
@Benchmark
public void concatMapThroughput(Blackhole bh) {
    source.concatMap(mapper).subscribe(bh::consume);
}
```

### Method 18

```java
/**
 * Benchmark the cost of delivering a normal onNext signal.
 */
@Benchmark
public void onNext() {
    subscriber.onNext(42);
    // Drain the queue to keep it from growing unboundedly.
    queue.poll();
}
```

### Method 19

```java
/**
 * Benchmark the cost of delivering an onComplete signal.
 */
@Benchmark
public void onComplete() {
    subscriber.onComplete();
    queue.poll();
}
```

### Method 20

```java
/**
 * Benchmark the cost of delivering an onError signal.
 */
@Benchmark
public void onError() {
    subscriber.onError(new RuntimeException("test"));
    queue.poll();
}
```

### Method 21

```java
/**
 * Benchmark the error path where the source emits more than one element.
 * The operator should terminate with an {@link IllegalArgumentException}.
 * The exception is caught to keep the benchmark running.
 */
@Benchmark
public void multipleElementsError() {
    Single<Integer> single = new FlowableSingleSingle<>(multiElementSource, null);
    try {
        single.blockingGet();
    } catch (IllegalArgumentException ignored) {
        // Expected – the operator signals an error when more than one element is observed.
    }
}
```

### Method 22

```java
/**
 * Benchmark the error‑path execution of {@link MaybeDelay}
 * with {@code delayError = true}.
 */
@Benchmark
public void delayError(Blackhole bh) {
    try {
        // blockingGet throws the upstream error; we capture it to avoid benchmark failure.
        delayWithError.blockingGet();
    } catch (Throwable ex) {
        bh.consume(ex);
    }
}
```

### Method 23

```java
/**
 * Benchmark the flatMap operator in throughput mode.
 *
 * @param bh Blackhole to consume the emitted items and prevent dead-code elimination.
 */
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
public void flatMapThroughput(Blackhole bh) {
    source.flatMap(mapper, delayErrors, maxConcurrency, bufferSize).subscribe(bh::consume);
}
```

### Method 24

```java
/**
 * Benchmark the fused async mode (queue‑style) where the downstream
 * pulls the value via {@link #poll()} after a request.
 *
 * This exercises the {@code requestFusion}, {@code poll}, and state
 * transitions specific to the fused path.
 */
@Benchmark
public void fusedAsyncPoll(Blackhole bh) {
    // Enable async fusion.
    subscription.requestFusion(DeferredScalarSubscription.ASYNC);
    // Complete the subscription (value will be stored in fused state).
    subscription.complete(value);
    // Pull the value via poll().
    Integer v = subscription.poll();
    bh.consume(v);
}
```

### Method 25

```java
/**
 * Benchmark the map operator when the downstream implements {@link io.reactivex.rxjava3.operators.ConditionalSubscriber}.
 * RxJava's {@code Flowable.map} detects ConditionalSubscriber and uses the optimized path.
 */
@Benchmark
public void mapConditionalSubscriber(Blackhole bh) {
    // ConditionalSubscriber is exercised via the internal TestSubscriber which implements it.
    subscriber.cancel();
    subscriber = new TestSubscriber<>();
    // forces a ConditionalSubscriber downstream
    // forces a ConditionalSubscriber downstream
    source.map(mapper).filter(v -> true).subscribe(subscriber);
    subscriber.awaitDone(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
    bh.consume(subscriber.values().size());
}
```

### Method 26

```java
/**
 * Benchmark the map operator with a regular Subscriber.
 */
@Benchmark
public void mapRegularSubscriber(Blackhole bh) {
    // Reset the subscriber to avoid state leakage between iterations.
    subscriber.cancel();
    subscriber = new TestSubscriber<>();
    // the operator under test
    // the operator under test
    source.// subscribe with a regular subscriber
    map(// subscribe with a regular subscriber
    mapper).subscribe(subscriber);
    // Ensure all items are consumed; block until termination.
    subscriber.awaitDone(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
    // Consume the result to prevent dead‑code elimination.
    bh.consume(subscriber.values().size());
}
```

### Method 27

```java
/**
 * Benchmark the success path (no disposal) for comparison.
 *
 * This measures the overhead of the operator when the stream completes normally.
 */
@Benchmark
public void successPath(Blackhole bh) {
    // Subscribe and let the Single emit its value.
    // onSuccess
    doOnDisposeSingle.// onSuccess
    subscribe(// onError
    bh::consume, bh::consume);
    // No explicit dispose – the upstream disposes itself after onSuccess.
}
```

### Method 28

```java
/**
 * Benchmark the switchMap operator in a hot chain.
 *
 * @param bh Blackhole to consume the downstream values.
 */
@Benchmark
public void switchMapThroughput(Blackhole bh) {
    source.compose(upstream -> new FlowableSwitchMap<>((Flowable<Integer>) upstream, mapper, bufferSize, delayErrors)).subscribe(new Consumer<Integer>() {

        @Override
        public void accept(Integer value) {
            // Consume the value via Blackhole to prevent dead‑code elimination.
            bh.consume(value);
        }
    });
}
```

### Method 29

```java
/**
 * Benchmark the throughput of {@link FlowableMapNotification} in the normal onNext path.
 *
 * @param bh Blackhole to consume the downstream values and prevent dead‑code elimination.
 */
@Benchmark
public void mapNotificationThroughput(Blackhole bh) {
    // Create the operator instance with the prepared mappers.
    Flowable<Integer> mapped = new FlowableMapNotification<>(source, onNextMapper, onErrorMapper, onCompleteSupplier);
    // Subscribe and consume all items; the subscription is synchronous for the range source.
    mapped.subscribe(bh::consume);
}
```

### Method 30

```java
/**
 * Benchmark the timeout operator with a fallback Observable.
 * The timeout indicator never fires, so the fallback is never used.
 */
@Benchmark
public void timeoutWithFallback(Blackhole bh) {
    source.timeout(neverTimeout, i -> neverTimeout, fallback).subscribe(bh::consume, bh::consume);
}
```

### Method 31

```java
/**
 * Benchmark the timeout operator without a fallback.
 * The timeout indicator never fires, so the operator should behave like a pass‑through.
 */
@Benchmark
public void timeoutWithoutFallback(Blackhole bh) {
    source.timeout(neverTimeout, i -> neverTimeout).subscribe(bh::consume, bh::consume);
}
```

### Method 32

```java
/**
 * Benchmark the {@code remove} operation.
 */
@Benchmark
public boolean remove() {
    // Ensure the disposable is present before removal.
    composite.add(reusableDisposable);
    return composite.remove(reusableDisposable);
}
```

### Method 33

```java
/**
 * Benchmark the {@code switchIfEmpty} operator when the upstream Observable is empty.
 *
 * <p>The fallback Observable is subscribed after the upstream completes.
 */
@Benchmark
public void switchIfEmpty_Empty(Blackhole bh) {
    emptySource.switchIfEmpty(fallback).subscribe(bh::consume);
}
```

### Method 34

```java
/**
 * Benchmark the {@code switchIfEmpty} operator when the upstream Observable is non‑empty.
 *
 * <p>The fallback Observable should never be subscribed.
 */
@Benchmark
public void switchIfEmpty_NonEmpty(Blackhole bh) {
    nonEmptySource.switchIfEmpty(fallback).subscribe(bh::consume);
}
```

### Method 35

```java
/**
 * Benchmark the {@code takeWhile} operator when the predicate never stops the stream.
 * This measures the steady‑state overhead of the operator.
 */
@Benchmark
public void takeWhileAlwaysTrue(BenchmarkState state, Blackhole bh) {
    state.takeWhileAlwaysTrue.subscribe(bh::consume);
}
```

### Method 36

```java
/**
 * Benchmark the {@code takeWhile} operator when the predicate stops the stream early.
 * This measures the cost of early termination logic.
 */
@Benchmark
public void takeWhileEarlyStop(BenchmarkState state, Blackhole bh) {
    state.takeWhileEarlyStop.subscribe(bh::consume);
}
```

### Method 37

```java
/**
 * Benchmark where the source completes before the timeout can fire.
 * The source {@code fastSource} emits a value immediately, the timeout {@code neverTimeout}
 * never emits, so the fallback is never used.
 */
@Benchmark
public void noTimeout(Blackhole bh) {
    Maybe<Integer> timeoutOperator = new MaybeTimeoutPublisher<>(fastSource, neverTimeout, fallback);
    TestObserver<Integer> to = new TestObserver<>();
    timeoutOperator.subscribe(to);
    to.awaitDone(5, TimeUnit.SECONDS);
    bh.consume(to.values());
}
```

### Method 38

```java
/**
 * Benchmark where the timeout fires and the fallback Maybe is subscribed.
 * The source {@code neverSource} never completes, the timeout {@code immediateTimeout}
 * emits right away, causing the fallback {@code fallback} to be subscribed.
 */
@Benchmark
public void timeoutWithFallback(Blackhole bh) {
    Maybe<Integer> timeoutOperator = new MaybeTimeoutPublisher<>(neverSource, immediateTimeout, fallback);
    TestObserver<Integer> to = new TestObserver<>();
    timeoutOperator.subscribe(to);
    to.awaitDone(5, TimeUnit.SECONDS);
    bh.consume(to.values());
}
```

### Method 39

```java
/**
 * Benchmark where the upstream Maybe emits a value.
 *
 * @param bh Blackhole to consume the emitted value and prevent dead‑code elimination.
 */
@Benchmark
public void switchIfEmpty_ValuePresent(Blackhole bh) {
    maybeWithValue.subscribe(bh::consume);
}
```

### Method 40

```java
/**
 * Benchmark where the upstream Maybe is empty and the operator switches to the fallback.
 *
 * @param bh Blackhole to consume the emitted value from the fallback.
 */
@Benchmark
public void switchIfEmpty_EmptySwitches(Blackhole bh) {
    maybeEmptySwitch.subscribe(bh::consume);
}
```

### Method 41

```java
/**
 * Benchmark where the upstream emits items, so the fallback is never used.
 */
@Benchmark
public void switchIfEmpty_NonEmptySource(Blackhole bh) {
    subscriber = new TestSubscriber<>();
    nonEmptySource.switchIfEmpty(fallback).subscribe(subscriber);
    subscriber.awaitDone(1, TimeUnit.MINUTES);
    bh.consume(subscriber.values());
}
```

### Method 42

```java
/**
 * Benchmark where the upstream is empty and the operator switches to the fallback.
 */
@Benchmark
public void switchIfEmpty_EmptySource(Blackhole bh) {
    subscriber = new TestSubscriber<>();
    emptySource.switchIfEmpty(fallback).subscribe(subscriber);
    // Consume all items to ensure the pipeline runs to completion.
    subscriber.awaitDone(1, TimeUnit.MINUTES);
    // Use Blackhole to prevent dead‑code elimination.
    bh.consume(subscriber.values());
}
```

### Method 43

```java
/**
 * Consumes the Flowable with {@code doAfterNext} operator.
 *
 * @param bh Blackhole to consume the emitted items.
 */
@Benchmark
public void doAfterNextConsume(Blackhole bh) {
    withDoAfterNext.subscribe(bh::consume);
}
```

### Method 44

```java
/**
 * Consumes the baseline Flowable.
 *
 * @param bh Blackhole to consume the emitted items.
 */
@Benchmark
public void baselineConsume(Blackhole bh) {
    baseline.subscribe(bh::consume);
}
```

### Method 45

```java
/**
 * Consumes the entire sequence produced by the {@code takeUntil} operator.
 *
 * @param state shared benchmark state containing the prepared Flowable
 * @param bh    Blackhole to consume each emitted item
 */
@Benchmark
public void takeUntilThroughput(BenchmarkState state, Blackhole bh) {
    // Subscribe with a consumer that forwards each item to the Blackhole.
    // The subscription requests an unbounded amount (Long.MAX_VALUE) internally.
    state.flowable.subscribe(bh::consume);
}
```

### Method 46

```java
/**
 * Consumes the entire stream and feeds each item into the Blackhole.
 * The Blackhole prevents dead‑code elimination.
 */
@Benchmark
public void peekThroughput(Blackhole bh) {
    // Convert back to a sequential Flowable, then block and consume.
    peekOperator.sequential().subscribe(bh::consume);
    // Ensure the subscription has completed before returning.
    // The sequential Flowable blocks until termination.
    // No additional synchronization is required because the
    // subscription runs on the computation scheduler and the
    // main thread waits for completion.
}
```

### Method 47

```java
/**
 * Exact buffering: size == skip.
 */
@Benchmark
public void exactBuffer(Blackhole bh) {
    source.buffer(size).subscribe(bh::consume, t -> bh.consume(t), () -> {
    });
}
```

### Method 48

```java
/**
 * Executes the benchmark. The subscription is performed for each iteration,
 * and emitted items are consumed by the {@link Blackhole} to avoid dead‑code
 * elimination.
 *
 * @param bh Blackhole to consume items and terminal signals.
 */
@Benchmark
public void runTimeoutOperator(Blackhole bh) {
    // onNext
    flowable.// onNext
    subscribe(// onError
    bh::consume, // onComplete (no value to consume)
    bh::consume, () -> {
    });
}
```

### Method 49

```java
/**
 * Executes the flatMap operation and consumes all emitted items.
 *
 * @param bh Blackhole to consume the items and prevent dead‑code elimination.
 */
@Benchmark
public void flatMapObservable(Blackhole bh) {
    source.flatMapObservable(mapper).subscribe(bh::consume);
}
```

### Method 50

```java
/**
 * Executes the merge operation and blocks until termination.
 *
 * @param state the benchmark state containing the prepared operator
 * @return a {@link TestObserver} that has received the terminal event
 */
@Benchmark
public TestObserver<Void> mergeAndAwait(BenchmarkState state) {
    TestObserver<Void> testObserver = new TestObserver<>();
    // Subscribe the test observer to the operator
    state.operator.subscribe(testObserver);
    // Block until the merge completes (or errors). This is safe because all inner
    // completables are synchronous and complete immediately.
    testObserver.awaitDone(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
    // Return the observer to prevent dead‑code elimination.
    return testObserver;
}
```

### Method 51

```java
/**
 * Executes the switchMap pipeline and consumes all emitted items.
 *
 * @param bh Blackhole to consume items and avoid dead‑code elimination.
 */
@Benchmark
public void switchMapThroughput(Blackhole bh) {
    // Subscribe synchronously; Observable.range and switchMap run on the calling thread.
    switched.subscribe(bh::consume);
}
```

### Method 52

```java
/**
 * Executes the {@code SingleFlatMapIterableObservable} pipeline and consumes all
 * emitted items with a {@link Blackhole}.
 *
 * @param bh Blackhole used to consume the items and avoid dead‑code elimination.
 */
@Benchmark
public void flatMapIterable(Blackhole bh) {
    Observable<Integer> observable = new SingleFlatMapIterableObservable<>(source, mapper);
    observable.subscribe(bh::consume);
}
```

### Method 53

```java
/**
 * Executes the {@code flatMapIterable} operator and consumes all emitted items.
 *
 * @param bh Blackhole to consume the items and prevent dead‑code elimination.
 */
@Benchmark
public void flatMapIterable(Blackhole bh) {
    observable.subscribe(bh::consume, bh::consume, () -> {
    });
}
```

### Method 54

```java
/**
 * Measures how many scan operations can be performed per second.
 *
 * @param bh Blackhole to consume emitted items and prevent dead‑code elimination.
 */
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
public void scanThroughput(Blackhole bh) {
    // Subscribe synchronously; the upstream is finite and completes quickly.
    source.scan(ACCUMULATOR).subscribe(bh::consume);
}
```

### Method 55

```java
/**
 * Measures the throughput when the {@code other} Publisher emits immediately,
 * causing the operator to cancel the upstream Single.
 */
@Benchmark
public void takeUntilCancelled(Blackhole bh) {
    TestObserver<Integer> observer = new TestObserver<>();
    cancelOperator.subscribe(observer);
    observer.awaitDone(5, TimeUnit.SECONDS);
    // Consume a simple state flag to prevent dead‑code elimination.
    bh.consume(observer.isDisposed());
}
```

### Method 56

```java
/**
 * Measures the throughput when the {@code other} Publisher never emits,
 * allowing the upstream Single to complete normally.
 */
@Benchmark
public void takeUntilSuccess(Blackhole bh) {
    TestObserver<Integer> observer = new TestObserver<>();
    successOperator.subscribe(observer);
    observer.awaitDone(5, TimeUnit.SECONDS);
    bh.consume(observer.values());
}
```

### Method 57

```java
/**
 * Overlapping buffering: skip < size.
 */
@Benchmark
public void overlappingBuffer(Blackhole bh) {
    source.buffer(size, skip).subscribe(bh::consume, t -> bh.consume(t), () -> {
    });
}
```

### Method 58

```java
/**
 * Skipping buffering: skip > size.
 */
@Benchmark
public void skipBuffer(Blackhole bh) {
    source.buffer(size, skip).subscribe(bh::consume, t -> bh.consume(t), () -> {
    });
}
```

### Method 59

```java
/**
 * Subscribe to the Completable and immediately dispose the subscription.
 * The onComplete and onError callbacks are no‑ops; errors are routed to a Blackhole
 * to avoid dead‑code elimination.
 *
 * @param bh Blackhole to consume any error that might be emitted.
 */
@Benchmark
public void subscribeAndDispose(Blackhole bh) {
    // Subscribe with empty onComplete and error consumer that feeds the Blackhole.
    completable.subscribe(() -> {
        /* onComplete – nothing to do */
    }, bh::consume);
}
```

### Method 60

```java
/**
 * Subscribe to the optimized Observable and consume the emitted value.
 * The {@link Blackhole} guarantees the value is observed by the JVM.
 */
@Benchmark
public void subscribeScalarXMapObservable(Blackhole bh) {
    ObservableScalarXMap.scalarXMap(42, scalarMapper).subscribe(bh::consume);
}
```

### Method 61

```java
/**
 * Subscribes to the Flowable and consumes every emitted item via a Blackhole.
 *
 * @param bh Blackhole to consume items and prevent dead‑code elimination.
 */
@Benchmark
public void doOnEachThroughput(Blackhole bh) {
    // onNext
    flowable.// onNext
    subscribe(// onError (should never happen)
    bh::consume, // onComplete (no‑op)
    bh::consume, () -> {
    });
}
```

### Method 62

```java
/**
 * Subscribes to the Flowable and consumes the emitted item.
 *
 * Each invocation creates a fresh subscription, which reflects the typical
 * usage pattern of the operator in real applications.
 *
 * @param bh Blackhole to consume the emitted value and avoid dead‑code elimination.
 */
@Benchmark
public void takeLastOne(Blackhole bh) {
    flowable.subscribe(bh::consume);
}
```

### Method 63

```java
/**
 * Subscribes to the Flowable and consumes the emitted value.
 *
 * The subscription is synchronous for {@code FlowableFromCallable}, so the method
 * returns only after the value has been emitted and the {@link Blackhole} has
 * consumed it.
 *
 * @param bh Blackhole to consume the emitted value and avoid dead‑code elimination.
 */
@Benchmark
public void subscribeAndConsume(Blackhole bh) {
    flowable.subscribe(bh::consume);
}
```

### Method 64

```java
/**
 * Subscribes to the ObservableRangeLong and drains all emitted items.
 * The Blackhole ensures that the emitted values are consumed and not optimized away.
 */
@Benchmark
public void rangeLongThroughput(BenchmarkState state, Blackhole bh) {
    state.observable.subscribe(bh::consume);
}
```

### Method 65

```java
/**
 * Subscribes to the dematerialized Flowable and drains all items.
 *
 * The {@link TestSubscriber} is used because it provides a lightweight way to
 * request all items and await completion without additional side effects.
 */
@Benchmark
public void dematerializeThroughput(Blackhole bh) {
    TestSubscriber<Integer> ts = new TestSubscriber<>(Integer.MAX_VALUE);
    dematerialized.subscribe(ts);
    // Wait for the upstream to finish; this is safe because the source is finite.
    ts.awaitDone(1, TimeUnit.SECONDS);
    // Consume the collected values to prevent dead‑code elimination.
    bh.consume(ts.values());
}
```

### Method 66

```java
/**
 * Subscribes to the observable and consumes all emitted items.
 *
 * @param bh Blackhole to consume items and avoid dead‑code elimination.
 */
@Benchmark
public void doOnLifecycleThroughput(Blackhole bh) {
    // onNext
    observable.// onNext
    subscribe(// onError
    bh::consume, // onComplete
    bh::consume, () -> bh.consume("complete"));
}
```

### Method 67

```java
/**
 * Subscribes to the {@link MaybeConcatIterable} and blocks until completion.
 *
 * The method returns the {@link TestSubscriber} to prevent dead‑code elimination.
 */
@Benchmark
public TestSubscriber<Integer> concatAndConsume() throws Exception {
    // Reset the subscriber to a clean state for each iteration.
    // ensure any previous subscription is disposed
    testSubscriber.cancel();
    testSubscriber = new TestSubscriber<>();
    concatFlowable.subscribe(testSubscriber);
    // Wait for the whole concatenated sequence to finish.
    testSubscriber.awaitDone(1, TimeUnit.MINUTES);
    // Verify that no error occurred (optional, can be omitted for pure throughput).
    testSubscriber.assertNoErrors();
    return testSubscriber;
}
```

### Method 68

```java
/**
 * Subscribes to the {@link MaybeConcatIterable} and blocks until completion.
 *
 * The method returns the {@link TestSubscriber} to prevent dead‑code elimination.
 */
@Benchmark
public TestSubscriber<Integer> concatAndConsume() throws Exception {
    // Reset the subscriber to a clean state for each iteration.
    // ensure any previous subscription is disposed
    testSubscriber.cancel();
    testSubscriber = new TestSubscriber<>();
    concatFlowable.subscribe(testSubscriber);
    // Wait for the whole concatenated sequence to finish.
    testSubscriber.awaitDone(1, TimeUnit.MINUTES);
    // Verify that no error occurred (optional, can be omitted for pure throughput).
    testSubscriber.assertNoErrors();
    return testSubscriber;
}
```

### Method 69

```java
// -----------------------------------------------------------------------
// Worker run loop – schedule a batch of tasks and let the worker drain them.
// This benchmark measures the cost of the runEager() loop.
// -----------------------------------------------------------------------
@Benchmark
public void workerRunEagerLoop(BenchmarkState state) {
    // schedule a small batch (e.g., 10 tasks) to be executed in the same run
    for (int i = 0; i < 10; i++) {
        state.worker.schedule(state.noop);
    }
    // The worker will automatically execute when tasks are queued.
    // No explicit call needed; the benchmark measures the time until all tasks are processed.
}
```

### Method 70

```java
@Benchmark
// 7 producers + 1 consumer
@Threads(8)
public void highContentionOffer(SharedState state) {
    // All threads perform offers; a separate consumer can be added in a different benchmark.
    state.queue.offer((int) Thread.currentThread().getId());
}
```

### Method 71

```java
@Benchmark
@Threads(1)
public void singleThreadOfferAndPoll(ThreadState state, Blackhole bh) {
    state.queue.offer(state.nextValue());
    Integer v = state.queue.poll();
    if (v != null) {
        bh.consume(v);
    }
}
```

### Method 72

```java
@Benchmark
public void addAllVarargs() {
    composite.addAll(disposables);
}
```

### Method 73

```java
@Benchmark
public void addSingle() {
    for (Disposable d : disposables) {
        composite.add(d);
    }
}
```

### Method 74

```java
@Benchmark
public void ambThroughput(Blackhole bh) throws Exception {
    TestSubscriber<Integer> ts = new TestSubscriber<>();
    ambFlowable.subscribe(ts);
    // Wait for the flowable to complete to ensure fair measurement.
    ts.awaitDone(5, TimeUnit.SECONDS);
    // Consume the emitted items to prevent dead‑code elimination.
    bh.consume(ts.values());
}
```

### Method 75

```java
@Benchmark
public void baseline(Blackhole bh) {
    plainSource.subscribe(bh::consume);
}
```

### Method 76

```java
@Benchmark
public void bufferBoundaryThroughput(Blackhole bh) throws InterruptedException {
    Flowable<List<Integer>> buffered = source.buffer(openPublisher, closeFunction, bufferSupplier);
    CountDownLatch latch = new CountDownLatch(1);
    // onNext
    buffered.// onNext
    subscribe(// onError
    bh::consume, // onComplete
    bh::consume, latch::countDown);
    latch.await();
}
```

### Method 77

```java
@Benchmark
public void bufferExactBoundary(Blackhole bh) {
    TestSubscriber<ArrayList<Integer>> ts = new TestSubscriber<>();
    new FlowableBufferExactBoundary<Integer, ArrayList<Integer>, Object>(source, boundary, bufferSupplier).subscribe(ts);
    // Wait for completion to ensure all work is done before consuming the result.
    ts.awaitDone(1, TimeUnit.MINUTES);
    // Consume the emitted buffers so that the JIT cannot dead‑code‑eliminate the operator.
    bh.consume(ts.values());
}
```

### Method 78

```java
@Benchmark
public void clear() {
    composite.addAll(disposables);
    composite.clear();
}
```

### Method 79

```java
@Benchmark
public void concatArrayDelayError(Blackhole bh) throws InterruptedException {
    CountDownLatch latch = new CountDownLatch(1);
    flowable.subscribe(new BenchmarkSubscriber(latch, bh));
    // Wait for the whole concatenation to finish.
    // A timeout guards against dead‑locks in case of bugs.
    latch.await(30, TimeUnit.SECONDS);
}
```

### Method 80

```java
@Benchmark
public void concatArrayThroughput() {
    concatArray.subscribe(subscriber);
    subscriber.awaitDone(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
    // Reset for the next benchmark iteration
    subscriber.cancel();
}
```

### Method 81

```java
@Benchmark
public void concatMapScheduler(Blackhole bh) {
    Flowable<Integer> flowable = new FlowableConcatMapScheduler<>(source, mapper, prefetch, errorMode, scheduler);
    flowable.subscribe(new Consumer<Integer>() {

        @Override
        public void accept(Integer value) {
            bh.consume(value);
        }
    }, bh::consume);
}
```

### Method 82

```java
@Benchmark
public void dispose() {
    composite.addAll(disposables);
    composite.dispose();
}
```

### Method 83

```java
@Benchmark
public void distinctThroughput(Blackhole bh) throws InterruptedException {
    CountDownLatch latch = new CountDownLatch(1);
    distinct.subscribe(bh::consume, bh::consume, latch::countDown);
    latch.await();
}
```

### Method 84

```java
@Benchmark
public void distinctThroughput(Blackhole bh) {
    distinctFlowable.subscribe(bh::consume);
}
```

### Method 85

```java
@Benchmark
public void distinctUntilChanged(Blackhole bh) {
    source.distinctUntilChanged(IDENTITY).subscribe(bh::consume, bh::consume, () -> {
    });
}
```

### Method 86

```java
@Benchmark
public void doFinallyThroughput(Blackhole bh) {
    // Subscribe with lambdas that forward all signals to the Blackhole.
    // onNext
    flowable.// onNext
    subscribe(// onError
    bh::consume, // onComplete (no‑op, as completion is already measured)
    bh::consume, () -> {
    });
}
```

### Method 87

```java
@Benchmark
public void doOnEach(Blackhole bh) {
    doOnEachSource.subscribe(bh::consume);
}
```

### Method 88

```java
@Benchmark
public void elementAtOutOfRangeNoDefault(BenchmarkState state, Blackhole bh) {
    try {
        state.elementAtOutOfRangeNoDefault.blockingGet();
    } catch (Throwable t) {
        // Expected error path; consume the exception to avoid dead‑code elimination.
        bh.consume(t);
    }
}
```

### Method 89

```java
@Benchmark
public void flatMapIterable(BenchmarkState state, Blackhole bh) {
    // Subscribe with a Consumer that forwards each item to the Blackhole.
    // The subscribe(Consumer) overload requests Long.MAX_VALUE internally,
    // ensuring the operator runs in an unbounded (fast‑path) mode.
    state.flowable.subscribe(bh::consume);
}
```

### Method 90

```java
@Benchmark
public void joinAndConsume() {
    TestObserver<Object> to = new TestObserver<>();
    leftSource.join(rightSource, leftEnd, rightEnd, resultSelector).subscribe(to);
    to.awaitDone(1, TimeUnit.MINUTES);
    to.assertNoErrors();
}
```

### Method 91

```java
@Benchmark
public void joinAndConsume() {
    TestObserver<Object> to = new TestObserver<>();
    leftSource.join(rightSource, leftEnd, rightEnd, resultSelector).subscribe(to);
    to.awaitDone(1, TimeUnit.MINUTES);
    to.assertNoErrors();
}
```

### Method 92

```java
@Benchmark
public void mapOptionalThroughput(Blackhole bh) {
    ParallelMapOptional<Integer, Integer> operator = new ParallelMapOptional<Integer, Integer>(source, mapper);
    operator.sequential().subscribe(bh::consume);
}
```

### Method 93

```java
@Benchmark
public void multipleElements(Blackhole bh) {
    // The operator should signal IllegalArgumentException.
    try {
        multipleElementsMaybe.blockingGet();
        // If no exception, consume a sentinel to avoid dead code elimination.
        bh.consume("no-error");
    } catch (IllegalArgumentException expected) {
        bh.consume(expected);
    } catch (Throwable t) {
        // Any other unexpected throwable is also consumed.
        bh.consume(t);
    }
}
```

### Method 94

```java
@Benchmark
public void onErrorReturnThroughput(Blackhole bh) {
    // onNext
    errorSource.onErrorReturn(fallbackSupplier).// onNext
    subscribe(// onError
    bh::consume, // onComplete (Action)
    bh::consume, () -> bh.consume("done"));
}
```

### Method 95

```java
@Benchmark
public void predicateThrows(Blackhole bh) {
    // Predicate throws an exception → the operator propagates the error.
    try {
        sourceError.all(throwsException).blockingGet();
    } catch (Throwable t) {
        // Expected path; consume to avoid dead‑code elimination.
        bh.consume(t);
    }
}
```

### Method 96

```java
@Benchmark
public void remove(Blackhole bh) {
    // fetch the next index to remove in a round‑robin fashion
    int idx = removalIndices[removePos];
    removePos = (removePos + 1) % removalIndices.length;
    // remove the element; to keep the set size stable we add it back
    boolean removed = set.remove(idx);
    // restore state for the next iteration
    set.add(idx);
    bh.consume(removed);
}
```

### Method 97

```java
@Benchmark
public void removeSingle() {
    // first fill the composite
    composite.addAll(disposables);
    // then remove one by one
    for (Disposable d : disposables) {
        composite.remove(d);
    }
}
```

### Method 98

```java
@Benchmark
public void removeSingle() {
    // first fill the composite
    composite.addAll(disposables);
    // then remove one by one
    for (Disposable d : disposables) {
        composite.remove(d);
    }
}
```

### Method 99

```java
@Benchmark
public void retryWhenThroughput(Blackhole bh) {
    TestSubscriber<Integer> ts = new TestSubscriber<>(0);
    retryWhenFlowable.subscribe(ts);
    ts.request(Long.MAX_VALUE);
    ts.awaitDone(5, TimeUnit.SECONDS);
    bh.consume(ts);
}
```

### Method 100

```java
@Benchmark
public void skipLastThroughput(BenchmarkState state, Blackhole bh) {
    state.source.skipLast(state.skip).subscribe(bh::consume);
}
```

### Method 101

```java
@Benchmark
public void subscribeAndConsume() {
    Observable<Integer> source = new ObservableFromCompletionStage<>(completedStage);
    TestObserver<Integer> testObserver = new TestObserver<>();
    source.subscribe(testObserver);
    // Ensure the emission is processed; timeout is generous for JMH stability
    testObserver.awaitDone(1, TimeUnit.SECONDS);
    // Optionally verify correctness (kept minimal to avoid affecting throughput)
    // testObserver.assertValue(VALUE).assertNoErrors().assertComplete();
}
```

### Method 102

```java
@Benchmark
public void subscribeAndConsume() {
    TestObserver<Integer> observer = new TestObserver<>();
    maybeUsing.subscribe(observer);
    observer.awaitDone(1, TimeUnit.SECONDS);
}
```

### Method 103

```java
@Benchmark
public void takeLastTimed(BenchmarkState state, Blackhole bh) {
    // Construct the internal operator directly (same package) to benchmark its exact behavior.
    new FlowableTakeLastTimed<>(state.source, state.count, state.timeMs, TimeUnit.MILLISECONDS, state.scheduler, state.bufferSize, state.delayError).subscribe(bh::consume, bh::consume, () -> {
    });
    // The subscription runs synchronously because we use the trampoline scheduler,
    // so the benchmark method returns only after all items have been processed.
}
```

### Method 104

```java
@Benchmark
public void takeLastTimedThroughput(BenchmarkState state, Blackhole bh) {
    // Build the operator instance directly to isolate its performance.
    ObservableTakeLastTimed<Integer> operator = new ObservableTakeLastTimed<>(state.source, state.count, state.timeMs, state.unit, state.scheduler, state.bufferSize, state.delayError);
    // Subscribe and consume all items, forcing the operator to drain.
    operator.subscribe(bh::consume);
}
```

### Method 105

```java
@Benchmark
public void timeoutWithoutFallback(Blackhole bh) {
    try {
        operatorTimeoutWithoutFallback.blockingGet();
        // Should not reach here; a TimeoutException is expected.
        bh.consume(false);
    } catch (Throwable t) {
        // The operator signals a TimeoutException as an error.
        if (t instanceof java.util.concurrent.TimeoutException) {
            bh.consume(true);
        } else {
            bh.consume(t);
        }
    }
}
```

### Method 106

```java
@Benchmark
public void windowBoundaryThroughput() {
    // Apply the window operator which internally uses FlowableWindowBoundary.
    source.window(boundary).subscribe(testSubscriber);
    // Wait for completion to ensure all windows are processed.
    testSubscriber.awaitDone(1, TimeUnit.MINUTES);
    // Reset for the next iteration.
    testSubscriber.cancel();
    testSubscriber = new TestSubscriber<>();
}
```

### Method 107

```java
@Benchmark
public void windowThroughput(Blackhole bh) {
    // Apply the window operator with the configured parameters.
    // The downstream flatMap flattens the windows back to items so that the
    // benchmark measures the cost of window creation, management, and emission.
    // flatten windows to individual items
    source.window(size, skip, bufferSize).// flatten windows to individual items
    flatMap(w -> w).subscribe(bh::consume, bh::consume, () -> {
    });
    // The subscription is synchronous for the range source, so the method
    // returns only after all items have been processed.
}
```

### Method 108

```java
@Benchmark
public void zipTwoSources(Blackhole bh) {
    Flowable.zip(Arrays.asList(source1, source2), zipper).subscribe(bh::consume);
}
```

## JMH FIXTURE USING INVOCATION SCOPE - Fixture methods configured with Invocation scope. 

### Method 1

```java
/**
 * Blackhole instance injected by JMH.
 */
@Setup(Level.Invocation)
public void setUp(Blackhole bh) {
    // Create a fresh subscription for each invocation to avoid state leakage.
    subscription = new DeferredScalarSubscription<>(new BlackholeSubscriber<>(bh));
}
```

### Method 2

```java
/**
 * Blackhole reference injected by JMH.
 */
@Setup(Level.Invocation)
public void setUp(Blackhole bh) {
    // Source Observable emitting a range of integers.
    Observable<Integer> source = Observable.range(1, itemCount);
    // Selector that maps each item to its double.
    Function<Observable<Integer>, ObservableSource<Integer>> selector = obs -> obs.map(i -> i * 2);
    // Create the ObservablePublishSelector instance.
    ObservablePublishSelector<Integer, Integer> publishSelector = new ObservablePublishSelector<>(source, selector);
    // The resulting Observable after applying the operator.
    operator = Observable.wrap(publishSelector);
}
```

### Method 3

```java
/**
 * Create a fresh subject and observer for each benchmark invocation.
 * Using Level.Invocation ensures that each measurement sees a clean
 * state, eliminating cross‑iteration interference.
 */
@Setup(Level.Invocation)
public void setUp() {
    subject = CompletableSubject.create();
    observer = new TestObserver();
}
```

### Method 4

```java
/**
 * Creates a new {@code MaybeAmb} instance before each benchmark invocation.
 * Using {@code Level.Invocation} ensures that the operator sees a fresh set of
 * sources for every measurement, eliminating caching effects.
 */
@Setup(Level.Invocation)
public void setUp() {
    @SuppressWarnings("unchecked")
    MaybeSource<Integer>[] sources = new MaybeSource[sourceCount];
    for (int i = 0; i < sourceCount; i++) {
        // Each source emits a distinct value immediately.
        sources[i] = Maybe.just(i);
    }
    // The iterable argument is not used when the array is supplied, so we pass null.
    maybeAmb = new MaybeAmb<>(sources, null);
}
```

### Method 5

```java
/**
 * Creates a {@link Flowable} that emits {@code itemCount} integers
 * synchronously using the selected backpressure strategy.
 */
@Setup(Level.Invocation)
public void setUp() {
    FlowableOnSubscribe<Integer> source = emitter -> {
        for (int i = 0; i < itemCount; i++) {
            emitter.onNext(i);
        }
        emitter.onComplete();
    };
    flowable = Flowable.create(source, strategy);
}
```

### Method 6

```java
/**
 * Prepare a fresh operator instance for each invocation to avoid cross‑iteration state.
 */
@Setup(Level.Invocation)
public void setUp() {
    // Observable.range emits a deterministic sequence of integers.
    // It implements ObservableSource<Integer>, which is accepted by ObservableCountSingle.
    countSingle = new ObservableCountSingle<>(Observable.range(1, size));
}
```

### Method 7

```java
/**
 * Prepare a new SingleUsing instance before each benchmark call.
 */
@Setup(Level.Invocation)
public void setUp() {
    // cheap resource
    Supplier<Object> resourceSupplier = () -> new Object();
    Function<Object, SingleSource<Integer>> singleFunction = r -> Single.just(1);
    Consumer<Object> disposer = r -> {
        // No‑op disposer; real disposers may have side‑effects.
    };
    single = new SingleUsing<>(resourceSupplier, singleFunction, disposer, eager);
}
```

### Method 8

```java
/**
 * Prepare the operator for the "both empty" scenario.
 */
@Setup(Level.Invocation)
public void prepareBothEmpty() {
    operator = new MaybeEqualSingle<>(empty, empty, predicate);
}
```

### Method 9

```java
/**
 * Prepare the operator for the "both have value" scenario.
 */
@Setup(Level.Invocation)
public void prepareBothValues() {
    operator = new MaybeEqualSingle<>(justOne, justTwo, predicate);
}
```

### Method 10

```java
/**
 * Prepare the operator for the "one empty, one value" scenario.
 */
@Setup(Level.Invocation)
public void prepareOneEmpty() {
    operator = new MaybeEqualSingle<>(justOne, empty, predicate);
}
```

### Method 11

```java
/**
 * Prepare the source Observable before each benchmark invocation.
 */
@Setup(Level.Invocation)
public void setUp() {
    // Clamp index to a valid range.
    int safeIndex = Math.min(index, sourceSize - 1);
    this.index = safeIndex;
    this.source = Observable.range(0, sourceSize);
}
```

### Method 12

```java
/**
 * Prepare the upstream Observable before each benchmark iteration.
 * Using {@code Observable.range} provides a deterministic, cheap source.
 */
@Setup(Level.Invocation)
public void setUp() {
    // Ensure count does not exceed size to keep the semantics correct.
    int effectiveCount = Math.min(count, size);
    source = Observable.range(1, size).takeLast(effectiveCount);
}
```

### Method 13

```java
/**
 * Reset the slot at index 0 before each invocation to keep the benchmark deterministic.
 */
@Setup(Level.Invocation)
public void resetSlot() {
    // Ensure the slot is cleared (null) before each operation.
    // Directly use the internal API via reflection is avoided; we simply replace it.
    composite.replaceResource(0, null);
}
```

### Method 14

```java
/**
 * Set up a fresh operator instance for each invocation to avoid
 * cross‑iteration state leakage.
 */
@Setup(Level.Invocation)
public void setUp() {
    Flowable<Integer> main = Flowable.range(1, size);
    // triggers immediate subscription
    Flowable<Long> other = Flowable.just(1L);
    flowable = new FlowableDelaySubscriptionOther<>(main, other);
}
```

### Method 15

```java
/**
 * Set up the sources and the operator before each benchmark iteration.
 * The sources are synchronous and emit a range of integers.
 */
@Setup(Level.Invocation)
public void setUp() {
    source1 = Observable.range(0, size);
    source2 = Observable.range(0, size);
    comparer = Objects::equals;
    sequenceEqualSingle = new ObservableSequenceEqualSingle<>(source1, source2, comparer, bufferSize);
}
```

### Method 16

```java
/**
 * Sets up a fresh {@link LinkedArrayList} before each benchmark iteration.
 */
@Setup(Level.Invocation)
public void setUp() {
    list = new LinkedArrayList(capacityHint);
}
```

### Method 17

```java
/**
 * Sets up the benchmark by creating an Observable that fails {@code failCount}
 * times and then emits a single integer. The retry operator is applied with a
 * predicate that allows unlimited retries.
 */
@Setup(Level.Invocation)
public void setUp() {
    AtomicInteger attempt = new AtomicInteger(0);
    ObservableSource<Integer> source = observer -> {
        int current = attempt.getAndIncrement();
        if (current < failCount) {
            observer.onError(new RuntimeException("Failure #" + current));
        } else {
            observer.onNext(1);
            observer.onComplete();
        }
    };
    // always retry
    BiPredicate<Integer, Throwable> predicate = (retry, error) -> true;
    // Wrap the source with the retry operator under test
    retryObservable = new ObservableRetryBiPredicate<>(Observable.wrap(source), predicate);
}
```

### Method 18

```java
@Setup(Level.Invocation)
@SuppressWarnings("unchecked")
public void setUp() {
    subject = SingleSubject.create();
    observers = new NoOpObserver[observerCount];
    for (int i = 0; i < observerCount; i++) {
        observers[i] = new NoOpObserver<>();
    }
}
```

### Method 19

```java
@Setup(Level.Invocation)
@SuppressWarnings("unchecked")
public void setUp() {
    subject = SingleSubject.create();
    observers = new NoOpObserver[observerCount];
    for (int i = 0; i < observerCount; i++) {
        observers[i] = new NoOpObserver<>();
    }
}
```

### Method 20

```java
@Setup(Level.Invocation)
public void init() {
    // The latch count equals the parallelism degree; it will be set by the benchmark method.
    latch = new CountDownLatch(0);
}
```

### Method 21

```java
@Setup(Level.Invocation)
public void perInvocationSetup() {
    // Create fresh operator instances for each benchmark invocation.
    successOperator = new SingleTakeUntil<>(source, neverOther);
    cancelOperator = new SingleTakeUntil<>(source, immediateOther);
}
```

### Method 22

```java
@Setup(Level.Invocation)
public void setUp() {
    // Create a cold source that emits a fixed number of items.
    source = Flowable.range(1, itemCount).subscribeOn(Schedulers.computation());
    // Create a boundary that emits a signal every {@code windowSize} items.
    // We use a PublishProcessor to manually emit boundary signals.
    PublishProcessor<Long> boundaryProcessor = PublishProcessor.create();
    boundary = boundaryProcessor.onBackpressureBuffer().subscribeOn(Schedulers.computation());
    // Emit boundary signals in a separate thread to avoid blocking the benchmark thread.
    new Thread(() -> {
        long signals = itemCount / windowSize;
        for (long i = 0; i < signals; i++) {
            boundaryProcessor.onNext(i);
        }
        boundaryProcessor.onComplete();
    }, "boundary-emitter").start();
    testSubscriber = new TestSubscriber<>();
}
```

### Method 23

```java
@Setup(Level.Invocation)
public void setUp() {
    // Create a cold source that emits a range of integers on the computation scheduler.
    source = Flowable.range(1, itemCount).subscribeOn(Schedulers.computation());
    // Trigger publisher: either emits immediately (delay 0) or after a short timer.
    if (triggerDelayMs == 0) {
        trigger = Flowable.just(new Object()).subscribeOn(Schedulers.computation());
    } else {
        trigger = Flowable.timer(triggerDelayMs, TimeUnit.MILLISECONDS, Schedulers.computation()).map(t -> new Object());
    }
}
```

### Method 24

```java
@Setup(Level.Invocation)
public void setUp() {
    // Create a finite source emitting {@code itemCount} integers.
    source = Observable.range(0, itemCount);
    // Directly instantiate the internal ObservablePublish operator.
    publish = new ObservablePublish<>(source);
}
```

### Method 25

```java
@Setup(Level.Invocation)
public void setUp() {
    // Create a fresh source for each invocation to avoid caching effects.
    source = Flowable.range(1, size);
}
```

### Method 26

```java
@Setup(Level.Invocation)
public void setUp() {
    // Fresh source for each invocation to avoid caching effects.
    source = // deterministic scheduler
    Flowable.range(1, itemCount).// deterministic scheduler
    subscribeOn(Schedulers.single());
}
```

### Method 27

```java
@Setup(Level.Invocation)
public void setUp() {
    // Observable.range is synchronous and cheap; we recreate it each invocation
    // to ensure the skip operator is applied to a fresh upstream.
    source = Observable.range(0, upstreamCount);
}
```

### Method 28

```java
@Setup(Level.Invocation)
public void setUp() {
    // Simple integer sources.
    Flowable<Integer> left = Flowable.range(1, size);
    Flowable<Integer> right = Flowable.range(1, size);
    // Keep each group open for the whole stream.
    Function<Integer, Publisher<Object>> leftEnd = v -> Flowable.never();
    Function<Integer, Publisher<Object>> rightEnd = v -> Flowable.never();
    // Non‑blocking result selector: just emit the left value as a string.
    BiFunction<Integer, Flowable<Integer>, String> resultSelector = (l, rs) -> l.toString();
    // Build the operator under test.
    joined = new FlowableGroupJoin<>(left, right, leftEnd, rightEnd, resultSelector);
}
```

### Method 29

```java
@Setup(Level.Invocation)
public void setUp() {
    // Source emits a deterministic range of integers.
    source = Flowable.range(1, itemCount).subscribeOn(Schedulers.trampoline());
    // Open publisher emits a token for each buffer we want to create.
    openPublisher = Flowable.range(1, openCount).subscribeOn(Schedulers.trampoline());
    // Each buffer closes immediately after it is opened (size‑1 buffer).
    closeFunction = token -> Flowable.just(token).subscribeOn(Schedulers.trampoline());
    // Buffer supplier creates a new ArrayList for each buffer.
    bufferSupplier = () -> new ArrayList<>();
}
```

### Method 30

```java
@Setup(Level.Invocation)
public void setUp() {
    // Suppress undeliverable error logging that could interfere with benchmark measurements.
    RxJavaPlugins.setErrorHandler(e -> {
    });
    // Create the required number of source observables.
    @SuppressWarnings("unchecked")
    Observable<Integer>[] sources = new Observable[sourceCount];
    for (int i = 0; i < sourceCount; i++) {
        sources[i] = Observable.range(1, itemCount);
    }
    // Simple zipper that sums the values from each source.
    Function<Object[], Integer> zipper = objects -> {
        int sum = 0;
        for (Object o : objects) {
            sum += (Integer) o;
        }
        return sum;
    };
    // Build the zipped observable using the public API (which internally uses ObservableZip).
    zipped = Observable.zipArray(zipper, delayError, bufferSize, sources);
}
```

### Method 31

```java
@Setup(Level.Invocation)
public void setUp() {
    // start from a known state for each invocation
    requested = new AtomicLong(0L);
}
```

### Method 32

```java
@Setup(Level.Invocation)
public void setUp() {
    @SuppressWarnings("unchecked")
    Flowable<Integer>[] sources = new Flowable[sourceCount];
    for (int i = 0; i < sourceCount; i++) {
        // Each source emits a fixed number of items on a separate thread.
        sources[i] = Flowable.range(1, 1_000).subscribeOn(Schedulers.computation());
    }
    ambFlowable = Flowable.ambArray(sources);
}
```

### Method 33

```java
@Setup(Level.Invocation)
public void setUp() {
    Flowable<Integer> left = Flowable.range(1, size);
    Flowable<Integer> right = Flowable.range(1, size);
    joinedFlowable = left.join(right, LEFT_END, RIGHT_END, RESULT_SELECTOR);
}
```

### Method 34

```java
@Setup(Level.Invocation)
public void setUp() {
    Flowable<Integer> source = Flowable.range(0, size).concatWith(Flowable.range(0, size));
    distinctFlowable = new FlowableDistinct<>(source, keySelector, collectionSupplier);
}
```

### Method 35

```java
@Setup(Level.Invocation)
public void setUp() {
    composite = new ListCompositeDisposable();
    disposables = new Disposable[SIZE];
    otherDisposables = new Disposable[SIZE];
    for (int i = 0; i < SIZE; i++) {
        disposables[i] = Disposable.empty();
        otherDisposables[i] = Disposable.empty();
    }
}
```

### Method 36

```java
@Setup(Level.Invocation)
public void setUp() {
    queue = new ArrayDeque<>(size);
    for (int i = 0; i < size; i++) {
        queue.offer(i);
    }
    state = new AtomicLong(0L);
    subscriber = new Subscriber<Integer>() {

        @Override
        public void onSubscribe(Subscription s) {
            s.request(Long.MAX_VALUE);
        }

        @Override
        public void onNext(Integer integer) {
        }

        @Override
        public void onError(Throwable t) {
        }

        @Override
        public void onComplete() {
        }
    };
    notCancelled = () -> false;
}
```

### Method 37

```java
@Setup(Level.Invocation)
public void setUp() {
    ref = new AtomicReference<>();
    disposable = new DummyDisposable();
    otherDisposable = new DummyDisposable();
}
```

### Method 38

```java
@Setup(Level.Invocation)
public void setUp() {
    source = Flowable.range(1, itemCount).parallel(parallelism).runOn(Schedulers.computation());
}
```

### Method 39

```java
@Setup(Level.Invocation)
public void setUp() {
    sr = new ScheduledRunnable(NO_OP_RUNNABLE, new NoOpContainer(), true);
}
```

### Method 40

```java
@Setup(Level.Invocation)
public void setUp() {
    sr = new ScheduledRunnable(NO_OP_RUNNABLE, new NoOpContainer(), true);
}
```

### Method 41

```java
@Setup(Level.Invocation)
public void setUp() {
    sr = new ScheduledRunnable(NO_OP_RUNNABLE, new NoOpContainer(), true);
}
```

### Method 42

```java
@Setup(Level.Invocation)
public void setUp() {
    subject = MaybeSubject.create();
    observer = new NoOpObserver<>();
}
```

### Method 43

```java
@Setup(Level.Invocation)
public void setUp(Blackhole bh) {
    // Reset RxJavaPlugins to avoid side‑effects from previous runs.
    RxJavaPlugins.reset();
    // Create a new SafeObserver for each invocation to avoid state leakage.
    safeObserver = new SafeObserver<>(new BlackholeObserver<>(bh));
    // Simulate a proper subscription before invoking callbacks.
    safeObserver.onSubscribe(DUMMY_UPSTREAM);
}
```

### Method 44

```java
@Setup(Level.Trial)
public void setUp() {
    acs = new ArrayCompositeSubscription(capacity);
    initialSubs = new DummySubscription[capacity];
    for (int i = 0; i < capacity; i++) {
        DummySubscription ds = new DummySubscription();
        initialSubs[i] = ds;
        acs.setResource(i, ds);
    }
}
```

### Method 45

```java
@Setup(Level.Trial)
public void setUp() {
    composite = new ArrayCompositeDisposable(CAPACITY);
    dummy = new NoOpDisposable();
}
```

## JMH STATE FINAL STATIC PRIMITIVE - JMH State primitive static field declared final.

### Method 1

```java
package io.reactivex.rxjava3.internal.disposables;

import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link ListCompositeDisposable}.
 *
 * The benchmarks focus on the most frequently used public operations:
 * add, addAll, remove, clear and dispose. Each benchmark runs in
 * {@link Mode#Throughput} to measure how many operations can be performed
 * per time unit under a warm JVM.
 *
 * Best‑practice JMH settings are applied:
 * - 5 warm‑up iterations (1 s each) to let the JIT stabilize.
 * - 10 measurement iterations (1 s each) for reliable results.
 * - 3 forks to isolate JVMs.
 * - {@code @State(Scope.Thread)} to avoid cross‑thread interference.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(3)
@State(Scope.Thread)
public class ListCompositeDisposableBenchmark {

    /**
     * Number of dummy disposables used in each benchmark iteration.
     */
    private static final int SIZE = 128;

    /**
     * The composite under test.
     */
    private ListCompositeDisposable composite;

    /**
     * Pre‑created disposables to avoid allocation overhead during the benchmark.
     */
    private Disposable[] disposables;

    /**
     * A second set of disposables used for remove/clear tests.
     */
    private Disposable[] otherDisposables;

    @Setup(Level.Invocation)
    public void setUp() {
        composite = new ListCompositeDisposable();
        disposables = new Disposable[SIZE];
        otherDisposables = new Disposable[SIZE];
        for (int i = 0; i < SIZE; i++) {
            disposables[i] = Disposable.empty();
            otherDisposables[i] = Disposable.empty();
        }
    }

    @Benchmark
    public void addSingle() {
        for (Disposable d : disposables) {
            composite.add(d);
        }
    }

    @Benchmark
    public void addAllVarargs() {
        composite.addAll(disposables);
    }

    @Benchmark
    public void removeSingle() {
        // first fill the composite
        composite.addAll(disposables);
        // then remove one by one
        for (Disposable d : disposables) {
            composite.remove(d);
        }
    }

    @Benchmark
    public void clear() {
        composite.addAll(disposables);
        composite.clear();
    }

    @Benchmark
    public void dispose() {
        composite.addAll(disposables);
        composite.dispose();
    }
}
```

### Method 2

```java
package io.reactivex.rxjava3.internal.disposables;

import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH micro‑benchmarks for {@link ArrayCompositeDisposable}.
 *
 * <p>All benchmarks are executed in {@link Mode#Throughput} mode, which measures
 * the number of operations per time unit. The benchmarks focus on the most
 * frequently used public methods: {@code setResource}, {@code replaceResource},
 * {@code dispose} and {@code isDisposed}.</p>
 *
 * <p>Best‑practice notes:</p>
 * <ul>
 *   <li>State objects are scoped to a single thread to avoid unwanted contention.</li>
 *   <li>{@link Blackhole} is used to consume return values and prevent dead‑code elimination.</li>
 *   <li>Separate {@code @Setup(Level.Invocation)} for {@code dispose} ensures a fresh instance per measurement.</li>
 *   <li>All allocations are performed in the setup phase to keep the measured code focused on the target operation.</li>
 * </ul>
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public class ArrayCompositeDisposableBenchmark {

    /**
     * Simple no‑op {@link Disposable} implementation used as a placeholder resource.
     */
    static final class NoOpDisposable implements Disposable {

        @Override
        public void dispose() {
            /* no‑op */
        }

        @Override
        public boolean isDisposed() {
            return false;
        }
    }

    /**
     * State shared by the {@code setResource}, {@code replaceResource} and {@code isDisposed} benchmarks.
     */
    @State(Scope.Thread)
    public static class SharedState {

        /**
         * Capacity chosen to be representative of typical usage (e.g., 16).
         */
        static final int CAPACITY = 16;

        ArrayCompositeDisposable composite;

        Disposable dummy;

        @Setup(Level.Trial)
        public void setUp() {
            composite = new ArrayCompositeDisposable(CAPACITY);
            dummy = new NoOpDisposable();
        }

        /**
         * Reset the slot at index 0 before each invocation to keep the benchmark deterministic.
         */
        @Setup(Level.Invocation)
        public void resetSlot() {
            // Ensure the slot is cleared (null) before each operation.
            // Directly use the internal API via reflection is avoided; we simply replace it.
            composite.replaceResource(0, null);
        }
    }

    /**
     * State used exclusively for the {@code dispose} benchmark to provide a fresh instance per invocation.
     */
    @State(Scope.Thread)
    public static class DisposeState {

        static final int CAPACITY = 16;

        ArrayCompositeDisposable composite;

        Disposable dummy;

        @Setup(Level.Invocation)
        public void setUp() {
            composite = new ArrayCompositeDisposable(CAPACITY);
            dummy = new NoOpDisposable();
            // Pre‑populate the array to simulate realistic work during dispose.
            for (int i = 0; i < CAPACITY; i++) {
                composite.setResource(i, dummy);
            }
        }
    }

    @Benchmark
    public void benchSetResource(SharedState state, Blackhole bh) {
        boolean result = state.composite.setResource(0, state.dummy);
        bh.consume(result);
    }

    @Benchmark
    public void benchReplaceResource(SharedState state, Blackhole bh) {
        Disposable previous = state.composite.replaceResource(0, state.dummy);
        bh.consume(previous);
    }

    @Benchmark
    public void benchIsDisposed(SharedState state, Blackhole bh) {
        boolean disposed = state.composite.isDisposed();
        bh.consume(disposed);
    }

    @Benchmark
    public void benchDispose(DisposeState state, Blackhole bh) {
        state.composite.dispose();
        // No return value, but we can verify the state to avoid dead‑code elimination.
        bh.consume(state.composite.isDisposed());
    }
}
```

### Method 3

```java
package io.reactivex.rxjava3.internal.disposables;

import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH micro‑benchmarks for {@link ArrayCompositeDisposable}.
 *
 * <p>All benchmarks are executed in {@link Mode#Throughput} mode, which measures
 * the number of operations per time unit. The benchmarks focus on the most
 * frequently used public methods: {@code setResource}, {@code replaceResource},
 * {@code dispose} and {@code isDisposed}.</p>
 *
 * <p>Best‑practice notes:</p>
 * <ul>
 *   <li>State objects are scoped to a single thread to avoid unwanted contention.</li>
 *   <li>{@link Blackhole} is used to consume return values and prevent dead‑code elimination.</li>
 *   <li>Separate {@code @Setup(Level.Invocation)} for {@code dispose} ensures a fresh instance per measurement.</li>
 *   <li>All allocations are performed in the setup phase to keep the measured code focused on the target operation.</li>
 * </ul>
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public class ArrayCompositeDisposableBenchmark {

    /**
     * Simple no‑op {@link Disposable} implementation used as a placeholder resource.
     */
    static final class NoOpDisposable implements Disposable {

        @Override
        public void dispose() {
            /* no‑op */
        }

        @Override
        public boolean isDisposed() {
            return false;
        }
    }

    /**
     * State shared by the {@code setResource}, {@code replaceResource} and {@code isDisposed} benchmarks.
     */
    @State(Scope.Thread)
    public static class SharedState {

        /**
         * Capacity chosen to be representative of typical usage (e.g., 16).
         */
        static final int CAPACITY = 16;

        ArrayCompositeDisposable composite;

        Disposable dummy;

        @Setup(Level.Trial)
        public void setUp() {
            composite = new ArrayCompositeDisposable(CAPACITY);
            dummy = new NoOpDisposable();
        }

        /**
         * Reset the slot at index 0 before each invocation to keep the benchmark deterministic.
         */
        @Setup(Level.Invocation)
        public void resetSlot() {
            // Ensure the slot is cleared (null) before each operation.
            // Directly use the internal API via reflection is avoided; we simply replace it.
            composite.replaceResource(0, null);
        }
    }

    /**
     * State used exclusively for the {@code dispose} benchmark to provide a fresh instance per invocation.
     */
    @State(Scope.Thread)
    public static class DisposeState {

        static final int CAPACITY = 16;

        ArrayCompositeDisposable composite;

        Disposable dummy;

        @Setup(Level.Invocation)
        public void setUp() {
            composite = new ArrayCompositeDisposable(CAPACITY);
            dummy = new NoOpDisposable();
            // Pre‑populate the array to simulate realistic work during dispose.
            for (int i = 0; i < CAPACITY; i++) {
                composite.setResource(i, dummy);
            }
        }
    }

    @Benchmark
    public void benchSetResource(SharedState state, Blackhole bh) {
        boolean result = state.composite.setResource(0, state.dummy);
        bh.consume(result);
    }

    @Benchmark
    public void benchReplaceResource(SharedState state, Blackhole bh) {
        Disposable previous = state.composite.replaceResource(0, state.dummy);
        bh.consume(previous);
    }

    @Benchmark
    public void benchIsDisposed(SharedState state, Blackhole bh) {
        boolean disposed = state.composite.isDisposed();
        bh.consume(disposed);
    }

    @Benchmark
    public void benchDispose(DisposeState state, Blackhole bh) {
        state.composite.dispose();
        // No return value, but we can verify the state to avoid dead‑code elimination.
        bh.consume(state.composite.isDisposed());
    }
}
```

### Method 4

```java
package io.reactivex.rxjava3.internal.jdk8;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionStage;
import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Thread)
public class ObservableFromCompletionStageBenchmark {

    private CompletionStage<Integer> completedStage;

    private static final int VALUE = 42;

    @Setup(Level.Trial)
    public void setUp() {
        // A pre‑completed stage to avoid measuring stage creation overhead
        completedStage = CompletableFuture.completedFuture(VALUE);
    }

    @Benchmark
    public void subscribeAndConsume() {
        Observable<Integer> source = new ObservableFromCompletionStage<>(completedStage);
        TestObserver<Integer> testObserver = new TestObserver<>();
        source.subscribe(testObserver);
        // Ensure the emission is processed; timeout is generous for JMH stability
        testObserver.awaitDone(1, TimeUnit.SECONDS);
        // Optionally verify correctness (kept minimal to avoid affecting throughput)
        // testObserver.assertValue(VALUE).assertNoErrors().assertComplete();
    }
}
```

### Method 5

```java
package io.reactivex.rxjava3.internal.operators.flowable;

import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * Benchmark for {@link io.reactivex.rxjava3.internal.operators.flowable.FlowableOnBackpressureBuffer}.
 * Measures the throughput (items processed per second) of the operator under different
 * configurations (buffer size, bounded/unbounded, delayError).
 *
 * Best practices applied:
 * - @State(Scope.Thread) isolates benchmark state per thread.
 * - @Param provides a matrix of configurations.
 * - @Setup(Level.Trial) prepares immutable sources once per trial.
 * - Blackhole consumes items to prevent dead‑code elimination.
 * - Blocking subscription ensures the benchmark measures the full processing pipeline.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
public class FlowableOnBackpressureBufferBenchmark {

    @State(Scope.Thread)
    public static class BenchmarkState {

        @Param({ "128", "1024" })
        public int bufferSize;

        @Param({ "true", "false" })
        public boolean unbounded;

        @Param({ "true", "false" })
        public boolean delayError;

        /**
         * Number of items emitted by the upstream source.
         */
        private static final int ELEMENT_COUNT = 1_000_000;

        private Flowable<Integer> source;

        private Flowable<Integer> buffered;

        @Setup(Level.Trial)
        public void setUp() {
            // Simple synchronous source that emits a known number of items.
            source = Flowable.range(1, ELEMENT_COUNT);
            // No‑op callbacks for overflow handling – they are required by the API.
            Action onOverflow = () -> {
            };
            Consumer<Integer> onDropped = v -> {
            };
            // Apply the operator with the current parameter set.
            buffered = source.onBackpressureBuffer(bufferSize, unbounded, delayError, onOverflow, onDropped);
        }
    }

    @Benchmark
    public void backpressureBufferThroughput(BenchmarkState state, Blackhole bh) {
        // blockingSubscribe guarantees the benchmark runs until the stream completes.
        state.buffered.blockingSubscribe(bh::consume);
    }
}
```

### Method 6

```java
package io.reactivex.rxjava3.internal.operators.flowable;

import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link io.reactivex.rxjava3.internal.operators.flowable.FlowableTakeUntil}.
 *
 * The benchmark measures the throughput (items processed per second) when a
 * {@code Flowable.range} source is combined with a {@code takeUntil} operator
 * whose "other" publisher never emits. This represents the steady‑state path
 * where the termination condition is not triggered, which is the most common
 * scenario for performance testing of this operator.
 *
 * Best practices applied:
 * • Use @State(Scope.Thread) to avoid sharing mutable state between threads.
 * • Initialise the Flowable once per trial in @Setup(Level.Trial) to exclude
 *   construction overhead from the measured time.
 * • Use Blackhole to consume items and prevent dead‑code elimination.
 * • Configure warm‑up, measurement, and fork parameters for reliable results.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
public class FlowableTakeUntilBenchmark {

    @State(Scope.Thread)
    public static class BenchmarkState {

        /**
         * Number of items emitted by the source Flowable.
         */
        private static final int ITEM_COUNT = 1_000_000;

        /**
         * The Flowable under test: source.takeUntil(other) where other never emits.
         */
        Flowable<Integer> flowable;

        @Setup(Level.Trial)
        public void setUp() {
            Flowable<Integer> source = Flowable.range(1, ITEM_COUNT);
            // never triggers termination
            Flowable<Object> other = Flowable.never();
            flowable = source.takeUntil(other);
        }
    }

    /**
     * Consumes the entire sequence produced by the {@code takeUntil} operator.
     *
     * @param state shared benchmark state containing the prepared Flowable
     * @param bh    Blackhole to consume each emitted item
     */
    @Benchmark
    public void takeUntilThroughput(BenchmarkState state, Blackhole bh) {
        // Subscribe with a consumer that forwards each item to the Blackhole.
        // The subscription requests an unbounded amount (Long.MAX_VALUE) internally.
        state.flowable.subscribe(bh::consume);
    }
}
```

### Method 7

```java
package io.reactivex.rxjava3.internal.operators.flowable;

import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * Benchmark for {@code FlowableDoOnEach}.
 *
 * Measures the throughput (items per second) of a Flowable that applies a no‑op
 * {@code doOnEach} operator. The benchmark uses a large, deterministic source
 * (range of 1 000 000 integers) to keep the workload stable across runs.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Thread)
public class FlowableDoOnEachBenchmark {

    /**
     * Number of items emitted by the source Flowable.
     */
    private static final int ITEM_COUNT = 1_000_000;

    /**
     * The Flowable under test – a range with a no‑op doOnEach attached.
     */
    private Flowable<Integer> flowable;

    /**
     * No‑op callbacks used for the doOnEach operator.
     */
    private static final Consumer<Integer> ON_NEXT = v -> {
        /* no‑op */
    };

    private static final Consumer<Throwable> ON_ERROR = e -> {
        /* no‑op */
    };

    private static final Action ON_COMPLETE = () -> {
        /* no‑op */
    };

    private static final Action ON_AFTER_TERMINATE = () -> {
        /* no‑op */
    };

    @Setup(Level.Trial)
    public void setUp() {
        // Directly instantiate the internal operator to avoid private API restrictions.
        flowable = new FlowableDoOnEach<>(Flowable.range(1, ITEM_COUNT), ON_NEXT, ON_ERROR, ON_COMPLETE, ON_AFTER_TERMINATE);
    }

    /**
     * Subscribes to the Flowable and consumes every emitted item via a Blackhole.
     *
     * @param bh Blackhole to consume items and prevent dead‑code elimination.
     */
    @Benchmark
    public void doOnEachThroughput(Blackhole bh) {
        flowable.subscribe(// onNext
        bh::consume, // onError (should never happen)
        bh::consume, // onComplete (no‑op)
        () -> {
        });
    }
}
```

### Method 8

```java
package io.reactivex.rxjava3.internal.operators.flowable;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link io.reactivex.rxjava3.internal.operators.flowable.FlowableOnBackpressureDrop}.
 *
 * The benchmark measures the throughput (items/second) when a fast upstream emits
 * a large number of items and the downstream simply consumes them via a {@link Blackhole}.
 *
 * Best practices applied:
 * - {@code @State(Scope.Thread)} isolates benchmark state per thread.
 * - Reuse the {@link Flowable} and {@link DisposableSubscriber} across iterations to avoid allocation overhead.
 * - Use {@code Blackhole} to prevent dead‑code elimination.
 * - Configure warm‑up and measurement iterations.
 * - Use {@code Mode.Throughput} with {@code TimeUnit.SECONDS}.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@Threads(1)
public class FlowableOnBackpressureDropBenchmark {

    /**
     * Benchmark state containing the hot source and the subscriber.
     */
    @State(Scope.Thread)
    public static class BenchmarkState {

        /**
         * Number of items emitted per iteration.
         */
        static final int BATCH_SIZE = 1_000_000;

        /**
         * Hot source that emits items as fast as possible.
         */
        Flowable<Integer> source;

        /**
         * Subscriber that requests {@code Long.MAX_VALUE} once and discards items via Blackhole.
         */
        TestSubscriber subscriber;

        /**
         * Counter used to generate distinct values (not required for the benchmark logic).
         */
        AtomicInteger counter = new AtomicInteger();

        @Setup(Level.Trial)
        public void setUp() {
            // Create a hot source that can be triggered manually.
            source = Flowable.<Integer>create(emitter -> {
                // No emission here; emission is driven by the benchmark method.
                // The emitter is stored so we can push items from the benchmark thread.
                emitter.setCancellable(() -> {
                    /* no‑op */
                });
                // Keep a reference for later emission.
                this.emitter = emitter;
            }, io.reactivex.rxjava3.core.BackpressureStrategy.MISSING).onBackpressureDrop().publish().autoConnect();
            subscriber = new TestSubscriber();
            source.subscribe(subscriber);
        }

        /**
         * Reference to the emitter used to push items in the benchmark method.
         */
        private io.reactivex.rxjava3.core.FlowableEmitter<Integer> emitter;

        /**
         * Emits {@code BATCH_SIZE} items to the source.
         */
        void emitBatch() {
            for (int i = 0; i < BATCH_SIZE; i++) {
                emitter.onNext(counter.getAndIncrement());
            }
        }

        /**
         * Simple subscriber that requests an unbounded number of items once
         * and forwards each received item to a Blackhole.
         */
        static final class TestSubscriber extends DisposableSubscriber<Integer> {

            @Override
            public void onStart() {
                // Request an unbounded number of items.
                request(Long.MAX_VALUE);
            }

            @Override
            public void onNext(Integer t) {
                // No work here; the benchmark method will consume via Blackhole.
            }

            @Override
            public void onError(Throwable t) {
                // Errors are unexpected in this benchmark.
                t.printStackTrace();
            }

            @Override
            public void onComplete() {
                // Not used.
            }
        }
    }

    /**
     * Benchmark method that pushes a batch of items through the {@code onBackpressureDrop}
     * operator and consumes them via {@link Blackhole}.
     *
     * @param state shared benchmark state
     * @param bh    Blackhole to consume items and prevent dead‑code elimination
     */
    @Benchmark
    public void backpressureDropThroughput(BenchmarkState state, Blackhole bh) {
        // Emit a batch of items; the operator will drop none because the subscriber
        // requests Long.MAX_VALUE.
        state.emitBatch();
        // Drain the subscriber's internal queue by consuming all items that have arrived.
        // Since the subscriber does not store items, we rely on the fact that the
        // Flowable's internal mechanisms will deliver items to the Blackhole via the
        // onNext hook we set up in the subscriber.
        // To make the consumption visible to JMH, we subscribe a temporary consumer
        // that forwards to Blackhole.
        state.source.subscribe(bh::consume);
    }
}
```

### Method 9

```java
package io.reactivex.rxjava3.internal.operators.flowable;

import java.util.concurrent.TimeUnit;
import org.reactivestreams.Subscriber;
import org.reactivestreams.Subscription;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@State(Scope.Thread)
public class FlowableTakeWhileBenchmark {

    private static final int ELEMENT_COUNT = 1_000_000;

    private Flowable<Integer> source;

    private Predicate<Integer> predicate;

    @Setup(Level.Trial)
    public void setup() {
        // A deterministic source of integers
        source = Flowable.range(1, ELEMENT_COUNT);
        // Predicate that returns true for the first half of the stream, then false
        predicate = v -> v < ELEMENT_COUNT / 2;
    }

    @Benchmark
    @BenchmarkMode(Mode.Throughput)
    @OutputTimeUnit(TimeUnit.MILLISECONDS)
    @Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
    @Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
    @Fork(2)
    public void takeWhileThroughput(Blackhole bh) {
        source.takeWhile(predicate).subscribe(new BlackholeSubscriber(bh));
    }

    /**
     * Subscriber that requests an unbounded number of items and forwards each
     * received element to the Blackhole to prevent dead‑code elimination.
     */
    static final class BlackholeSubscriber implements Subscriber<Integer> {

        private final Blackhole bh;

        private Subscription upstream;

        BlackholeSubscriber(Blackhole bh) {
            this.bh = bh;
        }

        @Override
        public void onSubscribe(Subscription s) {
            this.upstream = s;
            // Request as many items as possible; the operator will cancel when the predicate fails
            s.request(Long.MAX_VALUE);
        }

        @Override
        public void onNext(Integer t) {
            bh.consume(t);
        }

        @Override
        public void onError(Throwable t) {
            bh.consume(t);
        }

        @Override
        public void onComplete() {
            // No additional work needed on completion
        }
    }
}
```

### Method 10

```java
package io.reactivex.rxjava3.internal.operators.observable;

import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link ObservableFlattenIterable}.
 *
 * The benchmark measures the throughput (operations per second) of flattening an {@link Iterable}
 * produced by a mapper function for each upstream item. The mapper creates a small fixed-size list,
 * which mimics a typical use‑case where each source element expands to a few inner elements.
 *
 * Best practices applied:
 * - {@code @State(Scope.Thread)} isolates mutable state per benchmark thread.
 * - {@code @Setup(Level.Trial)} prepares immutable data structures once per trial.
 * - Use of {@link Blackhole} prevents dead‑code elimination.
 * - The benchmark runs in {@link Mode#Throughput} with results reported in operations per second.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public class ObservableFlattenIterableBenchmark {

    @State(Scope.Thread)
    public static class BenchmarkState {

        /**
         * Source Observable emitting a fixed range of integers.
         */
        Observable<Integer> source;

        /**
         * Mapper that expands each integer into a small list of integers.
         */
        Function<Integer, Iterable<Integer>> mapper;

        /**
         * Number of items emitted by the source per subscription.
         */
        static final int SOURCE_COUNT = 1_000;

        /**
         * Number of inner items produced per source item.
         */
        static final int INNER_PER_ITEM = 10;

        @Setup(Level.Trial)
        public void setUp() {
            // Synchronous source – no scheduling overhead.
            source = Observable.range(1, SOURCE_COUNT);
            // Simple mapper returning a List<Integer> of size INNER_PER_ITEM.
            mapper = i -> IntStream.range(0, INNER_PER_ITEM).boxed().collect(Collectors.toList());
        }
    }

    /**
     * Benchmark that subscribes to {@link ObservableFlattenIterable},
     * consumes all emitted items via a {@link Blackhole}, and completes.
     *
     * The use of {@code blockingSubscribe} guarantees that the method returns
     * only after the whole stream has been processed, providing a clean measurement
     * of end‑to‑end throughput.
     */
    @Benchmark
    public void flattenIterable(BenchmarkState state, Blackhole bh) {
        new ObservableFlattenIterable<>((ObservableSource<Integer>) state.source, state.mapper).blockingSubscribe(bh::consume);
    }
}
```

### Method 11

```java
package io.reactivex.rxjava3.internal.operators.observable;

import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link ObservableFlattenIterable}.
 *
 * The benchmark measures the throughput (operations per second) of flattening an {@link Iterable}
 * produced by a mapper function for each upstream item. The mapper creates a small fixed-size list,
 * which mimics a typical use‑case where each source element expands to a few inner elements.
 *
 * Best practices applied:
 * - {@code @State(Scope.Thread)} isolates mutable state per benchmark thread.
 * - {@code @Setup(Level.Trial)} prepares immutable data structures once per trial.
 * - Use of {@link Blackhole} prevents dead‑code elimination.
 * - The benchmark runs in {@link Mode#Throughput} with results reported in operations per second.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public class ObservableFlattenIterableBenchmark {

    @State(Scope.Thread)
    public static class BenchmarkState {

        /**
         * Source Observable emitting a fixed range of integers.
         */
        Observable<Integer> source;

        /**
         * Mapper that expands each integer into a small list of integers.
         */
        Function<Integer, Iterable<Integer>> mapper;

        /**
         * Number of items emitted by the source per subscription.
         */
        static final int SOURCE_COUNT = 1_000;

        /**
         * Number of inner items produced per source item.
         */
        static final int INNER_PER_ITEM = 10;

        @Setup(Level.Trial)
        public void setUp() {
            // Synchronous source – no scheduling overhead.
            source = Observable.range(1, SOURCE_COUNT);
            // Simple mapper returning a List<Integer> of size INNER_PER_ITEM.
            mapper = i -> IntStream.range(0, INNER_PER_ITEM).boxed().collect(Collectors.toList());
        }
    }

    /**
     * Benchmark that subscribes to {@link ObservableFlattenIterable},
     * consumes all emitted items via a {@link Blackhole}, and completes.
     *
     * The use of {@code blockingSubscribe} guarantees that the method returns
     * only after the whole stream has been processed, providing a clean measurement
     * of end‑to‑end throughput.
     */
    @Benchmark
    public void flattenIterable(BenchmarkState state, Blackhole bh) {
        new ObservableFlattenIterable<>((ObservableSource<Integer>) state.source, state.mapper).blockingSubscribe(bh::consume);
    }
}
```

### Method 12

```java
package io.reactivex.rxjava3.internal.operators.parallel;

import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link ParallelFilterTry}.
 *
 * Measures the throughput of the parallel filter operator with a simple predicate
 * and a no‑op error handler. The benchmark processes a fixed number of integers
 * (1_000_000) in parallel and consumes the results via {@link Blackhole} to avoid
 * dead‑code elimination.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2)
@State(Scope.Thread)
public class ParallelFilterTryBenchmark {

    /**
     * Number of items emitted by the source Flowable.
     */
    private static final int ITEM_COUNT = 1_000_000;

    /**
     * Parallel flowable source.
     */
    private ParallelFlowable<Integer> source;

    /**
     * Instance of the operator under test.
     */
    private ParallelFilterTry<Integer> operator;

    /**
     * Simple predicate that accepts even numbers.
     */
    private Predicate<Integer> predicate = v -> (v & 1) == 0;

    /**
     * Error handler that never retries, skips, or stops – it simply propagates the error.
     * This keeps the benchmark focused on the happy‑path performance.
     */
    private BiFunction<Long, Throwable, ParallelFailureHandling> errorHandler = (retryCount, throwable) -> ParallelFailureHandling.STOP;

    @Setup(Level.Trial)
    public void setUp() {
        // Create a parallel source that emits a range of integers.
        source = Flowable.range(1, ITEM_COUNT).parallel().runOn(io.reactivex.rxjava3.schedulers.Schedulers.computation());
        // Wrap the source with the ParallelFilterTry operator.
        operator = new ParallelFilterTry<>(source, predicate, errorHandler);
    }

    /**
     * Executes the parallel filter and consumes all emitted items.
     *
     * @param bh Blackhole to consume the items and prevent dead‑code elimination.
     */
    @Benchmark
    public void filterAndConsume(Blackhole bh) {
        // Convert back to a sequential Flowable and block until all items are processed.
        operator.sequential().blockingForEach(bh::consume);
    }
}
```

### Method 13

```java
package io.reactivex.rxjava3.internal.operators.single;

import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * Benchmark for {@link io.reactivex.rxjava3.internal.operators.single.SingleMap}.
 *
 * Measures the throughput of a {@code Single.map} operation where the mapper
 * performs a simple arithmetic transformation. The benchmark blocks on the
 * {@code Single} to obtain the result, ensuring that the measured work includes
 * the full operator chain (subscription, mapping, and emission).
 *
 * Best practices applied:
 * - Use {@code @State(Scope.Thread)} to avoid sharing mutable state across threads.
 * - Pre‑create the {@code Single} and mapper in {@code @Setup} to exclude construction overhead.
 * - Use {@code Blackhole} to consume the result and prevent dead‑code elimination.
 * - Configure warm‑up, measurement, forks and time units for reliable results.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 3, warmups = 1)
@State(Scope.Thread)
public class SingleMapBenchmark {

    /**
     * Source value emitted by the upstream {@code Single}.
     */
    private static final int SOURCE_VALUE = 42;

    /**
     * Mapper that adds a constant to the source value.
     */
    private Function<Integer, Integer> mapper;

    /**
     * The {@code Single} under test: {@code Single.just(SOURCE_VALUE).map(mapper)}.
     */
    private Single<Integer> mappedSingle;

    @Setup(Level.Trial)
    public void setup() {
        // Simple mapper – change to a more complex function if needed.
        mapper = v -> v + 1;
        // Build the Single chain once per trial to exclude construction cost.
        mappedSingle = Single.just(SOURCE_VALUE).map(mapper);
    }

    /**
     * Executes the mapping operation and blocks until the result is available.
     *
     * @param bh Blackhole to consume the result and avoid dead‑code elimination.
     */
    @Benchmark
    public void mapSingle(Blackhole bh) {
        // blockingGet() forces the whole chain to run synchronously on the current thread.
        int result = mappedSingle.blockingGet();
        bh.consume(result);
    }
}
```

### Method 14

```java
package io.reactivex.rxjava3.internal.util;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link VolatileSizeArrayList}.
 *
 * The benchmarks focus on the most common operations:
 * - add (append)
 * - get (random access)
 * - size (volatile read)
 * - remove (by index)
 * - iteration
 *
 * A baseline using {@link java.util.ArrayList} is also provided for comparison.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2)
@State(Scope.Thread)
public class VolatileSizeArrayListBenchmark {

    /**
     * Size of the pre‑filled list for read‑only benchmarks.
     */
    private static final int PREPOPULATED_SIZE = 10_000;

    /**
     * List under test – VolatileSizeArrayList.
     */
    private VolatileSizeArrayList<Integer> volatileList;

    /**
     * Baseline list – regular ArrayList.
     */
    private List<Integer> arrayList;

    /**
     * Index used for random‑access get benchmark (cycled).
     */
    private int getIndex;

    /**
     * Index used for remove benchmark (cycled).
     */
    private int removeIndex;

    @Setup(Level.Trial)
    public void setUp() {
        volatileList = new VolatileSizeArrayList<>(PREPOPULATED_SIZE);
        arrayList = new ArrayList<>(PREPOPULATED_SIZE);
        for (int i = 0; i < PREPOPULATED_SIZE; i++) {
            volatileList.add(i);
            arrayList.add(i);
        }
        getIndex = 0;
        removeIndex = 0;
    }

    /* --------------------------------------------------------------------- */
    /*                     Benchmarks for VolatileSizeArrayList              */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public boolean volatileAdd() {
        // Adding at the end; the list grows beyond the pre‑populated size.
        // The element value is irrelevant for throughput measurement.
        return volatileList.add(42);
    }

    @Benchmark
    public int volatileGet() {
        // Cycle through the list to avoid constant cache hits.
        int value = volatileList.get(getIndex);
        getIndex = (getIndex + 1) % volatileList.size();
        return value;
    }

    @Benchmark
    public int volatileSize() {
        // Simple volatile read of the size.
        return volatileList.size();
    }

    @Benchmark
    public int volatileRemove() {
        // Remove at a rotating index; re‑insert the removed element to keep size stable.
        int idx = removeIndex % volatileList.size();
        Integer removed = volatileList.remove(idx);
        volatileList.add(idx, removed);
        removeIndex = (removeIndex + 1) % volatileList.size();
        return idx;
    }

    @Benchmark
    public long volatileIterate() {
        long sum = 0;
        for (Integer i : volatileList) {
            sum += i;
        }
        return sum;
    }

    /* --------------------------------------------------------------------- */
    /*                     Baseline Benchmarks for java.util.ArrayList       */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public boolean arrayListAdd() {
        return arrayList.add(42);
    }

    @Benchmark
    public int arrayListGet() {
        int value = arrayList.get(getIndex);
        getIndex = (getIndex + 1) % arrayList.size();
        return value;
    }

    @Benchmark
    public int arrayListSize() {
        return arrayList.size();
    }

    @Benchmark
    public int arrayListRemove() {
        int idx = removeIndex % arrayList.size();
        Integer removed = arrayList.remove(idx);
        arrayList.add(idx, removed);
        removeIndex = (removeIndex + 1) % arrayList.size();
        return idx;
    }

    @Benchmark
    public long arrayListIterate() {
        long sum = 0;
        for (Integer i : arrayList) {
            sum += i;
        }
        return sum;
    }
}
```

### Method 15

```java
package io.reactivex.rxjava3.operators;

import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link SpscArrayQueue}.
 *
 * The benchmark measures throughput of the single‑producer single‑consumer
 * scenario as well as single‑threaded offer/poll operations.
 *
 * Best practices applied:
 * - @State(Scope.Group) to share the queue between producer and consumer threads.
 * - @Group and @GroupThreads to model the SPSC pattern.
 * - Blackhole consumption to prevent dead‑code elimination.
 * - Warmup, measurement, and fork settings that are commonly used for reliable results.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 7, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2, jvmArgsAppend = { "-XX:-RestrictContended" })
public class SpscArrayQueueBenchmark {

    /**
     * Shared state for the SPSC group.
     */
    @State(Scope.Group)
    public static class SpscState {

        /**
         * Queue capacity – a power of two for optimal indexing.
         */
        // 4096
        private static final int CAPACITY = 1 << 12;

        /**
         * The queue instance used by both producer and consumer.
         */
        SpscArrayQueue<Integer> queue;

        /**
         * A simple payload used for offers.
         */
        int counter = 0;

        @Setup(Level.Iteration)
        public void setUp() {
            queue = new SpscArrayQueue<>(CAPACITY);
        }

        /**
         * Returns a distinct integer for each offer to avoid accidental caching effects.
         */
        int nextValue() {
            return counter++;
        }
    }

    /**
     * Producer thread for the SPSC benchmark.
     */
    @Benchmark
    @Group("spsc")
    @GroupThreads(1)
    public void produce(SpscState state, Blackhole bh) {
        // Offer a new integer; the return value is consumed to avoid dead‑code elimination.
        boolean offered = state.queue.offer(state.nextValue());
        bh.consume(offered);
    }

    /**
     * Consumer thread for the SPSC benchmark.
     */
    @Benchmark
    @Group("spsc")
    @GroupThreads(1)
    public void consume(SpscState state, Blackhole bh) {
        // Poll the queue; the result (or null) is consumed.
        Integer value = state.queue.poll();
        bh.consume(value);
    }

    /**
     * Single‑threaded benchmark that measures the raw cost of an offer followed by a poll.
     * This isolates the queue's internal overhead from thread‑interaction effects.
     */
    @State(Scope.Thread)
    public static class SingleThreadState {

        private static final int CAPACITY = 1 << 12;

        SpscArrayQueue<Integer> queue;

        int counter = 0;

        @Setup(Level.Iteration)
        public void setUp() {
            queue = new SpscArrayQueue<>(CAPACITY);
        }

        int nextValue() {
            return counter++;
        }
    }

    @Benchmark
    @GroupThreads(1)
    public void singleThreadOfferPoll(SingleThreadState state, Blackhole bh) {
        // Offer then immediately poll; both results are consumed.
        boolean offered = state.queue.offer(state.nextValue());
        bh.consume(offered);
        Integer value = state.queue.poll();
        bh.consume(value);
    }
}
```

### Method 16

```java
package io.reactivex.rxjava3.operators;

import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link SpscArrayQueue}.
 *
 * The benchmark measures throughput of the single‑producer single‑consumer
 * scenario as well as single‑threaded offer/poll operations.
 *
 * Best practices applied:
 * - @State(Scope.Group) to share the queue between producer and consumer threads.
 * - @Group and @GroupThreads to model the SPSC pattern.
 * - Blackhole consumption to prevent dead‑code elimination.
 * - Warmup, measurement, and fork settings that are commonly used for reliable results.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 7, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2, jvmArgsAppend = { "-XX:-RestrictContended" })
public class SpscArrayQueueBenchmark {

    /**
     * Shared state for the SPSC group.
     */
    @State(Scope.Group)
    public static class SpscState {

        /**
         * Queue capacity – a power of two for optimal indexing.
         */
        // 4096
        private static final int CAPACITY = 1 << 12;

        /**
         * The queue instance used by both producer and consumer.
         */
        SpscArrayQueue<Integer> queue;

        /**
         * A simple payload used for offers.
         */
        int counter = 0;

        @Setup(Level.Iteration)
        public void setUp() {
            queue = new SpscArrayQueue<>(CAPACITY);
        }

        /**
         * Returns a distinct integer for each offer to avoid accidental caching effects.
         */
        int nextValue() {
            return counter++;
        }
    }

    /**
     * Producer thread for the SPSC benchmark.
     */
    @Benchmark
    @Group("spsc")
    @GroupThreads(1)
    public void produce(SpscState state, Blackhole bh) {
        // Offer a new integer; the return value is consumed to avoid dead‑code elimination.
        boolean offered = state.queue.offer(state.nextValue());
        bh.consume(offered);
    }

    /**
     * Consumer thread for the SPSC benchmark.
     */
    @Benchmark
    @Group("spsc")
    @GroupThreads(1)
    public void consume(SpscState state, Blackhole bh) {
        // Poll the queue; the result (or null) is consumed.
        Integer value = state.queue.poll();
        bh.consume(value);
    }

    /**
     * Single‑threaded benchmark that measures the raw cost of an offer followed by a poll.
     * This isolates the queue's internal overhead from thread‑interaction effects.
     */
    @State(Scope.Thread)
    public static class SingleThreadState {

        private static final int CAPACITY = 1 << 12;

        SpscArrayQueue<Integer> queue;

        int counter = 0;

        @Setup(Level.Iteration)
        public void setUp() {
            queue = new SpscArrayQueue<>(CAPACITY);
        }

        int nextValue() {
            return counter++;
        }
    }

    @Benchmark
    @GroupThreads(1)
    public void singleThreadOfferPoll(SingleThreadState state, Blackhole bh) {
        // Offer then immediately poll; both results are consumed.
        boolean offered = state.queue.offer(state.nextValue());
        bh.consume(offered);
        Integer value = state.queue.poll();
        bh.consume(value);
    }
}
```

### Method 17

```java
package io.reactivex.rxjava3.operators;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicReferenceArray;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link SpscLinkedArrayQueue}.
 *
 * The benchmark measures throughput of single‑producer single‑consumer (SPSC)
 * operations. Two threads are used: one produces elements, the other consumes
 * them. The queue is pre‑allocated with a power‑of‑two capacity to avoid
 * resizing during the measurement phase.
 *
 * Best‑practice JMH settings:
 * - Warm‑up iterations to let the JVM reach a steady state.
 * - Multiple measurement iterations for statistical confidence.
 * - Several forks to isolate JVM optimisations.
 * - Use of @Group to keep producer and consumer threads coordinated.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 3, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Group)
public class SpscLinkedArrayQueueBenchmark {

    /**
     * Queue capacity – must be a power of two and at least 8.
     */
    // 4096
    private static final int CAPACITY = 1 << 12;

    /**
     * The queue under test.
     */
    private SpscLinkedArrayQueue<Integer> queue;

    /**
     * A dummy value used for production.
     */
    private static final Integer ELEMENT = 1;

    /**
     * Initialise the queue before each group execution.
     * The queue is freshly allocated to avoid interference from previous runs.
     */
    @Setup(Level.Iteration)
    public void setUp() {
        queue = new SpscLinkedArrayQueue<>(CAPACITY);
    }

    /**
     * Producer thread – offers a single element to the queue.
     * The method returns {@code true} to keep the benchmark signature simple.
     */
    @Benchmark
    @Group("spsc")
    @GroupThreads(1)
    public boolean produce() {
        // In a real workload the element would vary; here we reuse a constant.
        return queue.offer(ELEMENT);
    }

    /**
     * Consumer thread – polls an element from the queue.
     * The returned value is ignored; the benchmark measures the call rate.
     */
    @Benchmark
    @Group("spsc")
    @GroupThreads(1)
    public Integer consume() {
        // poll() may return null if the producer is slower; this is acceptable
        // for throughput measurement as it reflects realistic back‑pressure.
        return queue.poll();
    }

    /**
     * Benchmark that measures the combined latency of a single offer‑followed‑by‑poll
     * pair executed by the same thread. Useful for single‑threaded baseline.
     */
    @Benchmark
    @GroupThreads(1)
    @Group("singleThread")
    public Integer offerAndPoll() {
        queue.offer(ELEMENT);
        return queue.poll();
    }
}
```

## JMH LOOP INSIDE BENCHMARK - Usage of loops in the JMH benchmark function.

### Method 1

```java
/* --------------------------------------------------------------------- */
/*  Emit benchmarks                                                       */
/* --------------------------------------------------------------------- */
@Benchmark
public void emitUnbounded(Blackhole bh) {
    for (int i = 0; i < batchSize; i++) {
        unbounded.onNext(i);
    }
    // Prevent the JIT from discarding the loop
    bh.consume(unbounded);
}
```

### Method 2

```java
/* --------------------------------------------------------------------- */
/*  Multi‑threaded benchmarks (multiple producers, single consumer)      */
/* --------------------------------------------------------------------- */
@Benchmark
// 3 producers + 1 consumer
@Threads(4)
public void multiProducerSingleConsumer(SharedState state, Blackhole bh) {
    // Thread 0 acts as the consumer, others as producers.
    int threadId = (int) Thread.currentThread().getId();
    if (threadId % 4 == 0) {
        // Consumer
        Integer v = state.queue.poll();
        if (v != null) {
            bh.consume(v);
        }
    } else {
        // Producer
        state.queue.offer(threadId);
    }
}
```

### Method 3

```java
/* --------------------------------------------------------------------- */
/*  Subscribe & replay benchmarks                                         */
/* --------------------------------------------------------------------- */
@Benchmark
public void subscribeAndReplayUnbounded(Blackhole bh) {
    // Pre‑populate a small amount of data to make replay non‑trivial
    for (int i = 0; i < batchSize; i++) {
        unbounded.onNext(i);
    }
    unbounded.subscribe(new BlackholeSubscriber(bh));
}
```

### Method 4

```java
/* --------------------------------------------------------------------- */
/* Helper benchmark that repeatedly schedules a batch of tasks.         */
/* This mimics a realistic usage pattern where many tasks are queued.   */
/* --------------------------------------------------------------------- */
@Benchmark
public void scheduleBatchOfTasks(Blackhole bh) {
    // Schedule a small batch (e.g., 10 tasks) to amortize loop overhead.
    for (int i = 0; i < 10; i++) {
        worker.schedule(() -> bh.consume(counter.incrementAndGet()));
    }
}
```

### Method 5

```java
/**
 * Baseline benchmark for a failing {@code Maybe} without error handling.
 * The RuntimeException is caught to prevent the benchmark from aborting.
 */
@Benchmark
public void errorBaselineThroughput(Blackhole bh) {
    Integer result;
    try {
        // throws
        result = errorSource.blockingGet();
    } catch (Throwable ex) {
        // In the error‑only baseline we treat the outcome as a null value.
        result = null;
    }
    bh.consume(result);
}
```

### Method 6

```java
/**
 * Benchmark method that subscribes the configured number of subscribers to the
 * cached Flowable and consumes all emitted items. The method measures how many
 * complete subscription cycles can be performed per second.
 *
 * @param state shared benchmark state
 * @param bh    JMH blackhole to consume emitted values
 */
@Benchmark
public void replayCache(BenchmarkState state, Blackhole bh) {
    // Subscribe all pre‑created subscribers.
    for (FlowableSubscriber<Integer> subscriber : state.subscribers) {
        // Wrap the subscriber to forward items to the blackhole.
        FlowableSubscriber<Integer> bhSubscriber = new FlowableSubscriber<Integer>() {

            @Override
            public void onSubscribe(org.reactivestreams.Subscription s) {
                subscriber.onSubscribe(s);
                s.request(Long.MAX_VALUE);
            }

            @Override
            public void onNext(Integer t) {
                bh.consume(t);
                subscriber.onNext(t);
            }

            @Override
            public void onError(Throwable t) {
                subscriber.onError(t);
            }

            @Override
            public void onComplete() {
                subscriber.onComplete();
            }
        };
        state.cachedFlowable.subscribe(bhSubscriber);
    }
}
```

### Method 7

```java
/**
 * Benchmark method that subscribes to the Flowable and consumes all items.
 *
 * @param bh Blackhole to consume values and avoid dead‑code elimination.
 */
@Benchmark
public void concatAndConsume(Blackhole bh) {
    // Use TestSubscriber to request all items and await completion.
    TestSubscriber<Integer> ts = new TestSubscriber<>(Long.MAX_VALUE);
    flowable.subscribe(ts);
    // Ensure the subscription has completed before returning.
    ts.awaitDone(5, TimeUnit.SECONDS);
    // Consume the received items via Blackhole.
    for (Integer v : ts.values()) {
        bh.consume(v);
    }
}
```

### Method 8

```java
/**
 * Benchmark that creates a replay ConnectableObservable, connects it,
 * and subscribes a single observer that consumes all items.
 *
 * The observer forwards each received item to the Blackhole to avoid dead‑code elimination.
 */
@Benchmark
public void replayAndConsume(Blackhole bh) {
    ConnectableObservable<Integer> replay;
    if (bufferSize == Integer.MAX_VALUE) {
        // Unbounded replay
        replay = ObservableReplay.createFrom(source);
    } else {
        // Size‑bounded replay
        replay = ObservableReplay.create(source, bufferSize, eagerTruncate);
    }
    // Connect the source (no need to keep the Disposable)
    replay.connect(Disposable::dispose);
    // Subscribe a consumer that forwards items to the Blackhole
    replay.subscribe(new Observer<Integer>() {

        @Override
        public void onSubscribe(Disposable d) {
            // No explicit disposal; the benchmark runs to completion
        }

        @Override
        public void onNext(Integer value) {
            bh.consume(value);
        }

        @Override
        public void onError(Throwable e) {
            // Propagate errors to the Blackhole to avoid swallowing them
            bh.consume(e);
        }

        @Override
        public void onComplete() {
            // No-op
        }
    });
}
```

### Method 9

```java
/**
 * Benchmark that iterates over the BlockingFlowableMostRecent and consumes each element.
 *
 * Each operation creates a fresh iterator, walks through all emitted items,
 * and feeds them into a Blackhole to avoid dead‑code elimination.
 */
@Benchmark
public void iterateAll(Blackhole bh) {
    Iterator<Integer> it = mostRecent.iterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 10

```java
/**
 * Benchmark that iterates over the entire Flowable using the blocking iterator.
 * The returned sum prevents dead‑code elimination.
 *
 * @return the sum of all emitted integers
 */
@Benchmark
public int iterateAndSum() {
    int sum = 0;
    Iterator<Integer> it = blocking.iterator();
    while (it.hasNext()) {
        sum += it.next();
    }
    return sum;
}
```

### Method 11

```java
/**
 * Benchmark the conversion where the upstream {@code Maybe} is empty
 * and no default value is supplied. The operator signals an error,
 * which we consume to avoid the benchmark aborting.
 */
@Benchmark
public void maybeToSingleEmptyNoDefault(Blackhole bh) {
    Single<Integer> single = emptyToSingleNoDefault;
    try {
        bh.consume(single.blockingGet());
    } catch (Throwable ignored) {
        // Expected NoSuchElementException; count the operation as completed.
        bh.consume(ignored);
    }
}
```

### Method 12

```java
/**
 * Benchmark the error path where the source emits more than one element.
 * The operator should terminate with an {@link IllegalArgumentException}.
 * The exception is caught to keep the benchmark running.
 */
@Benchmark
public void multipleElementsError() {
    Single<Integer> single = new FlowableSingleSingle<>(multiElementSource, null);
    try {
        single.blockingGet();
    } catch (IllegalArgumentException ignored) {
        // Expected – the operator signals an error when more than one element is observed.
    }
}
```

### Method 13

```java
/**
 * Benchmark the error‑path execution of {@link MaybeDelay}
 * with {@code delayError = true}.
 */
@Benchmark
public void delayError(Blackhole bh) {
    try {
        // blockingGet throws the upstream error; we capture it to avoid benchmark failure.
        delayWithError.blockingGet();
    } catch (Throwable ex) {
        bh.consume(ex);
    }
}
```

### Method 14

```java
/**
 * Benchmark the error‑path: supplier throws, causing the Completable to signal onError.
 */
@Benchmark
public void errorSubscribeAndAwait(ErrorState state, Blackhole bh) {
    try {
        state.completable.blockingAwait();
    } catch (Throwable t) {
        // Consume the exception to prevent dead‑code elimination.
        bh.consume(t);
    }
}
```

### Method 15

```java
/**
 * Benchmark the full lifecycle: onSubscribe → many onNext → onComplete.
 *
 * This gives a more realistic picture of end‑to‑end throughput.
 */
@Benchmark
public void fullLifecycle(Blackhole bh) {
    // Reset state for each iteration.
    subscriber.onSubscribe(upstream);
    for (int i = 0; i < bufferSize; i++) {
        subscriber.onNext(i);
    }
    subscriber.onComplete();
    bh.consume(upstream.requested.get());
}
```

### Method 16

```java
/**
 * Benchmark the {@code add(Object)} method.
 *
 * <p>Each invocation adds {@code elementCount} elements to a newly created list.
 * The list itself is not retained after the method returns, ensuring that the
 * benchmark measures only the cost of the add operation without interference
 * from subsequent reads.
 */
@Benchmark
public void addBenchmark() {
    for (int i = 0; i < elementCount; i++) {
        list.add(i);
    }
}
```

### Method 17

```java
/**
 * Benchmark the {@code toString()} method.
 *
 * <p>The list is pre‑filled with {@code elementCount} elements in the {@link #setUp()}
 * method, then {@code toString()} is invoked. The result is consumed by a {@link Blackhole}
 * to prevent dead‑code elimination.
 */
@Benchmark
public void toStringBenchmark(Blackhole bh) {
    // Populate the list once per invocation; this cost is part of the benchmark
    // because {@code toString()} depends on the internal layout.
    for (int i = 0; i < elementCount; i++) {
        list.add(i);
    }
    bh.consume(list.toString());
}
```

### Method 18

```java
/**
 * Executes the FlowableSingle operator and consumes the terminal signal.
 * Using {@code blockingFirst()} forces the whole reactive chain to run
 * synchronously, which is appropriate for a micro‑benchmark measuring
 * raw operator overhead.
 *
 * @param bh Blackhole to consume results and prevent dead‑code elimination.
 */
@Benchmark
public void runSingle(Blackhole bh) {
    try {
        // For the error case (multiple elements) blockingFirst() will throw.
        Integer result = singleFlowable.blockingFirst();
        bh.consume(result);
    } catch (Throwable t) {
        // Consume the exception to keep the benchmark realistic.
        bh.consume(t);
    }
}
```

### Method 19

```java
/**
 * Measures the throughput of iterating over the entire sequence.
 *
 * @param bh Blackhole to consume values and prevent optimizations.
 */
@Benchmark
public void iterate(Blackhole bh) {
    Iterator<Integer> it = blocking.iterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 20

```java
// -----------------------------------------------------------------------
// Worker run loop – schedule a batch of tasks and let the worker drain them.
// This benchmark measures the cost of the runEager() loop.
// -----------------------------------------------------------------------
@Benchmark
public void workerRunEagerLoop(BenchmarkState state) {
    // schedule a small batch (e.g., 10 tasks) to be executed in the same run
    for (int i = 0; i < 10; i++) {
        state.worker.schedule(state.noop);
    }
    // The worker will automatically execute when tasks are queued.
    // No explicit call needed; the benchmark measures the time until all tasks are processed.
}
```

### Method 21

```java
// -------------------------------------------------------------------------
// Benchmark methods
// -------------------------------------------------------------------------
@Benchmark
public void subscribeAndSuccess(Blackhole bh, SubscribeSuccessState state) {
    for (NoOpObserver<Integer> o : state.observers) {
        state.subject.subscribe(o);
    }
    state.subject.onSuccess(42);
    bh.consume(state.subject.getValue());
}
```

### Method 22

```java
@Benchmark
public long arrayListIterate() {
    long sum = 0;
    for (Integer i : arrayList) {
        sum += i;
    }
    return sum;
}
```

### Method 23

```java
@Benchmark
public long volatileIterate() {
    long sum = 0;
    for (Integer i : volatileList) {
        sum += i;
    }
    return sum;
}
```

### Method 24

```java
@Benchmark
public void addSingle() {
    for (Disposable d : disposables) {
        composite.add(d);
    }
}
```

### Method 25

```java
@Benchmark
public void concatMapCompletableThroughput(BenchmarkState state, Blackhole bh) {
    // Build the operator under test.
    Completable concat = new ObservableConcatMapCompletable<>(state.source, state.mapper, state.errorMode, state.prefetch);
    // Subscribe and block until completion.
    // Using an AtomicInteger to ensure the subscription side‑effects are observed.
    AtomicInteger done = new AtomicInteger();
    concat.subscribe(new CompletableObserver() {

        @Override
        public void onSubscribe(Disposable d) {
            // No-op
        }

        @Override
        public void onError(Throwable e) {
            // Propagate error to Blackhole to avoid dead‑code elimination.
            bh.consume(e);
            done.set(1);
        }

        @Override
        public void onComplete() {
            done.set(1);
        }
    });
    // Busy‑wait until the Completable signals termination.
    // This is safe in a benchmark because the work is tiny and the loop
    // will exit quickly; it also avoids using Thread.sleep which would
    // distort throughput measurements.
    while (done.get() == 0) {
        // spin
    }
    // Consume a dummy value to keep the JIT from optimizing away the whole pipeline.
    bh.consume(state.sourceSize);
}
```

### Method 26

```java
@Benchmark
public void disposeObservers(DisposeState state) {
    for (Disposable d : state.disposables) {
        d.dispose();
    }
}
```

### Method 27

```java
@Benchmark
public void elementAtOutOfRangeNoDefault(BenchmarkState state, Blackhole bh) {
    try {
        state.elementAtOutOfRangeNoDefault.blockingGet();
    } catch (Throwable t) {
        // Expected error path; consume the exception to avoid dead‑code elimination.
        bh.consume(t);
    }
}
```

### Method 28

```java
@Benchmark
public void emitSizeBounded(Blackhole bh) {
    for (int i = 0; i < batchSize; i++) {
        sizeBounded.onNext(i);
    }
    bh.consume(sizeBounded);
}
```

### Method 29

```java
@Benchmark
public void emitTimeAndSizeBounded(Blackhole bh) {
    for (int i = 0; i < batchSize; i++) {
        timeAndSizeBounded.onNext(i);
    }
    bh.consume(timeAndSizeBounded);
}
```

### Method 30

```java
@Benchmark
public void empty(Blackhole bh) {
    // For an empty source, blockingGet() returns null.
    try {
        Integer v = emptyMaybe.blockingGet();
        bh.consume(v);
    } catch (Throwable t) {
        bh.consume(t);
    }
}
```

### Method 31

```java
@Benchmark
public void iterate(Blackhole bh) {
    Iterator<Integer> it = iterable.iterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 32

```java
@Benchmark
public void iterateAll(Blackhole bh) {
    Iterator<Integer> it = blocking.iterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 33

```java
@Benchmark
public void multipleElements(Blackhole bh) {
    // The operator should signal IllegalArgumentException.
    try {
        multipleElementsMaybe.blockingGet();
        // If no exception, consume a sentinel to avoid dead code elimination.
        bh.consume("no-error");
    } catch (IllegalArgumentException expected) {
        bh.consume(expected);
    } catch (Throwable t) {
        // Any other unexpected throwable is also consumed.
        bh.consume(t);
    }
}
```

### Method 34

```java
@Benchmark
public void parallelDoOnNextTry(Blackhole bh) throws InterruptedException {
    // Wrap the source with the operator under test
    ParallelDoOnNextTry<Integer> operator = new ParallelDoOnNextTry<>(source, onNextConsumer, errorHandler);
    // Latch to wait for all parallel rails to finish
    CountDownLatch latch = new CountDownLatch(parallelism);
    // Prepare subscribers for each rail
    @SuppressWarnings("unchecked")
    FlowableSubscriber<? super Integer>[] subscribers = new FlowableSubscriber[parallelism];
    for (int i = 0; i < parallelism; i++) {
        subscribers[i] = new BlackholeSubscriber<>(bh, latch);
    }
    // Subscribe the parallel flowable
    operator.subscribe(subscribers);
    // Wait for completion
    latch.await();
}
```

### Method 35

```java
@Benchmark
public void parallelFilter(Blackhole bh, BenchmarkState state) throws InterruptedException {
    CountDownLatch latch = new CountDownLatch(state.parallelism);
    @SuppressWarnings("unchecked")
    Subscriber<Integer>[] subscribers = new Subscriber[state.parallelism];
    for (int i = 0; i < state.parallelism; i++) {
        subscribers[i] = new Subscriber<Integer>() {

            Subscription upstream;

            @Override
            public void onSubscribe(Subscription s) {
                this.upstream = s;
                s.request(Long.MAX_VALUE);
            }

            @Override
            public void onNext(Integer t) {
                bh.consume(t);
            }

            @Override
            public void onError(Throwable t) {
                latch.countDown();
            }

            @Override
            public void onComplete() {
                latch.countDown();
            }
        };
    }
    state.source.filter(state.predicate).subscribe(subscribers);
    latch.await();
}
```

### Method 36

```java
@Benchmark
public void parallelFromPublisherThroughput(BenchmarkConsumer consumer) throws InterruptedException {
    // Create an array of subscribers – one per rail.
    Subscriber<Integer>[] subs = new Subscriber[parallelism];
    for (int i = 0; i < parallelism; i++) {
        subs[i] = new DrainSubscriber<>(consumer.latch, consumer.received);
    }
    // Subscribe the parallel operator.
    operator.subscribe(subs);
    // Wait until all rails have completed.
    consumer.latch.await();
}
```

### Method 37

```java
@Benchmark
public void predicateThrows(Blackhole bh) {
    // Predicate throws an exception → the operator propagates the error.
    try {
        sourceError.all(throwsException).blockingGet();
    } catch (Throwable t) {
        // Expected path; consume to avoid dead‑code elimination.
        bh.consume(t);
    }
}
```

### Method 38

```java
@Benchmark
public void publishThroughput(Blackhole bh) throws Exception {
    CountDownLatch latch = new CountDownLatch(subscriberCount);
    // Subscribe the requested number of observers.
    for (int i = 0; i < subscriberCount; i++) {
        publish.subscribe(new Observer<Integer>() {

            @Override
            public void onSubscribe(Disposable d) {
                /* no‑op */
            }

            @Override
            public void onNext(Integer value) {
                // Consume the value to avoid dead‑code elimination.
                bh.consume(value);
            }

            @Override
            public void onError(Throwable e) {
                // Treat error as completion for latch counting.
                latch.countDown();
            }

            @Override
            public void onComplete() {
                latch.countDown();
            }
        });
    }
    // Connect the publish operator; the Disposable is ignored for the benchmark.
    publish.connect(d -> {
        /* no‑op */
    });
    // Wait until all subscribers have received the terminal event.
    latch.await();
}
```

### Method 39

```java
@Benchmark
public void removeSingle() {
    // first fill the composite
    composite.addAll(disposables);
    // then remove one by one
    for (Disposable d : disposables) {
        composite.remove(d);
    }
}
```

### Method 40

```java
@Benchmark
public void requestZero() {
    // Zero is illegal and triggers the error path; we catch the exception to keep the benchmark running
    try {
        strictSubscriber.request(0L);
    } catch (IllegalArgumentException ignored) {
        // ignored – the benchmark measures the cost of the validation path
    }
}
```

### Method 41

```java
@Benchmark
public void singleElement(Blackhole bh) {
    // blockingGet() returns the value or throws; we consume the result with Blackhole.
    try {
        Integer v = singleElementMaybe.blockingGet();
        bh.consume(v);
    } catch (Throwable t) {
        // Should not happen for the single‑element case.
        bh.consume(t);
    }
}
```

### Method 42

```java
@Benchmark
public void subscribeAndConsume(BenchmarkState state, Blackhole bh) {
    if (state.conditional) {
        ConditionalSubscriber<Integer> subscriber = new ConditionalSubscriber<Integer>() {

            @Override
            public void onSubscribe(org.reactivestreams.Subscription s) {
                // request according to mode
                if (state.mode == Mode.FAST) {
                    s.request(Long.MAX_VALUE);
                } else {
                    s.request(state.arraySize);
                }
            }

            @Override
            public void onNext(Integer integer) {
                // not used, tryOnNext is preferred
            }

            @Override
            public void onError(Throwable t) {
                t.printStackTrace();
            }

            @Override
            public void onComplete() {
                // no-op
            }

            @Override
            public boolean tryOnNext(Integer t) {
                bh.consume(t);
                // count every element as "accepted"
                return true;
            }
        };
        state.flowable.subscribe(subscriber);
    } else {
        DefaultSubscriber<Integer> subscriber = new DefaultSubscriber<Integer>() {

            @Override
            public void onStart() {
                // request according to mode
                if (state.mode == Mode.FAST) {
                    request(Long.MAX_VALUE);
                } else {
                    request(state.arraySize);
                }
            }

            @Override
            public void onNext(Integer t) {
                bh.consume(t);
            }

            @Override
            public void onError(Throwable t) {
                t.printStackTrace();
            }

            @Override
            public void onComplete() {
                // no-op
            }
        };
        // DefaultSubscriber implements onStart() which is called by RxJava's subscribe()
        state.flowable.subscribe(subscriber);
    }
}
```

### Method 43

```java
@Benchmark
public void subscribeAndError(Blackhole bh, SubscribeErrorState state) {
    for (NoOpObserver<Integer> o : state.observers) {
        state.subject.subscribe(o);
    }
    state.subject.onError(new RuntimeException("benchmark"));
    bh.consume(state.subject.getThrowable());
}
```

### Method 44

```java
@Benchmark
public void subscribeAndReplaySizeBounded(Blackhole bh) {
    for (int i = 0; i < batchSize; i++) {
        sizeBounded.onNext(i);
    }
    sizeBounded.subscribe(new BlackholeSubscriber(bh));
}
```

### Method 45

```java
@Benchmark
public void subscribeAndReplayTimeAndSizeBounded(Blackhole bh) {
    for (int i = 0; i < batchSize; i++) {
        timeAndSizeBounded.onNext(i);
    }
    timeAndSizeBounded.subscribe(new BlackholeSubscriber(bh));
}
```

### Method 46

```java
@Benchmark
public void timeoutWithoutFallback(Blackhole bh) {
    try {
        operatorTimeoutWithoutFallback.blockingGet();
        // Should not reach here; a TimeoutException is expected.
        bh.consume(false);
    } catch (Throwable t) {
        // The operator signals a TimeoutException as an error.
        if (t instanceof java.util.concurrent.TimeoutException) {
            bh.consume(true);
        } else {
            bh.consume(t);
        }
    }
}
```

### Method 47

```java
@Benchmark
public void timeoutWithoutFallback(Blackhole bh) {
    try {
        operatorTimeoutWithoutFallback.blockingGet();
        // Should not reach here; a TimeoutException is expected.
        bh.consume(false);
    } catch (Throwable t) {
        // The operator signals a TimeoutException as an error.
        if (t instanceof java.util.concurrent.TimeoutException) {
            bh.consume(true);
        } else {
            bh.consume(t);
        }
    }
}
```

### Method 48

```java
@Benchmark
public void wrapOrThrow_error(WrapOrThrowState s, Blackhole bh) {
    try {
        ExceptionHelper.wrapOrThrow(s.error);
    } catch (Throwable t) {
        // The method is expected to re‑throw the Error; consume it to avoid benchmark failure.
        bh.consume(t);
    }
}
```

## JMH IGNORED STATIC METHOD RETURN - Static method return not used or consumed by a Blackhole.

### Method 1

```java
/**
 * Baseline benchmark that measures the throughput of the source Observable alone.
 *
 * @param bh Blackhole to consume emitted items.
 */
@Benchmark
public void baseline(Blackhole bh) {
    baseline.blockingSubscribe(bh::consume);
}
```

### Method 2

```java
/**
 * Baseline benchmark without the scan operator to help isolate its overhead.
 */
@Benchmark
public void baselineThroughput(Blackhole bh) {
    source.subscribe(bh::consume);
}
```

### Method 3

```java
/**
 * Baseline benchmark without the {@code defer} operator.
 *
 * <p>This provides a reference point to understand the overhead introduced by
 * {@code FlowableDefer}.
 */
@Benchmark
public void direct(Blackhole bh) {
    directFlowable.blockingSubscribe(bh::consume);
}
```

### Method 4

```java
/**
 * Baseline: subscribe to the source without any scheduling indirection.
 */
@Benchmark
public void baseline(BenchmarkState state, Blackhole bh) {
    state.source.blockingSubscribe(bh::consume);
}
```

### Method 5

```java
/**
 * Benchmark a non‑scalar mapping scenario where the mapper returns a
 * Publisher that does not implement {@code Supplier}. This forces the
 * fallback path inside {@code scalarXMap}.
 */
@Benchmark
public void scalarXMapNonScalar(Blackhole bh) {
    Flowable<Integer> flowable = FlowableScalarXMap.scalarXMap(value, nonScalarMapper);
    flowable.blockingSubscribe(bh::consume);
}
```

### Method 6

```java
/**
 * Benchmark a regular Flowable.map() path for comparison.
 *
 * This uses Flowable.just(value) followed by a standard map operator,
 * which also ends up on the scalar path but goes through the regular
 * operator chain, providing a baseline.
 */
@Benchmark
public void regularMap(Blackhole bh) {
    Flowable<Integer> flowable = Flowable.just(value).map(v -> v + 1);
    flowable.blockingSubscribe(bh::consume);
}
```

### Method 7

```java
/**
 * Benchmark for integer streams.
 */
@Benchmark
public void reduceInt(Blackhole bh) {
    Flowable<Integer> reduced = new FlowableOnBackpressureReduce<>(intSource, intReducer);
    reduced.blockingSubscribe(bh::consume);
}
```

### Method 8

```java
/**
 * Benchmark for string concatenation (object allocation heavy).
 */
@Benchmark
public void reduceString(Blackhole bh) {
    if (!"concat".equals(reducerType)) {
        return;
    }
    Flowable<String> reduced = new FlowableOnBackpressureReduce<>(stringSource, stringReducer);
    reduced.blockingSubscribe(bh::consume);
}
```

### Method 9

```java
/**
 * Benchmark method that applies {@code onBackpressureLatest} to the source
 * and consumes all emitted items via {@link Blackhole}.
 *
 * @param bh Blackhole to consume items and avoid dead‑code elimination.
 */
@Benchmark
public void onBackpressureLatestThroughput(Blackhole bh) {
    source.onBackpressureLatest(NO_OP_DROP).blockingSubscribe(bh::consume, bh::consume);
}
```

### Method 10

```java
/**
 * Benchmark method that applies {@code skipUntil} and consumes the resulting
 * stream. The {@link Blackhole} is used to prevent dead‑code elimination.
 */
@Benchmark
public void skipUntilThroughput(Blackhole bh) {
    source.skipUntil(trigger).blockingSubscribe(bh::consume);
}
```

### Method 11

```java
/**
 * Benchmark method that concatenates the upstream Observable with the Single
 * using the internal {@link ObservableConcatWithSingle} operator and consumes
 * all emitted items via a Blackhole.
 *
 * @param bh Blackhole to consume the items and avoid dead‑code elimination.
 */
@Benchmark
public void concatWithSingle(Blackhole bh) {
    // Directly instantiate the internal operator to avoid extra operator wrapping.
    Observable<Integer> concat = new ObservableConcatWithSingle<>(upstream, single);
    // Subscribe and block until completion, feeding each item into the Blackhole.
    concat.blockingSubscribe(bh::consume);
}
```

### Method 12

```java
/**
 * Benchmark method that measures how many complete subscriptions can be performed per second.
 *
 * @param bh Blackhole to consume emitted items and prevent dead‑code elimination.
 */
@Benchmark
public void subscribeAndConsume(Blackhole bh) {
    // blockingSubscribe ensures the subscription finishes before the next iteration starts.
    operator.blockingSubscribe(bh::consume);
}
```

### Method 13

```java
/**
 * Benchmark method that pushes a batch of items through the {@code onBackpressureDrop}
 * operator and consumes them via {@link Blackhole}.
 *
 * @param state shared benchmark state
 * @param bh    Blackhole to consume items and prevent dead‑code elimination
 */
@Benchmark
public void backpressureDropThroughput(BenchmarkState state, Blackhole bh) {
    // Emit a batch of items; the operator will drop none because the subscriber
    // requests Long.MAX_VALUE.
    state.emitBatch();
    // Drain the subscriber's internal queue by consuming all items that have arrived.
    // Since the subscriber does not store items, we rely on the fact that the
    // Flowable's internal mechanisms will deliver items to the Blackhole via the
    // onNext hook we set up in the subscriber.
    // To make the consumption visible to JMH, we subscribe a temporary consumer
    // that forwards to Blackhole.
    state.source.subscribe(bh::consume);
}
```

### Method 14

```java
/**
 * Benchmark method that subscribes to the Flowable, consumes all items,
 * and blocks until completion. The {@link Blackhole} ensures the consumed
 * values are not optimized away.
 *
 * @param bh Blackhole to consume emitted items.
 */
@Benchmark
public void subscribeAndConsume(Blackhole bh) {
    flowable.blockingSubscribe(bh::consume);
}
```

### Method 15

```java
/**
 * Benchmark method that subscribes to the FlowableFlatMapStream operator,
 * consumes all emitted items, and blocks until completion.
 *
 * @param bh Blackhole to consume items and prevent dead‑code elimination.
 */
@Benchmark
public void flatMapStreamThroughput(Blackhole bh) {
    // Create the operator instance
    Flowable<Integer> flatMapped = new FlowableFlatMapStream<>(source, mapper, prefetch);
    // Subscribe and block, consuming each item with the Blackhole
    flatMapped.blockingSubscribe(bh::consume);
}
```

### Method 16

```java
/**
 * Benchmark method that subscribes to the FlowableMapOptional,
 * consumes all emitted items, and blocks until completion.
 *
 * @param bh Blackhole to consume emitted items and avoid dead‑code elimination.
 */
@Benchmark
public void mapOptionalThroughput(Blackhole bh) {
    flowableUnderTest.subscribe(bh::consume);
    // The subscription is synchronous for the range source, so no explicit
    // blocking is required. If an asynchronous source were used, one would
    // need to block (e.g., using blockingSubscribe()).
}
```

### Method 17

```java
/**
 * Benchmark method that subscribes to the FlowableRepeatUntil and consumes all items.
 * The Blackhole ensures that the emitted values are not optimized away.
 */
@Benchmark
public void repeatUntilThroughput(Blackhole bh) {
    // blockingSubscribe will block until the sequence completes,
    // which is appropriate for a throughput measurement.
    repeatUntilFlowable.blockingSubscribe(bh::consume);
}
```

### Method 18

```java
/**
 * Benchmark method that subscribes to the FlowableSwitchMapMaybe and consumes all emitted items.
 * The {@link Blackhole} ensures that the JIT compiler does not eliminate the consumption.
 */
@Benchmark
public void switchMapMaybeThroughput(Blackhole bh) {
    // Use blockingForEach to synchronously consume all items.
    flowableSwitchMapMaybe.blockingForEach(bh::consume);
}
```

### Method 19

```java
/**
 * Benchmark method that subscribes to the ObservableGenerate and consumes all emitted items.
 *
 * @param bh Blackhole to consume the items and avoid dead‑code elimination.
 */
@Benchmark
public void generateAndConsume(Blackhole bh) {
    // blockingSubscribe ensures the benchmark measures the full generation cycle.
    observable.blockingSubscribe(bh::consume);
}
```

### Method 20

```java
/**
 * Benchmark method that subscribes to the buffered Flowable and blocks until completion.
 * The emitted buffers are consumed by a Blackhole to avoid dead‑code elimination.
 */
@Benchmark
public void bufferTimedThroughput(Blackhole bh) {
    // blockingSubscribe ensures the benchmark measures the full processing of the stream.
    bufferedFlowable.blockingSubscribe(bh::consume);
}
```

### Method 21

```java
/**
 * Benchmark method that subscribes to the buffered observable and consumes all emitted buffers.
 *
 * @param bh Blackhole to consume the buffers and prevent dead‑code elimination.
 */
@Benchmark
public void bufferBoundaryThroughput(Blackhole bh) {
    // blockingSubscribe ensures the method returns only after the whole stream has been processed.
    bufferedObservable.blockingSubscribe(bh::consume);
}
```

### Method 22

```java
/**
 * Benchmark method that subscribes to the filtered Observable and consumes all items.
 *
 * @param bh Blackhole to consume the emitted items and avoid dead‑code elimination.
 */
@Benchmark
public void filterAndConsume(Blackhole bh) {
    source.filter(predicate).subscribe(bh::consume);
}
```

### Method 23

```java
/**
 * Benchmark method that subscribes to the materialized Observable and consumes all notifications.
 *
 * @param bh Blackhole to consume the emitted {@link Notification}s and prevent dead‑code elimination.
 */
@Benchmark
public void materialize(Blackhole bh) {
    // blockingSubscribe ensures the whole stream is processed within the benchmark iteration.
    materialized.blockingSubscribe(bh::consume);
}
```

### Method 24

```java
/**
 * Benchmark method that subscribes to the operator and consumes all items.
 *
 * @param bh Blackhole to consume emitted values and avoid dead‑code elimination.
 */
@Benchmark
public void onErrorNextThroughput(Blackhole bh) {
    // blockingSubscribe ensures the benchmark measures the complete execution path.
    operatorObservable.blockingSubscribe(bh::consume);
}
```

### Method 25

```java
/**
 * Benchmark method that subscribes to the operator and consumes all items.
 *
 * @param bh Blackhole to consume the emitted values.
 */
@Benchmark
public void testPublishSelector(Blackhole bh) {
    // Subscribe and block until completion, feeding each item to the Blackhole.
    operator.blockingSubscribe(bh::consume);
}
```

### Method 26

```java
/**
 * Benchmark method that subscribes to the operator and consumes all items.
 *
 * The subscription is performed using {@code blockingSubscribe} to ensure the
 * benchmark measures the complete processing of the stream.
 */
@Benchmark
public void withLatestFromMany(Blackhole bh) {
    // Apply the operator.
    Flowable<Integer> combined = new FlowableWithLatestFromMany<>(source, others, combiner);
    // Consume all items, feeding them into the Blackhole to prevent dead-code elimination.
    combined.blockingSubscribe(bh::consume);
}
```

### Method 27

```java
/**
 * Benchmark method that subscribes to the switchMapMaybe chain and consumes
 * all emitted items. The subscription is performed on each iteration to
 * include the full cost of the operator.
 *
 * @param bh Blackhole to consume the items and avoid dead‑code elimination.
 */
@Benchmark
public void switchMapMaybeThroughput(Blackhole bh) {
    Observable<String> result = source.switchMapMaybe(mapper);
    // blockingSubscribe ensures the benchmark thread waits for completion.
    result.blockingSubscribe(bh::consume);
}
```

### Method 28

```java
/**
 * Benchmark method that subscribes to the throttled Flowable and consumes all emitted items.
 * The Blackhole ensures that the consumed values are not optimized away.
 */
@Benchmark
public void throttleFirstTimed(Blackhole bh) {
    throttled.blockingSubscribe(bh::consume);
}
```

### Method 29

```java
/**
 * Benchmark method that subscribes to the {@link SingleFlatMapObservable},
 * blocks until completion, and consumes the emitted items via {@link Blackhole}
 * to prevent dead‑code elimination.
 *
 * @param bh Blackhole to consume emitted values.
 */
@Benchmark
public void flatMapSingleToObservable(Blackhole bh) {
    new SingleFlatMapObservable<>(source, mapper).blockingSubscribe(bh::consume);
}
```

### Method 30

```java
/**
 * Benchmark that applies the buffer operator and consumes all emitted collections.
 * The buffer supplier creates a new {@link ArrayList} for each buffer.
 *
 * @param state shared benchmark state
 * @param bh    JMH blackhole to consume the buffered collections
 */
@Benchmark
public void bufferOperator(BenchmarkState state, Blackhole bh) {
    state.source.buffer(state.count, state.skip, ArrayList::new).blockingSubscribe(bh::consume);
}
```

### Method 31

```java
/**
 * Benchmark that applies the {@code window} operator and then flattens the
 * windows back into a single stream, consuming each element with a Blackhole.
 *
 * The flattening step ensures that the benchmark measures the full cost of
 * window creation, emission, and completion.
 */
@Benchmark
public void windowAndFlatten(Blackhole bh) {
    source.window(count, skip, capacityHint).flatMap(w -> w).subscribe(bh::consume, bh::consume, () -> {
    });
}
```

### Method 32

```java
/**
 * Benchmark that subscribes to the concatenated Observable and consumes all
 * emitted items using a {@link Blackhole}. The subscription is performed
 * synchronously via {@code blockingForEach} to keep the measurement focused
 * on the operator's overhead rather than thread scheduling.
 *
 * @param bh Blackhole to consume the emitted items.
 */
@Benchmark
public void concatWithMaybeThroughput(Blackhole bh) {
    concatenated.blockingForEach(bh::consume);
}
```

### Method 33

```java
/**
 * Benchmark that subscribes to the flat‑mapped Observable and consumes all items.
 *
 * @param bh Blackhole to consume emitted values.
 */
@Benchmark
public void flatMapStreamThroughput(Blackhole bh) {
    // The operator under test.
    Observable<Integer> flatMapped = new ObservableFlatMapStream<>(source, mapper);
    // Subscribe and consume all items; blockingSubscribe ensures the benchmark
    // measures the complete processing of one subscription.
    flatMapped.blockingSubscribe(bh::consume);
}
```

### Method 34

```java
/**
 * Benchmark that subscribes to the scanned Observable and consumes all emitted items.
 * The subscription runs synchronously because the source is a cold, non‑async Observable.
 */
@Benchmark
public void scanThroughput(Blackhole bh) {
    source.scan(accumulator).subscribe(bh::consume);
}
```

### Method 35

```java
/**
 * Benchmark that subscribes to the source, applies {@code distinctUntilChanged}
 * with an identity key selector, and consumes all emitted items via {@link Blackhole}.
 *
 * The subscription is performed using {@code blockingSubscribe} to ensure the
 * benchmark measures the complete processing of the stream.
 *
 * @param bh Blackhole to consume the items and avoid dead‑code elimination.
 */
@Benchmark
public void distinctUntilChanged(Blackhole bh) {
    source.distinctUntilChanged(IDENTITY).blockingSubscribe(bh::consume);
}
```

### Method 36

```java
/**
 * Benchmark that subscribes to the {@code takeLast} operator and drains all
 * items, feeding them into the Blackhole.
 *
 * @param bh Blackhole to consume the emitted items.
 */
@Benchmark
public void takeLastThroughput(Blackhole bh) {
    // Apply the operator with the configured count.
    Flowable<Integer> flow = source.takeLast(takeCount);
    // blockingSubscribe ensures the benchmark measures the complete
    // processing of the stream while preventing dead‑code elimination.
    flow.blockingSubscribe(bh::consume);
}
```

### Method 37

```java
/**
 * Benchmark that subscribes to the {@code take} Flowable and consumes all
 * emitted items using {@link Blackhole}. The subscription is performed
 * synchronously via {@code blockingSubscribe} to ensure the benchmark
 * measures the complete processing of the stream.
 *
 * @param bh Blackhole to consume items and avoid dead‑code elimination.
 */
@Benchmark
public void takeAndConsume(Blackhole bh) {
    // blockingSubscribe guarantees that the method returns only after
    // the upstream has completed, giving a clean measurement of the
    // whole pipeline.
    takeFlowable.blockingSubscribe(bh::consume);
}
```

### Method 38

```java
/**
 * Benchmark that subscribes to {@link ObservableFlattenIterable},
 * consumes all emitted items via a {@link Blackhole}, and completes.
 *
 * The use of {@code blockingSubscribe} guarantees that the method returns
 * only after the whole stream has been processed, providing a clean measurement
 * of end‑to‑end throughput.
 */
@Benchmark
public void flattenIterable(BenchmarkState state, Blackhole bh) {
    new ObservableFlattenIterable<>((ObservableSource<Integer>) state.source, state.mapper).blockingSubscribe(bh::consume);
}
```

### Method 39

```java
/**
 * Benchmark the concatMap operator in its default (IMMEDIATE error) mode.
 *
 * @param bh Blackhole to consume the emitted items and avoid dead‑code elimination.
 */
@Benchmark
public void concatMapThroughput(Blackhole bh) {
    source.concatMap(mapper).subscribe(bh::consume);
}
```

### Method 40

```java
/**
 * Benchmark the dispose path of {@link SingleDoOnDispose}.
 *
 * The subscription is immediately disposed, triggering the {@code onDispose} Action.
 */
@Benchmark
public void disposePath(Blackhole bh) {
    // Subscribe with a dummy observer that does nothing on success/error.
    Disposable d = // onSuccess consumer (won't be called)
    doOnDisposeSingle.// onSuccess consumer (won't be called)
    subscribe(// onError consumer (won't be called)
    bh::consume, bh::consume);
    // Immediately dispose to exercise the doOnDispose logic.
    d.dispose();
    // Consume the counter to prevent dead‑code elimination of the Action.
    bh.consume(disposeCounter.get());
}
```

### Method 41

```java
/**
 * Benchmark the dispose path of {@link SingleDoOnDispose}.
 *
 * The subscription is immediately disposed, triggering the {@code onDispose} Action.
 */
@Benchmark
public void disposePath(Blackhole bh) {
    // Subscribe with a dummy observer that does nothing on success/error.
    Disposable d = // onSuccess consumer (won't be called)
    doOnDisposeSingle.// onSuccess consumer (won't be called)
    subscribe(// onError consumer (won't be called)
    bh::consume, bh::consume);
    // Immediately dispose to exercise the doOnDispose logic.
    d.dispose();
    // Consume the counter to prevent dead‑code elimination of the Action.
    bh.consume(disposeCounter.get());
}
```

### Method 42

```java
/**
 * Benchmark the eager disposal path.
 *
 * @param bh Blackhole to consume emitted items.
 */
@Benchmark
public void eager(Blackhole bh) {
    // Subscribe and block until completion, feeding each item to the Blackhole.
    eagerObservable.blockingSubscribe(bh::consume, bh::consume, () -> {
    });
}
```

### Method 43

```java
/**
 * Benchmark the flatMap operator in throughput mode.
 *
 * @param bh Blackhole to consume the emitted items and prevent dead-code elimination.
 */
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
public void flatMapThroughput(Blackhole bh) {
    source.flatMap(mapper, delayErrors, maxConcurrency, bufferSize).subscribe(bh::consume);
}
```

### Method 44

```java
/**
 * Benchmark the flatMapSingle operator with a simple mapper that returns
 * {@code Single.just(i)}. The downstream consumes the values via Blackhole.
 *
 * @param bh Blackhole to consume emitted items and avoid dead‑code elimination.
 */
@Benchmark
public void flatMapSingle(Blackhole bh) {
    source.flatMapSingle(i -> Single.just(i * 2)).blockingSubscribe(bh::consume);
}
```

### Method 45

```java
/**
 * Benchmark the lazy (non‑eager) disposal path.
 *
 * @param bh Blackhole to consume emitted items.
 */
@Benchmark
public void lazy(Blackhole bh) {
    lazyObservable.blockingSubscribe(bh::consume, bh::consume, () -> {
    });
}
```

### Method 46

```java
/**
 * Benchmark the mergeWith operation. The subscription is performed inside the benchmark
 * method to include the full lifecycle (subscription, request, emission, completion).
 * {@link Blackhole#consume(Object)} guarantees that the emitted items are observed.
 */
@Benchmark
public void mergeWithMaybe(Blackhole bh) {
    source.mergeWith(other).blockingSubscribe(bh::consume);
}
```

### Method 47

```java
/**
 * Benchmark the onComplete → supplier path.
 */
@Benchmark
public void completePath(Blackhole bh) {
    // Source that completes without a value.
    Maybe<Integer> source = Maybe.empty();
    Maybe<String> operator = new MaybeFlatMapNotification<>(source, successMapper, errorMapper, completeSupplier);
    operator.blockingSubscribe(bh::consume, bh::consume, () -> bh.consume("completed"));
}
```

### Method 48

```java
/**
 * Benchmark the onError → mapper path.
 */
@Benchmark
public void errorPath(Blackhole bh) {
    // Source that terminates with an exception.
    Maybe<Integer> source = Maybe.error(new IllegalStateException("boom"));
    Maybe<String> operator = new MaybeFlatMapNotification<>(source, successMapper, errorMapper, completeSupplier);
    // blockingSubscribe returns after onError/onComplete.
    operator.blockingSubscribe(bh::consume, bh::consume, () -> bh.consume("completed"));
}
```

### Method 49

```java
/**
 * Benchmark the path where the predicate does not swallow the error and the downstream receives {@code onError}.
 */
@Benchmark
public void onErrorComplete_propagateError(Blackhole bh) {
    // onSuccess (won't be called)
    propagateOnError.// onSuccess (won't be called)
    blockingSubscribe(// onError (expected)
    bh::consume, // onComplete (won't be called)
    bh::consume, () -> {
    });
}
```

### Method 50

```java
/**
 * Benchmark the path where the predicate does not swallow the error and the downstream receives {@code onError}.
 */
@Benchmark
public void onErrorComplete_propagateError(Blackhole bh) {
    // onSuccess (won't be called)
    propagateOnError.// onSuccess (won't be called)
    blockingSubscribe(// onError (expected)
    bh::consume, // onComplete (won't be called)
    bh::consume, () -> {
    });
}
```

### Method 51

```java
/**
 * Benchmark the path where the predicate swallows the error and the downstream receives {@code onComplete}.
 */
@Benchmark
public void onErrorComplete_swallowError(Blackhole bh) {
    // blockingSubscribe blocks until termination, ensuring the whole chain is executed.
    // onSuccess (won't be called)
    completeOnError.// onSuccess (won't be called)
    blockingSubscribe(// onError (won't be called)
    bh::consume, // onComplete
    bh::consume, () -> {
    });
}
```

### Method 52

```java
/**
 * Benchmark the path where the predicate swallows the error and the downstream receives {@code onComplete}.
 */
@Benchmark
public void onErrorComplete_swallowError(Blackhole bh) {
    // blockingSubscribe blocks until termination, ensuring the whole chain is executed.
    // onSuccess (won't be called)
    completeOnError.// onSuccess (won't be called)
    blockingSubscribe(// onError (won't be called)
    bh::consume, // onComplete
    bh::consume, () -> {
    });
}
```

### Method 53

```java
/**
 * Benchmark the scalarXMap optimization path.
 *
 * The FlowableScalarXMap.scalarXMap method creates a Flowable that, when
 * subscribed to, should take the fast scalar route because both the source
 * value and the mapper result implement {@code Supplier}.
 */
@Benchmark
public void scalarXMap(Blackhole bh) {
    Flowable<Integer> flowable = FlowableScalarXMap.scalarXMap(value, scalarMapper);
    flowable.blockingSubscribe(bh::consume);
}
```

### Method 54

```java
/**
 * Benchmark the success path (no disposal) for comparison.
 *
 * This measures the overhead of the operator when the stream completes normally.
 */
@Benchmark
public void successPath(Blackhole bh) {
    // Subscribe and let the Single emit its value.
    // onSuccess
    doOnDisposeSingle.// onSuccess
    subscribe(// onError
    bh::consume, bh::consume);
    // No explicit dispose – the upstream disposes itself after onSuccess.
}
```

### Method 55

```java
/**
 * Benchmark the success path (no disposal) for comparison.
 *
 * This measures the overhead of the operator when the stream completes normally.
 */
@Benchmark
public void successPath(Blackhole bh) {
    // Subscribe and let the Single emit its value.
    // onSuccess
    doOnDisposeSingle.// onSuccess
    subscribe(// onError
    bh::consume, bh::consume);
    // No explicit dispose – the upstream disposes itself after onSuccess.
}
```

### Method 56

```java
/**
 * Benchmark the throughput of converting a {@code Maybe.just} into an {@code Observable}
 * and consuming the emitted value.
 *
 * @param bh Blackhole to consume the emitted item and avoid dead‑code elimination.
 */
@Benchmark
public void justThroughput(Blackhole bh) {
    // blockingSubscribe ensures the subscription completes before the method returns.
    justOperator.blockingSubscribe(bh::consume);
}
```

### Method 57

```java
/**
 * Benchmark the throughput of the {@code concatWith} operator.
 *
 * @param bh Blackhole to consume emitted items.
 */
@Benchmark
public void concatWithCompletable(Blackhole bh) {
    // Subscribe and block until the stream terminates.
    concatWithCompletable.blockingSubscribe(bh::consume);
}
```

### Method 58

```java
/**
 * Benchmark the throughput of {@code source.takeUntil(other)}.
 *
 * @param bh Blackhole to consume the emitted items.
 */
@Benchmark
public void takeUntil(Blackhole bh) {
    source.takeUntil(other).blockingSubscribe(bh::consume);
}
```

### Method 59

```java
/**
 * Benchmark the throughput of {@link FlowableMapNotification} in the normal onNext path.
 *
 * @param bh Blackhole to consume the downstream values and prevent dead‑code elimination.
 */
@Benchmark
public void mapNotificationThroughput(Blackhole bh) {
    // Create the operator instance with the prepared mappers.
    Flowable<Integer> mapped = new FlowableMapNotification<>(source, onNextMapper, onErrorMapper, onCompleteSupplier);
    // Subscribe and consume all items; the subscription is synchronous for the range source.
    mapped.subscribe(bh::consume);
}
```

### Method 60

```java
/**
 * Benchmark the timeout operator with a fallback Observable.
 * The timeout indicator never fires, so the fallback is never used.
 */
@Benchmark
public void timeoutWithFallback(Blackhole bh) {
    source.timeout(neverTimeout, i -> neverTimeout, fallback).subscribe(bh::consume, bh::consume);
}
```

### Method 61

```java
/**
 * Benchmark the timeout operator without a fallback.
 * The timeout indicator never fires, so the operator should behave like a pass‑through.
 */
@Benchmark
public void timeoutWithoutFallback(Blackhole bh) {
    source.timeout(neverTimeout, i -> neverTimeout).subscribe(bh::consume, bh::consume);
}
```

### Method 62

```java
/**
 * Benchmark the {@code defer} operator.
 *
 * <p>Each operation subscribes to the {@code FlowableDefer} and consumes the emitted
 * value via {@link Blackhole}. The subscription is performed synchronously using
 * {@code blockingSubscribe} to ensure the whole pipeline is executed within the
 * benchmark iteration.
 */
@Benchmark
public void defer(Blackhole bh) {
    deferFlowable.blockingSubscribe(bh::consume);
}
```

### Method 63

```java
/**
 * Benchmark the {@code switchIfEmpty} operator when the upstream Observable is empty.
 *
 * <p>The fallback Observable is subscribed after the upstream completes.
 */
@Benchmark
public void switchIfEmpty_Empty(Blackhole bh) {
    emptySource.switchIfEmpty(fallback).subscribe(bh::consume);
}
```

### Method 64

```java
/**
 * Benchmark the {@code switchIfEmpty} operator when the upstream Observable is non‑empty.
 *
 * <p>The fallback Observable should never be subscribed.
 */
@Benchmark
public void switchIfEmpty_NonEmpty(Blackhole bh) {
    nonEmptySource.switchIfEmpty(fallback).subscribe(bh::consume);
}
```

### Method 65

```java
/**
 * Benchmark the {@code takeWhile} operator when the predicate never stops the stream.
 * This measures the steady‑state overhead of the operator.
 */
@Benchmark
public void takeWhileAlwaysTrue(BenchmarkState state, Blackhole bh) {
    state.takeWhileAlwaysTrue.subscribe(bh::consume);
}
```

### Method 66

```java
/**
 * Benchmark the {@code takeWhile} operator when the predicate stops the stream early.
 * This measures the cost of early termination logic.
 */
@Benchmark
public void takeWhileEarlyStop(BenchmarkState state, Blackhole bh) {
    state.takeWhileEarlyStop.subscribe(bh::consume);
}
```

### Method 67

```java
/**
 * Benchmark where the upstream Maybe emits a value.
 *
 * @param bh Blackhole to consume the emitted value and prevent dead‑code elimination.
 */
@Benchmark
public void switchIfEmpty_ValuePresent(Blackhole bh) {
    maybeWithValue.subscribe(bh::consume);
}
```

### Method 68

```java
/**
 * Benchmark where the upstream Maybe is empty and the operator switches to the fallback.
 *
 * @param bh Blackhole to consume the emitted value from the fallback.
 */
@Benchmark
public void switchIfEmpty_EmptySwitches(Blackhole bh) {
    maybeEmptySwitch.subscribe(bh::consume);
}
```

### Method 69

```java
/**
 * Consumes the Flowable with {@code doAfterNext} operator.
 *
 * @param bh Blackhole to consume the emitted items.
 */
@Benchmark
public void doAfterNextConsume(Blackhole bh) {
    withDoAfterNext.subscribe(bh::consume);
}
```

### Method 70

```java
/**
 * Consumes the baseline Flowable.
 *
 * @param bh Blackhole to consume the emitted items.
 */
@Benchmark
public void baselineConsume(Blackhole bh) {
    baseline.subscribe(bh::consume);
}
```

### Method 71

```java
/**
 * Consumes the concatenated sequence using a blocking subscription.
 *
 * @param bh Blackhole to consume the emitted items and avoid dead‑code elimination.
 */
@Benchmark
public void concatWithSingleThroughput(Blackhole bh) {
    // blockingForEach will subscribe, request all items, and block until completion.
    flowableWithSingle.blockingForEach(bh::consume);
}
```

### Method 72

```java
/**
 * Consumes the entire Flowable, measuring how many items per second can be processed.
 *
 * @param bh Blackhole to consume each emitted item and avoid dead‑code elimination.
 */
@Benchmark
public void skipLastThroughput(Blackhole bh) {
    // blockingSubscribe ensures the benchmark measures the full processing time.
    flowable.blockingSubscribe(bh::consume);
}
```

### Method 73

```java
/**
 * Consumes the entire sequence produced by the scan operator.
 * The Blackhole ensures that the consumed values are not optimized away.
 */
@Benchmark
public void scanSeed(Blackhole bh) {
    scanned.blockingForEach(bh::consume);
}
```

### Method 74

```java
/**
 * Consumes the entire sequence produced by the {@code takeUntil} operator.
 *
 * @param state shared benchmark state containing the prepared Flowable
 * @param bh    Blackhole to consume each emitted item
 */
@Benchmark
public void takeUntilThroughput(BenchmarkState state, Blackhole bh) {
    // Subscribe with a consumer that forwards each item to the Blackhole.
    // The subscription requests an unbounded amount (Long.MAX_VALUE) internally.
    state.flowable.subscribe(bh::consume);
}
```

### Method 75

```java
/**
 * Consumes the entire stream and feeds each item into the Blackhole.
 * The Blackhole prevents dead‑code elimination.
 */
@Benchmark
public void peekThroughput(Blackhole bh) {
    // Convert back to a sequential Flowable, then block and consume.
    peekOperator.sequential().subscribe(bh::consume);
    // Ensure the subscription has completed before returning.
    // The sequential Flowable blocks until termination.
    // No additional synchronization is required because the
    // subscription runs on the computation scheduler and the
    // main thread waits for completion.
}
```

### Method 76

```java
/**
 * Exact bounded windows: timespan == timeskip and maxSize < Long.MAX_VALUE.
 */
@Benchmark
public void exactBounded(Blackhole bh) {
    Flowable<Integer> source = Flowable.range(1, itemCount).subscribeOn(scheduler);
    source.window(timespanMs, TimeUnit.MILLISECONDS, scheduler, maxSize, restartTimerOnMaxSize, bufferSize).flatMap(w -> w).blockingSubscribe(bh::consume);
}
```

### Method 77

```java
/**
 * Exact buffering: size == skip.
 */
@Benchmark
public void exactBuffer(Blackhole bh) {
    source.buffer(size).subscribe(bh::consume, t -> bh.consume(t), () -> {
    });
}
```

### Method 78

```java
/**
 * Exact unbounded windows: timespan == timeskip and maxSize == Long.MAX_VALUE.
 */
@Benchmark
public void exactUnbounded(Blackhole bh) {
    Flowable<Integer> source = Flowable.range(1, itemCount).subscribeOn(scheduler);
    source.window(timespanMs, TimeUnit.MILLISECONDS, scheduler, bufferSize).flatMap(w -> w).blockingSubscribe(bh::consume);
}
```

### Method 79

```java
/**
 * Executes the Flowable and consumes all emitted items.
 *
 * @param bh Blackhole to consume items and avoid dead‑code elimination.
 */
@Benchmark
public void backpressureBufferThroughput(Blackhole bh) {
    // blockingSubscribe runs the whole stream synchronously and returns only after completion.
    testFlowable.blockingSubscribe(bh::consume);
}
```

### Method 80

```java
/**
 * Executes the benchmark. The subscription is performed for each iteration,
 * and emitted items are consumed by the {@link Blackhole} to avoid dead‑code
 * elimination.
 *
 * @param bh Blackhole to consume items and terminal signals.
 */
@Benchmark
public void runTimeoutOperator(Blackhole bh) {
    // onNext
    flowable.// onNext
    subscribe(// onError
    bh::consume, // onComplete (no value to consume)
    bh::consume, () -> {
    });
}
```

### Method 81

```java
/**
 * Executes the benchmark. The subscription is performed for each iteration,
 * and emitted items are consumed by the {@link Blackhole} to avoid dead‑code
 * elimination.
 *
 * @param bh Blackhole to consume items and terminal signals.
 */
@Benchmark
public void runTimeoutOperator(Blackhole bh) {
    // onNext
    flowable.// onNext
    subscribe(// onError
    bh::consume, // onComplete (no value to consume)
    bh::consume, () -> {
    });
}
```

### Method 82

```java
/**
 * Executes the concatMapSingle operator and consumes all resulting items.
 *
 * Uses the overload that accepts a mapper and a prefetch size.
 */
@Benchmark
public void concatMapSingleThroughput(Blackhole bh) {
    source.concatMapSingle(mapper, prefetch).blockingSubscribe(bh::consume);
}
```

### Method 83

```java
/**
 * Executes the flatMap operation and consumes all emitted items.
 *
 * @param bh Blackhole to consume the items and prevent dead‑code elimination.
 */
@Benchmark
public void flatMapObservable(Blackhole bh) {
    source.flatMapObservable(mapper).subscribe(bh::consume);
}
```

### Method 84

```java
/**
 * Executes the flatMapMaybe operator and consumes all emitted items.
 *
 * The benchmark measures how many complete flatMapMaybe executions can be performed per second.
 */
@Benchmark
public void flatMapMaybeThroughput(Blackhole bh) {
    // The blockingSubscribe ensures the whole stream is processed before the method returns.
    source.flatMapMaybe(mapper).blockingSubscribe(bh::consume);
}
```

### Method 85

```java
/**
 * Executes the flatMapMaybe operator and returns the total number of items processed.
 *
 * @param bh Blackhole to consume each emitted item and avoid dead‑code elimination.
 * @return the number of items emitted downstream (should equal {@code sourceSize}).
 */
@Benchmark
public long flatMapMaybe(Blackhole bh) {
    // Build the operator with the current parameters.
    Flowable<Integer> flow = new FlowableFlatMapMaybe<>(source, mapper, delayErrors, maxConcurrency);
    // Count the items downstream; the count operation itself is a Single<Long>.
    // We also consume each item with Blackhole to ensure the values are used.
    return flow.doOnNext(bh::consume).count().blockingGet();
}
```

### Method 86

```java
/**
 * Executes the materialize operator and consumes all notifications.
 *
 * @param bh Blackhole to consume the notifications and avoid dead‑code elimination.
 */
@Benchmark
public void materialize(Blackhole bh) {
    // materialize() converts each onNext/onError/onComplete into a Notification.
    // blockingForEach forces the Flowable to run to completion synchronously.
    source.materialize().blockingForEach(bh::consume);
}
```

### Method 87

```java
/**
 * Executes the mergeWith operator and consumes all emitted items.
 *
 * @param bh Blackhole to consume the items and avoid dead‑code elimination.
 */
@Benchmark
public void mergeWithSingle(Blackhole bh) {
    // Create a fresh merged Observable for each iteration to get a new subscription.
    Observable<Integer> merged = source.mergeWith(single);
    // blockingSubscribe guarantees the benchmark thread waits until the stream completes.
    merged.blockingSubscribe(bh::consume);
}
```

### Method 88

```java
/**
 * Executes the operator and consumes all emitted inner {@link ObservableSource}s.
 *
 * Using {@code blockingSubscribe} ensures the benchmark measures the full
 * end‑to‑end processing of the stream without introducing additional
 * asynchronous coordination overhead.
 */
@Benchmark
public void mapNotificationThroughput(Blackhole bh) {
    operator.blockingSubscribe(bh::consume);
}
```

### Method 89

```java
/**
 * Executes the operator and consumes the result.
 *
 * The {@link Blackhole} ensures the returned value is used, preventing the JIT
 * from optimizing away the whole call chain.
 */
@Benchmark
public void filterSingle(Blackhole bh) {
    // blockingGet() is appropriate for a micro‑benchmark; it forces the
    // subscription to complete synchronously.
    maybeFilterSingle.blockingSubscribe(bh::consume, bh::consume, () -> bh.consume(null));
}
```

### Method 90

```java
/**
 * Executes the parallel filter and consumes all emitted items.
 *
 * @param bh Blackhole to consume the items and prevent dead‑code elimination.
 */
@Benchmark
public void filterAndConsume(Blackhole bh) {
    // Convert back to a sequential Flowable and block until all items are processed.
    operator.sequential().blockingForEach(bh::consume);
}
```

### Method 91

```java
/**
 * Executes the repeat‑until flow and consumes all emitted items.
 *
 * <p>The {@link Blackhole} ensures that the JIT compiler cannot
 * eliminate the subscription logic as dead code.
 *
 * @param bh Blackhole to consume emitted items.
 */
@Benchmark
public void repeatUntil(Blackhole bh) {
    // blockingSubscribe is appropriate for a synchronous source and
    // guarantees that the benchmark measures the complete execution.
    repeatUntil.blockingSubscribe(bh::consume);
}
```

### Method 92

```java
/**
 * Executes the retry Observable and consumes the emitted value.
 * The {@link Blackhole} ensures the JIT does not eliminate the subscription.
 */
@Benchmark
public void retryThroughput(Blackhole bh) {
    // blockingSubscribe ensures the whole chain runs synchronously for the benchmark iteration
    // onNext
    retryObservable.// onNext
    blockingSubscribe(// onError (should not happen)
    bh::consume, // onComplete
    bh::consume, () -> {
    });
}
```

### Method 93

```java
/**
 * Executes the retry Observable and consumes the emitted value.
 * The {@link Blackhole} ensures the JIT does not eliminate the subscription.
 */
@Benchmark
public void retryThroughput(Blackhole bh) {
    // blockingSubscribe ensures the whole chain runs synchronously for the benchmark iteration
    // onNext
    retryObservable.// onNext
    blockingSubscribe(// onError (should not happen)
    bh::consume, // onComplete
    bh::consume, () -> {
    });
}
```

### Method 94

```java
/**
 * Executes the skip operator and consumes all resulting items.
 *
 * @param bh Blackhole to consume items and prevent dead-code elimination.
 */
@Benchmark
public void skipAndConsume(Blackhole bh) {
    // The blockingForEach call ensures the whole stream is processed before the benchmark method returns.
    source.skip(skipCount).blockingForEach(bh::consume);
}
```

### Method 95

```java
/**
 * Executes the skipLastTimed operator and consumes all emitted items.
 *
 * @param bh Blackhole to consume the items and avoid dead‑code elimination.
 */
@Benchmark
public void skipLastTimed(Blackhole bh) {
    source.skipLast(1, TimeUnit.MILLISECONDS, Schedulers.computation()).blockingForEach(bh::consume);
}
```

### Method 96

```java
/**
 * Executes the switchMap pipeline and consumes all emitted items.
 *
 * @param bh Blackhole to consume items and avoid dead‑code elimination.
 */
@Benchmark
public void switchMapThroughput(Blackhole bh) {
    // Subscribe synchronously; Observable.range and switchMap run on the calling thread.
    switched.subscribe(bh::consume);
}
```

### Method 97

```java
/**
 * Executes the whole flow and consumes the final reduced value.
 *
 * @param bh Blackhole to consume the result and avoid dead‑code elimination.
 */
@Benchmark
public void reduceWith(Blackhole bh) {
    // blockingSubscribe ensures the flow runs to completion within the benchmark iteration.
    flowable.blockingSubscribe(bh::consume);
}
```

### Method 98

```java
/**
 * Executes the {@code SingleFlatMapIterableObservable} pipeline and consumes all
 * emitted items with a {@link Blackhole}.
 *
 * @param bh Blackhole used to consume the items and avoid dead‑code elimination.
 */
@Benchmark
public void flatMapIterable(Blackhole bh) {
    Observable<Integer> observable = new SingleFlatMapIterableObservable<>(source, mapper);
    observable.subscribe(bh::consume);
}
```

### Method 99

```java
/**
 * Executes the {@code flatMapIterable} operator and consumes all emitted items.
 *
 * @param bh Blackhole to consume the items and prevent dead‑code elimination.
 */
@Benchmark
public void flatMapIterable(Blackhole bh) {
    observable.subscribe(bh::consume, bh::consume, () -> {
    });
}
```

### Method 100

```java
/**
 * Executes the {@code skipLastTimed} operator and drains the resulting stream.
 *
 * @param state per‑thread benchmark state containing the source Flowable.
 * @param bh    Blackhole to consume each emitted item and prevent dead‑code elimination.
 */
@Benchmark
public void skipLastTimedThroughput(BenchmarkState state, Blackhole bh) {
    new FlowableSkipLastTimed<>(state.source, 1L, TimeUnit.MILLISECONDS, state.scheduler, 128, false).blockingForEach(bh::consume);
}
```

### Method 101

```java
/**
 * Executes the {@code takeLast(1)} operator and consumes the emitted value.
 * The {@link Blackhole} ensures the JIT does not eliminate the subscription logic.
 *
 * @param state benchmark state containing the source Observable
 * @param bh    blackhole to consume the emitted item
 */
@Benchmark
public void takeLastOne(BenchmarkState state, Blackhole bh) {
    state.source.takeLast(1).blockingSubscribe(bh::consume);
}
```

### Method 102

```java
/**
 * Measures how many items per second can be processed through the debounce operator.
 * Each iteration processes exactly 1 000 items to keep the workload constant.
 *
 * @param state shared benchmark state
 * @param bh    JMH blackhole to consume the emitted values
 */
@Benchmark
public void debounceThroughput(BenchmarkState state, Blackhole bh) {
    // Take a fixed number of items to keep the benchmark duration bounded,
    // then block until all items have been consumed.
    state.debounced.take(1_000).blockingSubscribe(bh::consume);
}
```

### Method 103

```java
/**
 * Measures how many scan operations can be performed per second.
 *
 * @param bh Blackhole to consume emitted items and prevent dead‑code elimination.
 */
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
public void scanThroughput(Blackhole bh) {
    // Subscribe synchronously; the upstream is finite and completes quickly.
    source.scan(ACCUMULATOR).subscribe(bh::consume);
}
```

### Method 104

```java
/**
 * Measures the throughput of {@code source.repeat(repeatCount)} by consuming all items.
 *
 * <p>The {@link Blackhole} ensures that the emitted values are observed by the JVM,
 * preventing the JIT compiler from optimizing the whole pipeline away.
 *
 * @param bh Blackhole used to consume each emitted item.
 */
@Benchmark
public void repeatAndConsume(Blackhole bh) {
    // The blockingSubscribe call guarantees that the benchmark method returns only
    // after the entire sequence (including all repetitions) has been processed.
    source.repeat(repeatCount).blockingSubscribe(bh::consume);
}
```

### Method 105

```java
/**
 * Overlapping buffering: skip < size.
 */
@Benchmark
public void overlappingBuffer(Blackhole bh) {
    source.buffer(size, skip).subscribe(bh::consume, t -> bh.consume(t), () -> {
    });
}
```

### Method 106

```java
/**
 * Skip windows: timespan != timeskip.
 */
@Benchmark
public void skip(Blackhole bh) {
    Flowable<Integer> source = Flowable.range(1, itemCount).subscribeOn(scheduler);
    source.window(timespanMs, timeskipMs, TimeUnit.MILLISECONDS, scheduler, bufferSize).flatMap(w -> w).blockingSubscribe(bh::consume);
}
```

### Method 107

```java
/**
 * Skipping buffering: skip > size.
 */
@Benchmark
public void skipBuffer(Blackhole bh) {
    source.buffer(size, skip).subscribe(bh::consume, t -> bh.consume(t), () -> {
    });
}
```

### Method 108

```java
/**
 * Subscribe to the Completable and immediately dispose the subscription.
 * The onComplete and onError callbacks are no‑ops; errors are routed to a Blackhole
 * to avoid dead‑code elimination.
 *
 * @param bh Blackhole to consume any error that might be emitted.
 */
@Benchmark
public void subscribeAndDispose(Blackhole bh) {
    // Subscribe with empty onComplete and error consumer that feeds the Blackhole.
    completable.subscribe(() -> {
        /* onComplete – nothing to do */
    }, bh::consume);
}
```

### Method 109

```java
/**
 * Subscribe to the optimized Observable and consume the emitted value.
 * The {@link Blackhole} guarantees the value is observed by the JVM.
 */
@Benchmark
public void subscribeScalarXMapObservable(Blackhole bh) {
    ObservableScalarXMap.scalarXMap(42, scalarMapper).subscribe(bh::consume);
}
```

### Method 110

```java
/**
 * Subscribes to the Completable and immediately disposes the subscription.
 *
 * The Blackhole consumes the onError callback (which should never be invoked)
 * to prevent the JIT from optimizing the lambda away.
 */
@Benchmark
public void disposeOn(Blackhole bh) {
    // Subscribe with a no‑op onComplete and a Blackhole‑consumed onError,
    // then dispose immediately to trigger scheduled disposal.
    completable.subscribe(() -> {
        /* onComplete – never called */
    }, bh::consume).dispose();
}
```

### Method 111

```java
/**
 * Subscribes to the Flowable and blocks until it completes.
 * The Blackhole is used to consume each emitted item to prevent dead‑code elimination.
 */
@Benchmark
public void throughput(Blackhole bh) {
    flowable.blockingSubscribe(bh::consume);
}
```

### Method 112

```java
/**
 * Subscribes to the Flowable and consumes every emitted item via a Blackhole.
 *
 * @param bh Blackhole to consume items and prevent dead‑code elimination.
 */
@Benchmark
public void doOnEachThroughput(Blackhole bh) {
    // onNext
    flowable.// onNext
    subscribe(// onError (should never happen)
    bh::consume, // onComplete (no‑op)
    bh::consume, () -> {
    });
}
```

### Method 113

```java
/**
 * Subscribes to the Flowable and consumes every emitted item via a Blackhole.
 *
 * @param bh Blackhole to consume items and prevent dead‑code elimination.
 */
@Benchmark
public void doOnEachThroughput(Blackhole bh) {
    // onNext
    flowable.// onNext
    subscribe(// onError (should never happen)
    bh::consume, // onComplete (no‑op)
    bh::consume, () -> {
    });
}
```

### Method 114

```java
/**
 * Subscribes to the Flowable and consumes the emitted item.
 *
 * Each invocation creates a fresh subscription, which reflects the typical
 * usage pattern of the operator in real applications.
 *
 * @param bh Blackhole to consume the emitted value and avoid dead‑code elimination.
 */
@Benchmark
public void takeLastOne(Blackhole bh) {
    flowable.subscribe(bh::consume);
}
```

### Method 115

```java
/**
 * Subscribes to the Flowable and consumes the emitted value.
 *
 * The subscription is synchronous for {@code FlowableFromCallable}, so the method
 * returns only after the value has been emitted and the {@link Blackhole} has
 * consumed it.
 *
 * @param bh Blackhole to consume the emitted value and avoid dead‑code elimination.
 */
@Benchmark
public void subscribeAndConsume(Blackhole bh) {
    flowable.subscribe(bh::consume);
}
```

### Method 116

```java
/**
 * Subscribes to the Observable and blocks until it terminates.
 * The Blackhole consumes any possible onNext/onError signals,
 * even though this operator never emits items.
 */
@Benchmark
public void subscribeAndComplete(BenchmarkState state, Blackhole bh) {
    // onNext (won't be called)
    state.observable.// onNext (won't be called)
    blockingSubscribe(// onError (won't be called)
    bh::consume, // onComplete
    bh::consume, () -> {
    });
}
```

### Method 117

```java
/**
 * Subscribes to the Observable and blocks until it terminates.
 * The Blackhole consumes any possible onNext/onError signals,
 * even though this operator never emits items.
 */
@Benchmark
public void subscribeAndComplete(BenchmarkState state, Blackhole bh) {
    // onNext (won't be called)
    state.observable.// onNext (won't be called)
    blockingSubscribe(// onError (won't be called)
    bh::consume, // onComplete
    bh::consume, () -> {
    });
}
```

### Method 118

```java
/**
 * Subscribes to the Observable, consumes all emitted items via Blackhole,
 * and then disposes the subscription to trigger the {@code unsubscribeOn}
 * path. The method is measured in throughput mode (operations per second).
 *
 * @param bh Blackhole to consume emitted items and avoid dead‑code elimination.
 */
@Benchmark
public void subscribeConsumeAndDispose(Blackhole bh) {
    // Subscribe and forward each item to the Blackhole.
    // The Disposable is retained so we can dispose it immediately,
    // exercising the asynchronous disposal logic.
    var disposable = source.subscribe(bh::consume);
    // Trigger the asynchronous disposal path.
    disposable.dispose();
}
```

### Method 119

```java
/**
 * Subscribes to the ObservableRangeLong and drains all emitted items.
 * The Blackhole ensures that the emitted values are consumed and not optimized away.
 */
@Benchmark
public void rangeLongThroughput(BenchmarkState state, Blackhole bh) {
    state.observable.subscribe(bh::consume);
}
```

### Method 120

```java
/**
 * Subscribes to the observable and consumes all emitted items.
 *
 * @param bh Blackhole to consume items and avoid dead‑code elimination.
 */
@Benchmark
public void doOnLifecycleThroughput(Blackhole bh) {
    // onNext
    observable.// onNext
    subscribe(// onError
    bh::consume, // onComplete
    bh::consume, () -> bh.consume("complete"));
}
```

### Method 121

```java
/**
 * Subscribes to the observable and consumes all emitted items.
 *
 * @param bh Blackhole to consume items and avoid dead‑code elimination.
 */
@Benchmark
public void doOnLifecycleThroughput(Blackhole bh) {
    // onNext
    observable.// onNext
    subscribe(// onError
    bh::consume, // onComplete
    bh::consume, () -> bh.consume("complete"));
}
```

### Method 122

```java
/**
 * Variant using {@code subscribeOn} to shift subscription onto the provided scheduler.
 */
@Benchmark
public void withSubscribeOn(BenchmarkState state, Blackhole bh) {
    state.source.subscribeOn(state.scheduler).blockingSubscribe(bh::consume);
}
```

### Method 123

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
public void skipWhileThroughput(Blackhole bh) {
    // Consume the observable synchronously; Blackhole prevents dead-code elimination
    observable.blockingSubscribe(bh::consume);
}
```

### Method 124

```java
@Benchmark
public void backpressureBufferThroughput(BenchmarkState state, Blackhole bh) {
    // blockingSubscribe guarantees the benchmark runs until the stream completes.
    state.buffered.blockingSubscribe(bh::consume);
}
```

### Method 125

```java
@Benchmark
public void baseline(Blackhole bh) {
    // Consume the source without the operator
    source.blockingSubscribe(bh::consume);
}
```

### Method 126

```java
@Benchmark
public void baseline(Blackhole bh) {
    plainSource.subscribe(bh::consume);
}
```

### Method 127

```java
@Benchmark
public void bufferBoundaryThroughput(Blackhole bh) throws InterruptedException {
    Flowable<List<Integer>> buffered = source.buffer(openPublisher, closeFunction, bufferSupplier);
    CountDownLatch latch = new CountDownLatch(1);
    // onNext
    buffered.// onNext
    subscribe(// onError
    bh::consume, // onComplete
    bh::consume, latch::countDown);
    latch.await();
}
```

### Method 128

```java
@Benchmark
public void bufferBoundaryThroughput(Blackhole bh) throws InterruptedException {
    Flowable<List<Integer>> buffered = source.buffer(openPublisher, closeFunction, bufferSupplier);
    CountDownLatch latch = new CountDownLatch(1);
    // onNext
    buffered.// onNext
    subscribe(// onError
    bh::consume, // onComplete
    bh::consume, latch::countDown);
    latch.await();
}
```

### Method 129

```java
@Benchmark
public void bufferBoundaryThroughput(Blackhole bh) throws InterruptedException {
    Flowable<List<Integer>> buffered = source.buffer(openPublisher, closeFunction, bufferSupplier);
    CountDownLatch latch = new CountDownLatch(1);
    // onNext
    buffered.// onNext
    subscribe(// onError
    bh::consume, // onComplete
    bh::consume, latch::countDown);
    latch.await();
}
```

### Method 130

```java
@Benchmark
public void bufferExactBoundary(Blackhole bh) {
    // Apply the buffer operator (which uses ObservableBufferExactBoundary internally)
    // and consume each emitted collection via Blackhole to avoid dead‑code elimination.
    source.buffer(boundary).blockingForEach(bh::consume);
}
```

### Method 131

```java
@Benchmark
public void combineLatestThroughput(BenchmarkState state, Blackhole bh) {
    // combineLatestArray internally uses ObservableCombineLatest.
    Observable.combineLatestArray(state.sources, state.combiner).blockingSubscribe(bh::consume);
}
```

### Method 132

```java
@Benchmark
public void combineLatestThroughput(BenchmarkState state, Blackhole bh) {
    state.combined.blockingForEach(bh::consume);
}
```

### Method 133

```java
@Benchmark
public void concatMapMaybeThroughput(Blackhole bh) {
    source.concatMapMaybe(mapper, prefetch).blockingSubscribe(bh::consume);
}
```

### Method 134

```java
@Benchmark
public void concatMapScheduler(Blackhole bh) {
    Flowable<Integer> flowable = new FlowableConcatMapScheduler<>(source, mapper, prefetch, errorMode, scheduler);
    flowable.subscribe(new Consumer<Integer>() {

        @Override
        public void accept(Integer value) {
            bh.consume(value);
        }
    }, bh::consume);
}
```

### Method 135

```java
@Benchmark
public void concatMapThroughput(Blackhole bh) {
    // Use the overload without explicit ErrorMode; it defaults to IMMEDIATE.
    source.concatMap(mapper, 128).blockingForEach(bh::consume);
}
```

### Method 136

```java
@Benchmark
public void concatMapThroughput(Blackhole bh) {
    source.concatMap(mapper, prefetch).sequential().blockingSubscribe(bh::consume);
}
```

### Method 137

```java
@Benchmark
public void concatWithMaybe(Blackhole bh) {
    // Concatenate the Flowable with the Maybe and block until completion,
    // feeding each emitted item into the Blackhole.
    // ensure downstream runs on the same thread for consistency
    sourceFlowable.concatWith(maybeSource).// ensure downstream runs on the same thread for consistency
    observeOn(scheduler).blockingSubscribe(bh::consume);
}
```

### Method 138

```java
@Benchmark
public void debounceThroughput(Blackhole bh) {
    // Apply debounce with the configured timeout and scheduler.
    // Use blockingSubscribe to ensure the benchmark measures the full pipeline.
    source.debounce(timeout, unit, scheduler).blockingSubscribe(bh::consume);
}
```

### Method 139

```java
@Benchmark
public void debounceThroughput(Blackhole bh) {
    // Apply the debounce operator and consume all items.
    source.debounce(SELECTOR).blockingSubscribe(bh::consume);
}
```

### Method 140

```java
@Benchmark
public void dematerializeThroughput(BenchmarkState state, Blackhole bh) {
    // Consume all items; blockingForEach ensures the benchmark measures the full pipeline.
    state.observable.blockingForEach(bh::consume);
}
```

### Method 141

```java
@Benchmark
public void detachThroughput(Blackhole bh) {
    // Apply the internal ObservableDetach operator and consume all items.
    // blockingSubscribe ensures the benchmark measures the complete lifecycle.
    new ObservableDetach<>(source).blockingSubscribe(bh::consume);
}
```

### Method 142

```java
@Benchmark
public void distinctThroughput(Blackhole bh) throws InterruptedException {
    CountDownLatch latch = new CountDownLatch(1);
    distinct.subscribe(bh::consume, bh::consume, latch::countDown);
    latch.await();
}
```

### Method 143

```java
@Benchmark
public void distinctThroughput(Blackhole bh) {
    distinctFlowable.subscribe(bh::consume);
}
```

### Method 144

```java
@Benchmark
public void distinctUntilChanged(Blackhole bh) {
    source.distinctUntilChanged(IDENTITY).subscribe(bh::consume, bh::consume, () -> {
    });
}
```

### Method 145

```java
@Benchmark
public void doAfterNext(Blackhole bh) {
    // Consume the observable that includes the doAfterNext operator
    withDoAfterNext.blockingSubscribe(bh::consume);
}
```

### Method 146

```java
@Benchmark
public void doFinallyThroughput(Blackhole bh) {
    // Run the whole pipeline and consume each emitted item with Blackhole.
    observable.blockingSubscribe(bh::consume);
}
```

### Method 147

```java
@Benchmark
public void doFinallyThroughput(Blackhole bh) {
    // Subscribe with lambdas that forward all signals to the Blackhole.
    // onNext
    flowable.// onNext
    subscribe(// onError
    bh::consume, // onComplete (no‑op, as completion is already measured)
    bh::consume, () -> {
    });
}
```

### Method 148

```java
@Benchmark
public void doFinallyThroughput(Blackhole bh) {
    // Subscribe with lambdas that forward all signals to the Blackhole.
    // onNext
    flowable.// onNext
    subscribe(// onError
    bh::consume, // onComplete (no‑op, as completion is already measured)
    bh::consume, () -> {
    });
}
```

### Method 149

```java
@Benchmark
public void doOnEach(Blackhole bh) {
    doOnEachSource.subscribe(bh::consume);
}
```

### Method 150

```java
@Benchmark
public void eagerConcatMapThroughput(Blackhole bh) {
    flowable.blockingSubscribe(bh::consume);
}
```

### Method 151

```java
@Benchmark
public void filterThroughput(Blackhole bh) {
    Flowable<Integer> source = Flowable.range(1, itemCount);
    source.filter(predicate).blockingForEach(bh::consume);
}
```

### Method 152

```java
@Benchmark
public void flatMapIterable(BenchmarkState state, Blackhole bh) {
    // Apply the ParallelFlatMapIterable operator and consume all items.
    // Convert back to a regular Flowable.
    new ParallelFlatMapIterable<>(state.source, state.mapper, state.prefetch).// Consume items using Blackhole.
    sequential().// Consume items using Blackhole.
    blockingForEach(bh::consume);
}
```

### Method 153

```java
@Benchmark
public void flatMapIterable(BenchmarkState state, Blackhole bh) {
    // Subscribe with a Consumer that forwards each item to the Blackhole.
    // The subscribe(Consumer) overload requests Long.MAX_VALUE internally,
    // ensuring the operator runs in an unbounded (fast‑path) mode.
    state.flowable.subscribe(bh::consume);
}
```

### Method 154

```java
@Benchmark
public void flatMapIterableThroughput(BenchmarkState state, Blackhole bh) {
    // Subscribe and consume all items, using Blackhole to avoid dead‑code elimination.
    state.flowable.blockingSubscribe(bh::consume);
}
```

### Method 155

```java
@Benchmark
public void flatMapPublisherThroughput(BenchmarkState state, Blackhole bh) {
    // blockingSubscribe ensures the benchmark measures the complete processing
    // of the inner Flowable and prevents asynchronous side‑effects from leaking
    // into the measurement.
    state.flowable.blockingSubscribe(bh::consume);
}
```

### Method 156

```java
@Benchmark
public void flatMapThroughput(Blackhole bh) {
    Flowable<Integer> source = Flowable.range(0, sourceSize);
    source.flatMap(mapper, delayErrors, maxConcurrency, bufferSize).blockingSubscribe(bh::consume);
}
```

### Method 157

```java
@Benchmark
public void generateItems(Blackhole bh) {
    flowable.take(itemCount).blockingForEach(bh::consume);
}
```

### Method 158

```java
@Benchmark
public void groupByThroughput(Blackhole bh) {
    source.groupBy(KEY_SELECTOR, VALUE_SELECTOR, delayError, bufferSize).flatMap(g -> g).doOnNext(bh::consume).blockingSubscribe();
}
```

### Method 159

```java
@Benchmark
public void groupJoin(Blackhole bh) {
    // Subscribe and consume all emitted items.
    joined.blockingSubscribe(bh::consume);
}
```

### Method 160

```java
@Benchmark
public void mapOptionalThroughput(Blackhole bh) {
    ParallelMapOptional<Integer, Integer> operator = new ParallelMapOptional<Integer, Integer>(source, mapper);
    operator.sequential().subscribe(bh::consume);
}
```

### Method 161

```java
@Benchmark
public void mapThroughput(BenchmarkState state, Blackhole bh) {
    // Apply the map operator and consume all items synchronously.
    state.source.map(state.mapper).blockingSubscribe(bh::consume);
}
```

### Method 162

```java
@Benchmark
public void mapTryOptionalThroughput(Blackhole bh) {
    parallelFlow.sequential().blockingForEach(bh::consume);
}
```

### Method 163

```java
@Benchmark
public void mergeWithMaybe(Blackhole bh) {
    // Consume all items; blockingForEach ensures the whole stream is processed
    merged.blockingForEach(bh::consume);
}
```

### Method 164

```java
@Benchmark
public void onErrorReturnThroughput(Blackhole bh) {
    // onNext
    errorSource.onErrorReturn(fallbackSupplier).// onNext
    subscribe(// onError
    bh::consume, // onComplete (Action)
    bh::consume, () -> bh.consume("done"));
}
```

### Method 165

```java
@Benchmark
public void onErrorReturnThroughput(Blackhole bh) {
    // onNext
    errorSource.onErrorReturn(fallbackSupplier).// onNext
    subscribe(// onError
    bh::consume, // onComplete (Action)
    bh::consume, () -> bh.consume("done"));
}
```

### Method 166

```java
@Benchmark
public void parallelMapThroughput(Blackhole bh) {
    // Apply the ParallelMap operator and consume all items.
    source.map(mapper).sequential().blockingForEach(bh::consume);
}
```

### Method 167

```java
@Benchmark
public void repeatThroughput(Blackhole bh) {
    Disposable d = // onNext
    repeatedObservable.// onNext
    subscribe(// onError (should not happen)
    bh::consume, // onComplete
    bh::consume, () -> bh.consume(0));
    d.dispose();
}
```

### Method 168

```java
@Benchmark
public void repeatThroughput(Blackhole bh) {
    Disposable d = // onNext
    repeatedObservable.// onNext
    subscribe(// onError (should not happen)
    bh::consume, // onComplete
    bh::consume, () -> bh.consume(0));
    d.dispose();
}
```

### Method 169

```java
@Benchmark
public void repeatWhen(Blackhole bh) {
    // Subscribe and consume all items; blockingForEach ensures the whole sequence is processed.
    repeatWhenObservable.blockingForEach(bh::consume);
}
```

### Method 170

```java
@Benchmark
public void scanSeedThroughput(Blackhole bh) {
    Observable<Integer> scanned = source.scanWith(seedSupplier, accumulator);
    scanned.blockingSubscribe(bh::consume);
}
```

### Method 171

```java
@Benchmark
public void skipLastThroughput(BenchmarkState state, Blackhole bh) {
    state.source.skipLast(state.skip).subscribe(bh::consume);
}
```

### Method 172

```java
@Benchmark
public void skipThroughput(Blackhole bh) {
    // Apply the skip operator and consume all remaining items.
    // Using blockingSubscribe ensures the benchmark measures the complete
    // processing of the stream before returning.
    source.skip(skipCount).blockingSubscribe(bh::consume);
}
```

### Method 173

```java
@Benchmark
public void skipUntilThroughput(BenchmarkState state, Blackhole bh) {
    // Apply skipUntil operator and consume all items using blockingSubscribe.
    // The Blackhole ensures the emitted values are used.
    state.source.skipUntil(state.trigger).blockingSubscribe(bh::consume);
}
```

### Method 174

```java
@Benchmark
public void skipWhileThroughput(Blackhole bh) {
    // Subscribe and consume all items, ensuring the work is not optimized away.
    flowable.blockingSubscribe(bh::consume);
}
```

### Method 175

```java
@Benchmark
public void switchMapSingleThroughput(BenchmarkState state, Blackhole bh) {
    // The pipeline: source -> switchMapSingle(mapper) -> blocking consumption.
    // Using blockingForEach ensures the whole stream is processed within the benchmark iteration.
    state.source.switchMapSingle(state.mapper).blockingForEach(bh::consume);
}
```

### Method 176

```java
@Benchmark
public void switchMapSingleThroughput(Blackhole bh) {
    // The public API uses FlowableSwitchMapSingle internally.
    source.switchMapSingle(mapper).blockingSubscribe(bh::consume);
}
```

### Method 177

```java
@Benchmark
public void take(Blackhole bh) {
    // Apply the take operator and consume the emitted items with Blackhole to prevent dead‑code elimination.
    source.take(limit).blockingSubscribe(bh::consume);
}
```

### Method 178

```java
@Benchmark
public void takeLastTimed(BenchmarkState state, Blackhole bh) {
    // Construct the internal operator directly (same package) to benchmark its exact behavior.
    new FlowableTakeLastTimed<>(state.source, state.count, state.timeMs, TimeUnit.MILLISECONDS, state.scheduler, state.bufferSize, state.delayError).subscribe(bh::consume, bh::consume, () -> {
    });
    // The subscription runs synchronously because we use the trampoline scheduler,
    // so the benchmark method returns only after all items have been processed.
}
```

### Method 179

```java
@Benchmark
public void takeLastTimedThroughput(BenchmarkState state, Blackhole bh) {
    // Build the operator instance directly to isolate its performance.
    ObservableTakeLastTimed<Integer> operator = new ObservableTakeLastTimed<>(state.source, state.count, state.timeMs, state.unit, state.scheduler, state.bufferSize, state.delayError);
    // Subscribe and consume all items, forcing the operator to drain.
    operator.subscribe(bh::consume);
}
```

### Method 180

```java
@Benchmark
public void takeUntilPredicate(Blackhole bh) {
    // Apply the internal operator directly and block until the stream completes.
    new ObservableTakeUntilPredicate<>(source, predicate).blockingSubscribe(bh::consume);
}
```

### Method 181

```java
@Benchmark
public void throttleLatestThroughput(Blackhole bh) {
    // Apply the operator with the configured parameters.
    Flowable<Long> throttled = source.throttleLatest(timeout, TimeUnit.MILLISECONDS, scheduler, emitLast, onDropped);
    // Subscribe and consume items with Blackhole to prevent dead‑code elimination.
    subscription = throttled.subscribe(bh::consume, bh::consume, () -> {
    });
}
```

### Method 182

```java
@Benchmark
public void throughput(BenchmarkState state, Blackhole bh) {
    // Consume the entire stream; each emitted item is passed to Blackhole.
    state.combined.blockingForEach(bh::consume);
}
```

### Method 183

```java
@Benchmark
public void windowBoundarySelectorThroughput(Blackhole bh) throws InterruptedException {
    Observable<Integer> source = Observable.range(1, itemCount).subscribeOn(scheduler);
    Observable<Long> open = Observable.intervalRange(0, (itemCount + windowOpenInterval - 1) / windowOpenInterval, 0, 0, TimeUnit.MILLISECONDS, scheduler).map(i -> i * windowOpenInterval);
    Function<Long, ObservableSource<Long>> closingIndicator = start -> {
        long closeAfter = Math.min(windowCloseInterval, itemCount - start);
        return Observable.timer(closeAfter, TimeUnit.MILLISECONDS, scheduler);
    };
    Observable<Observable<Integer>> windowed = new ObservableWindowBoundarySelector<>(source, open, closingIndicator, bufferSize);
    CountDownLatch latch = latchFactory.createLatch(1);
    Disposable d = windowed.flatMap(w -> w.doOnNext(item -> bh.consume(item)).ignoreElements().toObservable()).doOnComplete(latch::countDown).subscribe();
    if (!latch.await(30, TimeUnit.SECONDS)) {
        d.dispose();
        throw new IllegalStateException("Benchmark timed out");
    }
    d.dispose();
}
```

### Method 184

```java
@Benchmark
public void windowBoundaryThroughput(BenchmarkState state, Blackhole bh) throws InterruptedException {
    // Create the operator instance with the pre‑built source and boundary.
    ObservableWindowBoundary<Integer, Integer> operator = new ObservableWindowBoundary<>(state.source, state.boundary, state.capacityHint);
    // Latch to wait for completion of the whole stream.
    CountDownLatch latch = new CountDownLatch(1);
    // Subscribe to the operator.
    operator.subscribe(new Observer<Observable<Integer>>() {

        @Override
        public void onSubscribe(Disposable d) {
            // No need to keep the Disposable; the benchmark runs to completion.
        }

        @Override
        public void onNext(Observable<Integer> window) {
            // For each window, subscribe and consume its items.
            window.subscribe(new Observer<Integer>() {

                @Override
                public void onSubscribe(Disposable d) {
                    // No action needed.
                }

                @Override
                public void onNext(Integer value) {
                    // Consume the value to avoid dead‑code elimination.
                    bh.consume(value);
                }

                @Override
                public void onError(Throwable e) {
                    // Propagate errors to the latch to avoid hanging.
                    latch.countDown();
                }

                @Override
                public void onComplete() {
                    // No per‑window completion handling required.
                }
            });
        }

        @Override
        public void onError(Throwable e) {
            // Signal benchmark termination on error.
            latch.countDown();
        }

        @Override
        public void onComplete() {
            // Signal that the whole stream has finished.
            latch.countDown();
        }
    });
    // Wait for the stream to finish before returning control to JMH.
    latch.await();
}
```

### Method 185

```java
@Benchmark
public void windowThroughput(Blackhole bh) {
    // Apply the window operator with the configured parameters.
    // The downstream flatMap flattens the windows back to items so that the
    // benchmark measures the cost of window creation, management, and emission.
    // flatten windows to individual items
    source.window(size, skip, bufferSize).// flatten windows to individual items
    flatMap(w -> w).subscribe(bh::consume, bh::consume, () -> {
    });
    // The subscription is synchronous for the range source, so the method
    // returns only after all items have been processed.
}
```

### Method 186

```java
@Benchmark
public void windowTimedThroughput(BenchmarkState state, Blackhole bh) {
    // Use the exact‑window overload that includes maxSize, restartTimerOnMaxSize and bufferSize.
    Observable<Observable<Integer>> windows = state.source.window(state.timespanMs, TimeUnit.MILLISECONDS, state.scheduler, state.maxSize, state.restartTimerOnMaxSize, state.bufferSize);
    // Consume each window fully using lastOrError() to obtain a Single per window.
    windows.flatMapSingle(w -> w.lastOrError()).blockingSubscribe(bh::consume);
}
```

### Method 187

```java
@Benchmark
public void withLatestFromMany(BenchmarkState state, Blackhole bh) {
    // Create the operator instance directly (public constructor).
    ObservableWithLatestFromMany<Integer, Integer> observable = new ObservableWithLatestFromMany<>(state.source, state.others, state.combiner);
    // Subscribe and consume all items, ensuring the pipeline runs to completion.
    observable.blockingSubscribe(bh::consume);
}
```

### Method 188

```java
@Benchmark
public void zipTwoSources(Blackhole bh) {
    Flowable.zip(Arrays.asList(source1, source2), zipper).subscribe(bh::consume);
}
```

## JMH UNSINKED VARIABLE - Unsinked variable inside benchmark method

### Method 1

```java
/**
 * Baseline benchmark for a failing {@code Maybe} without error handling.
 * The RuntimeException is caught to prevent the benchmark from aborting.
 */
@Benchmark
public void errorBaselineThroughput(Blackhole bh) {
    Integer result;
    try {
        // throws
        result = errorSource.blockingGet();
    } catch (Throwable ex) {
        // In the error‑only baseline we treat the outcome as a null value.
        result = null;
    }
    bh.consume(result);
}
```

### Method 2

```java
/**
 * Benchmark a non‑scalar mapping scenario where the mapper returns a
 * Publisher that does not implement {@code Supplier}. This forces the
 * fallback path inside {@code scalarXMap}.
 */
@Benchmark
public void scalarXMapNonScalar(Blackhole bh) {
    Flowable<Integer> flowable = FlowableScalarXMap.scalarXMap(value, nonScalarMapper);
    flowable.blockingSubscribe(bh::consume);
}
```

### Method 3

```java
/**
 * Benchmark a regular Flowable.map() path for comparison.
 *
 * This uses Flowable.just(value) followed by a standard map operator,
 * which also ends up on the scalar path but goes through the regular
 * operator chain, providing a baseline.
 */
@Benchmark
public void regularMap(Blackhole bh) {
    Flowable<Integer> flowable = Flowable.just(value).map(v -> v + 1);
    flowable.blockingSubscribe(bh::consume);
}
```

### Method 4

```java
/**
 * Benchmark for integer streams.
 */
@Benchmark
public void reduceInt(Blackhole bh) {
    Flowable<Integer> reduced = new FlowableOnBackpressureReduce<>(intSource, intReducer);
    reduced.blockingSubscribe(bh::consume);
}
```

### Method 5

```java
/**
 * Benchmark for string concatenation (object allocation heavy).
 */
@Benchmark
public void reduceString(Blackhole bh) {
    if (!"concat".equals(reducerType)) {
        return;
    }
    Flowable<String> reduced = new FlowableOnBackpressureReduce<>(stringSource, stringReducer);
    reduced.blockingSubscribe(bh::consume);
}
```

### Method 6

```java
/**
 * Benchmark method that concatenates the upstream Observable with the Single
 * using the internal {@link ObservableConcatWithSingle} operator and consumes
 * all emitted items via a Blackhole.
 *
 * @param bh Blackhole to consume the items and avoid dead‑code elimination.
 */
@Benchmark
public void concatWithSingle(Blackhole bh) {
    // Directly instantiate the internal operator to avoid extra operator wrapping.
    Observable<Integer> concat = new ObservableConcatWithSingle<>(upstream, single);
    // Subscribe and block until completion, feeding each item into the Blackhole.
    concat.blockingSubscribe(bh::consume);
}
```

### Method 7

```java
/**
 * Benchmark method that creates a new {@link SingleFlatMapPublisher},
 * subscribes a {@link DisposableSubscriber}, and waits for completion.
 *
 * The measured part is the whole flat‑map operation including subscription,
 * request handling and emission of all inner items.
 */
@Benchmark
public void flatMapPublisher(Blackhole bh) throws InterruptedException {
    // Create the operator instance
    SingleFlatMapPublisher<Integer, Integer> operator = new SingleFlatMapPublisher<>(source, mapper);
    // Latch to wait for onComplete / onError
    CountDownLatch latch = new CountDownLatch(1);
    // Subscriber that forwards each item to Blackhole and signals completion
    operator.subscribe(new DisposableSubscriber<Integer>() {

        @Override
        public void onNext(Integer t) {
            bh.consume(t);
        }

        @Override
        public void onError(Throwable t) {
            t.printStackTrace();
            latch.countDown();
        }

        @Override
        public void onComplete() {
            latch.countDown();
        }
    });
    // Wait for the stream to finish; timeout guards against deadlocks
    if (!latch.await(5, TimeUnit.SECONDS)) {
        throw new IllegalStateException("Benchmark timed out");
    }
}
```

### Method 8

```java
/**
 * Benchmark method that merges the Flowable with the Completable and subscribes
 * a blackhole‑draining subscriber.
 *
 * @param bh Blackhole to consume emitted items.
 */
@Benchmark
public void mergeWithCompletable(Blackhole bh) {
    // Merge the source Flowable with the Completable using the operator under test.
    Flowable<Integer> merged = source.mergeWith(other);
    // Subscribe with a subscriber that requests unbounded demand.
    merged.subscribe(new DefaultSubscriber<Integer>() {

        @Override
        public void onStart() {
            request(Long.MAX_VALUE);
        }

        @Override
        public void onNext(Integer t) {
            bh.consume(t);
        }

        @Override
        public void onError(Throwable t) {
            // Errors are not expected in this benchmark; rethrow to fail fast.
            throw new RuntimeException(t);
        }

        @Override
        public void onComplete() {
            // No action needed on completion.
        }
    });
}
```

### Method 9

```java
/**
 * Benchmark method that schedules a delayed action (1 ms) on the SchedulerWhen.
 */
@Benchmark
public Disposable scheduleDelayed(Blackhole bh) {
    SchedulerWhen.Worker worker = schedulerWhen.createWorker();
    Disposable d = worker.schedule(NOOP, 1, TimeUnit.MILLISECONDS);
    counter.incrementAndGet();
    bh.consume(d);
    worker.dispose();
    return d;
}
```

### Method 10

```java
/**
 * Benchmark method that schedules an immediate no‑op action on the SchedulerWhen.
 */
@Benchmark
public Disposable scheduleImmediate(Blackhole bh) {
    SchedulerWhen.Worker worker = schedulerWhen.createWorker();
    Disposable d = worker.schedule(NOOP);
    counter.incrementAndGet();
    bh.consume(d);
    worker.dispose();
    return d;
}
```

### Method 11

```java
/**
 * Benchmark method that subscribes to the FlowableFlatMapStream operator,
 * consumes all emitted items, and blocks until completion.
 *
 * @param bh Blackhole to consume items and prevent dead‑code elimination.
 */
@Benchmark
public void flatMapStreamThroughput(Blackhole bh) {
    // Create the operator instance
    Flowable<Integer> flatMapped = new FlowableFlatMapStream<>(source, mapper, prefetch);
    // Subscribe and block, consuming each item with the Blackhole
    flatMapped.blockingSubscribe(bh::consume);
}
```

### Method 12

```java
/**
 * Benchmark method that subscribes to the operator and consumes all items.
 *
 * The subscription is performed using {@code blockingSubscribe} to ensure the
 * benchmark measures the complete processing of the stream.
 */
@Benchmark
public void withLatestFromMany(Blackhole bh) {
    // Apply the operator.
    Flowable<Integer> combined = new FlowableWithLatestFromMany<>(source, others, combiner);
    // Consume all items, feeding them into the Blackhole to prevent dead-code elimination.
    combined.blockingSubscribe(bh::consume);
}
```

### Method 13

```java
/**
 * Benchmark method that subscribes to the switchMapMaybe chain and consumes
 * all emitted items. The subscription is performed on each iteration to
 * include the full cost of the operator.
 *
 * @param bh Blackhole to consume the items and avoid dead‑code elimination.
 */
@Benchmark
public void switchMapMaybeThroughput(Blackhole bh) {
    Observable<String> result = source.switchMapMaybe(mapper);
    // blockingSubscribe ensures the benchmark thread waits for completion.
    result.blockingSubscribe(bh::consume);
}
```

### Method 14

```java
/**
 * Benchmark method.
 *
 * Creates a new {@link CompletableMerge} instance for each iteration,
 * subscribes to it and blocks until completion.
 *
 * The use of {@code blockingAwait()} guarantees that the benchmark measures
 * the full lifecycle of the merged Completable, not just the subscription cost.
 */
@Benchmark
public void mergeCompletable() {
    CompletableMerge merge = new CompletableMerge(upstream, maxConcurrency, delayErrors);
    // block until the merged Completable terminates
    merge.blockingAwait();
}
```

### Method 15

```java
/**
 * Benchmark that creates a fresh {@link Stream}, wraps it into an {@link ObservableFromStream},
 * subscribes with a {@link TestObserver}, and blocks until completion.
 *
 * The use of a fresh Stream per invocation ensures that the benchmark measures the
 * full cost of stream creation, iterator acquisition, emission, and resource cleanup.
 *
 * @return a {@link TestObserver} that has completed the subscription.
 */
@Benchmark
public TestObserver<Integer> subscribeAndConsume() {
    // Create a new Stream for each benchmark iteration.
    Stream<Integer> stream = sourceList.stream();
    // Wrap the Stream into the Observable under test.
    Observable<Integer> observable = new ObservableFromStream<>(stream);
    // Use TestObserver to subscribe and await terminal event.
    TestObserver<Integer> observer = new TestObserver<>();
    observable.subscribe(observer);
    observer.awaitDone(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
    // The observer now holds the consumed items; returning it prevents dead‑code elimination.
    return observer;
}
```

### Method 16

```java
/**
 * Benchmark that creates a replay ConnectableObservable, connects it,
 * and subscribes a single observer that consumes all items.
 *
 * The observer forwards each received item to the Blackhole to avoid dead‑code elimination.
 */
@Benchmark
public void replayAndConsume(Blackhole bh) {
    ConnectableObservable<Integer> replay;
    if (bufferSize == Integer.MAX_VALUE) {
        // Unbounded replay
        replay = ObservableReplay.createFrom(source);
    } else {
        // Size‑bounded replay
        replay = ObservableReplay.create(source, bufferSize, eagerTruncate);
    }
    // Connect the source (no need to keep the Disposable)
    replay.connect(Disposable::dispose);
    // Subscribe a consumer that forwards items to the Blackhole
    replay.subscribe(new Observer<Integer>() {

        @Override
        public void onSubscribe(Disposable d) {
            // No explicit disposal; the benchmark runs to completion
        }

        @Override
        public void onNext(Integer value) {
            bh.consume(value);
        }

        @Override
        public void onError(Throwable e) {
            // Propagate errors to the Blackhole to avoid swallowing them
            bh.consume(e);
        }

        @Override
        public void onComplete() {
            // No-op
        }
    });
}
```

### Method 17

```java
/**
 * Benchmark that iterates over the BlockingFlowableMostRecent and consumes each element.
 *
 * Each operation creates a fresh iterator, walks through all emitted items,
 * and feeds them into a Blackhole to avoid dead‑code elimination.
 */
@Benchmark
public void iterateAll(Blackhole bh) {
    Iterator<Integer> it = mostRecent.iterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 18

```java
/**
 * Benchmark that iterates over the entire Flowable using the blocking iterator.
 * The returned sum prevents dead‑code elimination.
 *
 * @return the sum of all emitted integers
 */
@Benchmark
public int iterateAndSum() {
    int sum = 0;
    Iterator<Integer> it = blocking.iterator();
    while (it.hasNext()) {
        sum += it.next();
    }
    return sum;
}
```

### Method 19

```java
/**
 * Benchmark that subscribes to a fresh {@code FlowableRefCount} and cancels immediately.
 *
 * @param bh Blackhole to prevent dead‑code elimination.
 */
@Benchmark
public void subscribeAndCancel(Blackhole bh) {
    // Create a fresh source for each invocation.
    Flowable<Integer> source = Flowable.range(1, 1000);
    ConnectableFlowable<Integer> connectable = source.publish();
    Flowable<Integer> refCounted = new FlowableRefCount<>(connectable);
    refCounted.subscribe(new Subscriber<Integer>() {

        private Subscription upstream;

        @Override
        public void onSubscribe(Subscription s) {
            this.upstream = s;
            // Immediate cancellation.
            s.cancel();
        }

        @Override
        public void onNext(Integer t) {
            /* never called */
        }

        @Override
        public void onError(Throwable t) {
            /* ignore */
        }

        @Override
        public void onComplete() {
            /* ignore */
        }
    });
    // Consume the reference so the JIT cannot eliminate the whole call.
    bh.consume(refCounted);
}
```

### Method 20

```java
/**
 * Benchmark that subscribes to a fresh {@code FlowableRefCount}, requests a few items,
 * and consumes them.
 *
 * @param bh Blackhole to consume emitted items.
 */
@Benchmark
public void subscribeAndConsume(Blackhole bh) {
    // Fresh source per invocation.
    Flowable<Integer> source = Flowable.range(1, 1000);
    ConnectableFlowable<Integer> connectable = source.publish();
    Flowable<Integer> refCounted = new FlowableRefCount<>(connectable);
    refCounted.subscribe(new Subscriber<Integer>() {

        private Subscription upstream;

        // number of items to consume
        private int remaining = 10;

        @Override
        public void onSubscribe(Subscription s) {
            this.upstream = s;
            s.request(remaining);
        }

        @Override
        public void onNext(Integer t) {
            bh.consume(t);
            if (--remaining == 0) {
                upstream.cancel();
            }
        }

        @Override
        public void onError(Throwable t) {
            /* ignore */
        }

        @Override
        public void onComplete() {
            /* ignore */
        }
    });
}
```

### Method 21

```java
/**
 * Benchmark that subscribes to a {@link FlowableUnsubscribeOn},
 * requests all items, consumes them via {@link Blackhole},
 * and then cancels the subscription.
 *
 * @param bh Blackhole to consume emitted items and avoid dead‑code elimination.
 */
@Benchmark
public void unsubscribeOn(Blackhole bh) {
    Flowable<Integer> flowable = new FlowableUnsubscribeOn<>(source, scheduler);
    flowable.subscribe(new Subscriber<Integer>() {

        Subscription upstream;

        @Override
        public void onSubscribe(Subscription s) {
            this.upstream = s;
            // Request all items immediately.
            s.request(Long.MAX_VALUE);
        }

        @Override
        public void onNext(Integer t) {
            bh.consume(t);
        }

        @Override
        public void onError(Throwable t) {
            // Errors are not expected in this benchmark; rethrow to fail fast.
            throw new RuntimeException(t);
        }

        @Override
        public void onComplete() {
            // No action needed; cancellation will be triggered after completion.
        }
    });
    // The FlowableUnsubscribeOn schedules the actual upstream.cancel()
    // on the provided scheduler when the downstream cancels.
    // In this benchmark the upstream completes naturally, exercising the
    // scheduled cancellation path.
}
```

### Method 22

```java
/**
 * Benchmark that subscribes to the flat‑mapped Observable and consumes all items.
 *
 * @param bh Blackhole to consume emitted values.
 */
@Benchmark
public void flatMapStreamThroughput(Blackhole bh) {
    // The operator under test.
    Observable<Integer> flatMapped = new ObservableFlatMapStream<>(source, mapper);
    // Subscribe and consume all items; blockingSubscribe ensures the benchmark
    // measures the complete processing of one subscription.
    flatMapped.blockingSubscribe(bh::consume);
}
```

### Method 23

```java
/**
 * Benchmark that subscribes to the {@code takeLast} operator and drains all
 * items, feeding them into the Blackhole.
 *
 * @param bh Blackhole to consume the emitted items.
 */
@Benchmark
public void takeLastThroughput(Blackhole bh) {
    // Apply the operator with the configured count.
    Flowable<Integer> flow = source.takeLast(takeCount);
    // blockingSubscribe ensures the benchmark measures the complete
    // processing of the stream while preventing dead‑code elimination.
    flow.blockingSubscribe(bh::consume);
}
```

### Method 24

```java
/**
 * Benchmark that subscribes to {@code source.count()} and blocks for the result.
 *
 * @param bh Blackhole to consume the result and avoid dead‑code elimination.
 */
@Benchmark
public void countSingle(Blackhole bh) {
    // Create the Single that counts the elements.
    Single<Long> countSingle = source.count();
    // Block until the count is computed.
    long result = countSingle.blockingGet();
    // Consume the result so the JIT does not eliminate the call.
    bh.consume(result);
}
```

### Method 25

```java
/**
 * Benchmark the dispose path of {@link SingleDoOnDispose}.
 *
 * The subscription is immediately disposed, triggering the {@code onDispose} Action.
 */
@Benchmark
public void disposePath(Blackhole bh) {
    // Subscribe with a dummy observer that does nothing on success/error.
    Disposable d = // onSuccess consumer (won't be called)
    doOnDisposeSingle.// onSuccess consumer (won't be called)
    subscribe(// onError consumer (won't be called)
    bh::consume, bh::consume);
    // Immediately dispose to exercise the doOnDispose logic.
    d.dispose();
    // Consume the counter to prevent dead‑code elimination of the Action.
    bh.consume(disposeCounter.get());
}
```

### Method 26

```java
/**
 * Benchmark the early‑termination path where the other Publisher emits first.
 *
 * <p>The operator should complete without emitting the source value.
 */
@Benchmark
public void takeUntilPublisher_earlyTermination(Blackhole bh) {
    Maybe<Integer> maybe = new MaybeTakeUntilPublisher<>(source, otherImmediate);
    // will be null because the Maybe completes without a value
    Integer result = maybe.blockingGet();
    bh.consume(result);
}
```

### Method 27

```java
/**
 * Benchmark the error path where the source emits more than one element.
 * The operator should terminate with an {@link IllegalArgumentException}.
 * The exception is caught to keep the benchmark running.
 */
@Benchmark
public void multipleElementsError() {
    Single<Integer> single = new FlowableSingleSingle<>(multiElementSource, null);
    try {
        single.blockingGet();
    } catch (IllegalArgumentException ignored) {
        // Expected – the operator signals an error when more than one element is observed.
    }
}
```

### Method 28

```java
/**
 * Benchmark the fallback path where the source is empty and a default value is supplied.
 * The operator should emit the default value.
 */
@Benchmark
public Integer emptyWithDefault() {
    Single<Integer> single = new FlowableSingleSingle<>(emptySource, DEFAULT_VALUE);
    return single.blockingGet();
}
```

### Method 29

```java
/**
 * Benchmark the fast‑path (unbounded request) subscription.
 */
@Benchmark
public void fastPath(Blackhole bh) {
    Flowable<Integer> flowable = new FlowableFromIterable<>(source);
    flowable.subscribe(new FastSubscriber(bh));
}
```

### Method 30

```java
/**
 * Benchmark the happy‑path where the source contains exactly one element.
 * The operator should forward the element as {@code Single.onSuccess}.
 */
@Benchmark
public Integer singleElement() {
    Single<Integer> single = new FlowableSingleSingle<>(singleElementSource, null);
    // blockingGet is used to materialise the result synchronously for the benchmark.
    return single.blockingGet();
}
```

### Method 31

```java
/**
 * Benchmark the normal path where the source succeeds before the other Publisher emits.
 *
 * <p>The operator should forward the source value downstream.
 */
@Benchmark
public void takeUntilPublisher_normalPath(Blackhole bh) {
    // The operator under test
    Maybe<Integer> maybe = new MaybeTakeUntilPublisher<>(source, otherNever);
    // blockingGet blocks until the Maybe terminates (either onSuccess or onComplete)
    Integer result = maybe.blockingGet();
    bh.consume(result);
}
```

### Method 32

```java
/**
 * Benchmark the onComplete → supplier path.
 */
@Benchmark
public void completePath(Blackhole bh) {
    // Source that completes without a value.
    Maybe<Integer> source = Maybe.empty();
    Maybe<String> operator = new MaybeFlatMapNotification<>(source, successMapper, errorMapper, completeSupplier);
    operator.blockingSubscribe(bh::consume, bh::consume, () -> bh.consume("completed"));
}
```

### Method 33

```java
/**
 * Benchmark the onError → mapper path.
 */
@Benchmark
public void errorPath(Blackhole bh) {
    // Source that terminates with an exception.
    Maybe<Integer> source = Maybe.error(new IllegalStateException("boom"));
    Maybe<String> operator = new MaybeFlatMapNotification<>(source, successMapper, errorMapper, completeSupplier);
    // blockingSubscribe returns after onError/onComplete.
    operator.blockingSubscribe(bh::consume, bh::consume, () -> bh.consume("completed"));
}
```

### Method 34

```java
/**
 * Benchmark the onSuccess → mapper path.
 */
@Benchmark
public void successPath(Blackhole bh) {
    // Source that emits a single integer value.
    Maybe<Integer> source = Maybe.just(42);
    // Operator under test.
    Maybe<String> operator = new MaybeFlatMapNotification<>(source, successMapper, errorMapper, completeSupplier);
    // Subscribe and block until the value is emitted.
    String result = operator.blockingGet();
    // Consume the result to avoid dead‑code elimination.
    bh.consume(result);
}
```

### Method 35

```java
/**
 * Benchmark the scalarXMap optimization path.
 *
 * The FlowableScalarXMap.scalarXMap method creates a Flowable that, when
 * subscribed to, should take the fast scalar route because both the source
 * value and the mapper result implement {@code Supplier}.
 */
@Benchmark
public void scalarXMap(Blackhole bh) {
    Flowable<Integer> flowable = FlowableScalarXMap.scalarXMap(value, scalarMapper);
    flowable.blockingSubscribe(bh::consume);
}
```

### Method 36

```java
/**
 * Benchmark the slow‑path (bounded request) subscription.
 * The subscriber requests {@code requestSize} items per {@code request} call.
 */
@Benchmark
public void slowPath(Blackhole bh) {
    Flowable<Integer> flowable = new FlowableFromIterable<>(source);
    flowable.subscribe(new SlowSubscriber(bh, requestSize));
}
```

### Method 37

```java
/**
 * Benchmark the success path (no error) to provide a baseline for comparison.
 *
 * Uses a source that emits a value directly; the operator should forward it unchanged.
 */
@Benchmark
public Integer successPath() {
    Single<Integer> successSource = Single.just(1);
    Single<Integer> operator = new SingleOnErrorReturn<>(successSource, FALLBACK_SUPPLIER, 0);
    return operator.blockingGet();
}
```

### Method 38

```java
/**
 * Benchmark the throughput of counting elements in the Flowable.
 *
 * @param bh Blackhole to consume the result and prevent dead‑code elimination.
 */
@Benchmark
public void countElements(Blackhole bh) {
    // count() returns a Single<Long>; blockingGet() materializes the result.
    Single<Long> countSingle = source.count();
    long count = countSingle.blockingGet();
    bh.consume(count);
}
```

### Method 39

```java
/**
 * Benchmark the throughput of the {@code elementAtMaybe} operator.
 */
@Benchmark
public void elementAtMaybe(Blackhole bh) {
    // Create the Maybe that will emit the element at the requested index.
    Maybe<Integer> maybe = new ObservableElementAtMaybe<>(source, index);
    // Force execution and obtain the result.
    Integer result = maybe.blockingGet();
    // Consume the result to avoid dead‑code elimination.
    bh.consume(result);
}
```

### Method 40

```java
/**
 * Benchmark the throughput of {@code FlowableLastMaybe}.
 *
 * @param bh Blackhole to consume the result and avoid dead‑code elimination.
 */
@Benchmark
public void lastMaybeThroughput(Blackhole bh) {
    // Create the operator instance.
    Maybe<Integer> maybe = new FlowableLastMaybe<>(source);
    // Execute the flow and block until completion.
    // blockingGet() returns the last element or {@code null} if the source is empty.
    Integer result = maybe.blockingGet();
    // Consume the result so the JIT cannot optimize the call away.
    bh.consume(result);
}
```

### Method 41

```java
/**
 * Benchmark the throughput of {@link FlowableMapNotification} in the normal onNext path.
 *
 * @param bh Blackhole to consume the downstream values and prevent dead‑code elimination.
 */
@Benchmark
public void mapNotificationThroughput(Blackhole bh) {
    // Create the operator instance with the prepared mappers.
    Flowable<Integer> mapped = new FlowableMapNotification<>(source, onNextMapper, onErrorMapper, onCompleteSupplier);
    // Subscribe and consume all items; the subscription is synchronous for the range source.
    mapped.subscribe(bh::consume);
}
```

### Method 42

```java
/**
 * Benchmark the {@code onComplete} path where the mapper returns an empty Optional.
 *
 * @param bh Blackhole to consume the result (null) and prevent dead‑code elimination.
 */
@Benchmark
public void mapEmpty(Blackhole bh) {
    Maybe<Integer> mapped = new MaybeMapOptional<Integer, Integer>(source, mapperEmpty);
    // returns null when empty
    Integer result = mapped.blockingGet();
    bh.consume(result);
}
```

### Method 43

```java
/**
 * Benchmark the {@code onSuccess} path where the mapper returns a present Optional.
 *
 * @param bh Blackhole to consume the result and prevent dead‑code elimination.
 */
@Benchmark
public void mapPresent(Blackhole bh) {
    Maybe<Integer> mapped = new MaybeMapOptional<Integer, Integer>(source, mapperPresent);
    // always succeeds in this scenario
    Integer result = mapped.blockingGet();
    bh.consume(result);
}
```

### Method 44

```java
/**
 * Benchmark the {@link FlowableAllSingle} operator using {@link Single#blockingGet()}.
 *
 * @param bh Blackhole to consume the result and avoid dead‑code elimination.
 */
@Benchmark
public void allSingleThroughput(Blackhole bh) {
    // Create the operator instance.
    Single<Boolean> allSingle = new FlowableAllSingle<>(source, predicate);
    // Execute the flow synchronously and consume the result.
    Boolean result = allSingle.blockingGet();
    bh.consume(result);
}
```

### Method 45

```java
/**
 * Benchmark using the normal (non‑fusion) path.
 */
@Benchmark
public void normalPath(Blackhole bh) throws InterruptedException {
    Observable<Integer> source = new ObservableFromIterable<>(data);
    CountDownLatch latch = new CountDownLatch(1);
    source.subscribe(new BenchmarkObserver(bh, latch));
    // wait until onComplete
    latch.await();
}
```

### Method 46

```java
/**
 * Benchmark where the source completes before the timeout can fire.
 * The source {@code fastSource} emits a value immediately, the timeout {@code neverTimeout}
 * never emits, so the fallback is never used.
 */
@Benchmark
public void noTimeout(Blackhole bh) {
    Maybe<Integer> timeoutOperator = new MaybeTimeoutPublisher<>(fastSource, neverTimeout, fallback);
    TestObserver<Integer> to = new TestObserver<>();
    timeoutOperator.subscribe(to);
    to.awaitDone(5, TimeUnit.SECONDS);
    bh.consume(to.values());
}
```

### Method 47

```java
/**
 * Benchmark where the timeout fires and the fallback Maybe is subscribed.
 * The source {@code neverSource} never completes, the timeout {@code immediateTimeout}
 * emits right away, causing the fallback {@code fallback} to be subscribed.
 */
@Benchmark
public void timeoutWithFallback(Blackhole bh) {
    Maybe<Integer> timeoutOperator = new MaybeTimeoutPublisher<>(neverSource, immediateTimeout, fallback);
    TestObserver<Integer> to = new TestObserver<>();
    timeoutOperator.subscribe(to);
    to.awaitDone(5, TimeUnit.SECONDS);
    bh.consume(to.values());
}
```

### Method 48

```java
/**
 * Exact bounded windows: timespan == timeskip and maxSize < Long.MAX_VALUE.
 */
@Benchmark
public void exactBounded(Blackhole bh) {
    Flowable<Integer> source = Flowable.range(1, itemCount).subscribeOn(scheduler);
    source.window(timespanMs, TimeUnit.MILLISECONDS, scheduler, maxSize, restartTimerOnMaxSize, bufferSize).flatMap(w -> w).blockingSubscribe(bh::consume);
}
```

### Method 49

```java
/**
 * Exact unbounded windows: timespan == timeskip and maxSize == Long.MAX_VALUE.
 */
@Benchmark
public void exactUnbounded(Blackhole bh) {
    Flowable<Integer> source = Flowable.range(1, itemCount).subscribeOn(scheduler);
    source.window(timespanMs, TimeUnit.MILLISECONDS, scheduler, bufferSize).flatMap(w -> w).blockingSubscribe(bh::consume);
}
```

### Method 50

```java
/**
 * Executes the collect operation using {@link ObservableCollectWithCollector}.
 *
 * The result is consumed by {@link Blackhole} to avoid dead‑code elimination.
 */
@Benchmark
public void collect(Blackhole bh) {
    ObservableCollectWithCollector<Integer, ?, List<Integer>> op = new ObservableCollectWithCollector<>(source, collector);
    // blockingFirst() blocks until the upstream completes and the collector emits the final list.
    List<Integer> result = op.blockingFirst();
    // Consume the result so the JIT cannot optimize the whole pipeline away.
    bh.consume(result);
}
```

### Method 51

```java
/**
 * Executes the flatMapMaybe operator and returns the total number of items processed.
 *
 * @param bh Blackhole to consume each emitted item and avoid dead‑code elimination.
 * @return the number of items emitted downstream (should equal {@code sourceSize}).
 */
@Benchmark
public long flatMapMaybe(Blackhole bh) {
    // Build the operator with the current parameters.
    Flowable<Integer> flow = new FlowableFlatMapMaybe<>(source, mapper, delayErrors, maxConcurrency);
    // Count the items downstream; the count operation itself is a Single<Long>.
    // We also consume each item with Blackhole to ensure the values are used.
    return flow.doOnNext(bh::consume).count().blockingGet();
}
```

### Method 52

```java
/**
 * Executes the mergeWith operator and consumes all emitted items.
 *
 * @param bh Blackhole to consume the items and avoid dead‑code elimination.
 */
@Benchmark
public void mergeWithSingle(Blackhole bh) {
    // Create a fresh merged Observable for each iteration to get a new subscription.
    Observable<Integer> merged = source.mergeWith(single);
    // blockingSubscribe guarantees the benchmark thread waits until the stream completes.
    merged.blockingSubscribe(bh::consume);
}
```

### Method 53

```java
/**
 * Executes the reduce‑with‑seed operation and consumes the result.
 *
 * @param bh Blackhole to consume the final reduced value.
 */
@Benchmark
public void reduceWithSeed(Blackhole bh) {
    // Construct the operator directly to avoid extra operator chaining overhead.
    ObservableReduceSeedSingle<Integer, Integer> reduceSingle = new ObservableReduceSeedSingle<>(source, seed, sumReducer);
    // Subscribe and block to obtain the result. The blocking call is appropriate
    // for a micro‑benchmark because it forces the whole pipeline to execute.
    Single<Integer> single = reduceSingle;
    Integer result = single.blockingGet();
    // Consume the result to prevent dead‑code elimination.
    bh.consume(result);
}
```

### Method 54

```java
/**
 * Executes the sequence‑equal operator and consumes the result.
 *
 * @param bh Blackhole to avoid dead‑code elimination.
 */
@Benchmark
public void sequenceEqual(Blackhole bh) {
    // The operator under test.
    Observable<Boolean> result = new ObservableSequenceEqual<>(source1, source2, EQUALS, bufferSize);
    // Blocking subscription ensures the benchmark measures the full execution.
    boolean equal = result.blockingFirst();
    // Consume the result so the JIT cannot eliminate the call.
    bh.consume(equal);
}
```

### Method 55

```java
/**
 * Executes the {@code SingleFlatMapIterableObservable} pipeline and consumes all
 * emitted items with a {@link Blackhole}.
 *
 * @param bh Blackhole used to consume the items and avoid dead‑code elimination.
 */
@Benchmark
public void flatMapIterable(Blackhole bh) {
    Observable<Integer> observable = new SingleFlatMapIterableObservable<>(source, mapper);
    observable.subscribe(bh::consume);
}
```

### Method 56

```java
/**
 * Measures the throughput of iterating over the entire sequence.
 *
 * @param bh Blackhole to consume values and prevent optimizations.
 */
@Benchmark
public void iterate(Blackhole bh) {
    Iterator<Integer> it = blocking.iterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 57

```java
/**
 * Skip windows: timespan != timeskip.
 */
@Benchmark
public void skip(Blackhole bh) {
    Flowable<Integer> source = Flowable.range(1, itemCount).subscribeOn(scheduler);
    source.window(timespanMs, timeskipMs, TimeUnit.MILLISECONDS, scheduler, bufferSize).flatMap(w -> w).blockingSubscribe(bh::consume);
}
```

### Method 58

```java
/**
 * Subscribes to the Observable, consumes all emitted items via Blackhole,
 * and then disposes the subscription to trigger the {@code unsubscribeOn}
 * path. The method is measured in throughput mode (operations per second).
 *
 * @param bh Blackhole to consume emitted items and avoid dead‑code elimination.
 */
@Benchmark
public void subscribeConsumeAndDispose(Blackhole bh) {
    // Subscribe and forward each item to the Blackhole.
    // The Disposable is retained so we can dispose it immediately,
    // exercising the asynchronous disposal logic.
    var disposable = source.subscribe(bh::consume);
    // Trigger the asynchronous disposal path.
    disposable.dispose();
}
```

### Method 59

```java
/**
 * Subscribes to the SingleFlattenStreamAsObservable and consumes all emitted items.
 * The Blackhole ensures that the emitted values are not optimized away.
 */
@Benchmark
public void flattenStreamAsObservable(Blackhole bh) {
    Observable<Integer> observable = new SingleFlattenStreamAsObservable<>(source, mapper);
    observable.subscribe(new Observer<Integer>() {

        @Override
        public void onSubscribe(@NonNull Disposable d) {
            // No-op
        }

        @Override
        public void onNext(@NonNull Integer value) {
            bh.consume(value);
        }

        @Override
        public void onError(@NonNull Throwable e) {
            // Propagate errors to the Blackhole to avoid dead code elimination
            bh.consume(e);
        }

        @Override
        public void onComplete() {
            // No-op
        }
    });
}
```

### Method 60

```java
/**
 * Variant that runs the merge on a dedicated Scheduler to emulate typical
 * asynchronous usage. This helps to assess the overhead of thread hopping.
 */
@Benchmark
public void mergeCompletableAsync() {
    CompletableMerge merge = new CompletableMerge(upstream, maxConcurrency, delayErrors);
    // Subscribe on a computation scheduler to introduce async boundaries.
    merge.subscribeOn(Schedulers.computation()).blockingAwait();
}
```

### Method 61

```java
@Benchmark
public Boolean anySingleThroughput() {
    ObservableAnySingle<Integer> anySingle = new ObservableAnySingle<>(source, predicate);
    return anySingle.blockingGet();
}
```

### Method 62

```java
@Benchmark
public Integer reduceAndBlock() {
    // Observable.reduce returns a Maybe directly
    Maybe<Integer> maybe = source.reduce(sumReducer);
    return maybe.blockingGet();
}
```

### Method 63

```java
@Benchmark
public long arrayListIterate() {
    long sum = 0;
    for (Integer i : arrayList) {
        sum += i;
    }
    return sum;
}
```

### Method 64

```java
@Benchmark
public long conditionalSubscriber(StreamHolder holder) {
    Stream<Integer> stream = holder.newStream();
    Flowable<Integer> flowable = new FlowableFromStream<>(stream);
    CountingConditionalSubscriber<Integer> subscriber = new CountingConditionalSubscriber<>();
    flowable.subscribe(subscriber);
    long emitted = subscriber.getCount();
    subscriber.reset();
    return emitted;
}
```

### Method 65

```java
@Benchmark
public long eagerConcatMapThroughput(BenchmarkState state, Blackhole bh) throws InterruptedException {
    ObservableConcatMapEager<Integer, Integer> operator = new ObservableConcatMapEager<>(state.source, state.mapper, ErrorMode.IMMEDIATE, state.maxConcurrency, state.prefetch);
    CountDownLatch latch = new CountDownLatch(1);
    BenchmarkState.CountingObserver observer = new BenchmarkState.CountingObserver(latch, bh);
    operator.subscribe(observer);
    latch.await();
    return observer.count.get();
}
```

### Method 66

```java
@Benchmark
public long regularSubscriber(StreamHolder holder) {
    Stream<Integer> stream = holder.newStream();
    Flowable<Integer> flowable = new FlowableFromStream<>(stream);
    CountingSubscriber<Integer> subscriber = new CountingSubscriber<>();
    flowable.subscribe(subscriber);
    long emitted = subscriber.getCount();
    subscriber.reset();
    return emitted;
}
```

### Method 67

```java
@Benchmark
public long testRetryWhen() {
    AtomicInteger counter = new AtomicInteger();
    observable.blockingForEach(i -> counter.incrementAndGet());
    return counter.get();
}
```

### Method 68

```java
@Benchmark
public long volatileIterate() {
    long sum = 0;
    for (Integer i : volatileList) {
        sum += i;
    }
    return sum;
}
```

### Method 69

```java
@Benchmark
public void bufferBoundaryThroughput(Blackhole bh) throws InterruptedException {
    Flowable<List<Integer>> buffered = source.buffer(openPublisher, closeFunction, bufferSupplier);
    CountDownLatch latch = new CountDownLatch(1);
    // onNext
    buffered.// onNext
    subscribe(// onError
    bh::consume, // onComplete
    bh::consume, latch::countDown);
    latch.await();
}
```

### Method 70

```java
@Benchmark
public void collectToList(Blackhole bh) {
    // Instantiate the operator directly.
    ObservableToList<Integer, List<Integer>> toListOperator = new ObservableToList<>(source, collectionSupplier);
    // Blocking call to trigger the whole flow and obtain the resulting list.
    List<Integer> result = toListOperator.blockingFirst();
    // Consume the result to avoid dead‑code elimination.
    bh.consume(result);
}
```

### Method 71

```java
@Benchmark
public void concatMapCompletableThroughput(BenchmarkState state, Blackhole bh) {
    // Build the operator under test.
    Completable concat = new ObservableConcatMapCompletable<>(state.source, state.mapper, state.errorMode, state.prefetch);
    // Subscribe and block until completion.
    // Using an AtomicInteger to ensure the subscription side‑effects are observed.
    AtomicInteger done = new AtomicInteger();
    concat.subscribe(new CompletableObserver() {

        @Override
        public void onSubscribe(Disposable d) {
            // No-op
        }

        @Override
        public void onError(Throwable e) {
            // Propagate error to Blackhole to avoid dead‑code elimination.
            bh.consume(e);
            done.set(1);
        }

        @Override
        public void onComplete() {
            done.set(1);
        }
    });
    // Busy‑wait until the Completable signals termination.
    // This is safe in a benchmark because the work is tiny and the loop
    // will exit quickly; it also avoids using Thread.sleep which would
    // distort throughput measurements.
    while (done.get() == 0) {
        // spin
    }
    // Consume a dummy value to keep the JIT from optimizing away the whole pipeline.
    bh.consume(state.sourceSize);
}
```

### Method 72

```java
@Benchmark
public void concatMapScheduler(Blackhole bh) {
    Flowable<Integer> flowable = new FlowableConcatMapScheduler<>(source, mapper, prefetch, errorMode, scheduler);
    flowable.subscribe(new Consumer<Integer>() {

        @Override
        public void accept(Integer value) {
            bh.consume(value);
        }
    }, bh::consume);
}
```

### Method 73

```java
@Benchmark
public void disposeObservers(DisposeState state) {
    for (Disposable d : state.disposables) {
        d.dispose();
    }
}
```

### Method 74

```java
@Benchmark
public void filterThroughput(Blackhole bh) {
    Flowable<Integer> source = Flowable.range(1, itemCount);
    source.filter(predicate).blockingForEach(bh::consume);
}
```

### Method 75

```java
@Benchmark
public void flatMapIterable(Blackhole bh) throws InterruptedException {
    // Create the operator instance directly
    MaybeFlatMapIterableFlowable<Integer, Integer> flowable = new MaybeFlatMapIterableFlowable<>(source, mapper);
    // Latch to wait for onComplete/onError
    CountDownLatch latch = new CountDownLatch(1);
    flowable.subscribe(new io.reactivex.rxjava3.core.FlowableSubscriber<Integer>() {

        @Override
        public void onSubscribe(org.reactivestreams.Subscription s) {
            // Request an unbounded number of items for the benchmark
            s.request(Long.MAX_VALUE);
        }

        @Override
        public void onNext(Integer t) {
            // Consume the item to avoid dead‑code elimination
            bh.consume(t);
        }

        @Override
        public void onError(Throwable t) {
            // Propagate errors to the benchmark harness
            t.printStackTrace();
            latch.countDown();
        }

        @Override
        public void onComplete() {
            latch.countDown();
        }
    });
    // Wait until the flowable signals completion
    latch.await();
}
```

### Method 76

```java
@Benchmark
public void flatMapThroughput(Blackhole bh) {
    Flowable<Integer> source = Flowable.range(0, sourceSize);
    source.flatMap(mapper, delayErrors, maxConcurrency, bufferSize).blockingSubscribe(bh::consume);
}
```

### Method 77

```java
@Benchmark
public void iterate(Blackhole bh) {
    Iterator<Integer> it = iterable.iterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 78

```java
@Benchmark
public void iterateAll(Blackhole bh) {
    Iterator<Integer> it = blocking.iterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 79

```java
@Benchmark
public void joinAndConsume(Blackhole bh) throws InterruptedException {
    CountDownLatch latch = new CountDownLatch(1);
    ParallelJoin<Integer> joined = new ParallelJoin<>(source, prefetch, delayErrors);
    joined.subscribe(new Subscriber<Integer>() {

        @Override
        public void onSubscribe(Subscription s) {
            s.request(Long.MAX_VALUE);
        }

        @Override
        public void onNext(Integer t) {
            bh.consume(t);
        }

        @Override
        public void onError(Throwable t) {
            latch.countDown();
        }

        @Override
        public void onComplete() {
            latch.countDown();
        }
    });
    if (!latch.await(30, TimeUnit.SECONDS)) {
        throw new IllegalStateException("Benchmark timed out");
    }
}
```

### Method 80

```java
@Benchmark
public void mapOptionalThroughput(Blackhole bh) {
    ObservableMapOptional<Integer, Integer> mapped = new ObservableMapOptional<Integer, Integer>(source, mapper);
    mapped.blockingSubscribe(new Observer<Integer>() {

        @Override
        public void onSubscribe(Disposable d) {
            // no‑op
        }

        @Override
        public void onNext(Integer value) {
            bh.consume(value);
        }

        @Override
        public void onError(Throwable e) {
            throw new RuntimeException(e);
        }

        @Override
        public void onComplete() {
            // no‑op
        }
    });
}
```

### Method 81

```java
@Benchmark
public void mapOptionalThroughput(Blackhole bh) {
    ParallelMapOptional<Integer, Integer> operator = new ParallelMapOptional<Integer, Integer>(source, mapper);
    operator.sequential().subscribe(bh::consume);
}
```

### Method 82

```java
@Benchmark
public void mergeCompletableIterables(Blackhole bh) throws InterruptedException {
    CompletableMergeIterable merge = new CompletableMergeIterable(iterableSources);
    CountDownLatch latch = new CountDownLatch(1);
    merge.subscribe(new CompletableObserver() {

        @Override
        public void onSubscribe(Disposable d) {
            // No need to keep the disposable; the benchmark will wait for completion.
        }

        @Override
        public void onError(Throwable e) {
            // Propagate error to Blackhole to avoid dead code elimination.
            bh.consume(e);
            latch.countDown();
        }

        @Override
        public void onComplete() {
            latch.countDown();
        }
    });
    // Wait for the merged Completable to finish.
    latch.await();
}
```

### Method 83

```java
@Benchmark
public void reduceWithSeed(Blackhole bh) {
    Single<Integer> reduced = new FlowableReduceSeedSingle<Integer, Integer>(source, SEED, SUM_REDUCER);
    Integer result = reduced.blockingGet();
    bh.consume(result);
}
```

### Method 84

```java
@Benchmark
public void repeatThroughput(Blackhole bh) {
    Disposable d = // onNext
    repeatedObservable.// onNext
    subscribe(// onError (should not happen)
    bh::consume, // onComplete
    bh::consume, () -> bh.consume(0));
    d.dispose();
}
```

### Method 85

```java
@Benchmark
public void runOnThroughput(Blackhole bh) throws InterruptedException {
    // Build the parallel flow, apply runOn, then merge back to sequential.
    ParallelFlowable<Integer> parallel = source.parallel(parallelism);
    Flowable<Integer> runOn = parallel.runOn(Schedulers.computation(), prefetch).sequential();
    // Use a latch to wait for completion without blocking the JMH thread.
    CountDownLatch latch = new CountDownLatch(1);
    runOn.subscribe(new DisposableSubscriber<Integer>() {

        @Override
        public void onNext(Integer t) {
            // Consume the item via Blackhole to prevent dead‑code elimination.
            bh.consume(t);
        }

        @Override
        public void onError(Throwable t) {
            // Errors are unexpected in this benchmark; rethrow to fail the run.
            t.printStackTrace();
            latch.countDown();
        }

        @Override
        public void onComplete() {
            latch.countDown();
        }
    });
    // Wait until the flow finishes processing all items.
    latch.await();
}
```

### Method 86

```java
@Benchmark
public void scanSeedThroughput(Blackhole bh) {
    Observable<Integer> scanned = source.scanWith(seedSupplier, accumulator);
    scanned.blockingSubscribe(bh::consume);
}
```

### Method 87

```java
@Benchmark
public void sortedJoin(Blackhole bh) throws InterruptedException {
    CountDownLatch latch = new CountDownLatch(1);
    ParallelSortedJoin<Integer> operator = new ParallelSortedJoin<>(source, comparator);
    operator.subscribe(new Subscriber<Integer>() {

        Subscription upstream;

        @Override
        public void onSubscribe(Subscription s) {
            this.upstream = s;
            // Request an unbounded number of items to keep the benchmark focused on
            // the operator's internal merging logic.
            s.request(Long.MAX_VALUE);
        }

        @Override
        public void onNext(Integer t) {
            bh.consume(t);
        }

        @Override
        public void onError(Throwable t) {
            latch.countDown();
        }

        @Override
        public void onComplete() {
            latch.countDown();
        }
    });
    // Wait for the flow to finish before ending the measurement iteration.
    latch.await();
}
```

### Method 88

```java
@Benchmark
public void subscribeAndConsume() {
    Observable<Integer> source = new ObservableFromCompletionStage<>(completedStage);
    TestObserver<Integer> testObserver = new TestObserver<>();
    source.subscribe(testObserver);
    // Ensure the emission is processed; timeout is generous for JMH stability
    testObserver.awaitDone(1, TimeUnit.SECONDS);
    // Optionally verify correctness (kept minimal to avoid affecting throughput)
    // testObserver.assertValue(VALUE).assertNoErrors().assertComplete();
}
```

### Method 89

```java
@Benchmark
public void takeLastTimedThroughput(BenchmarkState state, Blackhole bh) {
    // Build the operator instance directly to isolate its performance.
    ObservableTakeLastTimed<Integer> operator = new ObservableTakeLastTimed<>(state.source, state.count, state.timeMs, state.unit, state.scheduler, state.bufferSize, state.delayError);
    // Subscribe and consume all items, forcing the operator to drain.
    operator.subscribe(bh::consume);
}
```

### Method 90

```java
@Benchmark
public void throttleLatestThroughput(Blackhole bh) {
    // Apply the operator with the configured parameters.
    Flowable<Long> throttled = source.throttleLatest(timeout, TimeUnit.MILLISECONDS, scheduler, emitLast, onDropped);
    // Subscribe and consume items with Blackhole to prevent dead‑code elimination.
    subscription = throttled.subscribe(bh::consume, bh::consume, () -> {
    });
}
```

### Method 91

```java
@Benchmark
public void windowBoundarySelectorThroughput(Blackhole bh) throws InterruptedException {
    Observable<Integer> source = Observable.range(1, itemCount).subscribeOn(scheduler);
    Observable<Long> open = Observable.intervalRange(0, (itemCount + windowOpenInterval - 1) / windowOpenInterval, 0, 0, TimeUnit.MILLISECONDS, scheduler).map(i -> i * windowOpenInterval);
    Function<Long, ObservableSource<Long>> closingIndicator = start -> {
        long closeAfter = Math.min(windowCloseInterval, itemCount - start);
        return Observable.timer(closeAfter, TimeUnit.MILLISECONDS, scheduler);
    };
    Observable<Observable<Integer>> windowed = new ObservableWindowBoundarySelector<>(source, open, closingIndicator, bufferSize);
    CountDownLatch latch = latchFactory.createLatch(1);
    Disposable d = windowed.flatMap(w -> w.doOnNext(item -> bh.consume(item)).ignoreElements().toObservable()).doOnComplete(latch::countDown).subscribe();
    if (!latch.await(30, TimeUnit.SECONDS)) {
        d.dispose();
        throw new IllegalStateException("Benchmark timed out");
    }
    d.dispose();
}
```

### Method 92

```java
@Benchmark
public void windowBoundaryThroughput(BenchmarkState state, Blackhole bh) throws InterruptedException {
    // Create the operator instance with the pre‑built source and boundary.
    ObservableWindowBoundary<Integer, Integer> operator = new ObservableWindowBoundary<>(state.source, state.boundary, state.capacityHint);
    // Latch to wait for completion of the whole stream.
    CountDownLatch latch = new CountDownLatch(1);
    // Subscribe to the operator.
    operator.subscribe(new Observer<Observable<Integer>>() {

        @Override
        public void onSubscribe(Disposable d) {
            // No need to keep the Disposable; the benchmark runs to completion.
        }

        @Override
        public void onNext(Observable<Integer> window) {
            // For each window, subscribe and consume its items.
            window.subscribe(new Observer<Integer>() {

                @Override
                public void onSubscribe(Disposable d) {
                    // No action needed.
                }

                @Override
                public void onNext(Integer value) {
                    // Consume the value to avoid dead‑code elimination.
                    bh.consume(value);
                }

                @Override
                public void onError(Throwable e) {
                    // Propagate errors to the latch to avoid hanging.
                    latch.countDown();
                }

                @Override
                public void onComplete() {
                    // No per‑window completion handling required.
                }
            });
        }

        @Override
        public void onError(Throwable e) {
            // Signal benchmark termination on error.
            latch.countDown();
        }

        @Override
        public void onComplete() {
            // Signal that the whole stream has finished.
            latch.countDown();
        }
    });
    // Wait for the stream to finish before returning control to JMH.
    latch.await();
}
```

### Method 93

```java
@Benchmark
public void windowTimedThroughput(BenchmarkState state, Blackhole bh) {
    // Use the exact‑window overload that includes maxSize, restartTimerOnMaxSize and bufferSize.
    Observable<Observable<Integer>> windows = state.source.window(state.timespanMs, TimeUnit.MILLISECONDS, state.scheduler, state.maxSize, state.restartTimerOnMaxSize, state.bufferSize);
    // Consume each window fully using lastOrError() to obtain a Single per window.
    windows.flatMapSingle(w -> w.lastOrError()).blockingSubscribe(bh::consume);
}
```

### Method 94

```java
@Benchmark
public void withLatestFromMany(BenchmarkState state, Blackhole bh) {
    // Create the operator instance directly (public constructor).
    ObservableWithLatestFromMany<Integer, Integer> observable = new ObservableWithLatestFromMany<>(state.source, state.others, state.combiner);
    // Subscribe and consume all items, ensuring the pipeline runs to completion.
    observable.blockingSubscribe(bh::consume);
}
```

### Method 95

```java
@Benchmark
public void zipSingleThroughput(BenchmarkState state, Blackhole bh) {
    // Create the zip operator.
    Single<Integer> zipSingle = state.createZipSingle();
    // Subscribe and block to obtain the result.
    // The blocking call is part of the measured operation because it represents the
    // end‑to‑end latency of the zip operator.
    Integer result = // ensure subscription happens on the dedicated scheduler
    zipSingle.// ensure subscription happens on the dedicated scheduler
    subscribeOn(state.scheduler).blockingGet();
    // Consume the result to prevent dead‑code elimination.
    bh.consume(result);
}
```

## JMH UNSAFELOOP INSIDE BENCHMARK - Suspicious numeric accumulation inside a loop in the JMH benchmark function.

### Method 1

```java
/**
 * Benchmark that iterates over the entire Flowable using the blocking iterator.
 * The returned sum prevents dead‑code elimination.
 *
 * @return the sum of all emitted integers
 */
@Benchmark
public int iterateAndSum() {
    int sum = 0;
    Iterator<Integer> it = blocking.iterator();
    while (it.hasNext()) {
        sum += it.next();
    }
    return sum;
}
```

### Method 2

```java
@Benchmark
public long arrayListIterate() {
    long sum = 0;
    for (Integer i : arrayList) {
        sum += i;
    }
    return sum;
}
```

### Method 3

```java
@Benchmark
public long volatileIterate() {
    long sum = 0;
    for (Integer i : volatileList) {
        sum += i;
    }
    return sum;
}
```

## JMH STATE FINAL PRIMITIVE - JMH State primitive field declared final.

### Method 1

```java
package io.reactivex.rxjava3.internal.operators.observable;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * Benchmark for {@link ObservableWindowBoundary}.
 *
 * The benchmark creates a source Observable that emits a configurable number of integers
 * and a boundary Observable that emits a signal after each item, causing a new window to be opened.
 * Throughput is measured as the number of windows (and consequently the number of items) processed per second.
 *
 * Best practices applied:
 * - Use @State(Scope.Thread) to avoid sharing mutable state between threads.
 * - Pre‑create the source and boundary Observables in @Setup(Level.Trial) to exclude their construction cost.
 * - Use Blackhole to consume emitted items and prevent dead‑code elimination.
 * - Block until the stream completes with a CountDownLatch to ensure the benchmark measures the full processing.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
public class ObservableWindowBoundaryBenchmark {

    @State(Scope.Thread)
    public static class BenchmarkState {

        /**
         * Number of items emitted by the source Observable.
         */
        @Param({ "1000", "10000", "100000" })
        public int itemCount;

        /**
         * Hint for the internal UnicastSubject capacity.
         */
        public final int capacityHint = 128;

        /**
         * Source Observable emitting a range of integers.
         */
        public Observable<Integer> source;

        /**
         * Boundary Observable that emits a signal after each source item, closing the current window.
         */
        public Observable<Integer> boundary;

        @Setup(Level.Trial)
        public void setUp() {
            // Emit exactly {@code itemCount} items.
            source = Observable.range(1, itemCount);
            // Emit a boundary signal after each source item, forcing a new window per item.
            // Using the same range ensures deterministic behavior without timers.
            boundary = Observable.range(0, itemCount);
        }
    }

    @Benchmark
    public void windowBoundaryThroughput(BenchmarkState state, Blackhole bh) throws InterruptedException {
        // Create the operator instance with the pre‑built source and boundary.
        ObservableWindowBoundary<Integer, Integer> operator = new ObservableWindowBoundary<>(state.source, state.boundary, state.capacityHint);
        // Latch to wait for completion of the whole stream.
        CountDownLatch latch = new CountDownLatch(1);
        // Subscribe to the operator.
        operator.subscribe(new Observer<Observable<Integer>>() {

            @Override
            public void onSubscribe(Disposable d) {
                // No need to keep the Disposable; the benchmark runs to completion.
            }

            @Override
            public void onNext(Observable<Integer> window) {
                // For each window, subscribe and consume its items.
                window.subscribe(new Observer<Integer>() {

                    @Override
                    public void onSubscribe(Disposable d) {
                        // No action needed.
                    }

                    @Override
                    public void onNext(Integer value) {
                        // Consume the value to avoid dead‑code elimination.
                        bh.consume(value);
                    }

                    @Override
                    public void onError(Throwable e) {
                        // Propagate errors to the latch to avoid hanging.
                        latch.countDown();
                    }

                    @Override
                    public void onComplete() {
                        // No per‑window completion handling required.
                    }
                });
            }

            @Override
            public void onError(Throwable e) {
                // Signal benchmark termination on error.
                latch.countDown();
            }

            @Override
            public void onComplete() {
                // Signal that the whole stream has finished.
                latch.countDown();
            }
        });
        // Wait for the stream to finish before returning control to JMH.
        latch.await();
    }
}
```

### Method 2

```java
package io.reactivex.rxjava3.internal.operators.single;

import java.util.concurrent.TimeUnit;
import io.reactivex.rxjava3.annotations.*;
import io.reactivex.rxjava3.core.*;
import io.reactivex.rxjava3.disposables.*;
import io.reactivex.rxjava3.exceptions.*;
import io.reactivex.rxjava3.flowables.*;
import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.disposables.*;
import io.reactivex.rxjava3.internal.functions.*;
import io.reactivex.rxjava3.internal.fuseable.*;
import io.reactivex.rxjava3.internal.jdk8.*;
import io.reactivex.rxjava3.internal.observers.*;
import io.reactivex.rxjava3.internal.operators.completable.*;
import io.reactivex.rxjava3.internal.operators.flowable.*;
import io.reactivex.rxjava3.internal.operators.maybe.*;
import io.reactivex.rxjava3.internal.operators.mixed.*;
import io.reactivex.rxjava3.internal.operators.observable.*;
import io.reactivex.rxjava3.internal.operators.parallel.*;
import io.reactivex.rxjava3.internal.operators.single.*;
import io.reactivex.rxjava3.internal.queue.*;
import io.reactivex.rxjava3.internal.schedulers.*;
import io.reactivex.rxjava3.internal.subscribers.*;
import io.reactivex.rxjava3.internal.subscriptions.*;
import io.reactivex.rxjava3.internal.util.*;
import io.reactivex.rxjava3.observables.*;
import io.reactivex.rxjava3.observers.*;
import io.reactivex.rxjava3.operators.*;
import io.reactivex.rxjava3.parallel.*;
import io.reactivex.rxjava3.plugins.*;
import io.reactivex.rxjava3.processors.*;
import io.reactivex.rxjava3.schedulers.*;
import io.reactivex.rxjava3.subjects.*;
import io.reactivex.rxjava3.subscribers.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link SingleTimeout}.
 *
 * The benchmarks measure the throughput of:
 * 1. A plain {@link Single#just(Object)} (baseline).
 * 2. A {@link SingleTimeout} that completes before the timeout (happy path).
 *
 * The timeout is set to a value larger than the execution time of the source
 * to avoid triggering the fallback, thus measuring the overhead of the operator
 * itself.
 *
 * Best practices applied:
 * - Use @State(Scope.Thread) to avoid sharing mutable state between threads.
 * - Warm‑up and measurement iterations are defined.
 * - Blackhole consumes the result to prevent dead‑code elimination.
 * - The benchmark runs in Mode.Throughput with results expressed per second.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@Threads(1)
public class SingleTimeoutBenchmark {

    @State(Scope.Thread)
    public static class BenchmarkState {

        /**
         * Scheduler used by the timeout operator.
         */
        Scheduler scheduler;

        /**
         * Source that emits a value immediately.
         */
        Single<Integer> source;

        /**
         * SingleTimeout wrapping the source with a timeout that never fires.
         */
        Single<Integer> timeoutSingle;

        /**
         * Timeout duration (large enough to never trigger).
         */
        // 10 seconds
        final long timeout = 10_000L;

        final TimeUnit unit = TimeUnit.MILLISECONDS;

        @Setup(Level.Trial)
        public void setUp() {
            // Use a single‑threaded scheduler to keep scheduling deterministic.
            scheduler = Schedulers.single();
            // Immediate source.
            source = Single.just(1);
            // No fallback – we only want to measure the successful path.
            SingleSource<? extends Integer> fallback = null;
            // Create the operator under test.
            timeoutSingle = new SingleTimeout<>(source, timeout, unit, scheduler, fallback);
        }
    }

    /**
     * Baseline benchmark: subscribe to a plain Single.just and block for the result.
     */
    @Benchmark
    public void baseline(Blackhole bh, BenchmarkState state) {
        int value = state.source.blockingGet();
        bh.consume(value);
    }

    /**
     * Benchmark the SingleTimeout operator when the source completes before the timeout.
     */
    @Benchmark
    public void timeoutSuccess(Blackhole bh, BenchmarkState state) {
        int value = state.timeoutSingle.blockingGet();
        bh.consume(value);
    }
}
```

