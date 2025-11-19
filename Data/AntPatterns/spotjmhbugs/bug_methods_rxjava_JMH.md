## JMH IGNORED METHOD RETURN - Method return not used or consumed by a Blackhole.

### Method 1 (true anti-pattern)

```java
@Benchmark
public void flowable() {
    final CountDownLatch cdl = new CountDownLatch(1);
    flowable.subscribe(this, Functions.emptyConsumer(), new Action() {

        @Override
        public void run() {
            cdl.countDown();
        }
    });
    while (cdl.getCount() != 0) {
    }
}
```

### Method 2 (true anti-pattern)

```java
@Benchmark
public void observable() {
    final CountDownLatch cdl = new CountDownLatch(1);
    observable.subscribe(this, Functions.emptyConsumer(), new Action() {

        @Override
        public void run() {
            cdl.countDown();
        }
    });
    while (cdl.getCount() != 0) {
    }
}
```

### Method 3 (false alert)

```java
@Benchmark
public void observeOnCompletable(Blackhole bh) {
    observeOnCompletable.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```

### Method 4

```java
@Benchmark
public void observeOnCompletable(Blackhole bh) {
    observeOnCompletable.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```

### Method 5 (false alert)

```java
@Benchmark
public void observeOnFlowable(Blackhole bh) {
    observeOnFlowable.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```

### Method 7 (false alert)

```java
@Benchmark
public void observeOnMaybe(Blackhole bh) {
    observeOnMaybe.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```


### Method 9 (false alert)

```java
@Benchmark
public void observeOnObservable(Blackhole bh) {
    observeOnObservable.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```

### Method 11

```java
@Benchmark
public void observeOnSingle(Blackhole bh) {
    observeOnSingle.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```


### Method 13 (false alert)

```java
@Benchmark
public void pipelineCompletable(Blackhole bh) {
    pipelineCompletable.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```

### Method 15 (false alert)

```java
@Benchmark
public void pipelineFlowable(Blackhole bh) {
    pipelineFlowable.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```


### Method 17 (false alert)

```java
@Benchmark
public void pipelineMaybe(Blackhole bh) {
    pipelineMaybe.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```


### Method 19 (false alert)

```java
@Benchmark
public void pipelineObservable(Blackhole bh) {
    pipelineObservable.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```

### Method 21 (false alert)

```java
@Benchmark
public void pipelineSingle(Blackhole bh) {
    pipelineSingle.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```

### Method 23 (false alert)

```java
@Benchmark
public void subscribeOnCompletable(Blackhole bh) {
    subscribeOnCompletable.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```

### Method 25 (false alert)

```java
@Benchmark
public void subscribeOnFlowable(Blackhole bh) {
    subscribeOnFlowable.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```

### Method 27 (false alert)

```java
@Benchmark
public void subscribeOnMaybe(Blackhole bh) {
    subscribeOnMaybe.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```


### Method 29 (false alert)

```java
@Benchmark
public void subscribeOnObservable(Blackhole bh) {
    subscribeOnObservable.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```


### Method 31 (false alert)

```java
@Benchmark
public void subscribeOnSingle(Blackhole bh) {
    subscribeOnSingle.subscribeWith(new PerfAsyncConsumer(bh)).await(1);
}
```


## JMH LOOP INSIDE BENCHMARK - Usage of loops in the JMH benchmark function.

### Method 1

```java
// flatMap
@Benchmark
public void merge1SyncStreamOfN(final InputMillion input) throws InterruptedException {
    Flowable<Flowable<Integer>> os = Flowable.just(1).map(new Function<Integer, Flowable<Integer>>() {

        @Override
        public Flowable<Integer> apply(Integer i) {
            return Flowable.range(0, input.size);
        }
    });
    PerfSubscriber o = input.newLatchedObserver();
    Flowable.merge(os).subscribe(o);
    if (input.size == 1) {
        while (o.latch.getCount() != 0) {
        }
    } else {
        o.latch.await();
    }
}
```

### Method 2

```java
// flatMap
@Benchmark
public void oneStreamOfNthatMergesIn1(final InputMillion input) throws InterruptedException {
    Flowable<Flowable<Integer>> os = Flowable.range(1, input.size).map(new Function<Integer, Flowable<Integer>>() {

        @Override
        public Flowable<Integer> apply(Integer v) {
            return Flowable.just(v);
        }
    });
    PerfSubscriber o = input.newLatchedObserver();
    Flowable.merge(os).subscribe(o);
    if (input.size == 1) {
        while (o.latch.getCount() != 0) {
        }
    } else {
        o.latch.await();
    }
}
```

### Method 3

```java
@Benchmark
public void bounded1k() {
    for (int i = 0; i < 1000; i++) {
        bounded.onNext(1);
    }
}
```

### Method 4

```java
@Benchmark
public void bounded1m() {
    for (int i = 0; i < 1000000; i++) {
        bounded.onNext(1);
    }
}
```

### Method 5

```java
@Benchmark
public void flatMapIntPassthruAsync(Input input) throws InterruptedException {
    PerfSubscriber latchedObserver = input.newLatchedObserver();
    input.flowable.flatMap(new Function<Integer, Publisher<Integer>>() {

        @Override
        public Publisher<Integer> apply(Integer i) {
            return Flowable.just(i).subscribeOn(Schedulers.computation());
        }
    }).subscribe(latchedObserver);
    if (input.size == 1) {
        while (latchedObserver.latch.getCount() != 0) {
        }
    } else {
        latchedObserver.latch.await();
    }
}
```

### Method 6

```java
@Benchmark
public void flowable() {
    final CountDownLatch cdl = new CountDownLatch(1);
    flowable.subscribe(this, Functions.emptyConsumer(), new Action() {

        @Override
        public void run() {
            cdl.countDown();
        }
    });
    while (cdl.getCount() != 0) {
    }
}
```

### Method 7

```java
@Benchmark
public void mergeNAsyncStreamsOfN(final InputThousand input) throws InterruptedException {
    Flowable<Flowable<Integer>> os = input.flowable.map(new Function<Integer, Flowable<Integer>>() {

        @Override
        public Flowable<Integer> apply(Integer i) {
            return Flowable.range(0, input.size).subscribeOn(Schedulers.computation());
        }
    });
    PerfSubscriber o = input.newLatchedObserver();
    Flowable.merge(os).subscribe(o);
    if (input.size == 1) {
        while (o.latch.getCount() != 0) {
        }
    } else {
        o.latch.await();
    }
}
```

### Method 8

```java
@Benchmark
public void mergeNSyncStreamsOf1(final InputForMergeN input) throws InterruptedException {
    PerfSubscriber o = input.newLatchedObserver();
    Flowable.merge(input.observables).subscribe(o);
    if (input.size == 1) {
        while (o.latch.getCount() != 0) {
        }
    } else {
        o.latch.await();
    }
}
```

### Method 9

```java
@Benchmark
public void mergeNSyncStreamsOfN(final InputThousand input) throws InterruptedException {
    Flowable<Flowable<Integer>> os = input.flowable.map(new Function<Integer, Flowable<Integer>>() {

        @Override
        public Flowable<Integer> apply(Integer i) {
            return Flowable.range(0, input.size);
        }
    });
    PerfSubscriber o = input.newLatchedObserver();
    Flowable.merge(os).subscribe(o);
    if (input.size == 1) {
        while (o.latch.getCount() != 0) {
        }
    } else {
        o.latch.await();
    }
}
```

### Method 10

```java
@Benchmark
public void mergeTwoAsyncStreamsOfN(final InputThousand input) throws InterruptedException {
    PerfSubscriber o = input.newLatchedObserver();
    Flowable<Integer> ob = Flowable.range(0, input.size).subscribeOn(Schedulers.computation());
    Flowable.merge(ob, ob).subscribe(o);
    if (input.size == 1) {
        while (o.latch.getCount() != 0) {
        }
    } else {
        o.latch.await();
    }
}
```

### Method 11

```java
@Benchmark
public void observable() {
    final CountDownLatch cdl = new CountDownLatch(1);
    observable.subscribe(this, Functions.emptyConsumer(), new Action() {

        @Override
        public void run() {
            cdl.countDown();
        }
    });
    while (cdl.getCount() != 0) {
    }
}
```

### Method 12

```java
@Benchmark
public void subject1k() {
    for (int i = 0; i < 1000; i++) {
        subject.onNext(1);
    }
}
```

### Method 13

```java
@Benchmark
public void subject1m() {
    for (int i = 0; i < 1000000; i++) {
        subject.onNext(1);
    }
}
```

### Method 14

```java
@Benchmark
public void unbounded1k() {
    for (int i = 0; i < 1000; i++) {
        unbounded.onNext(1);
    }
}
```

### Method 15

```java
@Benchmark
public void unbounded1m() {
    for (int i = 0; i < 1000000; i++) {
        unbounded.onNext(1);
    }
}
```

## JMH STATE FINAL STATIC PRIMITIVE - JMH State primitive static field declared final.

### Method 1

```java
/*
 * Copyright (c) 2016-present, RxJava Contributors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in
 * compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License is
 * distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See
 * the License for the specific language governing permissions and limitations under the License.
 */

package io.reactivex.rxjava3.core;

import java.util.concurrent.*;

import org.openjdk.jmh.annotations.*;

import io.reactivex.rxjava3.functions.*;
import io.reactivex.rxjava3.internal.functions.Functions;
import io.reactivex.rxjava3.schedulers.Schedulers;

@BenchmarkMode(Mode.Throughput)
@Warmup(iterations = 5)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(value = 1)
@State(Scope.Thread)
@AuxCounters
public class TakeUntilPerf implements Consumer<Integer> {

    public volatile int items;

    static final int count = 10000;

    Flowable<Integer> flowable;

    Observable<Integer> observable;

    @Override
    public void accept(Integer t) {
        items++;
    }

    @Setup
    public void setup() {

        flowable = Flowable.range(1, 1000 * 1000).takeUntil(Flowable.fromCallable(new Callable<Object>() {
            @Override
            public Object call() {
                int c = count;
                while (items < c) { }
                return 1;
            }
        }).subscribeOn(Schedulers.single()));

        observable = Observable.range(1, 1000 * 1000).takeUntil(Observable.fromCallable(new Callable<Object>() {
            @Override
            public Object call() {
                int c = count;
                while (items < c) { }
                return 1;
            }
        }).subscribeOn(Schedulers.single()));
    }

    @Benchmark
    public void flowable() {
        final CountDownLatch cdl = new CountDownLatch(1);

        flowable.subscribe(this, Functions.emptyConsumer(), new Action() {
            @Override
            public void run() {
                cdl.countDown();
            }
        });

        while (cdl.getCount() != 0) { }
    }

    @Benchmark
    public void observable() {
        final CountDownLatch cdl = new CountDownLatch(1);

        observable.subscribe(this, Functions.emptyConsumer(), new Action() {
            @Override
            public void run() {
                cdl.countDown();
            }
        });

        while (cdl.getCount() != 0) { }
    }
}
```

