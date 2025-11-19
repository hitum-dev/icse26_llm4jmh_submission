## JMH STATE FINAL STATIC PRIMITIVE - JMH State primitive static field declared final.

### Method 1

```java
package org.eclipse.collections.impl.bag.mutable;

import java.util.Iterator;
import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.block.predicate.primitive.IntPredicate;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for the core operations of {@link AbstractHashBag}.
 * The benchmarks run in throughput mode and measure operations per second.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public class AbstractHashBagBenchmark {

    @State(Scope.Thread)
    public static class BenchmarkState {

        SimpleHashBag<Integer> bag;

        static final int PREPOPULATE_SIZE = 10_000;

        @Setup(Level.Trial)
        public void setUp() {
            bag = new SimpleHashBag<>();
            // pre‑populate the bag with a deterministic distribution
            for (int i = 0; i < PREPOPULATE_SIZE; i++) {
                // many duplicates to exercise counting logic
                bag.add(i % 1_000);
            }
        }
    }

    /**
     * Simple concrete implementation required for instantiating the abstract class.
     */
    private static final class SimpleHashBag<T> extends AbstractHashBag<T> {

        public SimpleHashBag() {
            this.items = new ObjectIntHashMap<>();
            this.size = 0;
        }

        @Override
        protected int computeHashCode(T item) {
            return item == null ? 0 : item.hashCode();
        }

        @Override
        public MutableBag<T> newEmpty() {
            return new SimpleHashBag<>();
        }

        @Override
        public MutableBag<T> selectByOccurrences(IntPredicate predicate) {
            SimpleHashBag<T> result = new SimpleHashBag<>();
            this.items.forEachKeyValue((item, count) -> {
                if (predicate.accept(count)) {
                    result.addOccurrences(item, count);
                }
            });
            return result;
        }
    }

    @Benchmark
    public boolean add(BenchmarkState state) {
        int value = ThreadLocalRandom.current().nextInt(0, 1_000);
        return state.bag.add(value);
    }

    @Benchmark
    public boolean remove(BenchmarkState state) {
        int value = ThreadLocalRandom.current().nextInt(0, 1_000);
        return state.bag.remove(value);
    }

    @Benchmark
    public boolean contains(BenchmarkState state) {
        int value = ThreadLocalRandom.current().nextInt(0, 1_000);
        return state.bag.contains(value);
    }

    @Benchmark
    public int iterate(BenchmarkState state) {
        int sum = 0;
        Iterator<Integer> it = state.bag.iterator();
        while (it.hasNext()) {
            sum += it.next();
        }
        // return to prevent dead‑code elimination
        return sum;
    }

    @Benchmark
    public int sizeDistinct(BenchmarkState state) {
        return state.bag.sizeDistinct();
    }

    @Benchmark
    public int occurrencesOf(BenchmarkState state) {
        int value = ThreadLocalRandom.current().nextInt(0, 1_000);
        return state.bag.occurrencesOf(value);
    }
}
```

### Method 2

```java
package org.eclipse.collections.impl.bag.mutable;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Benchmark)
public class MultiReaderHashBagBenchmark {

    private static final int ELEMENT_COUNT = 1_000_000;

    private static final int READ_KEY = 42;

    private static final int WRITE_KEY = 99;

    private MultiReaderHashBag<Integer> bag;

    @Setup(Level.Trial)
    public void setUp() {
        bag = MultiReaderHashBag.newBag();
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            bag.add(i % 100);
        }
    }

    @Benchmark
    public int readOccurrences() {
        return bag.occurrencesOf(READ_KEY);
    }

    @Benchmark
    public void writeAddOccurrence() {
        bag.addOccurrences(WRITE_KEY, 1);
    }

    @Benchmark
    public int readIterateAndCount() {
        final int[] sum = new int[1];
        bag.withReadLockAndDelegate(delegate -> {
            for (Integer i : delegate) {
                sum[0] += i;
            }
        });
        return sum[0];
    }

    @Benchmark
    public void writeRemove() {
        bag.removeOccurrences(WRITE_KEY, 1);
    }
}
```

### Method 3

```java
package org.eclipse.collections.impl.bag.mutable;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Benchmark)
public class MultiReaderHashBagBenchmark {

    private static final int ELEMENT_COUNT = 1_000_000;

    private static final int READ_KEY = 42;

    private static final int WRITE_KEY = 99;

    private MultiReaderHashBag<Integer> bag;

    @Setup(Level.Trial)
    public void setUp() {
        bag = MultiReaderHashBag.newBag();
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            bag.add(i % 100);
        }
    }

    @Benchmark
    public int readOccurrences() {
        return bag.occurrencesOf(READ_KEY);
    }

    @Benchmark
    public void writeAddOccurrence() {
        bag.addOccurrences(WRITE_KEY, 1);
    }

    @Benchmark
    public int readIterateAndCount() {
        final int[] sum = new int[1];
        bag.withReadLockAndDelegate(delegate -> {
            for (Integer i : delegate) {
                sum[0] += i;
            }
        });
        return sum[0];
    }

    @Benchmark
    public void writeRemove() {
        bag.removeOccurrences(WRITE_KEY, 1);
    }
}
```

### Method 4

```java
package org.eclipse.collections.impl.bag.mutable;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Benchmark)
public class MultiReaderHashBagBenchmark {

    private static final int ELEMENT_COUNT = 1_000_000;

    private static final int READ_KEY = 42;

    private static final int WRITE_KEY = 99;

    private MultiReaderHashBag<Integer> bag;

    @Setup(Level.Trial)
    public void setUp() {
        bag = MultiReaderHashBag.newBag();
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            bag.add(i % 100);
        }
    }

    @Benchmark
    public int readOccurrences() {
        return bag.occurrencesOf(READ_KEY);
    }

    @Benchmark
    public void writeAddOccurrence() {
        bag.addOccurrences(WRITE_KEY, 1);
    }

    @Benchmark
    public int readIterateAndCount() {
        final int[] sum = new int[1];
        bag.withReadLockAndDelegate(delegate -> {
            for (Integer i : delegate) {
                sum[0] += i;
            }
        });
        return sum[0];
    }

    @Benchmark
    public void writeRemove() {
        bag.removeOccurrences(WRITE_KEY, 1);
    }
}
```

### Method 5

```java
package org.eclipse.collections.impl.bag.sorted.mutable;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2)
@State(Scope.Thread)
public class TreeBagBenchmark {

    /**
     * Size of the pre‑populated bag for read‑only benchmarks.
     */
    private static final int PREPOPULATED_SIZE = 10_000;

    /**
     * Number of elements added/removed per benchmark invocation.
     */
    private static final int BATCH_SIZE = 1_000;

    private TreeBag<Integer> prepopulatedBag;

    private TreeBag<Integer> mutableBag;

    private int[] randomValues;

    private int index;

    @Setup(Level.Trial)
    public void setUp() {
        Random rnd = new Random(12345L);
        prepopulatedBag = TreeBag.newBag();
        mutableBag = TreeBag.newBag();
        // Fill both bags with the same data set
        for (int i = 0; i < PREPOPULATED_SIZE; i++) {
            int value = rnd.nextInt(PREPOPULATED_SIZE * 10);
            prepopulatedBag.add(value);
            mutableBag.add(value);
        }
        // Prepare a reusable array of random values for add/remove benchmarks
        randomValues = new int[BATCH_SIZE];
        for (int i = 0; i < BATCH_SIZE; i++) {
            randomValues[i] = rnd.nextInt(PREPOPULATED_SIZE * 10);
        }
        index = 0;
    }

    /**
     * Benchmark for adding a batch of elements.
     */
    @Benchmark
    public void addBatch() {
        for (int i = 0; i < BATCH_SIZE; i++) {
            mutableBag.add(randomValues[i]);
        }
    }

    /**
     * Benchmark for removing a batch of elements that are known to exist.
     */
    @Benchmark
    public void removeBatch() {
        // Ensure we have enough elements to remove; if not, repopulate
        if (mutableBag.size() < BATCH_SIZE) {
            mutableBag.clear();
            for (int i = 0; i < PREPOPULATED_SIZE; i++) {
                mutableBag.add(i);
            }
        }
        for (int i = 0; i < BATCH_SIZE; i++) {
            mutableBag.remove(randomValues[i]);
        }
    }

    /**
     * Benchmark for checking containment of random elements.
     */
    @Benchmark
    public boolean contains() {
        // Cycle through the pre‑generated values to avoid allocation overhead
        int value = randomValues[(index++) & (BATCH_SIZE - 1)];
        return prepopulatedBag.contains(value);
    }

    /**
     * Benchmark for iterating over the whole bag using the iterator.
     */
    @Benchmark
    public long iterate() {
        long sum = 0L;
        for (Integer i : prepopulatedBag) {
            sum += i;
        }
        // return to prevent dead‑code elimination
        return sum;
    }

    /**
     * Benchmark for the forEach method that processes each element.
     */
    @Benchmark
    public long forEach() {
        final long[] sum = { 0L };
        prepopulatedBag.each(item -> sum[0] += item);
        return sum[0];
    }

    /**
     * Benchmark for indexOf – a typical read‑only operation that walks the map.
     */
    @Benchmark
    public int indexOf() {
        // Use a deterministic value to keep the benchmark stable
        return prepopulatedBag.indexOf(randomValues[0]);
    }

    /**
     * Benchmark for addOccurrences – adds multiple copies of a single element.
     */
    @Benchmark
    public void addOccurrences() {
        mutableBag.addOccurrences(randomValues[0], 5);
    }

    /**
     * Benchmark for removeOccurrences – removes multiple copies of a single element.
     */
    @Benchmark
    public void removeOccurrences() {
        mutableBag.removeOccurrences(randomValues[0], 3);
    }
}
```

### Method 6

```java
package org.eclipse.collections.impl.bag.sorted.mutable;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2)
@State(Scope.Thread)
public class TreeBagBenchmark {

    /**
     * Size of the pre‑populated bag for read‑only benchmarks.
     */
    private static final int PREPOPULATED_SIZE = 10_000;

    /**
     * Number of elements added/removed per benchmark invocation.
     */
    private static final int BATCH_SIZE = 1_000;

    private TreeBag<Integer> prepopulatedBag;

    private TreeBag<Integer> mutableBag;

    private int[] randomValues;

    private int index;

    @Setup(Level.Trial)
    public void setUp() {
        Random rnd = new Random(12345L);
        prepopulatedBag = TreeBag.newBag();
        mutableBag = TreeBag.newBag();
        // Fill both bags with the same data set
        for (int i = 0; i < PREPOPULATED_SIZE; i++) {
            int value = rnd.nextInt(PREPOPULATED_SIZE * 10);
            prepopulatedBag.add(value);
            mutableBag.add(value);
        }
        // Prepare a reusable array of random values for add/remove benchmarks
        randomValues = new int[BATCH_SIZE];
        for (int i = 0; i < BATCH_SIZE; i++) {
            randomValues[i] = rnd.nextInt(PREPOPULATED_SIZE * 10);
        }
        index = 0;
    }

    /**
     * Benchmark for adding a batch of elements.
     */
    @Benchmark
    public void addBatch() {
        for (int i = 0; i < BATCH_SIZE; i++) {
            mutableBag.add(randomValues[i]);
        }
    }

    /**
     * Benchmark for removing a batch of elements that are known to exist.
     */
    @Benchmark
    public void removeBatch() {
        // Ensure we have enough elements to remove; if not, repopulate
        if (mutableBag.size() < BATCH_SIZE) {
            mutableBag.clear();
            for (int i = 0; i < PREPOPULATED_SIZE; i++) {
                mutableBag.add(i);
            }
        }
        for (int i = 0; i < BATCH_SIZE; i++) {
            mutableBag.remove(randomValues[i]);
        }
    }

    /**
     * Benchmark for checking containment of random elements.
     */
    @Benchmark
    public boolean contains() {
        // Cycle through the pre‑generated values to avoid allocation overhead
        int value = randomValues[(index++) & (BATCH_SIZE - 1)];
        return prepopulatedBag.contains(value);
    }

    /**
     * Benchmark for iterating over the whole bag using the iterator.
     */
    @Benchmark
    public long iterate() {
        long sum = 0L;
        for (Integer i : prepopulatedBag) {
            sum += i;
        }
        // return to prevent dead‑code elimination
        return sum;
    }

    /**
     * Benchmark for the forEach method that processes each element.
     */
    @Benchmark
    public long forEach() {
        final long[] sum = { 0L };
        prepopulatedBag.each(item -> sum[0] += item);
        return sum[0];
    }

    /**
     * Benchmark for indexOf – a typical read‑only operation that walks the map.
     */
    @Benchmark
    public int indexOf() {
        // Use a deterministic value to keep the benchmark stable
        return prepopulatedBag.indexOf(randomValues[0]);
    }

    /**
     * Benchmark for addOccurrences – adds multiple copies of a single element.
     */
    @Benchmark
    public void addOccurrences() {
        mutableBag.addOccurrences(randomValues[0], 5);
    }

    /**
     * Benchmark for removeOccurrences – removes multiple copies of a single element.
     */
    @Benchmark
    public void removeOccurrences() {
        mutableBag.removeOccurrences(randomValues[0], 3);
    }
}
```

### Method 7

```java
package org.eclipse.collections.impl.bag;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Thread)
public class AbstractBagBenchmark {

    private static final int ELEMENT_COUNT = 100_000;

    private MutableBag<Integer> bag;

    @Setup(Level.Trial)
    public void setUp() {
        bag = org.eclipse.collections.impl.factory.Bags.mutable.withInitialCapacity(ELEMENT_COUNT);
        // Populate with a mix of distinct and duplicate values
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            // 1,000 distinct keys, each repeated ~100 times
            bag.add(i % 1_000);
        }
    }

    @Benchmark
    public long sumOfInt() {
        // Benchmark the sumOfInt aggregation
        return bag.sumOfInt(i -> i);
    }

    @Benchmark
    public MutableBag<Integer> selectEven() {
        // Benchmark select with a simple predicate
        return bag.select(i -> (i & 1) == 0, org.eclipse.collections.impl.factory.Bags.mutable.empty());
    }

    @Benchmark
    public MutableBag<Integer> rejectEven() {
        // Benchmark reject with the same predicate
        return bag.reject(i -> (i & 1) == 0, org.eclipse.collections.impl.factory.Bags.mutable.empty());
    }

    @Benchmark
    public MutableBag<Integer> collectSquare() {
        // Benchmark collect (map) operation
        return bag.collect(i -> i * i, org.eclipse.collections.impl.factory.Bags.mutable.empty());
    }

    @Benchmark
    public MutableBag<Integer> toBag() {
        // Benchmark conversion to a new mutable bag (copy)
        return bag.toBag();
    }

    @Benchmark
    public MutableList<Integer> toList() {
        // Benchmark conversion to a mutable list
        return bag.toList();
    }
}
```

### Method 8

```java
package org.eclipse.collections.impl.bimap.mutable;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@State(Scope.Benchmark)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public class AbstractMutableBiMapBenchmark {

    /**
     * Size of the map used for the benchmarks.
     */
    private static final int SIZE = 10_000;

    /**
     * The map under test.
     */
    private HashBiMap<Integer, String> map;

    /**
     * A second map used for bulk‑operation benchmarks.
     */
    private HashBiMap<Integer, String> otherMap;

    /**
     * Pre‑generated keys for read‑only benchmarks.
     */
    private int[] keys;

    /**
     * Pre‑generated values for read‑only benchmarks.
     */
    private String[] values;

    @Setup(Level.Trial)
    public void setUp() {
        map = new HashBiMap<>(SIZE);
        otherMap = new HashBiMap<>(SIZE);
        keys = new int[SIZE];
        values = new String[SIZE];
        for (int i = 0; i < SIZE; i++) {
            int key = i;
            String value = "value-" + i;
            map.put(key, value);
            otherMap.put(key + SIZE, "other-" + i);
            keys[i] = key;
            values[i] = value;
        }
    }

    /**
     * Benchmark for a single put operation (new key).
     */
    @Benchmark
    public void putNewKey() {
        // Use a key that is not present to avoid overwriting.
        int newKey = SIZE + (int) (Math.random() * SIZE);
        map.put(newKey, "new-" + newKey);
    }

    /**
     * Benchmark for a single put operation that updates an existing key.
     */
    @Benchmark
    public void putExistingKey() {
        int idx = (int) (Math.random() * SIZE);
        int key = keys[idx];
        map.put(key, "updated-" + key);
    }

    /**
     * Benchmark for a single get operation.
     */
    @Benchmark
    public String get() {
        int idx = (int) (Math.random() * SIZE);
        return map.get(keys[idx]);
    }

    /**
     * Benchmark for a single remove operation.
     */
    @Benchmark
    public void remove() {
        int idx = (int) (Math.random() * SIZE);
        map.remove(keys[idx]);
    }

    /**
     * Benchmark for iterating over values.
     */
    @Benchmark
    public long iterateValues() {
        long sum = 0;
        for (String v : map.values()) {
            sum += v.length();
        }
        return sum;
    }

    /**
     * Benchmark for iterating over entries.
     */
    @Benchmark
    public long iterateEntries() {
        long sum = 0;
        for (Pair<Integer, String> entry : map.keyValuesView()) {
            sum += entry.getOne() + entry.getTwo().length();
        }
        return sum;
    }

    /**
     * Benchmark for the inverse view lookup (value → key).
     */
    @Benchmark
    public Integer inverseLookup() {
        int idx = (int) (Math.random() * SIZE);
        return map.inverse().get(values[idx]);
    }

    /**
     * Benchmark for bulk putAll operation.
     */
    @Benchmark
    public void putAll() {
        map.putAll(otherMap);
    }

    /**
     * Benchmark for the flip operation (produces a Multimap).
     */
    @Benchmark
    public void flip() {
        map.flip();
    }

    /**
     * Benchmark for the clear operation.
     */
    @Benchmark
    public void clear() {
        map.clear();
        // Re‑populate to keep other benchmarks meaningful.
        for (int i = 0; i < SIZE; i++) {
            map.put(keys[i], values[i]);
        }
    }
}
```

### Method 9

```java
package org.eclipse.collections.impl.block.procedure;

import java.util.Collections;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link MultimapEachPutProcedure}.
 *
 * The benchmark measures the throughput of inserting a batch of values into a {@link MutableMultimap}
 * using the procedure. The test data consists of a list of random strings; the key function maps each
 * string to a single integer key derived from its length. The multimap is cleared before each iteration
 * to keep the workload constant.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
public class MultimapEachPutProcedureBenchmark {

    @State(Scope.Thread)
    public static class BenchmarkState {

        /**
         * Size of the input batch for each benchmark invocation.
         */
        private static final int BATCH_SIZE = 1_000;

        /**
         * The multimap used by the procedure.
         */
        MutableMultimap<Integer, String> multimap;

        /**
         * Procedure under test.
         */
        MultimapEachPutProcedure<Integer, String> procedure;

        /**
         * Input values for the benchmark.
         */
        List<String> values;

        /**
         * Key function: maps a string to an Iterable containing its length as the key.
         */
        Function<String, Iterable<Integer>> keyFunction = s -> Collections.singletonList(s.length());

        @Setup(Level.Trial)
        public void setUpTrial() {
            // Create a fresh multimap implementation (HashBagMultimap is a typical choice).
            multimap = new HashBagMultimap<>();
            // Initialise the procedure with the multimap and key function.
            procedure = MultimapEachPutProcedure.on(multimap, keyFunction);
            // Generate deterministic test data (random strings of length 10).
            values = IntStream.range(0, BATCH_SIZE).mapToObj(i -> "value-" + i).collect(Collectors.toList());
        }

        @Setup(Level.Iteration)
        public void setUpIteration() {
            // Ensure the multimap is empty before each iteration to avoid side‑effects.
            multimap.clear();
        }

        @TearDown(Level.Trial)
        public void tearDownTrial() {
            // Release references for GC.
            multimap = null;
            procedure = null;
            values = null;
        }
    }

    @Benchmark
    public void putBatch(BenchmarkState state) {
        // Apply the procedure to each element in the pre‑generated batch.
        for (String value : state.values) {
            state.procedure.value(value);
        }
    }
}
```

### Method 10

```java
package org.eclipse.collections.impl.block.procedure;

import org.eclipse.collections.api.block.function.primitive.FloatFunction;
import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link SumOfFloatProcedure}.
 *
 * Measures the throughput of the {@code value} method when processing a stream of {@code Float} values.
 * The benchmark follows JMH best‑practice guidelines:
 * <ul>
 *   <li>State is scoped to a single thread to avoid contention.</li>
 *   <li>Data is pre‑generated in {@code @Setup(Level.Trial)} to exclude allocation costs.</li>
 *   <li>Blackhole is used to prevent dead‑code elimination.</li>
 *   <li>Warm‑up and measurement iterations are left to the default JMH runner configuration.</li>
 * </ul>
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Thread)
public class SumOfFloatProcedureBenchmark {

    /**
     * Number of elements processed per trial. Adjust as needed for realistic workloads.
     */
    private static final int DATASET_SIZE = 1_000_000;

    /**
     * The procedure under test.
     */
    private SumOfFloatProcedure<Float> procedure;

    /**
     * Pre‑generated input data.
     */
    private Float[] data;

    /**
     * Index of the next element to process.
     */
    private int cursor;

    /**
     * Simple identity FloatFunction (returns the primitive float value of a Float).
     */
    private static final FloatFunction<Float> IDENTITY_FUNCTION = Float::floatValue;

    @Setup(Level.Trial)
    public void setUp() {
        // Initialise the procedure with the identity function.
        this.procedure = new SumOfFloatProcedure<>(IDENTITY_FUNCTION);
        // Populate the dataset with pseudo‑random floats.
        this.data = new Float[DATASET_SIZE];
        Random random = new Random(12345L);
        for (int i = 0; i < DATASET_SIZE; i++) {
            this.data[i] = random.nextFloat();
        }
        this.cursor = 0;
    }

    /**
     * Benchmark the {@code value} method. The method is invoked with a pre‑generated Float,
     * and the resulting sum is consumed by a Blackhole to avoid dead‑code elimination.
     */
    @Benchmark
    public void sumValue(Blackhole bh) {
        // Feed the next element to the procedure.
        procedure.value(data[cursor]);
        // Advance cursor cyclically.
        cursor = (cursor + 1) % DATASET_SIZE;
        // Consume the current result to keep the JIT from discarding the computation.
        bh.consume(procedure.getResult());
    }

    @TearDown(Level.Trial)
    public void tearDown() {
        // Optional: expose the final result to ensure the whole computation is performed.
        System.out.println("Final sum (ignored by benchmark): " + procedure.getResult());
    }
}
```

### Method 11

```java
package org.eclipse.collections.impl.collection;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link AbstractSynchronizedRichIterable}.
 *
 * The benchmark measures the overhead introduced by the synchronized wrapper
 * compared to a plain {@link RichIterable} implementation.
 *
 * Throughput mode is used because we are interested in the number of
 * operations per time unit that can be performed under typical usage
 * patterns (size, contains, iteration, and conversion to a list).
 *
 * Best practices applied:
 * • @State(Scope.Thread) isolates benchmark state per thread to avoid contention.
 * • @Setup(Level.Trial) prepares immutable data once per trial.
 * • Blackhole consumes results to prevent dead‑code elimination.
 * • Warm‑up and measurement iterations are configured to let the JVM reach a steady state.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@State(Scope.Thread)
public class AbstractSynchronizedRichIterableBenchmark {

    /**
     * Size of the test collection.
     */
    private static final int ELEMENT_COUNT = 10_000;

    /**
     * Plain (unsynchronized) iterable used as baseline.
     */
    private RichIterable<Integer> plainIterable;

    /**
     * Synchronized wrapper around the same delegate.
     */
    private RichIterable<Integer> synchronizedIterable;

    /**
     * Simple concrete subclass of {@link AbstractSynchronizedRichIterable}.
     */
    private static final class SynchronizedRichIterable<T> extends AbstractSynchronizedRichIterable<T> {

        private SynchronizedRichIterable(RichIterable<T> delegate, Object lock) {
            super(delegate, lock);
        }
    }

    @Setup(Level.Trial)
    public void setUp() {
        // Build a mutable list with a known number of elements.
        List<Integer> backingList = new ArrayList<>(ELEMENT_COUNT);
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            backingList.add(i);
        }
        // Use Eclipse Collections' FastList as the RichIterable implementation.
        this.plainIterable = FastList.newList(backingList);
        // Wrap the same delegate with the synchronized implementation.
        this.synchronizedIterable = new SynchronizedRichIterable<>(this.plainIterable, new Object());
    }

    /* --------------------------------------------------------------------- */
    /* Benchmark methods – each measures a typical operation on the wrapper. */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public int sizePlain() {
        return plainIterable.size();
    }

    @Benchmark
    public int sizeSynchronized() {
        return synchronizedIterable.size();
    }

    @Benchmark
    public boolean containsPlain() {
        // Look for a value that is present (middle of the range) to avoid early exit.
        return plainIterable.contains(ELEMENT_COUNT / 2);
    }

    @Benchmark
    public boolean containsSynchronized() {
        return synchronizedIterable.contains(ELEMENT_COUNT / 2);
    }

    @Benchmark
    public void iteratePlain(Blackhole bh) {
        plainIterable.forEach(bh::consume);
    }

    @Benchmark
    public void iterateSynchronized(Blackhole bh) {
        synchronizedIterable.forEach(bh::consume);
    }

    @Benchmark
    public List<Integer> toListPlain() {
        // The toList() method returns a mutable Eclipse Collections list.
        return plainIterable.toList();
    }

    @Benchmark
    public List<Integer> toListSynchronized() {
        return synchronizedIterable.toList();
    }
}
```

### Method 12

```java
package org.eclipse.collections.impl.lazy.iterator;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class TakeWhileIteratorBenchmark {

    private static final int SIZE = 10_000;

    private List<Integer> data;

    private Predicate<Integer> predicate;

    @Setup(Level.Trial)
    public void setUp() {
        data = new ArrayList<>(SIZE);
        for (int i = 0; i < SIZE; i++) {
            data.add(i);
        }
        // Accept values less than half the size to trigger early termination
        predicate = value -> value < SIZE / 2;
    }

    @Benchmark
    public int iterateTakeWhile(Blackhole bh) {
        TakeWhileIterator<Integer> iterator = new TakeWhileIterator<>(data, predicate);
        int count = 0;
        while (iterator.hasNext()) {
            bh.consume(iterator.next());
            count++;
        }
        return count;
    }
}
```

### Method 13

```java
package org.eclipse.collections.impl.lazy.iterator;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link CollectIterator}.
 * Measures the throughput of {@code next()} calls in a typical usage scenario.
 * The benchmark resets the iterator when it is exhausted to keep the measurement steady.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Thread)
public class CollectIteratorBenchmark {

    /**
     * Size of the data set used for the benchmark.
     */
    private static final int DATA_SIZE = 10_000;

    /**
     * Source data over which the iterator works.
     */
    private List<Integer> source;

    /**
     * Function applied by the {@link CollectIterator}.
     */
    private Function<Integer, Integer> function;

    /**
     * The iterator under test.
     */
    private CollectIterator<Integer, Integer> iterator;

    /**
     * Index used to detect when the iterator is exhausted.
     */
    private int consumed;

    @Setup(Level.Trial)
    public void setUp() {
        // Prepare a deterministic data set.
        source = new ArrayList<>(DATA_SIZE);
        for (int i = 0; i < DATA_SIZE; i++) {
            source.add(i);
        }
        // Simple function that performs a lightweight computation.
        function = new Function<Integer, Integer>() {

            @Override
            public Integer valueOf(Integer argument) {
                // Example workload: double the value.
                return argument * 2;
            }
        };
        // Initialise the iterator and consumption counter.
        resetIterator();
    }

    /**
     * Resets the iterator to the beginning of the data set.
     * Called when the iterator has been fully consumed.
     */
    private void resetIterator() {
        iterator = new CollectIterator<>(source, function);
        consumed = 0;
    }

    /**
     * Benchmark method that invokes {@link CollectIterator#next()}.
     * When the iterator is exhausted it is recreated to keep the benchmark running.
     *
     * @return the transformed element (to prevent dead‑code elimination)
     */
    @Benchmark
    public Integer next() {
        if (!iterator.hasNext()) {
            resetIterator();
        }
        consumed++;
        return iterator.next();
    }

    /**
     * Optional sanity check to ensure the iterator works correctly.
     * Not part of the measured benchmark.
     */
    @TearDown(Level.Trial)
    public void verify() {
        // Simple verification that the total number of consumed elements matches expectations.
        // This helps catch accidental optimisations that would skip the iterator logic.
        if (consumed == 0) {
            throw new IllegalStateException("Benchmark did not consume any elements");
        }
    }
}
```

### Method 14

```java
package org.eclipse.collections.impl.lazy.parallel.list;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.ReentrantReadWriteLock;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@State(Scope.Benchmark)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
public class MultiReaderParallelListIterableBenchmark {

    private static final int SIZE = 10_000;

    private ParallelListIterable<Integer> delegate;

    private MultiReaderParallelListIterable<Integer> wrapper;

    @Setup(Level.Trial)
    public void setUp() {
        // Build a mutable list of integers
        List<Integer> data = new ArrayList<>(SIZE);
        for (int i = 0; i < SIZE; i++) {
            data.add(i);
        }
        // Obtain a parallel view of the FastList
        this.delegate = FastList.newList(data).asParallel(defaultExecutor(), Runtime.getRuntime().availableProcessors());
        // Wrap the parallel iterable with a read‑write lock
        this.wrapper = new MultiReaderParallelListIterable<>(this.delegate, new ReentrantReadWriteLock());
    }

    // Helper to provide a simple ExecutorService for the parallel iterable
    private ExecutorService defaultExecutor() {
        return java.util.concurrent.Executors.newWorkStealingPool();
    }

    @Benchmark
    public ListMultimap<Integer, Integer> groupByModulo() {
        // Group by the remainder of division by 10
        return wrapper.groupBy(i -> i % 10);
    }

    @Benchmark
    public ListMultimap<Integer, Integer> groupByEachDivisors() {
        // For each element, produce a small iterable of its divisors (1..3) as a demo
        return wrapper.groupByEach(i -> java.util.stream.IntStream.rangeClosed(1, 3).mapToObj(d -> d).toList());
    }
}
```

### Method 15

```java
package org.eclipse.collections.impl.lazy.parallel.list;

import java.util.Collections;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@State(Scope.Thread)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@Threads(1)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
public class ListIterableBatchBenchmark {

    private static final int SIZE = 1_000_000;

    private ListIterable<Integer> list;

    private ListIterableBatch<Integer> batch;

    private Predicate<Integer> evenPredicate;

    private Function<Integer, Integer> squareFunction;

    private ConcurrentHashMap<Integer, Boolean> distinctMap;

    @Setup(Level.Trial)
    public void setUp() {
        FastList<Integer> mutable = new FastList<>(SIZE);
        for (int i = 0; i < SIZE; i++) {
            mutable.add(i);
        }
        this.list = mutable;
        this.batch = new ListIterableBatch<>(list, 0, SIZE);
        this.evenPredicate = value -> (value & 1) == 0;
        this.squareFunction = value -> value * value;
        this.distinctMap = new ConcurrentHashMap<>();
    }

    @Benchmark
    public void forEach(Blackhole bh) {
        batch.forEach((Procedure<Integer>) bh::consume);
    }

    @Benchmark
    public int count() {
        return batch.count(evenPredicate);
    }

    @Benchmark
    public boolean anySatisfy() {
        return batch.anySatisfy(evenPredicate);
    }

    @Benchmark
    public boolean allSatisfy() {
        return batch.allSatisfy(evenPredicate);
    }

    @Benchmark
    public Integer detect() {
        return batch.detect(evenPredicate);
    }

    @Benchmark
    public void select(Blackhole bh) {
        bh.consume(batch.select(evenPredicate));
    }

    @Benchmark
    public void collect(Blackhole bh) {
        bh.consume(batch.collect(squareFunction));
    }

    @Benchmark
    public void flatCollect(Blackhole bh) {
        Function<Integer, Iterable<Integer>> f = v -> Collections.singletonList(v);
        bh.consume(batch.flatCollect(f));
    }

    @Benchmark
    public void distinct(Blackhole bh) {
        bh.consume(batch.distinct(distinctMap));
    }
}
```

### Method 16

```java
package org.eclipse.collections.impl.lazy.parallel.set.sorted;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link SynchronizedParallelSortedSetIterable}.
 *
 * Measures throughput of synchronized vs. unsynchronized {@code groupBy} and {@code groupByEach}
 * operations on a parallel sorted set.
 */
@State(Scope.Benchmark)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
public class SynchronizedParallelSortedSetIterableBenchmark {

    private static final int ELEMENT_COUNT = 10_000;

    private static final int PARALLELISM = Runtime.getRuntime().availableProcessors();

    private ParallelSortedSetIterable<Integer> unsynchronizedParallel;

    private ParallelSortedSetIterable<Integer> synchronizedParallel;

    private ExecutorService executor;

    @Setup
    public void setUp() {
        // Create a mutable sorted set with natural ordering.
        MutableSortedSet<Integer> mutableSet = org.eclipse.collections.impl.factory.SortedSets.mutable.withAll(IntStream.rangeClosed(1, ELEMENT_COUNT).boxed().collect(Collectors.toList()));
        // Shared executor for parallel operations.
        executor = Executors.newWorkStealingPool(PARALLELISM);
        // Obtain the parallel iterable.
        unsynchronizedParallel = mutableSet.asParallel(executor, PARALLELISM);
        // Wrap with synchronization.
        synchronizedParallel = new SynchronizedParallelSortedSetIterable<>(unsynchronizedParallel, new Object());
    }

    @Benchmark
    public SortedSetMultimap<Integer, Integer> unsyncGroupBy() {
        // Group by modulo 10.
        return unsynchronizedParallel.groupBy(i -> i % 10);
    }

    @Benchmark
    public SortedSetMultimap<Integer, Integer> syncGroupBy() {
        // Group by modulo 10.
        return synchronizedParallel.groupBy(i -> i % 10);
    }

    @Benchmark
    public SortedSetMultimap<Integer, Integer> unsyncGroupByEach() {
        // For each integer, produce a list of its two lowest bits.
        return unsynchronizedParallel.groupByEach(i -> java.util.List.of(i & 1, (i >> 1) & 1));
    }

    @Benchmark
    public SortedSetMultimap<Integer, Integer> syncGroupByEach() {
        // For each integer, produce a list of its two lowest bits.
        return synchronizedParallel.groupByEach(i -> java.util.List.of(i & 1, (i >> 1) & 1));
    }
}
```

### Method 17

```java
package org.eclipse.collections.impl.lazy.parallel.set.sorted;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link SynchronizedParallelSortedSetIterable}.
 *
 * Measures throughput of synchronized vs. unsynchronized {@code groupBy} and {@code groupByEach}
 * operations on a parallel sorted set.
 */
@State(Scope.Benchmark)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
public class SynchronizedParallelSortedSetIterableBenchmark {

    private static final int ELEMENT_COUNT = 10_000;

    private static final int PARALLELISM = Runtime.getRuntime().availableProcessors();

    private ParallelSortedSetIterable<Integer> unsynchronizedParallel;

    private ParallelSortedSetIterable<Integer> synchronizedParallel;

    private ExecutorService executor;

    @Setup
    public void setUp() {
        // Create a mutable sorted set with natural ordering.
        MutableSortedSet<Integer> mutableSet = org.eclipse.collections.impl.factory.SortedSets.mutable.withAll(IntStream.rangeClosed(1, ELEMENT_COUNT).boxed().collect(Collectors.toList()));
        // Shared executor for parallel operations.
        executor = Executors.newWorkStealingPool(PARALLELISM);
        // Obtain the parallel iterable.
        unsynchronizedParallel = mutableSet.asParallel(executor, PARALLELISM);
        // Wrap with synchronization.
        synchronizedParallel = new SynchronizedParallelSortedSetIterable<>(unsynchronizedParallel, new Object());
    }

    @Benchmark
    public SortedSetMultimap<Integer, Integer> unsyncGroupBy() {
        // Group by modulo 10.
        return unsynchronizedParallel.groupBy(i -> i % 10);
    }

    @Benchmark
    public SortedSetMultimap<Integer, Integer> syncGroupBy() {
        // Group by modulo 10.
        return synchronizedParallel.groupBy(i -> i % 10);
    }

    @Benchmark
    public SortedSetMultimap<Integer, Integer> unsyncGroupByEach() {
        // For each integer, produce a list of its two lowest bits.
        return unsynchronizedParallel.groupByEach(i -> java.util.List.of(i & 1, (i >> 1) & 1));
    }

    @Benchmark
    public SortedSetMultimap<Integer, Integer> syncGroupByEach() {
        // For each integer, produce a list of its two lowest bits.
        return synchronizedParallel.groupByEach(i -> java.util.List.of(i & 1, (i >> 1) & 1));
    }
}
```

### Method 18

```java
package org.eclipse.collections.impl.lazy.parallel;

import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.ReentrantReadWriteLock;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Benchmark)
public class MultiReaderParallelIterableBenchmark {

    private static final int ELEMENT_COUNT = 1_000_000;

    private static final int BATCH_SIZE = 10_000;

    private ParallelIterable<Integer> delegate;

    private MultiReaderParallelIterable<Integer> wrapped;

    private Function<Integer, Integer> mod10;

    @Setup(Level.Trial)
    public void setUp() {
        // Create a FastList with values 0 .. ELEMENT_COUNT-1
        FastList<Integer> list = IntInterval.oneTo(ELEMENT_COUNT).collect(i -> i, FastList.newList());
        delegate = list.asParallel(Executors.newWorkStealingPool(), BATCH_SIZE);
        wrapped = new MultiReaderParallelIterable<>(delegate, new ReentrantReadWriteLock());
        mod10 = i -> i % 10;
    }

    @Benchmark
    public Multimap<Integer, Integer> groupByWithLock() {
        return wrapped.groupBy(mod10);
    }

    @Benchmark
    public Multimap<Integer, Integer> groupByWithoutLock() {
        return delegate.groupBy(mod10);
    }

    @Benchmark
    public Multimap<Integer, Integer> groupByEachWithLock() {
        return wrapped.groupByEach(i -> FastList.newListWith(i % 10));
    }

    @Benchmark
    public Multimap<Integer, Integer> groupByEachWithoutLock() {
        return delegate.groupByEach(i -> FastList.newListWith(i % 10));
    }
}
```

### Method 19

```java
package org.eclipse.collections.impl.lazy.parallel;

import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.ReentrantReadWriteLock;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Benchmark)
public class MultiReaderParallelIterableBenchmark {

    private static final int ELEMENT_COUNT = 1_000_000;

    private static final int BATCH_SIZE = 10_000;

    private ParallelIterable<Integer> delegate;

    private MultiReaderParallelIterable<Integer> wrapped;

    private Function<Integer, Integer> mod10;

    @Setup(Level.Trial)
    public void setUp() {
        // Create a FastList with values 0 .. ELEMENT_COUNT-1
        FastList<Integer> list = IntInterval.oneTo(ELEMENT_COUNT).collect(i -> i, FastList.newList());
        delegate = list.asParallel(Executors.newWorkStealingPool(), BATCH_SIZE);
        wrapped = new MultiReaderParallelIterable<>(delegate, new ReentrantReadWriteLock());
        mod10 = i -> i % 10;
    }

    @Benchmark
    public Multimap<Integer, Integer> groupByWithLock() {
        return wrapped.groupBy(mod10);
    }

    @Benchmark
    public Multimap<Integer, Integer> groupByWithoutLock() {
        return delegate.groupBy(mod10);
    }

    @Benchmark
    public Multimap<Integer, Integer> groupByEachWithLock() {
        return wrapped.groupByEach(i -> FastList.newListWith(i % 10));
    }

    @Benchmark
    public Multimap<Integer, Integer> groupByEachWithoutLock() {
        return delegate.groupByEach(i -> FastList.newListWith(i % 10));
    }
}
```

### Method 20

```java
package org.eclipse.collections.impl.lazy.primitive;

import java.util.concurrent.TimeUnit;
import java.util.stream.IntStream;
import org.eclipse.collections.api.block.function.primitive.BooleanFunction;
import org.eclipse.collections.api.block.predicate.primitive.BooleanPredicate;
import org.eclipse.collections.api.block.procedure.primitive.BooleanProcedure;
import org.eclipse.collections.api.list.primitive.MutableBooleanList;
import org.eclipse.collections.api.set.primitive.MutableBooleanSet;
import org.eclipse.collections.api.bag.primitive.MutableBooleanBag;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmark for {@link CollectBooleanIterable}.
 *
 * The benchmark focuses on the most frequently used operations:
 * iteration, forEach/each, size, count, anySatisfy/allSatisfy,
 * and conversion to primitive collections.
 *
 * Best‑practice settings:
 * - Warm‑up and measurement phases are separated.
 * - A single fork isolates JVM warm‑up effects.
 * - Throughput mode reports operations per time unit.
 * - Blackhole is used to avoid dead‑code elimination.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Benchmark)
public class CollectBooleanIterableBenchmark {

    /**
     * Size of the source collection used for all benchmarks.
     */
    private static final int ELEMENT_COUNT = 10_000;

    /**
     * Source lazy iterable of Integer values.
     */
    private LazyIterable<Integer> source;

    /**
     * Boolean function mapping Integer -> boolean (even numbers).
     */
    private BooleanFunction<Integer> isEvenFunction;

    /**
     * Predicate used for count/anySatisfy/allSatisfy (identity on boolean).
     */
    private BooleanPredicate isEvenPredicate;

    /**
     * The CollectBooleanIterable instance under test.
     */
    private CollectBooleanIterable<Integer> booleanIterable;

    @Setup(Level.Trial)
    public void setUp() {
        // Build an immutable list of integers and adapt it to a LazyIterable.
        this.source = org.eclipse.collections.impl.factory.Lists.immutable.withAll(IntStream.range(0, ELEMENT_COUNT).boxed().toList()).asLazy();
        // Function: true for even numbers, false otherwise.
        this.isEvenFunction = each -> each % 2 == 0;
        // Predicate that returns the boolean value unchanged (identity).
        this.isEvenPredicate = value -> value;
        // Create the CollectBooleanIterable to be benchmarked.
        this.booleanIterable = new CollectBooleanIterable<>(this.source, this.isEvenFunction);
    }

    @Benchmark
    public void benchmarkBooleanIterator(Blackhole bh) {
        var iterator = this.booleanIterable.booleanIterator();
        while (iterator.hasNext()) {
            bh.consume(iterator.next());
        }
    }

    @Benchmark
    public void benchmarkForEach(Blackhole bh) {
        this.booleanIterable.forEach((BooleanProcedure) bh::consume);
    }

    @Benchmark
    public void benchmarkEach(Blackhole bh) {
        this.booleanIterable.each((BooleanProcedure) bh::consume);
    }

    @Benchmark
    public int benchmarkSize() {
        return this.booleanIterable.size();
    }

    @Benchmark
    public int benchmarkCount() {
        return this.booleanIterable.count(this.isEvenPredicate);
    }

    @Benchmark
    public boolean benchmarkAnySatisfy() {
        return this.booleanIterable.anySatisfy(this.isEvenPredicate);
    }

    @Benchmark
    public boolean benchmarkAllSatisfy() {
        return this.booleanIterable.allSatisfy(this.isEvenPredicate);
    }

    @Benchmark
    public boolean[] benchmarkToArray(Blackhole bh) {
        boolean[] array = this.booleanIterable.toArray();
        bh.consume(array);
        return array;
    }

    @Benchmark
    public MutableBooleanList benchmarkToList(Blackhole bh) {
        MutableBooleanList list = this.booleanIterable.toList();
        bh.consume(list);
        return list;
    }

    @Benchmark
    public MutableBooleanSet benchmarkToSet(Blackhole bh) {
        MutableBooleanSet set = this.booleanIterable.toSet();
        bh.consume(set);
        return set;
    }

    @Benchmark
    public MutableBooleanBag benchmarkToBag(Blackhole bh) {
        MutableBooleanBag bag = this.booleanIterable.toBag();
        bh.consume(bag);
        return bag;
    }
}
```

### Method 21

```java
package org.eclipse.collections.impl.lazy;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link DropIterable}.
 *
 * The benchmarks focus on throughput (operations per time unit) which is the most common
 * metric when measuring collection transformations. Warm‑up, measurement iterations,
 * forks and proper state isolation are configured following JMH best practices.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 3, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Thread)
public class DropIterableBenchmark {

    /**
     * Size of the source collection used in all benchmarks.
     */
    private static final int SIZE = 10_000;

    /**
     * Number of elements to drop from the beginning of the iterable.
     */
    private static final int DROP_COUNT = 100;

    /**
     * Source data populated with sequential integers.
     */
    private List<Integer> source;

    /**
     * DropIterable instance under test.
     */
    private DropIterable<Integer> dropIterable;

    /**
     * Simple predicate used for filtering operations.
     */
    private Predicate<Integer> evenPredicate;

    @Setup(Level.Trial)
    public void setUp() {
        source = new ArrayList<>(SIZE);
        for (int i = 0; i < SIZE; i++) {
            source.add(i);
        }
        dropIterable = new DropIterable<>(source, DROP_COUNT);
        evenPredicate = i -> i % 2 == 0;
    }

    @Benchmark
    public void iterator(Blackhole bh) {
        dropIterable.iterator().forEachRemaining(bh::consume);
    }

    @Benchmark
    public void each(Blackhole bh) {
        dropIterable.each(bh::consume);
    }

    @Benchmark
    public void forEachWithIndex(Blackhole bh) {
        dropIterable.forEachWithIndex((obj, idx) -> bh.consume(obj + idx));
    }

    @Benchmark
    public boolean anySatisfy() {
        return dropIterable.anySatisfy(evenPredicate);
    }

    @Benchmark
    public boolean allSatisfy() {
        return dropIterable.allSatisfy(evenPredicate);
    }

    @Benchmark
    public boolean noneSatisfy() {
        return dropIterable.noneSatisfy(evenPredicate);
    }

    @Benchmark
    public Integer detect() {
        return dropIterable.detect(evenPredicate);
    }

    @Benchmark
    public Optional<Integer> detectOptional() {
        return dropIterable.detectOptional(evenPredicate);
    }
}
```

### Method 22

```java
package org.eclipse.collections.impl.lazy;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link DropIterable}.
 *
 * The benchmarks focus on throughput (operations per time unit) which is the most common
 * metric when measuring collection transformations. Warm‑up, measurement iterations,
 * forks and proper state isolation are configured following JMH best practices.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 3, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Thread)
public class DropIterableBenchmark {

    /**
     * Size of the source collection used in all benchmarks.
     */
    private static final int SIZE = 10_000;

    /**
     * Number of elements to drop from the beginning of the iterable.
     */
    private static final int DROP_COUNT = 100;

    /**
     * Source data populated with sequential integers.
     */
    private List<Integer> source;

    /**
     * DropIterable instance under test.
     */
    private DropIterable<Integer> dropIterable;

    /**
     * Simple predicate used for filtering operations.
     */
    private Predicate<Integer> evenPredicate;

    @Setup(Level.Trial)
    public void setUp() {
        source = new ArrayList<>(SIZE);
        for (int i = 0; i < SIZE; i++) {
            source.add(i);
        }
        dropIterable = new DropIterable<>(source, DROP_COUNT);
        evenPredicate = i -> i % 2 == 0;
    }

    @Benchmark
    public void iterator(Blackhole bh) {
        dropIterable.iterator().forEachRemaining(bh::consume);
    }

    @Benchmark
    public void each(Blackhole bh) {
        dropIterable.each(bh::consume);
    }

    @Benchmark
    public void forEachWithIndex(Blackhole bh) {
        dropIterable.forEachWithIndex((obj, idx) -> bh.consume(obj + idx));
    }

    @Benchmark
    public boolean anySatisfy() {
        return dropIterable.anySatisfy(evenPredicate);
    }

    @Benchmark
    public boolean allSatisfy() {
        return dropIterable.allSatisfy(evenPredicate);
    }

    @Benchmark
    public boolean noneSatisfy() {
        return dropIterable.noneSatisfy(evenPredicate);
    }

    @Benchmark
    public Integer detect() {
        return dropIterable.detect(evenPredicate);
    }

    @Benchmark
    public Optional<Integer> detectOptional() {
        return dropIterable.detectOptional(evenPredicate);
    }
}
```

### Method 23

```java
package org.eclipse.collections.impl.lazy;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link DistinctIterable}.
 *
 * The benchmarks focus on throughput (operations per second) and use a realistic data set
 * containing many duplicate elements.  Blackhole is used to prevent dead‑code elimination.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class DistinctIterableBenchmark {

    /**
     * Size of the base data set (unique elements).
     */
    private static final int UNIQUE_COUNT = 1_000;

    /**
     * Number of repetitions of each unique element to create duplicates.
     */
    private static final int REPEAT = 10;

    /**
     * The source collection with many duplicates.
     */
    private List<Integer> source;

    /**
     * The DistinctIterable under test.
     */
    private DistinctIterable<Integer> distinctIterable;

    /**
     * Simple predicate that always returns true.
     */
    private static final Predicate<Integer> ALWAYS_TRUE = each -> true;

    /**
     * Simple predicate that always returns false.
     */
    private static final Predicate<Integer> ALWAYS_FALSE = each -> false;

    /**
     * Predicate that matches a specific value (used for detect).
     */
    private static final Predicate<Integer> MATCH_FIVE = each -> each == 5;

    /**
     * No‑op procedure used in {@code each}.
     */
    private static final Procedure<Integer> NO_OP = each -> {
        // intentionally empty
    };

    @Setup(Level.Trial)
    public void setUp() {
        // Build a list with many duplicate values.
        source = new ArrayList<>(UNIQUE_COUNT * REPEAT);
        for (int i = 0; i < REPEAT; i++) {
            for (int v = 0; v < UNIQUE_COUNT; v++) {
                source.add(v);
            }
        }
        distinctIterable = new DistinctIterable<>(source);
    }

    @Benchmark
    public void benchmarkEach(Blackhole bh) {
        distinctIterable.each(item -> bh.consume(item));
    }

    @Benchmark
    public void benchmarkAnySatisfy(Blackhole bh) {
        boolean result = distinctIterable.anySatisfy(ALWAYS_TRUE);
        bh.consume(result);
    }

    @Benchmark
    public void benchmarkAllSatisfy(Blackhole bh) {
        boolean result = distinctIterable.allSatisfy(ALWAYS_TRUE);
        bh.consume(result);
    }

    @Benchmark
    public void benchmarkNoneSatisfy(Blackhole bh) {
        boolean result = distinctIterable.noneSatisfy(ALWAYS_FALSE);
        bh.consume(result);
    }

    @Benchmark
    public void benchmarkDetect(Blackhole bh) {
        Integer found = distinctIterable.detect(MATCH_FIVE);
        bh.consume(found);
    }

    @Benchmark
    public void benchmarkDetectOptional(Blackhole bh) {
        var opt = distinctIterable.detectOptional(MATCH_FIVE);
        bh.consume(opt);
    }

    @Benchmark
    public void benchmarkIterator(Blackhole bh) {
        var it = distinctIterable.iterator();
        while (it.hasNext()) {
            bh.consume(it.next());
        }
    }
}
```

### Method 24

```java
package org.eclipse.collections.impl.lazy;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link DistinctIterable}.
 *
 * The benchmarks focus on throughput (operations per second) and use a realistic data set
 * containing many duplicate elements.  Blackhole is used to prevent dead‑code elimination.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class DistinctIterableBenchmark {

    /**
     * Size of the base data set (unique elements).
     */
    private static final int UNIQUE_COUNT = 1_000;

    /**
     * Number of repetitions of each unique element to create duplicates.
     */
    private static final int REPEAT = 10;

    /**
     * The source collection with many duplicates.
     */
    private List<Integer> source;

    /**
     * The DistinctIterable under test.
     */
    private DistinctIterable<Integer> distinctIterable;

    /**
     * Simple predicate that always returns true.
     */
    private static final Predicate<Integer> ALWAYS_TRUE = each -> true;

    /**
     * Simple predicate that always returns false.
     */
    private static final Predicate<Integer> ALWAYS_FALSE = each -> false;

    /**
     * Predicate that matches a specific value (used for detect).
     */
    private static final Predicate<Integer> MATCH_FIVE = each -> each == 5;

    /**
     * No‑op procedure used in {@code each}.
     */
    private static final Procedure<Integer> NO_OP = each -> {
        // intentionally empty
    };

    @Setup(Level.Trial)
    public void setUp() {
        // Build a list with many duplicate values.
        source = new ArrayList<>(UNIQUE_COUNT * REPEAT);
        for (int i = 0; i < REPEAT; i++) {
            for (int v = 0; v < UNIQUE_COUNT; v++) {
                source.add(v);
            }
        }
        distinctIterable = new DistinctIterable<>(source);
    }

    @Benchmark
    public void benchmarkEach(Blackhole bh) {
        distinctIterable.each(item -> bh.consume(item));
    }

    @Benchmark
    public void benchmarkAnySatisfy(Blackhole bh) {
        boolean result = distinctIterable.anySatisfy(ALWAYS_TRUE);
        bh.consume(result);
    }

    @Benchmark
    public void benchmarkAllSatisfy(Blackhole bh) {
        boolean result = distinctIterable.allSatisfy(ALWAYS_TRUE);
        bh.consume(result);
    }

    @Benchmark
    public void benchmarkNoneSatisfy(Blackhole bh) {
        boolean result = distinctIterable.noneSatisfy(ALWAYS_FALSE);
        bh.consume(result);
    }

    @Benchmark
    public void benchmarkDetect(Blackhole bh) {
        Integer found = distinctIterable.detect(MATCH_FIVE);
        bh.consume(found);
    }

    @Benchmark
    public void benchmarkDetectOptional(Blackhole bh) {
        var opt = distinctIterable.detectOptional(MATCH_FIVE);
        bh.consume(opt);
    }

    @Benchmark
    public void benchmarkIterator(Blackhole bh) {
        var it = distinctIterable.iterator();
        while (it.hasNext()) {
            bh.consume(it.next());
        }
    }
}
```

### Method 25

```java
package org.eclipse.collections.impl.lazy;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link DropWhileIterable}.
 *
 * The benchmarks cover the most frequently used operations:
 * - iteration via the enhanced for‑loop (uses iterator())
 * - {@code each} traversal
 * - predicate based queries (anySatisfy, allSatisfy, noneSatisfy, detect)
 *
 * Best practices applied:
 * • @State(Scope.Thread) to avoid sharing mutable state between threads.
 * • @Setup(Level.Trial) to build a stable data set once per fork.
 * • Warm‑up and measurement iterations with reasonable duration.
 * • Multiple forks to reduce JVM warm‑up noise.
 * • Blackhole consumption to prevent dead‑code elimination.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Thread)
public class DropWhileIterableBenchmark {

    private static final int SIZE = 10_000;

    private List<Integer> data;

    private DropWhileIterable<Integer> dropWhileIterable;

    private Predicate<Integer> dropPredicate;

    private Predicate<Integer> testPredicate;

    @Setup(Level.Trial)
    public void setUp() {
        // Prepare a deterministic data set
        data = new ArrayList<>(SIZE);
        for (int i = 0; i < SIZE; i++) {
            data.add(i);
        }
        // Drop while values are less than half the size
        dropPredicate = i -> i < SIZE / 2;
        // Simple predicate used by the query benchmarks
        // even numbers
        testPredicate = i -> (i & 1) == 0;
        // Create the lazy iterable under test
        dropWhileIterable = new DropWhileIterable<>(data, dropPredicate);
    }

    @Benchmark
    public void iterate(Blackhole bh) {
        // Enhanced‑for loop uses iterator()
        for (Integer i : dropWhileIterable) {
            bh.consume(i);
        }
    }

    @Benchmark
    public void each(Blackhole bh) {
        // Direct call to the each method
        dropWhileIterable.each(bh::consume);
    }

    @Benchmark
    public boolean anySatisfy() {
        // Short‑circuiting predicate query
        return dropWhileIterable.anySatisfy(testPredicate);
    }

    @Benchmark
    public boolean allSatisfy() {
        // Full scan predicate query
        return dropWhileIterable.allSatisfy(testPredicate);
    }

    @Benchmark
    public boolean noneSatisfy() {
        // Full scan predicate query
        return dropWhileIterable.noneSatisfy(testPredicate);
    }

    @Benchmark
    public Integer detect() {
        // Find‑first matching element
        return dropWhileIterable.detect(testPredicate);
    }
}
```

### Method 26

```java
package org.eclipse.collections.impl.lazy;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link SelectInstancesOfIterable}.
 *
 * The benchmarks measure throughput (operations per time unit) of the most common
 * operations provided by the lazy iterable. The data set consists of a mixed list
 * of {@link Integer} and {@link String} objects to emulate realistic usage where
 * the filter must inspect each element.
 *
 * Best‑practice settings:
 * - 5 warm‑up iterations to let the JIT stabilize.
 * - 10 measurement iterations for reliable results.
 * - 2 forks to isolate JVM state.
 * - Single thread per benchmark (Scope.Thread) to avoid contention.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Thread)
public class SelectInstancesOfIterableBenchmark {

    /**
     * Size of the test collection.
     */
    private static final int SIZE = 1_000_000;

    /**
     * Mixed collection of Integers and Strings.
     */
    private List<Object> mixedList;

    /**
     * Lazy iterable that selects only Integer instances.
     */
    private SelectInstancesOfIterable<Integer> integerIterable;

    /**
     * Predicates used for the various benchmarks.
     */
    private static final Predicate<Integer> ALWAYS_TRUE = i -> true;

    private static final Predicate<Integer> ALWAYS_FALSE = i -> false;

    private static final Predicate<Integer> IS_EVEN = i -> (i & 1) == 0;

    @Setup(Level.Trial)
    public void setUp() {
        mixedList = new ArrayList<>(SIZE);
        for (int i = 0; i < SIZE; i++) {
            // Alternate between Integer and String to create a realistic mix.
            if ((i & 1) == 0) {
                mixedList.add(i);
            } else {
                mixedList.add("str-" + i);
            }
        }
        integerIterable = new SelectInstancesOfIterable<>(mixedList, Integer.class);
    }

    @Benchmark
    public void benchmarkEach(Blackhole bh) {
        integerIterable.each(bh::consume);
    }

    @Benchmark
    public void benchmarkIterator(Blackhole bh) {
        integerIterable.iterator().forEachRemaining(bh::consume);
    }

    @Benchmark
    public void benchmarkGetFirst(Blackhole bh) {
        bh.consume(integerIterable.getFirst());
    }

    @Benchmark
    public void benchmarkAnySatisfyTrue(Blackhole bh) {
        bh.consume(integerIterable.anySatisfy(ALWAYS_TRUE));
    }

    @Benchmark
    public void benchmarkAllSatisfyTrue(Blackhole bh) {
        bh.consume(integerIterable.allSatisfy(ALWAYS_TRUE));
    }

    @Benchmark
    public void benchmarkNoneSatisfyFalse(Blackhole bh) {
        bh.consume(integerIterable.noneSatisfy(ALWAYS_FALSE));
    }

    @Benchmark
    public void benchmarkDetectEven(Blackhole bh) {
        bh.consume(integerIterable.detect(IS_EVEN));
    }

    @Benchmark
    public void benchmarkDetectOptionalEven(Blackhole bh) {
        bh.consume(integerIterable.detectOptional(IS_EVEN));
    }
}
```

### Method 27

```java
package org.eclipse.collections.impl.list.fixed;

import java.io.*;
import java.util.*;
import java.util.concurrent.TimeUnit;
import java.util.stream.IntStream;
import org.openjdk.jmh.runner.*;
import org.openjdk.jmh.runner.options.*;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Thread)
public class ArrayAdapterBenchmark {

    /**
     * Size of the test data set. Adjust to reflect realistic workloads.
     */
    private static final int DATA_SIZE = 1_000;

    /**
     * Pre‑populated adapter used for read‑only benchmarks.
     */
    private ArrayAdapter<Integer> populatedAdapter;

    /**
     * Fresh adapter used for mutating benchmarks (each iteration gets a clean copy).
     */
    private ArrayAdapter<Integer> freshAdapter;

    /**
     * Serialized form of an adapter for deserialization benchmark.
     */
    private byte[] serializedForm;

    @Setup(Level.Trial)
    public void setUpTrial() throws IOException {
        // Build a baseline adapter with sequential integers.
        Integer[] base = IntStream.range(0, DATA_SIZE).boxed().toArray(Integer[]::new);
        populatedAdapter = ArrayAdapter.adapt(base);
        // Serialize once; reuse the byte array for deserialization benchmark.
        try (ByteArrayOutputStream bos = new ByteArrayOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(bos)) {
            oos.writeObject(populatedAdapter);
            oos.flush();
            serializedForm = bos.toByteArray();
        }
    }

    @Setup(Level.Iteration)
    public void setUpIteration() {
        // Provide a fresh copy for each iteration to avoid cross‑iteration state leakage.
        freshAdapter = populatedAdapter.clone();
    }

    /* ------------------------------------- */
    /* Creation benchmarks */
    /* ------------------------------------- */
    @Benchmark
    public ArrayAdapter<Integer> adaptArray() {
        Integer[] data = IntStream.range(0, DATA_SIZE).boxed().toArray(Integer[]::new);
        return ArrayAdapter.adapt(data);
    }

    @Benchmark
    public ArrayAdapter<Integer> newArrayWithVarargs() {
        // Use a small var‑args call to measure overhead of cloning.
        return ArrayAdapter.newArrayWith(1, 2, 3, 4, 5);
    }

    /* ------------------------------------- */
    /* Read‑only benchmarks */
    /* ------------------------------------- */
    @Benchmark
    public int getElement() {
        // Random access pattern; index is deterministic for reproducibility.
        return freshAdapter.get(123);
    }

    @Benchmark
    public int iterateViaSpliterator() {
        int[] sum = new int[1];
        Spliterator<Integer> spliterator = freshAdapter.spliterator();
        // Simple forEachRemaining to keep the benchmark focused on traversal cost.
        spliterator.forEachRemaining(v -> sum[0] += v);
        return sum[0];
    }

    /* ------------------------------------- */
    /* Mutating benchmarks */
    /* ------------------------------------- */
    @Benchmark
    public ArrayAdapter<Integer> setElement() {
        // Mutate a middle element; returns the previous value (ignored).
        freshAdapter.set(500, -1);
        return freshAdapter;
    }

    @Benchmark
    public ArrayAdapter<Integer> withElement() {
        // 'with' creates a new adapter; we benchmark the allocation path.
        return freshAdapter.with(42);
    }

    @Benchmark
    public ArrayAdapter<Integer> withoutElement() {
        // Remove an element that is present.
        return freshAdapter.without(0);
    }

    @Benchmark
    public ArrayAdapter<Integer> withAllElements() {
        // Add a small collection to the adapter.
        List<Integer> extra = Arrays.asList(1001, 1002, 1003);
        return freshAdapter.withAll(extra);
    }

    @Benchmark
    public ArrayAdapter<Integer> withoutAllElements() {
        // Remove a small collection from the adapter.
        List<Integer> toRemove = Arrays.asList(0, 1, 2);
        return freshAdapter.withoutAll(toRemove);
    }

    @Benchmark
    public ArrayAdapter<Integer> cloneAdapter() {
        return freshAdapter.clone();
    }

    @Benchmark
    public ArrayAdapter<Integer> sortAdapter() {
        // Sort using natural order; the adapter is already sorted, measuring overhead.
        return freshAdapter.sortThis(Integer::compareTo);
    }

    @Benchmark
    public ArrayAdapter<Integer> toReversed() {
        return (ArrayAdapter<Integer>) freshAdapter.toReversed();
    }

    /* ------------------------------------- */
    /* Serialization benchmarks */
    /* ------------------------------------- */
    @Benchmark
    public byte[] serializeAdapter() throws IOException {
        try (ByteArrayOutputStream bos = new ByteArrayOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(bos)) {
            oos.writeObject(freshAdapter);
            oos.flush();
            return bos.toByteArray();
        }
    }

    @Benchmark
    public ArrayAdapter<Integer> deserializeAdapter() throws IOException, ClassNotFoundException {
        try (ByteArrayInputStream bis = new ByteArrayInputStream(serializedForm);
            ObjectInputStream ois = new ObjectInputStream(bis)) {
            @SuppressWarnings("unchecked")
            ArrayAdapter<Integer> deserialized = (ArrayAdapter<Integer>) ois.readObject();
            return deserialized;
        }
    }

    /* ------------------------------------- */
    /* Main entry point to run the benchmarks without external tooling. */
    /* ------------------------------------- */
    public static void main(String[] args) throws RunnerException {
        Options opt = new OptionsBuilder().include(ArrayAdapterBenchmark.class.getSimpleName()).detectJvmArgs().build();
        new Runner(opt).run();
    }
}
```

### Method 28

```java
package org.eclipse.collections.impl.list.immutable;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.block.function.primitive.IntFunction;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Benchmark)
public class ImmutableArrayListBenchmark {

    private static final int SIZE = 10_000;

    private ImmutableArrayList<Integer> list;

    private Random random;

    @Setup(Level.Trial)
    public void setUp() {
        Integer[] data = new Integer[SIZE];
        for (int i = 0; i < SIZE; i++) {
            data[i] = i;
        }
        list = ImmutableArrayList.newListWith(data);
        random = new Random(12345);
    }

    @Benchmark
    public Integer benchmarkGet() {
        int index = random.nextInt(SIZE);
        return list.get(index);
    }

    @Benchmark
    public void benchmarkEach() {
        list.each(item -> {
            // no-op; just force iteration
        });
    }

    @Benchmark
    public ImmutableArrayList<Integer> benchmarkSelectEven() {
        Predicate<Integer> isEven = i -> (i & 1) == 0;
        return (ImmutableArrayList<Integer>) list.select(isEven);
    }

    @Benchmark
    public ImmutableArrayList<Integer> benchmarkCollectDouble() {
        Function<Integer, Integer> doubleFn = i -> i * 2;
        return (ImmutableArrayList<Integer>) list.collect(doubleFn);
    }

    @Benchmark
    public long benchmarkSumOfInt() {
        IntFunction<Integer> identity = i -> i;
        return list.sumOfInt(identity);
    }

    @Benchmark
    public ImmutableArrayList<Integer> benchmarkTakeWhileLessThanHalf() {
        Predicate<Integer> lessThanHalf = i -> i < (SIZE / 2);
        return (ImmutableArrayList<Integer>) list.takeWhile(lessThanHalf);
    }

    @Benchmark
    public Integer benchmarkReduceSum() {
        return list.reduce((a, b) -> a + b).orElse(0);
    }
}
```

### Method 29

```java
package org.eclipse.collections.impl.list.mutable.primitive;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link BooleanArrayList}.
 * Measures throughput of common operations.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Thread)
public class BooleanArrayListBenchmark {

    /**
     * Size of the list used for most benchmarks.
     */
    private static final int LIST_SIZE = 10_000;

    /**
     * Number of elements added/removed in add/remove benchmarks.
     */
    private static final int BATCH_SIZE = 1_000;

    /**
     * The list under test.
     */
    private BooleanArrayList list;

    /**
     * A pre‑filled array of random booleans used for bulk operations.
     */
    private boolean[] randomValues;

    /**
     * Random generator with a fixed seed for reproducibility.
     */
    private Random random = new Random(12345L);

    @Setup(Level.Trial)
    public void setUp() {
        // Initialise list with a deterministic pattern.
        list = new BooleanArrayList(LIST_SIZE);
        for (int i = 0; i < LIST_SIZE; i++) {
            list.add(random.nextBoolean());
        }
        // Prepare a reusable array for bulk add/remove.
        randomValues = new boolean[BATCH_SIZE];
        for (int i = 0; i < BATCH_SIZE; i++) {
            randomValues[i] = random.nextBoolean();
        }
    }

    /* --------------------------------------------------------------------- */
    /*  Throughput benchmarks for individual operations                       */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public boolean get() {
        // Random access pattern.
        int index = random.nextInt(list.size());
        return list.get(index);
    }

    @Benchmark
    public boolean contains() {
        // Random boolean to search for.
        boolean value = random.nextBoolean();
        return list.contains(value);
    }

    @Benchmark
    public boolean add() {
        // Add a single element at the end.
        // The list grows; we reset it in the teardown to keep size bounded.
        boolean value = random.nextBoolean();
        return list.add(value);
    }

    @Benchmark
    public boolean addAll() {
        // Bulk add using the pre‑generated array.
        return list.addAll(randomValues);
    }

    @Benchmark
    public boolean remove() {
        // Remove a random element if present.
        boolean value = random.nextBoolean();
        return list.remove(value);
    }

    @Benchmark
    public boolean removeAtIndex() {
        // Remove element at a random valid index.
        if (list.isEmpty()) {
            return false;
        }
        int index = random.nextInt(list.size());
        list.removeAtIndex(index);
        return true;
    }

    @Benchmark
    public void iterate() {
        // Simple iteration using the primitive iterator.
        var iterator = list.booleanIterator();
        while (iterator.hasNext()) {
            iterator.next();
        }
    }

    @Benchmark
    public BooleanArrayList reverseThis() {
        // Reverse the list in‑place.
        // Clone to avoid mutating the shared state for other benchmarks.
        BooleanArrayList copy = BooleanArrayList.newList(list);
        return copy.reverseThis();
    }

    @Benchmark
    public BooleanArrayList select() {
        // Select all true values.
        return list.select(v -> v);
    }

    @Benchmark
    public BooleanArrayList reject() {
        // Reject all true values.
        return list.reject(v -> v);
    }

    @Benchmark
    public int countTrue() {
        // Count true values using a predicate.
        return list.count(v -> v);
    }

    /* --------------------------------------------------------------------- */
    /*  Teardown to keep the list size bounded for repeated add benchmarks   */
    /* --------------------------------------------------------------------- */
    @TearDown(Level.Iteration)
    public void tearDownIteration() {
        // Trim the list back to the original size after bulk adds.
        if (list.size() > LIST_SIZE) {
            // Remove excess elements from the end.
            while (list.size() > LIST_SIZE) {
                list.removeAtIndex(list.size() - 1);
            }
        }
    }
}
```

### Method 30

```java
package org.eclipse.collections.impl.list.mutable.primitive;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link BooleanArrayList}.
 * Measures throughput of common operations.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Thread)
public class BooleanArrayListBenchmark {

    /**
     * Size of the list used for most benchmarks.
     */
    private static final int LIST_SIZE = 10_000;

    /**
     * Number of elements added/removed in add/remove benchmarks.
     */
    private static final int BATCH_SIZE = 1_000;

    /**
     * The list under test.
     */
    private BooleanArrayList list;

    /**
     * A pre‑filled array of random booleans used for bulk operations.
     */
    private boolean[] randomValues;

    /**
     * Random generator with a fixed seed for reproducibility.
     */
    private Random random = new Random(12345L);

    @Setup(Level.Trial)
    public void setUp() {
        // Initialise list with a deterministic pattern.
        list = new BooleanArrayList(LIST_SIZE);
        for (int i = 0; i < LIST_SIZE; i++) {
            list.add(random.nextBoolean());
        }
        // Prepare a reusable array for bulk add/remove.
        randomValues = new boolean[BATCH_SIZE];
        for (int i = 0; i < BATCH_SIZE; i++) {
            randomValues[i] = random.nextBoolean();
        }
    }

    /* --------------------------------------------------------------------- */
    /*  Throughput benchmarks for individual operations                       */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public boolean get() {
        // Random access pattern.
        int index = random.nextInt(list.size());
        return list.get(index);
    }

    @Benchmark
    public boolean contains() {
        // Random boolean to search for.
        boolean value = random.nextBoolean();
        return list.contains(value);
    }

    @Benchmark
    public boolean add() {
        // Add a single element at the end.
        // The list grows; we reset it in the teardown to keep size bounded.
        boolean value = random.nextBoolean();
        return list.add(value);
    }

    @Benchmark
    public boolean addAll() {
        // Bulk add using the pre‑generated array.
        return list.addAll(randomValues);
    }

    @Benchmark
    public boolean remove() {
        // Remove a random element if present.
        boolean value = random.nextBoolean();
        return list.remove(value);
    }

    @Benchmark
    public boolean removeAtIndex() {
        // Remove element at a random valid index.
        if (list.isEmpty()) {
            return false;
        }
        int index = random.nextInt(list.size());
        list.removeAtIndex(index);
        return true;
    }

    @Benchmark
    public void iterate() {
        // Simple iteration using the primitive iterator.
        var iterator = list.booleanIterator();
        while (iterator.hasNext()) {
            iterator.next();
        }
    }

    @Benchmark
    public BooleanArrayList reverseThis() {
        // Reverse the list in‑place.
        // Clone to avoid mutating the shared state for other benchmarks.
        BooleanArrayList copy = BooleanArrayList.newList(list);
        return copy.reverseThis();
    }

    @Benchmark
    public BooleanArrayList select() {
        // Select all true values.
        return list.select(v -> v);
    }

    @Benchmark
    public BooleanArrayList reject() {
        // Reject all true values.
        return list.reject(v -> v);
    }

    @Benchmark
    public int countTrue() {
        // Count true values using a predicate.
        return list.count(v -> v);
    }

    /* --------------------------------------------------------------------- */
    /*  Teardown to keep the list size bounded for repeated add benchmarks   */
    /* --------------------------------------------------------------------- */
    @TearDown(Level.Iteration)
    public void tearDownIteration() {
        // Trim the list back to the original size after bulk adds.
        if (list.size() > LIST_SIZE) {
            // Remove excess elements from the end.
            while (list.size() > LIST_SIZE) {
                list.removeAtIndex(list.size() - 1);
            }
        }
    }
}
```

### Method 31

```java
package org.eclipse.collections.impl.list.mutable;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link MultiReaderFastList}.
 *
 * <p>
 * The benchmarks focus on the most common operations:
 * <ul>
 *   <li>read access – {@code get(int)}</li>
 *   <li>write access – {@code add(T)}</li>
 *   <li>iteration – {@code forEach(Procedure)}</li>
 *   <li>sorting – {@code sortThis()}</li>
 * </ul>
 * Each benchmark runs in {@link Mode#Throughput} to measure operations per time unit.
 * The state is shared across all threads (Scope.Benchmark) to emulate realistic
 * contention on the internal {@link java.util.concurrent.locks.ReadWriteLock}.
 * </p>
 *
 * <p>
 * Best‑practice notes:
 * <ul>
 *   <li>Use {@link Blackhole} to consume results and avoid dead‑code elimination.</li>
 *   <li>Warm‑up and measurement iterations are kept short but sufficient for JIT
 *       stabilization; they can be tuned per project needs.</li>
 *   <li>Forking isolates the benchmark from JVM warm‑up effects.</li>
 *   <li>Thread count is configurable via the {@code -t} JMH option; the default
 *       is the number of available processors.</li>
 * </ul>
 * </p>
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 7, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Benchmark)
public class MultiReaderFastListBenchmark {

    /**
     * Size of the list used for read‑only benchmarks.
     */
    private static final int LIST_SIZE = 10_000;

    /**
     * Shared list instance for all benchmarks.
     */
    private MultiReaderFastList<Integer> list;

    /**
     * Random generator for write benchmarks.
     */
    private Random random;

    /**
     * Executor used by the parallel iteration benchmark.
     */
    private ExecutorService executor;

    @Setup(Level.Trial)
    public void setUp() {
        // Initialise the list with a deterministic sequence.
        list = MultiReaderFastList.newList();
        for (int i = 0; i < LIST_SIZE; i++) {
            list.add(i);
        }
        random = new Random(12345L);
        executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown(Level.Trial)
    public void tearDown() {
        executor.shutdownNow();
    }

    /* --------------------------------------------------------------------- */
    /*  Read‑only operations                                                */
    /* --------------------------------------------------------------------- */
    @Benchmark
    @Group("read")
    // 4 concurrent readers
    @GroupThreads(4)
    public void getRandomElement(Blackhole bh) {
        int index = random.nextInt(LIST_SIZE);
        bh.consume(list.get(index));
    }

    @Benchmark
    @Group("read")
    @GroupThreads(4)
    public void iterate(Blackhole bh) {
        // The internal iteration uses a read lock; we simply consume each element.
        list.forEach(bh::consume);
    }

    /* --------------------------------------------------------------------- */
    /*  Write operations                                                    */
    /* --------------------------------------------------------------------- */
    @Benchmark
    @Group("write")
    // 2 concurrent writers
    @GroupThreads(2)
    public void addElement() {
        // Adding at the end; the list grows, but we keep the size bounded
        // by removing the first element to avoid unbounded memory growth.
        list.add(random.nextInt());
        list.remove(0);
    }

    @Benchmark
    @Group("write")
    @GroupThreads(2)
    public void sort() {
        // Sorting acquires a write lock; we sort a copy to keep the original order.
        // This mimics a realistic workload where sorting is occasional.
        MultiReaderList<Integer> copy = list.clone();
        copy.sortThis();
    }

    /* --------------------------------------------------------------------- */
    /*  Parallel iteration (optional)                                       */
    /* --------------------------------------------------------------------- */
    @Benchmark
    @Group("parallel")
    @GroupThreads(4)
    public void parallelForEach(Blackhole bh) {
        // Demonstrates the parallel view provided by the collection.
        list.asParallel(executor, 1_000).forEach(bh::consume);
    }
}
```

### Method 32

```java
package org.eclipse.collections.impl.map.fixed;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link TripletonMap}.
 *
 * The benchmarks focus on the most common operations:
 * - lookup (get, containsKey)
 * - mutation (withKeyValue, withoutKey)
 * - structural transformations (flipUniqueValues)
 * - iteration (forEachKeyValue, entrySet)
 *
 * All benchmarks run in {@link Mode#Throughput} to measure operations per time unit.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class TripletonMapBenchmark {

    private static final Integer K1 = 1;

    private static final Integer K2 = 2;

    private static final Integer K3 = 3;

    private static final String V1 = "one";

    private static final String V2 = "two";

    private static final String V3 = "three";

    /**
     * Map with exactly three entries, used as the baseline for most benchmarks.
     */
    private TripletonMap<Integer, String> tripletonMap;

    /**
     * A map that has been converted to a larger map after adding a fourth entry.
     */
    private MutableMap<Integer, String> mapAfterAdd;

    /**
     * A map that has been converted to a smaller map after removing one entry.
     */
    private MutableMap<Integer, String> mapAfterRemove;

    @Setup(Level.Trial)
    public void setUp() {
        tripletonMap = new TripletonMap<>(K1, V1, K2, V2, K3, V3);
        // Force conversion to a larger map (UnifiedMap) by adding a new key.
        mapAfterAdd = tripletonMap.withKeyValue(4, "four");
        // Force conversion to a smaller map (DoubletonMap) by removing a key.
        mapAfterRemove = tripletonMap.withoutKey(K3);
    }

    /* --------------------------------------------------------------------- */
    /* Lookup benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public String getExisting(Blackhole bh) {
        bh.consume(tripletonMap.get(K2));
        return V2;
    }

    @Benchmark
    public String getMissing(Blackhole bh) {
        bh.consume(tripletonMap.get(99));
        return null;
    }

    @Benchmark
    public boolean containsKeyExisting(Blackhole bh) {
        bh.consume(tripletonMap.containsKey(K1));
        return true;
    }

    @Benchmark
    public boolean containsKeyMissing(Blackhole bh) {
        bh.consume(tripletonMap.containsKey(99));
        return false;
    }

    /* --------------------------------------------------------------------- */
    /* Mutation benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public MutableMap<Integer, String> withKeyValueExisting() {
        // Update an existing key – stays a TripletonMap.
        return tripletonMap.withKeyValue(K1, "ONE");
    }

    @Benchmark
    public MutableMap<Integer, String> withKeyValueNew() {
        // Add a new key – triggers conversion to UnifiedMap.
        return tripletonMap.withKeyValue(4, "four");
    }

    @Benchmark
    public MutableMap<Integer, String> withoutKeyExisting() {
        // Remove an existing key – returns a DoubletonMap.
        return tripletonMap.withoutKey(K2);
    }

    @Benchmark
    public MutableMap<Integer, String> withoutKeyMissing() {
        // Attempt to remove a non‑existent key – returns the same instance.
        return tripletonMap.withoutKey(99);
    }

    /* --------------------------------------------------------------------- */
    /* Structural transformation benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public MutableMap<String, Integer> flipUniqueValues() {
        // Flip keys and values – stays a TripletonMap because values are unique.
        return tripletonMap.flipUniqueValues();
    }

    /* --------------------------------------------------------------------- */
    /* Iteration benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void forEachKeyValue(Blackhole bh) {
        tripletonMap.forEachKeyValue((k, v) -> {
            bh.consume(k);
            bh.consume(v);
        });
    }

    @Benchmark
    public void entrySetIteration(Blackhole bh) {
        tripletonMap.entrySet().forEach(entry -> {
            bh.consume(entry.getKey());
            bh.consume(entry.getValue());
        });
    }

    @Benchmark
    public void valuesIteration(Blackhole bh) {
        tripletonMap.values().forEach(bh::consume);
    }

    @Benchmark
    public void keySetIteration(Blackhole bh) {
        tripletonMap.keySet().forEach(bh::consume);
    }

    /* --------------------------------------------------------------------- */
    /* Post‑conversion benchmarks (optional) */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public Object getAfterAdd() {
        // Lookup on the map after it has been converted to a larger map.
        return mapAfterAdd.get(4);
    }

    @Benchmark
    public Object getAfterRemove() {
        // Lookup on the map after it has been converted to a smaller map.
        return mapAfterRemove.get(K1);
    }
}
```

### Method 33

```java
package org.eclipse.collections.impl.map.fixed;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link TripletonMap}.
 *
 * The benchmarks focus on the most common operations:
 * - lookup (get, containsKey)
 * - mutation (withKeyValue, withoutKey)
 * - structural transformations (flipUniqueValues)
 * - iteration (forEachKeyValue, entrySet)
 *
 * All benchmarks run in {@link Mode#Throughput} to measure operations per time unit.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class TripletonMapBenchmark {

    private static final Integer K1 = 1;

    private static final Integer K2 = 2;

    private static final Integer K3 = 3;

    private static final String V1 = "one";

    private static final String V2 = "two";

    private static final String V3 = "three";

    /**
     * Map with exactly three entries, used as the baseline for most benchmarks.
     */
    private TripletonMap<Integer, String> tripletonMap;

    /**
     * A map that has been converted to a larger map after adding a fourth entry.
     */
    private MutableMap<Integer, String> mapAfterAdd;

    /**
     * A map that has been converted to a smaller map after removing one entry.
     */
    private MutableMap<Integer, String> mapAfterRemove;

    @Setup(Level.Trial)
    public void setUp() {
        tripletonMap = new TripletonMap<>(K1, V1, K2, V2, K3, V3);
        // Force conversion to a larger map (UnifiedMap) by adding a new key.
        mapAfterAdd = tripletonMap.withKeyValue(4, "four");
        // Force conversion to a smaller map (DoubletonMap) by removing a key.
        mapAfterRemove = tripletonMap.withoutKey(K3);
    }

    /* --------------------------------------------------------------------- */
    /* Lookup benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public String getExisting(Blackhole bh) {
        bh.consume(tripletonMap.get(K2));
        return V2;
    }

    @Benchmark
    public String getMissing(Blackhole bh) {
        bh.consume(tripletonMap.get(99));
        return null;
    }

    @Benchmark
    public boolean containsKeyExisting(Blackhole bh) {
        bh.consume(tripletonMap.containsKey(K1));
        return true;
    }

    @Benchmark
    public boolean containsKeyMissing(Blackhole bh) {
        bh.consume(tripletonMap.containsKey(99));
        return false;
    }

    /* --------------------------------------------------------------------- */
    /* Mutation benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public MutableMap<Integer, String> withKeyValueExisting() {
        // Update an existing key – stays a TripletonMap.
        return tripletonMap.withKeyValue(K1, "ONE");
    }

    @Benchmark
    public MutableMap<Integer, String> withKeyValueNew() {
        // Add a new key – triggers conversion to UnifiedMap.
        return tripletonMap.withKeyValue(4, "four");
    }

    @Benchmark
    public MutableMap<Integer, String> withoutKeyExisting() {
        // Remove an existing key – returns a DoubletonMap.
        return tripletonMap.withoutKey(K2);
    }

    @Benchmark
    public MutableMap<Integer, String> withoutKeyMissing() {
        // Attempt to remove a non‑existent key – returns the same instance.
        return tripletonMap.withoutKey(99);
    }

    /* --------------------------------------------------------------------- */
    /* Structural transformation benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public MutableMap<String, Integer> flipUniqueValues() {
        // Flip keys and values – stays a TripletonMap because values are unique.
        return tripletonMap.flipUniqueValues();
    }

    /* --------------------------------------------------------------------- */
    /* Iteration benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void forEachKeyValue(Blackhole bh) {
        tripletonMap.forEachKeyValue((k, v) -> {
            bh.consume(k);
            bh.consume(v);
        });
    }

    @Benchmark
    public void entrySetIteration(Blackhole bh) {
        tripletonMap.entrySet().forEach(entry -> {
            bh.consume(entry.getKey());
            bh.consume(entry.getValue());
        });
    }

    @Benchmark
    public void valuesIteration(Blackhole bh) {
        tripletonMap.values().forEach(bh::consume);
    }

    @Benchmark
    public void keySetIteration(Blackhole bh) {
        tripletonMap.keySet().forEach(bh::consume);
    }

    /* --------------------------------------------------------------------- */
    /* Post‑conversion benchmarks (optional) */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public Object getAfterAdd() {
        // Lookup on the map after it has been converted to a larger map.
        return mapAfterAdd.get(4);
    }

    @Benchmark
    public Object getAfterRemove() {
        // Lookup on the map after it has been converted to a smaller map.
        return mapAfterRemove.get(K1);
    }
}
```

### Method 34

```java
package org.eclipse.collections.impl.map.fixed;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link TripletonMap}.
 *
 * The benchmarks focus on the most common operations:
 * - lookup (get, containsKey)
 * - mutation (withKeyValue, withoutKey)
 * - structural transformations (flipUniqueValues)
 * - iteration (forEachKeyValue, entrySet)
 *
 * All benchmarks run in {@link Mode#Throughput} to measure operations per time unit.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class TripletonMapBenchmark {

    private static final Integer K1 = 1;

    private static final Integer K2 = 2;

    private static final Integer K3 = 3;

    private static final String V1 = "one";

    private static final String V2 = "two";

    private static final String V3 = "three";

    /**
     * Map with exactly three entries, used as the baseline for most benchmarks.
     */
    private TripletonMap<Integer, String> tripletonMap;

    /**
     * A map that has been converted to a larger map after adding a fourth entry.
     */
    private MutableMap<Integer, String> mapAfterAdd;

    /**
     * A map that has been converted to a smaller map after removing one entry.
     */
    private MutableMap<Integer, String> mapAfterRemove;

    @Setup(Level.Trial)
    public void setUp() {
        tripletonMap = new TripletonMap<>(K1, V1, K2, V2, K3, V3);
        // Force conversion to a larger map (UnifiedMap) by adding a new key.
        mapAfterAdd = tripletonMap.withKeyValue(4, "four");
        // Force conversion to a smaller map (DoubletonMap) by removing a key.
        mapAfterRemove = tripletonMap.withoutKey(K3);
    }

    /* --------------------------------------------------------------------- */
    /* Lookup benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public String getExisting(Blackhole bh) {
        bh.consume(tripletonMap.get(K2));
        return V2;
    }

    @Benchmark
    public String getMissing(Blackhole bh) {
        bh.consume(tripletonMap.get(99));
        return null;
    }

    @Benchmark
    public boolean containsKeyExisting(Blackhole bh) {
        bh.consume(tripletonMap.containsKey(K1));
        return true;
    }

    @Benchmark
    public boolean containsKeyMissing(Blackhole bh) {
        bh.consume(tripletonMap.containsKey(99));
        return false;
    }

    /* --------------------------------------------------------------------- */
    /* Mutation benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public MutableMap<Integer, String> withKeyValueExisting() {
        // Update an existing key – stays a TripletonMap.
        return tripletonMap.withKeyValue(K1, "ONE");
    }

    @Benchmark
    public MutableMap<Integer, String> withKeyValueNew() {
        // Add a new key – triggers conversion to UnifiedMap.
        return tripletonMap.withKeyValue(4, "four");
    }

    @Benchmark
    public MutableMap<Integer, String> withoutKeyExisting() {
        // Remove an existing key – returns a DoubletonMap.
        return tripletonMap.withoutKey(K2);
    }

    @Benchmark
    public MutableMap<Integer, String> withoutKeyMissing() {
        // Attempt to remove a non‑existent key – returns the same instance.
        return tripletonMap.withoutKey(99);
    }

    /* --------------------------------------------------------------------- */
    /* Structural transformation benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public MutableMap<String, Integer> flipUniqueValues() {
        // Flip keys and values – stays a TripletonMap because values are unique.
        return tripletonMap.flipUniqueValues();
    }

    /* --------------------------------------------------------------------- */
    /* Iteration benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void forEachKeyValue(Blackhole bh) {
        tripletonMap.forEachKeyValue((k, v) -> {
            bh.consume(k);
            bh.consume(v);
        });
    }

    @Benchmark
    public void entrySetIteration(Blackhole bh) {
        tripletonMap.entrySet().forEach(entry -> {
            bh.consume(entry.getKey());
            bh.consume(entry.getValue());
        });
    }

    @Benchmark
    public void valuesIteration(Blackhole bh) {
        tripletonMap.values().forEach(bh::consume);
    }

    @Benchmark
    public void keySetIteration(Blackhole bh) {
        tripletonMap.keySet().forEach(bh::consume);
    }

    /* --------------------------------------------------------------------- */
    /* Post‑conversion benchmarks (optional) */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public Object getAfterAdd() {
        // Lookup on the map after it has been converted to a larger map.
        return mapAfterAdd.get(4);
    }

    @Benchmark
    public Object getAfterRemove() {
        // Lookup on the map after it has been converted to a smaller map.
        return mapAfterRemove.get(K1);
    }
}
```

### Method 35

```java
package org.eclipse.collections.impl.map.immutable;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * Micro‑benchmarks for {@link ImmutableSingletonMap}.
 *
 * The benchmarks focus on the most frequently used operations:
 * <ul>
 *   <li>lookup – {@code get}, {@code containsKey}, {@code containsValue}</li>
 *   <li>iteration – {@code forEachKeyValue}</li>
 *   <li>functional transformations – {@code select}, {@code reject}, {@code collect}</li>
 * </ul>
 *
 * All benchmarks run in {@link Mode#Throughput} to measure the number of
 * operations per time unit, which is the most relevant metric for typical
 * collection usage.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Thread)
public class ImmutableSingletonMapBenchmark {

    private static final Integer KEY = 42;

    private static final String VALUE = "the answer";

    private ImmutableMap<Integer, String> map;

    private static final org.eclipse.collections.api.block.predicate.Predicate2<Integer, String> ALWAYS_TRUE = (k, v) -> true;

    private static final org.eclipse.collections.api.block.predicate.Predicate2<Integer, String> ALWAYS_FALSE = (k, v) -> false;

    private static final org.eclipse.collections.api.block.function.Function2<Integer, String, Pair<String, Integer>> FLIP_PAIR = (k, v) -> Tuples.pair(v, k);

    @Setup(Level.Trial)
    public void setUp() {
        this.map = new ImmutableSingletonMap<>(KEY, VALUE);
    }

    /* --------------------------------------------------------------------- */
    /* Lookup operations */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public String get(Blackhole bh) {
        bh.consume(map.get(KEY));
        return VALUE;
    }

    @Benchmark
    public boolean containsKey() {
        return map.containsKey(KEY);
    }

    @Benchmark
    public boolean containsValue() {
        return map.containsValue(VALUE);
    }

    /* --------------------------------------------------------------------- */
    /* Iteration */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void forEachKeyValue(Blackhole bh) {
        map.forEachKeyValue((k, v) -> {
            bh.consume(k);
            bh.consume(v);
        });
    }

    /* --------------------------------------------------------------------- */
    /* Functional transformations */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public ImmutableMap<Integer, String> selectTrue() {
        return map.select(ALWAYS_TRUE);
    }

    @Benchmark
    public ImmutableMap<Integer, String> selectFalse() {
        return map.select(ALWAYS_FALSE);
    }

    @Benchmark
    public ImmutableMap<Integer, String> rejectTrue() {
        return map.reject(ALWAYS_TRUE);
    }

    @Benchmark
    public ImmutableMap<Integer, String> rejectFalse() {
        return map.reject(ALWAYS_FALSE);
    }

    @Benchmark
    public ImmutableMap<String, Integer> collectFlip() {
        return map.collect(FLIP_PAIR);
    }
}
```

### Method 36

```java
package org.eclipse.collections.impl.map.mutable.primitive;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.block.predicate.primitive.BooleanPredicate;
import org.eclipse.collections.api.block.procedure.primitive.BooleanProcedure;
import org.eclipse.collections.api.collection.primitive.MutableBooleanCollection;
import org.eclipse.collections.api.iterator.MutableBooleanIterator;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public class AbstractMutableBooleanValuesMapBenchmark {

    @State(Scope.Thread)
    public static class BenchmarkState {

        private static final int SIZE = 10_000;

        private TestBooleanValuesMap map;

        private final BooleanPredicate isTrue = value -> value;

        @Setup(Level.Trial)
        public void setUp() {
            map = new TestBooleanValuesMap(SIZE);
            map.populateRandomly();
        }

        /**
         * Simple concrete subclass that stores values in primitive arrays.
         */
        private static class TestBooleanValuesMap extends AbstractMutableBooleanValuesMap {

            private final boolean[] values;

            private final boolean[] occupied;

            private SentinelValues sentinel;

            TestBooleanValuesMap(int capacity) {
                this.values = new boolean[capacity];
                this.occupied = new boolean[capacity];
                this.sentinel = null;
            }

            void populateRandomly() {
                Random rnd = new Random(0);
                for (int i = 0; i < values.length; i++) {
                    values[i] = rnd.nextBoolean();
                    occupied[i] = true;
                }
                this.sentinel = new SentinelValues();
                this.sentinel.containsZeroKey = true;
                this.sentinel.zeroValue = true;
                this.sentinel.containsOneKey = true;
                this.sentinel.oneValue = false;
            }

            @Override
            protected int getOccupiedWithData() {
                int count = 0;
                for (boolean b : occupied) {
                    if (b)
                        count++;
                }
                return count;
            }

            @Override
            protected SentinelValues getSentinelValues() {
                return sentinel;
            }

            @Override
            protected void setSentinelValuesNull() {
                sentinel = null;
            }

            @Override
            protected boolean getEmptyValue() {
                return false;
            }

            @Override
            protected boolean getValueAtIndex(int index) {
                return values[index];
            }

            @Override
            protected int getTableSize() {
                return values.length;
            }

            @Override
            protected boolean isNonSentinelAtIndex(int index) {
                return occupied[index];
            }

            @Override
            public MutableBooleanIterator booleanIterator() {
                return new MutableBooleanIterator() {

                    private int idx = 0;

                    @Override
                    public boolean hasNext() {
                        while (idx < values.length && !occupied[idx]) {
                            idx++;
                        }
                        return idx < values.length;
                    }

                    @Override
                    public boolean next() {
                        return values[idx++];
                    }

                    @Override
                    public void remove() {
                        // No removal support in this simple benchmark implementation
                    }
                };
            }

            @Override
            public void clear() {
                for (int i = 0; i < occupied.length; i++) {
                    occupied[i] = false;
                }
                sentinel = null;
            }

            @Override
            public boolean containsValue(boolean value) {
                if (sentinel != null) {
                    if (sentinel.containsZeroKey && sentinel.zeroValue == value)
                        return true;
                    if (sentinel.containsOneKey && sentinel.oneValue == value)
                        return true;
                }
                for (int i = 0; i < values.length; i++) {
                    if (occupied[i] && values[i] == value)
                        return true;
                }
                return false;
            }

            @Override
            public MutableBooleanCollection values() {
                BooleanHashSet set = new BooleanHashSet();
                if (sentinel != null) {
                    if (sentinel.containsZeroKey)
                        set.add(sentinel.zeroValue);
                    if (sentinel.containsOneKey)
                        set.add(sentinel.oneValue);
                }
                for (int i = 0; i < values.length; i++) {
                    if (occupied[i])
                        set.add(values[i]);
                }
                return set;
            }
        }
    }

    @Benchmark
    public void benchmarkForEachValue(BenchmarkState state) {
        BooleanProcedure proc = value -> {
            // no‑op
        };
        state.map.forEachValue(proc);
    }

    @Benchmark
    public boolean[] benchmarkToArray(BenchmarkState state) {
        return state.map.toArray();
    }

    @Benchmark
    public boolean benchmarkContainsTrue(BenchmarkState state) {
        return state.map.contains(true);
    }

    @Benchmark
    public int benchmarkCountTrue(BenchmarkState state) {
        return state.map.count(state.isTrue);
    }

    @Benchmark
    public boolean benchmarkAnySatisfyTrue(BenchmarkState state) {
        return state.map.anySatisfy(state.isTrue);
    }
}
```

### Method 37

```java
package org.eclipse.collections.impl.map.mutable.primitive;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.tuple.primitive.ObjectBooleanPair;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Thread)
public class ObjectBooleanHashMapBenchmark {

    private static final int INITIAL_SIZE = 1_000_000;

    private static final int KEY_RANGE = 2 * INITIAL_SIZE;

    private ObjectBooleanHashMap<Integer> map;

    private int[] keys;

    private boolean[] values;

    private int nextPutIndex;

    private int nextGetIndex;

    private int nextRemoveIndex;

    private Random random;

    @Setup(Level.Trial)
    public void setUp() {
        map = new ObjectBooleanHashMap<>(INITIAL_SIZE);
        keys = new int[INITIAL_SIZE];
        values = new boolean[INITIAL_SIZE];
        random = new Random(12345L);
        for (int i = 0; i < INITIAL_SIZE; i++) {
            int key = random.nextInt(KEY_RANGE);
            boolean value = random.nextBoolean();
            keys[i] = key;
            values[i] = value;
            map.put(key, value);
        }
        nextPutIndex = 0;
        nextGetIndex = 0;
        nextRemoveIndex = 0;
    }

    @Benchmark
    public boolean benchmarkPut() {
        int key = random.nextInt(KEY_RANGE) + KEY_RANGE;
        boolean value = random.nextBoolean();
        map.put(key, value);
        return map.containsKey(key);
    }

    @Benchmark
    public boolean benchmarkGet() {
        int key = keys[nextGetIndex];
        nextGetIndex = (nextGetIndex + 1) % INITIAL_SIZE;
        return map.get(key);
    }

    @Benchmark
    public boolean benchmarkRemove() {
        int key = keys[nextRemoveIndex];
        nextRemoveIndex = (nextRemoveIndex + 1) % INITIAL_SIZE;
        boolean existed = map.containsKey(key);
        map.remove(key);
        return existed;
    }

    @Benchmark
    public long benchmarkIterateKeys() {
        long sum = 0;
        for (Integer key : map.keySet()) {
            sum += key;
        }
        return sum;
    }

    @Benchmark
    public long benchmarkIterateValues() {
        long trueCount = 0;
        for (boolean v : map.values().toArray()) {
            if (v)
                trueCount++;
        }
        return trueCount;
    }

    @Benchmark
    public long benchmarkIterateEntries() {
        long sum = 0;
        for (ObjectBooleanPair<Integer> entry : map.keyValuesView()) {
            sum += entry.getTwo() ? 1 : 0;
        }
        return sum;
    }
}
```

### Method 38

```java
package org.eclipse.collections.impl.map.mutable.primitive;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.tuple.primitive.ObjectBooleanPair;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Thread)
public class ObjectBooleanHashMapBenchmark {

    private static final int INITIAL_SIZE = 1_000_000;

    private static final int KEY_RANGE = 2 * INITIAL_SIZE;

    private ObjectBooleanHashMap<Integer> map;

    private int[] keys;

    private boolean[] values;

    private int nextPutIndex;

    private int nextGetIndex;

    private int nextRemoveIndex;

    private Random random;

    @Setup(Level.Trial)
    public void setUp() {
        map = new ObjectBooleanHashMap<>(INITIAL_SIZE);
        keys = new int[INITIAL_SIZE];
        values = new boolean[INITIAL_SIZE];
        random = new Random(12345L);
        for (int i = 0; i < INITIAL_SIZE; i++) {
            int key = random.nextInt(KEY_RANGE);
            boolean value = random.nextBoolean();
            keys[i] = key;
            values[i] = value;
            map.put(key, value);
        }
        nextPutIndex = 0;
        nextGetIndex = 0;
        nextRemoveIndex = 0;
    }

    @Benchmark
    public boolean benchmarkPut() {
        int key = random.nextInt(KEY_RANGE) + KEY_RANGE;
        boolean value = random.nextBoolean();
        map.put(key, value);
        return map.containsKey(key);
    }

    @Benchmark
    public boolean benchmarkGet() {
        int key = keys[nextGetIndex];
        nextGetIndex = (nextGetIndex + 1) % INITIAL_SIZE;
        return map.get(key);
    }

    @Benchmark
    public boolean benchmarkRemove() {
        int key = keys[nextRemoveIndex];
        nextRemoveIndex = (nextRemoveIndex + 1) % INITIAL_SIZE;
        boolean existed = map.containsKey(key);
        map.remove(key);
        return existed;
    }

    @Benchmark
    public long benchmarkIterateKeys() {
        long sum = 0;
        for (Integer key : map.keySet()) {
            sum += key;
        }
        return sum;
    }

    @Benchmark
    public long benchmarkIterateValues() {
        long trueCount = 0;
        for (boolean v : map.values().toArray()) {
            if (v)
                trueCount++;
        }
        return trueCount;
    }

    @Benchmark
    public long benchmarkIterateEntries() {
        long sum = 0;
        for (ObjectBooleanPair<Integer> entry : map.keyValuesView()) {
            sum += entry.getTwo() ? 1 : 0;
        }
        return sum;
    }
}
```

### Method 39

```java
package org.eclipse.collections.impl.map.mutable.primitive;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2)
@State(Scope.Thread)
public class ObjectBooleanHashMapWithHashingStrategyBenchmark {

    private static final int SIZE = 10_000;

    private ObjectBooleanHashMapWithHashingStrategy<Integer> map;

    private ObjectBooleanHashMapWithHashingStrategy<Integer> mapForIteration;

    private Integer[] keys;

    private boolean[] values;

    @Setup(Level.Trial)
    public void setUp() {
        // simple hashing strategy that uses Integer's hashCode and equals
        HashingStrategy<Integer> hashingStrategy = new HashingStrategy<Integer>() {

            @Override
            public int computeHashCode(Integer object) {
                return object == null ? 0 : object.hashCode();
            }

            @Override
            public boolean equals(Integer o1, Integer o2) {
                return o1 == null ? o2 == null : o1.equals(o2);
            }
        };
        map = new ObjectBooleanHashMapWithHashingStrategy<>(hashingStrategy, SIZE);
        mapForIteration = new ObjectBooleanHashMapWithHashingStrategy<>(hashingStrategy, SIZE);
        keys = new Integer[SIZE];
        values = new boolean[SIZE];
        for (int i = 0; i < SIZE; i++) {
            keys[i] = i;
            // true for even keys
            values[i] = (i & 1) == 0;
            map.put(keys[i], values[i]);
            mapForIteration.put(keys[i], values[i]);
        }
    }

    @Benchmark
    public void benchPut() {
        // put a new key each time to avoid overwriting existing entries
        int key = (int) (Math.random() * Integer.MAX_VALUE);
        map.put(key, key % 2 == 0);
    }

    @Benchmark
    public boolean benchGet() {
        // random existing key
        int idx = (int) (Math.random() * SIZE);
        return map.get(keys[idx]);
    }

    @Benchmark
    public boolean benchContainsKey() {
        int idx = (int) (Math.random() * SIZE);
        return map.containsKey(keys[idx]);
    }

    @Benchmark
    public void benchRemove() {
        // remove a random key; re‑insert to keep map size stable
        int idx = (int) (Math.random() * SIZE);
        Integer key = keys[idx];
        map.remove(key);
        map.put(key, values[idx]);
    }

    @Benchmark
    public int benchIteration() {
        // count true values using the public API
        final int[] sum = { 0 };
        mapForIteration.forEachKeyValue((k, v) -> {
            if (v) {
                sum[0]++;
            }
        });
        return sum[0];
    }

    @Benchmark
    public int benchKeyIteration() {
        // count keys using the public API
        final int[] count = { 0 };
        mapForIteration.forEachKey(k -> count[0]++);
        return count[0];
    }

    @Benchmark
    public int benchEntryIteration() {
        // count true values (same as benchIteration) using the public API
        final int[] trueCount = { 0 };
        mapForIteration.forEachKeyValue((k, v) -> {
            if (v) {
                trueCount[0]++;
            }
        });
        return trueCount[0];
    }
}
```

### Method 40

```java
package org.eclipse.collections.impl.map.strategy.immutable;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link ImmutableUnifiedMapWithHashingStrategy}.
 *
 * The benchmarks focus on the most frequently used operations:
 * <ul>
 *   <li>lookup via {@code get}</li>
 *   <li>key existence via {@code containsKey}</li>
 *   <li>creation of a new map with an additional entry via {@code newWithKeyValue}</li>
 *   <li>creation of a new map without a key via {@code newWithoutKey}</li>
 *   <li>iteration over {@code entrySet}</li>
 * </ul>
 *
 * The benchmark is configured for throughput mode, which measures how many
 * operations can be performed per time unit. Warm‑up and measurement
 * iterations, forks and time units follow common best‑practice defaults.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 3)
@State(Scope.Benchmark)
public class ImmutableUnifiedMapWithHashingStrategyBenchmark {

    /**
     * Size of the map used for the benchmarks.
     */
    private static final int MAP_SIZE = 10_000;

    /**
     * The immutable map under test.
     */
    private ImmutableUnifiedMapWithHashingStrategy<Integer, String> immutableMap;

    /**
     * Array of keys for random access; populated during @Setup.
     */
    private int[] keys;

    /**
     * Random generator for selecting keys during benchmarks.
     */
    private Random random;

    @Setup(Level.Trial)
    public void setUp() {
        // Build a mutable map with a default hashing strategy and populate it.
        UnifiedMapWithHashingStrategy<Integer, String> mutable = UnifiedMapWithHashingStrategy.newMap(HashingStrategies.defaultStrategy(), MAP_SIZE);
        for (int i = 0; i < MAP_SIZE; i++) {
            mutable.put(i, "value-" + i);
        }
        // Convert to immutable.
        this.immutableMap = new ImmutableUnifiedMapWithHashingStrategy<>(mutable);
        // Prepare a shuffled key array to avoid any ordering bias.
        this.keys = new int[MAP_SIZE];
        for (int i = 0; i < MAP_SIZE; i++) this.keys[i] = i;
        shuffleArray(this.keys);
        // deterministic seed for reproducibility
        this.random = new Random(12345L);
    }

    /**
     * Fisher‑Yates shuffle for the key array.
     */
    private static void shuffleArray(int[] array) {
        Random rnd = new Random(98765L);
        for (int i = array.length - 1; i > 0; i--) {
            int index = rnd.nextInt(i + 1);
            int a = array[index];
            array[index] = array[i];
            array[i] = a;
        }
    }

    /**
     * Benchmark for {@code get(Object)}.
     */
    @Benchmark
    public void benchGet(Blackhole bh) {
        int key = keys[random.nextInt(MAP_SIZE)];
        bh.consume(immutableMap.get(key));
    }

    /**
     * Benchmark for {@code containsKey(Object)}.
     */
    @Benchmark
    public void benchContainsKey(Blackhole bh) {
        int key = keys[random.nextInt(MAP_SIZE)];
        bh.consume(immutableMap.containsKey(key));
    }

    /**
     * Benchmark for {@code newWithKeyValue(K, V)} – creates a new immutable map.
     */
    @Benchmark
    public void benchNewWithKeyValue(Blackhole bh) {
        int newKey = MAP_SIZE + random.nextInt(1_000);
        ImmutableUnifiedMapWithHashingStrategy<Integer, String> newMap = (ImmutableUnifiedMapWithHashingStrategy<Integer, String>) immutableMap.newWithKeyValue(newKey, "new-value");
        bh.consume(newMap);
    }

    /**
     * Benchmark for {@code newWithoutKey(Object)} – creates a new immutable map without a key.
     */
    @Benchmark
    public void benchNewWithoutKey(Blackhole bh) {
        int keyToRemove = keys[random.nextInt(MAP_SIZE)];
        ImmutableUnifiedMapWithHashingStrategy<Integer, String> newMap = (ImmutableUnifiedMapWithHashingStrategy<Integer, String>) immutableMap.newWithoutKey(keyToRemove);
        bh.consume(newMap);
    }

    /**
     * Benchmark for iterating over {@code entrySet()} and consuming each entry.
     */
    @Benchmark
    public void benchEntrySetIteration(Blackhole bh) {
        // The entrySet is immutable; iterating over it should be cheap.
        for (var entry : immutableMap.entrySet()) {
            bh.consume(entry.getKey());
            bh.consume(entry.getValue());
        }
    }
}
```

### Method 41

```java
package org.eclipse.collections.impl.multimap.bag.sorted.mutable;

import java.util.Comparator;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link TreeBagMultimap}.
 *
 * The benchmarks focus on the most common operations:
 * <ul>
 *   <li>put (single entry)</li>
 *   <li>putAll (bulk insertion)</li>
 *   <li>get (lookup of a bag)</li>
 *   <li>remove (single entry)</li>
 *   <li>iteration over all entries</li>
 *   <li>flip (key/value inversion)</li>
 * </ul>
 *
 * Throughput mode is used because typical library usage cares about the number of
 * operations per time unit rather than latency of a single call.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2)
@State(Scope.Thread)
public class TreeBagMultimapBenchmark {

    /**
     * Size of the pre‑populated multimap.
     */
    private static final int PREPOPULATED_SIZE = 10_000;

    /**
     * Number of entries added/removed per benchmark invocation.
     */
    private static final int BATCH_SIZE = 100;

    /**
     * The multimap used for read‑only benchmarks (get, iteration, flip).
     */
    private TreeBagMultimap<Integer, String> readOnlyMultimap;

    /**
     * The multimap used for write benchmarks (put, remove).
     */
    private TreeBagMultimap<Integer, String> mutableMultimap;

    /**
     * Comparator used for the value type (String).
     */
    private final Comparator<String> stringComparator = Comparator.naturalOrder();

    /**
     * Helper method to generate a deterministic value for a given key.
     */
    private static String valueFor(int key) {
        return "value-" + key;
    }

    @Setup(Level.Trial)
    public void setUp() {
        // Initialise a multimap with a deterministic distribution of keys/values.
        readOnlyMultimap = TreeBagMultimap.newMultimap(stringComparator);
        mutableMultimap = TreeBagMultimap.newMultimap(stringComparator);
        for (int i = 0; i < PREPOPULATED_SIZE; i++) {
            // 10 distinct keys, each with many values
            int key = i % (PREPOPULATED_SIZE / 10);
            String value = valueFor(i);
            readOnlyMultimap.put(key, value);
            mutableMultimap.put(key, value);
        }
    }

    /* --------------------------------------------------------------------- */
    /* Write benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void putSingle(Blackhole bh) {
        // Use a fresh key to avoid collisions that could bias the measurement.
        int key = PREPOPULATED_SIZE + (int) (Math.random() * BATCH_SIZE);
        String value = valueFor(key);
        mutableMultimap.put(key, value);
        // Prevent dead‑code elimination.
        bh.consume(mutableMultimap);
    }

    @Benchmark
    public void putBatch(Blackhole bh) {
        // Insert a batch of entries in a tight loop.
        for (int i = 0; i < BATCH_SIZE; i++) {
            int key = PREPOPULATED_SIZE + i;
            mutableMultimap.put(key, valueFor(key));
        }
        bh.consume(mutableMultimap);
    }

    @Benchmark
    public void removeSingle(Blackhole bh) {
        // Remove a key that is guaranteed to exist.
        int key = (int) (Math.random() * (PREPOPULATED_SIZE / 10));
        mutableMultimap.removeAll(key);
        bh.consume(mutableMultimap);
    }

    /* --------------------------------------------------------------------- */
    /* Read benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void getBag(Blackhole bh) {
        // Retrieve the bag for a random existing key.
        int key = (int) (Math.random() * (PREPOPULATED_SIZE / 10));
        bh.consume(readOnlyMultimap.get(key));
    }

    @Benchmark
    public void iterateAll(Blackhole bh) {
        // Iterate over all key/value pairs using the multimap's multi‑value iterator.
        readOnlyMultimap.forEachKeyMultiValues((k, bag) -> {
            bag.forEach(value -> {
                bh.consume(k);
                bh.consume(value);
            });
        });
    }

    @Benchmark
    public void flipMultimap(Blackhole bh) {
        // Flip creates a new multimap with keys/values swapped.
        bh.consume(readOnlyMultimap.flip());
    }
}
```

### Method 42

```java
package org.eclipse.collections.impl.multimap.bag.sorted.mutable;

import java.util.Comparator;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link TreeBagMultimap}.
 *
 * The benchmarks focus on the most common operations:
 * <ul>
 *   <li>put (single entry)</li>
 *   <li>putAll (bulk insertion)</li>
 *   <li>get (lookup of a bag)</li>
 *   <li>remove (single entry)</li>
 *   <li>iteration over all entries</li>
 *   <li>flip (key/value inversion)</li>
 * </ul>
 *
 * Throughput mode is used because typical library usage cares about the number of
 * operations per time unit rather than latency of a single call.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2)
@State(Scope.Thread)
public class TreeBagMultimapBenchmark {

    /**
     * Size of the pre‑populated multimap.
     */
    private static final int PREPOPULATED_SIZE = 10_000;

    /**
     * Number of entries added/removed per benchmark invocation.
     */
    private static final int BATCH_SIZE = 100;

    /**
     * The multimap used for read‑only benchmarks (get, iteration, flip).
     */
    private TreeBagMultimap<Integer, String> readOnlyMultimap;

    /**
     * The multimap used for write benchmarks (put, remove).
     */
    private TreeBagMultimap<Integer, String> mutableMultimap;

    /**
     * Comparator used for the value type (String).
     */
    private final Comparator<String> stringComparator = Comparator.naturalOrder();

    /**
     * Helper method to generate a deterministic value for a given key.
     */
    private static String valueFor(int key) {
        return "value-" + key;
    }

    @Setup(Level.Trial)
    public void setUp() {
        // Initialise a multimap with a deterministic distribution of keys/values.
        readOnlyMultimap = TreeBagMultimap.newMultimap(stringComparator);
        mutableMultimap = TreeBagMultimap.newMultimap(stringComparator);
        for (int i = 0; i < PREPOPULATED_SIZE; i++) {
            // 10 distinct keys, each with many values
            int key = i % (PREPOPULATED_SIZE / 10);
            String value = valueFor(i);
            readOnlyMultimap.put(key, value);
            mutableMultimap.put(key, value);
        }
    }

    /* --------------------------------------------------------------------- */
    /* Write benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void putSingle(Blackhole bh) {
        // Use a fresh key to avoid collisions that could bias the measurement.
        int key = PREPOPULATED_SIZE + (int) (Math.random() * BATCH_SIZE);
        String value = valueFor(key);
        mutableMultimap.put(key, value);
        // Prevent dead‑code elimination.
        bh.consume(mutableMultimap);
    }

    @Benchmark
    public void putBatch(Blackhole bh) {
        // Insert a batch of entries in a tight loop.
        for (int i = 0; i < BATCH_SIZE; i++) {
            int key = PREPOPULATED_SIZE + i;
            mutableMultimap.put(key, valueFor(key));
        }
        bh.consume(mutableMultimap);
    }

    @Benchmark
    public void removeSingle(Blackhole bh) {
        // Remove a key that is guaranteed to exist.
        int key = (int) (Math.random() * (PREPOPULATED_SIZE / 10));
        mutableMultimap.removeAll(key);
        bh.consume(mutableMultimap);
    }

    /* --------------------------------------------------------------------- */
    /* Read benchmarks */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void getBag(Blackhole bh) {
        // Retrieve the bag for a random existing key.
        int key = (int) (Math.random() * (PREPOPULATED_SIZE / 10));
        bh.consume(readOnlyMultimap.get(key));
    }

    @Benchmark
    public void iterateAll(Blackhole bh) {
        // Iterate over all key/value pairs using the multimap's multi‑value iterator.
        readOnlyMultimap.forEachKeyMultiValues((k, bag) -> {
            bag.forEach(value -> {
                bh.consume(k);
                bh.consume(value);
            });
        });
    }

    @Benchmark
    public void flipMultimap(Blackhole bh) {
        // Flip creates a new multimap with keys/values swapped.
        bh.consume(readOnlyMultimap.flip());
    }
}
```

### Method 43

```java
package org.eclipse.collections.impl.multimap.bag;

import java.io.*;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for the core operations of {@link AbstractMutableBagMultimap}
 * using the concrete {@link HashBagMultimap} implementation.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 3, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Thread)
public class AbstractMutableBagMultimapBenchmark {

    private static final int KEY_COUNT = 10_000;

    private static final int VALUES_PER_KEY = 10;

    private HashBagMultimap<Integer, Integer> mutableMultimap;

    private byte[] serializedForm;

    private int putKey;

    private int putValue;

    @Setup(Level.Trial)
    public void setUp() throws IOException {
        mutableMultimap = HashBagMultimap.newMultimap();
        for (int k = 0; k < KEY_COUNT; k++) {
            for (int v = 0; v < VALUES_PER_KEY; v++) {
                mutableMultimap.put(k, v);
            }
        }
        putKey = KEY_COUNT / 2;
        putValue = VALUES_PER_KEY / 2;
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
            mutableMultimap.writeExternal(oos);
        }
        serializedForm = baos.toByteArray();
    }

    @Benchmark
    public void benchmarkPutOccurrences(Blackhole bh) {
        mutableMultimap.putOccurrences(putKey, putValue, 1);
        bh.consume(mutableMultimap);
    }

    @Benchmark
    public void benchmarkToImmutable(Blackhole bh) {
        var immutable = mutableMultimap.toImmutable();
        bh.consume(immutable);
    }

    @Benchmark
    public void benchmarkCollectKeysValues(Blackhole bh) {
        var result = mutableMultimap.collectKeysValues((k, v) -> Tuples.pair(k, v));
        bh.consume(result);
    }

    @Benchmark
    public void benchmarkWriteExternal(Blackhole bh) throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
            mutableMultimap.writeExternal(oos);
        }
        bh.consume(baos.toByteArray());
    }

    @Benchmark
    public void benchmarkReadExternal(Blackhole bh) throws IOException, ClassNotFoundException {
        HashBagMultimap<Integer, Integer> newMap = HashBagMultimap.newMultimap();
        try (ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(serializedForm))) {
            newMap.readExternal(ois);
        }
        bh.consume(newMap);
    }
}
```

### Method 44

```java
package org.eclipse.collections.impl.multimap.bag;

import java.io.*;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for the core operations of {@link AbstractMutableBagMultimap}
 * using the concrete {@link HashBagMultimap} implementation.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 3, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Thread)
public class AbstractMutableBagMultimapBenchmark {

    private static final int KEY_COUNT = 10_000;

    private static final int VALUES_PER_KEY = 10;

    private HashBagMultimap<Integer, Integer> mutableMultimap;

    private byte[] serializedForm;

    private int putKey;

    private int putValue;

    @Setup(Level.Trial)
    public void setUp() throws IOException {
        mutableMultimap = HashBagMultimap.newMultimap();
        for (int k = 0; k < KEY_COUNT; k++) {
            for (int v = 0; v < VALUES_PER_KEY; v++) {
                mutableMultimap.put(k, v);
            }
        }
        putKey = KEY_COUNT / 2;
        putValue = VALUES_PER_KEY / 2;
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
            mutableMultimap.writeExternal(oos);
        }
        serializedForm = baos.toByteArray();
    }

    @Benchmark
    public void benchmarkPutOccurrences(Blackhole bh) {
        mutableMultimap.putOccurrences(putKey, putValue, 1);
        bh.consume(mutableMultimap);
    }

    @Benchmark
    public void benchmarkToImmutable(Blackhole bh) {
        var immutable = mutableMultimap.toImmutable();
        bh.consume(immutable);
    }

    @Benchmark
    public void benchmarkCollectKeysValues(Blackhole bh) {
        var result = mutableMultimap.collectKeysValues((k, v) -> Tuples.pair(k, v));
        bh.consume(result);
    }

    @Benchmark
    public void benchmarkWriteExternal(Blackhole bh) throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
            mutableMultimap.writeExternal(oos);
        }
        bh.consume(baos.toByteArray());
    }

    @Benchmark
    public void benchmarkReadExternal(Blackhole bh) throws IOException, ClassNotFoundException {
        HashBagMultimap<Integer, Integer> newMap = HashBagMultimap.newMultimap();
        try (ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(serializedForm))) {
            newMap.readExternal(ois);
        }
        bh.consume(newMap);
    }
}
```

### Method 45

```java
package org.eclipse.collections.impl.multimap.bag;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link HashBagMultimap}.
 *
 * The benchmarks focus on typical operations:
 * <ul>
 *   <li>put (single entry)</li>
 *   <li>flip (key/value inversion)</li>
 *   <li>collectValues (value transformation)</li>
 *   <li>selectKeysValues (filtering by predicate)</li>
 *   <li>rejectKeysValues (inverse filtering)</li>
 * </ul>
 *
 * Throughput mode is used to measure how many operations can be performed per time unit.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Thread)
public class HashBagMultimapBenchmark {

    private static final int ELEMENT_COUNT = 10_000;

    private Random random;

    private HashBagMultimap<Integer, String> multimap;

    private Function<String, String> toUpperCaseFunction;

    private Predicate2<Integer, String> evenKeyPredicate;

    @Setup(Level.Trial)
    public void setUp() {
        this.random = new Random(12345L);
        this.multimap = new HashBagMultimap<>();
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            int key = i % 100;
            String value = "value-" + i;
            this.multimap.put(key, value);
        }
        this.toUpperCaseFunction = String::toUpperCase;
        this.evenKeyPredicate = (key, value) -> (key & 1) == 0;
    }

    @TearDown(Level.Trial)
    public void tearDown() {
        this.multimap = null;
    }

    @Benchmark
    public void benchmarkPut() {
        int key = random.nextInt(1_000);
        String value = "new-" + random.nextInt();
        multimap.put(key, value);
    }

    @Benchmark
    public void benchmarkFlip(Blackhole bh) {
        bh.consume(multimap.flip());
    }

    @Benchmark
    public void benchmarkCollectValues(Blackhole bh) {
        bh.consume(multimap.collectValues(toUpperCaseFunction));
    }

    @Benchmark
    public void benchmarkSelectKeysValues(Blackhole bh) {
        bh.consume(multimap.selectKeysValues(evenKeyPredicate));
    }

    @Benchmark
    public void benchmarkRejectKeysValues(Blackhole bh) {
        bh.consume(multimap.rejectKeysValues(evenKeyPredicate));
    }
}
```

### Method 46

```java
package org.eclipse.collections.impl.multimap.bag;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@Threads(4)
@State(Scope.Benchmark)
public class SynchronizedPutHashBagMultimapBenchmark {

    private static final int KEY_RANGE = 1_000;

    private static final int VALUE_RANGE = 10_000;

    private static final int INITIAL_SIZE = 100_000;

    private SynchronizedPutHashBagMultimap<Integer, Integer> multimap;

    private Pair<Integer, Integer> samplePair;

    private int sampleKey;

    private int sampleValue;

    @Setup(Level.Trial)
    public void setUp() {
        multimap = SynchronizedPutHashBagMultimap.newMultimap();
        for (int i = 0; i < INITIAL_SIZE; i++) {
            int key = i % KEY_RANGE;
            int value = i % VALUE_RANGE;
            multimap.put(key, value);
        }
        sampleKey = KEY_RANGE / 2;
        sampleValue = VALUE_RANGE / 2;
        samplePair = Tuples.pair(sampleKey, sampleValue);
    }

    @Benchmark
    public void putSingle() {
        multimap.put(sampleKey, sampleValue);
    }

    @Benchmark
    public void putOccurrences() {
        multimap.putOccurrences(sampleKey, sampleValue, 3);
    }

    @Benchmark
    public void getBag() {
        multimap.get(sampleKey);
    }

    @Benchmark
    public void iterateAll() {
        multimap.forEachKeyMutableBag((k, bag) -> bag.forEach(v -> {
        }));
    }

    @Benchmark
    public void selectKeysValues() {
        multimap.selectKeysValues((k, v) -> (k & 1) == 0 && (v & 1) == 0);
    }

    @Benchmark
    public void collectValues() {
        multimap.collectValues(v -> v * v);
    }

    @Benchmark
    public void flip() {
        multimap.flip();
    }
}
```

### Method 47

```java
package org.eclipse.collections.impl.multimap.bag;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@Threads(4)
@State(Scope.Benchmark)
public class SynchronizedPutHashBagMultimapBenchmark {

    private static final int KEY_RANGE = 1_000;

    private static final int VALUE_RANGE = 10_000;

    private static final int INITIAL_SIZE = 100_000;

    private SynchronizedPutHashBagMultimap<Integer, Integer> multimap;

    private Pair<Integer, Integer> samplePair;

    private int sampleKey;

    private int sampleValue;

    @Setup(Level.Trial)
    public void setUp() {
        multimap = SynchronizedPutHashBagMultimap.newMultimap();
        for (int i = 0; i < INITIAL_SIZE; i++) {
            int key = i % KEY_RANGE;
            int value = i % VALUE_RANGE;
            multimap.put(key, value);
        }
        sampleKey = KEY_RANGE / 2;
        sampleValue = VALUE_RANGE / 2;
        samplePair = Tuples.pair(sampleKey, sampleValue);
    }

    @Benchmark
    public void putSingle() {
        multimap.put(sampleKey, sampleValue);
    }

    @Benchmark
    public void putOccurrences() {
        multimap.putOccurrences(sampleKey, sampleValue, 3);
    }

    @Benchmark
    public void getBag() {
        multimap.get(sampleKey);
    }

    @Benchmark
    public void iterateAll() {
        multimap.forEachKeyMutableBag((k, bag) -> bag.forEach(v -> {
        }));
    }

    @Benchmark
    public void selectKeysValues() {
        multimap.selectKeysValues((k, v) -> (k & 1) == 0 && (v & 1) == 0);
    }

    @Benchmark
    public void collectValues() {
        multimap.collectValues(v -> v * v);
    }

    @Benchmark
    public void flip() {
        multimap.flip();
    }
}
```

### Method 48

```java
package org.eclipse.collections.impl.multimap.bag;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@Threads(4)
@State(Scope.Benchmark)
public class SynchronizedPutHashBagMultimapBenchmark {

    private static final int KEY_RANGE = 1_000;

    private static final int VALUE_RANGE = 10_000;

    private static final int INITIAL_SIZE = 100_000;

    private SynchronizedPutHashBagMultimap<Integer, Integer> multimap;

    private Pair<Integer, Integer> samplePair;

    private int sampleKey;

    private int sampleValue;

    @Setup(Level.Trial)
    public void setUp() {
        multimap = SynchronizedPutHashBagMultimap.newMultimap();
        for (int i = 0; i < INITIAL_SIZE; i++) {
            int key = i % KEY_RANGE;
            int value = i % VALUE_RANGE;
            multimap.put(key, value);
        }
        sampleKey = KEY_RANGE / 2;
        sampleValue = VALUE_RANGE / 2;
        samplePair = Tuples.pair(sampleKey, sampleValue);
    }

    @Benchmark
    public void putSingle() {
        multimap.put(sampleKey, sampleValue);
    }

    @Benchmark
    public void putOccurrences() {
        multimap.putOccurrences(sampleKey, sampleValue, 3);
    }

    @Benchmark
    public void getBag() {
        multimap.get(sampleKey);
    }

    @Benchmark
    public void iterateAll() {
        multimap.forEachKeyMutableBag((k, bag) -> bag.forEach(v -> {
        }));
    }

    @Benchmark
    public void selectKeysValues() {
        multimap.selectKeysValues((k, v) -> (k & 1) == 0 && (v & 1) == 0);
    }

    @Benchmark
    public void collectValues() {
        multimap.collectValues(v -> v * v);
    }

    @Benchmark
    public void flip() {
        multimap.flip();
    }
}
```

### Method 49

```java
package org.eclipse.collections.impl.multimap.bag;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class MultiReaderHashBagMultimapBenchmark {

    private static final int KEY_RANGE = 100;

    private static final int ELEMENT_COUNT = 10_000;

    private MultiReaderHashBagMultimap<Integer, String> populatedMap;

    @Setup(Level.Trial)
    public void setUp() {
        populatedMap = MultiReaderHashBagMultimap.newMultimap();
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            populatedMap.put(i % KEY_RANGE, "value-" + i);
        }
    }

    @Benchmark
    public MultiReaderHashBagMultimap<Integer, String> putBenchmark() {
        MultiReaderHashBagMultimap<Integer, String> map = MultiReaderHashBagMultimap.newMultimap();
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            map.put(i % KEY_RANGE, "v-" + i);
        }
        return map;
    }

    @Benchmark
    public MultiReaderHashBagMultimap<Integer, String> collectValuesBenchmark() {
        return populatedMap.collectValues(v -> v + "-collected");
    }

    @Benchmark
    public MutableBagMultimap<String, Integer> flipBenchmark() {
        return populatedMap.flip();
    }

    @Benchmark
    public MultiReaderHashBagMultimap<Integer, String> selectKeysValuesBenchmark() {
        return populatedMap.selectKeysValues((k, v) -> k % 2 == 0);
    }

    @Benchmark
    public MultiReaderHashBagMultimap<Integer, String> rejectKeysValuesBenchmark() {
        return populatedMap.rejectKeysValues((k, v) -> k % 2 != 0);
    }

    @Benchmark
    public MultiReaderHashBagMultimap<Integer, String> selectKeysMultiValuesBenchmark() {
        return populatedMap.selectKeysMultiValues((k, values) -> k < 50);
    }

    @Benchmark
    public MultiReaderHashBagMultimap<Integer, String> rejectKeysMultiValuesBenchmark() {
        return populatedMap.rejectKeysMultiValues((k, values) -> k >= 50);
    }
}
```

### Method 50

```java
package org.eclipse.collections.impl.multimap.bag;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class MultiReaderHashBagMultimapBenchmark {

    private static final int KEY_RANGE = 100;

    private static final int ELEMENT_COUNT = 10_000;

    private MultiReaderHashBagMultimap<Integer, String> populatedMap;

    @Setup(Level.Trial)
    public void setUp() {
        populatedMap = MultiReaderHashBagMultimap.newMultimap();
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            populatedMap.put(i % KEY_RANGE, "value-" + i);
        }
    }

    @Benchmark
    public MultiReaderHashBagMultimap<Integer, String> putBenchmark() {
        MultiReaderHashBagMultimap<Integer, String> map = MultiReaderHashBagMultimap.newMultimap();
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            map.put(i % KEY_RANGE, "v-" + i);
        }
        return map;
    }

    @Benchmark
    public MultiReaderHashBagMultimap<Integer, String> collectValuesBenchmark() {
        return populatedMap.collectValues(v -> v + "-collected");
    }

    @Benchmark
    public MutableBagMultimap<String, Integer> flipBenchmark() {
        return populatedMap.flip();
    }

    @Benchmark
    public MultiReaderHashBagMultimap<Integer, String> selectKeysValuesBenchmark() {
        return populatedMap.selectKeysValues((k, v) -> k % 2 == 0);
    }

    @Benchmark
    public MultiReaderHashBagMultimap<Integer, String> rejectKeysValuesBenchmark() {
        return populatedMap.rejectKeysValues((k, v) -> k % 2 != 0);
    }

    @Benchmark
    public MultiReaderHashBagMultimap<Integer, String> selectKeysMultiValuesBenchmark() {
        return populatedMap.selectKeysMultiValues((k, values) -> k < 50);
    }

    @Benchmark
    public MultiReaderHashBagMultimap<Integer, String> rejectKeysMultiValuesBenchmark() {
        return populatedMap.rejectKeysMultiValues((k, values) -> k >= 50);
    }
}
```

### Method 51

```java
package org.eclipse.collections.impl.multimap.bag;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class TreeBagMultimapBenchmark {

    private static final int KEY_COUNT = 100;

    private static final int VALUE_COUNT = 10_000;

    private TreeBagMultimap<Integer, Integer> multimap;

    @Setup(Level.Trial)
    public void setUp() {
        multimap = new TreeBagMultimap<>();
        for (int i = 0; i < VALUE_COUNT; i++) {
            int key = i % KEY_COUNT;
            multimap.put(key, i);
        }
    }

    @Benchmark
    public void putNewMap(Blackhole bh) {
        TreeBagMultimap<Integer, Integer> map = new TreeBagMultimap<>();
        for (int i = 0; i < VALUE_COUNT; i++) {
            int key = i % KEY_COUNT;
            map.put(key, i);
        }
        bh.consume(map);
    }

    @Benchmark
    public void getValues(Blackhole bh) {
        for (int key = 0; key < KEY_COUNT; key++) {
            bh.consume(multimap.get(key));
        }
    }

    @Benchmark
    public void selectKeysValues(Blackhole bh) {
        TreeBagMultimap<Integer, Integer> selected = multimap.selectKeysValues((k, v) -> (k & 1) == 0 && (v & 1) == 0);
        bh.consume(selected);
    }

    @Benchmark
    public void rejectKeysValues(Blackhole bh) {
        TreeBagMultimap<Integer, Integer> rejected = multimap.rejectKeysValues((k, v) -> (k & 1) == 0 && (v & 1) == 0);
        bh.consume(rejected);
    }

    @Benchmark
    public void flip(Blackhole bh) {
        bh.consume(multimap.flip());
    }

    @Benchmark
    public void iterateAllValues(Blackhole bh) {
        multimap.forEachKeyValue((k, v) -> bh.consume(v));
    }

    @Benchmark
    public void toImmutable(Blackhole bh) {
        bh.consume(multimap.toImmutable());
    }

    @Benchmark
    public void asSynchronized(Blackhole bh) {
        bh.consume(multimap.asSynchronized());
    }
}
```

### Method 52

```java
package org.eclipse.collections.impl.multimap.bag;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class TreeBagMultimapBenchmark {

    private static final int KEY_COUNT = 100;

    private static final int VALUE_COUNT = 10_000;

    private TreeBagMultimap<Integer, Integer> multimap;

    @Setup(Level.Trial)
    public void setUp() {
        multimap = new TreeBagMultimap<>();
        for (int i = 0; i < VALUE_COUNT; i++) {
            int key = i % KEY_COUNT;
            multimap.put(key, i);
        }
    }

    @Benchmark
    public void putNewMap(Blackhole bh) {
        TreeBagMultimap<Integer, Integer> map = new TreeBagMultimap<>();
        for (int i = 0; i < VALUE_COUNT; i++) {
            int key = i % KEY_COUNT;
            map.put(key, i);
        }
        bh.consume(map);
    }

    @Benchmark
    public void getValues(Blackhole bh) {
        for (int key = 0; key < KEY_COUNT; key++) {
            bh.consume(multimap.get(key));
        }
    }

    @Benchmark
    public void selectKeysValues(Blackhole bh) {
        TreeBagMultimap<Integer, Integer> selected = multimap.selectKeysValues((k, v) -> (k & 1) == 0 && (v & 1) == 0);
        bh.consume(selected);
    }

    @Benchmark
    public void rejectKeysValues(Blackhole bh) {
        TreeBagMultimap<Integer, Integer> rejected = multimap.rejectKeysValues((k, v) -> (k & 1) == 0 && (v & 1) == 0);
        bh.consume(rejected);
    }

    @Benchmark
    public void flip(Blackhole bh) {
        bh.consume(multimap.flip());
    }

    @Benchmark
    public void iterateAllValues(Blackhole bh) {
        multimap.forEachKeyValue((k, v) -> bh.consume(v));
    }

    @Benchmark
    public void toImmutable(Blackhole bh) {
        bh.consume(multimap.toImmutable());
    }

    @Benchmark
    public void asSynchronized(Blackhole bh) {
        bh.consume(multimap.asSynchronized());
    }
}
```

### Method 53

```java
package org.eclipse.collections.impl.multimap.list;

import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 3, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Thread)
public class MultiReaderFastListMultimapBenchmark {

    /**
     * Number of distinct keys used for the initial population.
     */
    private static final int KEY_COUNT = 10_000;

    /**
     * Number of values per key for the initial population.
     */
    private static final int VALUES_PER_KEY = 10;

    /**
     * The multimap instance used in the benchmarks.
     */
    private MultiReaderFastListMultimap<Integer, Integer> multimap;

    /**
     * Pre‑generated keys for read‑only operations to avoid allocation overhead inside the benchmark.
     */
    private int[] keys;

    /**
     * Pre‑generated values for write operations.
     */
    private int[] values;

    @Setup(Level.Trial)
    public void setUp() {
        multimap = new MultiReaderFastListMultimap<>(KEY_COUNT, VALUES_PER_KEY);
        keys = new int[KEY_COUNT];
        values = new int[KEY_COUNT * VALUES_PER_KEY];
        int vIdx = 0;
        for (int i = 0; i < KEY_COUNT; i++) {
            keys[i] = i;
            for (int j = 0; j < VALUES_PER_KEY; j++) {
                values[vIdx++] = i * VALUES_PER_KEY + j;
                multimap.put(i, values[vIdx - 1]);
            }
        }
    }

    /**
     * Benchmark for a single put operation.
     */
    @Benchmark
    public void putOne(BenchmarkState state) {
        int key = ThreadLocalRandom.current().nextInt(KEY_COUNT);
        int value = ThreadLocalRandom.current().nextInt();
        state.multimap.put(key, value);
    }

    /**
     * Benchmark for retrieving the collection associated with a key.
     */
    @Benchmark
    public void get(BenchmarkState state) {
        int key = state.keys[ThreadLocalRandom.current().nextInt(KEY_COUNT)];
        state.multimap.get(key);
    }

    /**
     * Benchmark for selecting key‑value pairs where the key is even.
     */
    @Benchmark
    public void selectKeysValuesEven(BenchmarkState state) {
        state.multimap.selectKeysValues((k, v) -> (k & 1) == 0);
    }

    /**
     * Benchmark for rejecting key‑value pairs where the key is even.
     */
    @Benchmark
    public void rejectKeysValuesEven(BenchmarkState state) {
        state.multimap.rejectKeysValues((k, v) -> (k & 1) == 0);
    }

    /**
     * Benchmark for flipping the multimap (producing a bag‑multimap).
     */
    @Benchmark
    public void flip(BenchmarkState state) {
        state.multimap.flip();
    }

    /**
     * Benchmark for creating a new empty multimap.
     */
    @Benchmark
    public MultiReaderFastListMultimap<Integer, Integer> newEmpty(BenchmarkState state) {
        return state.multimap.newEmpty();
    }

    /**
     * State holder to avoid accidental sharing between benchmark methods.
     */
    @State(Scope.Thread)
    public static class BenchmarkState {

        MultiReaderFastListMultimap<Integer, Integer> multimap;

        int[] keys;

        @Setup(Level.Iteration)
        public void init() {
            // Clone the pre‑populated multimap for each iteration to keep the workload consistent.
            multimap = MultiReaderFastListMultimap.newMultimap();
            // Populate with the same deterministic data as the trial setup.
            for (int i = 0; i < MultiReaderFastListMultimapBenchmark.KEY_COUNT; i++) {
                for (int j = 0; j < MultiReaderFastListMultimapBenchmark.VALUES_PER_KEY; j++) {
                    multimap.put(i, i * MultiReaderFastListMultimapBenchmark.VALUES_PER_KEY + j);
                }
            }
            keys = new int[MultiReaderFastListMultimapBenchmark.KEY_COUNT];
            for (int i = 0; i < keys.length; i++) {
                keys[i] = i;
            }
        }
    }
}
```

### Method 54

```java
package org.eclipse.collections.impl.multimap.list;

import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 3, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Thread)
public class MultiReaderFastListMultimapBenchmark {

    /**
     * Number of distinct keys used for the initial population.
     */
    private static final int KEY_COUNT = 10_000;

    /**
     * Number of values per key for the initial population.
     */
    private static final int VALUES_PER_KEY = 10;

    /**
     * The multimap instance used in the benchmarks.
     */
    private MultiReaderFastListMultimap<Integer, Integer> multimap;

    /**
     * Pre‑generated keys for read‑only operations to avoid allocation overhead inside the benchmark.
     */
    private int[] keys;

    /**
     * Pre‑generated values for write operations.
     */
    private int[] values;

    @Setup(Level.Trial)
    public void setUp() {
        multimap = new MultiReaderFastListMultimap<>(KEY_COUNT, VALUES_PER_KEY);
        keys = new int[KEY_COUNT];
        values = new int[KEY_COUNT * VALUES_PER_KEY];
        int vIdx = 0;
        for (int i = 0; i < KEY_COUNT; i++) {
            keys[i] = i;
            for (int j = 0; j < VALUES_PER_KEY; j++) {
                values[vIdx++] = i * VALUES_PER_KEY + j;
                multimap.put(i, values[vIdx - 1]);
            }
        }
    }

    /**
     * Benchmark for a single put operation.
     */
    @Benchmark
    public void putOne(BenchmarkState state) {
        int key = ThreadLocalRandom.current().nextInt(KEY_COUNT);
        int value = ThreadLocalRandom.current().nextInt();
        state.multimap.put(key, value);
    }

    /**
     * Benchmark for retrieving the collection associated with a key.
     */
    @Benchmark
    public void get(BenchmarkState state) {
        int key = state.keys[ThreadLocalRandom.current().nextInt(KEY_COUNT)];
        state.multimap.get(key);
    }

    /**
     * Benchmark for selecting key‑value pairs where the key is even.
     */
    @Benchmark
    public void selectKeysValuesEven(BenchmarkState state) {
        state.multimap.selectKeysValues((k, v) -> (k & 1) == 0);
    }

    /**
     * Benchmark for rejecting key‑value pairs where the key is even.
     */
    @Benchmark
    public void rejectKeysValuesEven(BenchmarkState state) {
        state.multimap.rejectKeysValues((k, v) -> (k & 1) == 0);
    }

    /**
     * Benchmark for flipping the multimap (producing a bag‑multimap).
     */
    @Benchmark
    public void flip(BenchmarkState state) {
        state.multimap.flip();
    }

    /**
     * Benchmark for creating a new empty multimap.
     */
    @Benchmark
    public MultiReaderFastListMultimap<Integer, Integer> newEmpty(BenchmarkState state) {
        return state.multimap.newEmpty();
    }

    /**
     * State holder to avoid accidental sharing between benchmark methods.
     */
    @State(Scope.Thread)
    public static class BenchmarkState {

        MultiReaderFastListMultimap<Integer, Integer> multimap;

        int[] keys;

        @Setup(Level.Iteration)
        public void init() {
            // Clone the pre‑populated multimap for each iteration to keep the workload consistent.
            multimap = MultiReaderFastListMultimap.newMultimap();
            // Populate with the same deterministic data as the trial setup.
            for (int i = 0; i < MultiReaderFastListMultimapBenchmark.KEY_COUNT; i++) {
                for (int j = 0; j < MultiReaderFastListMultimapBenchmark.VALUES_PER_KEY; j++) {
                    multimap.put(i, i * MultiReaderFastListMultimapBenchmark.VALUES_PER_KEY + j);
                }
            }
            keys = new int[MultiReaderFastListMultimapBenchmark.KEY_COUNT];
            for (int i = 0; i < keys.length; i++) {
                keys[i] = i;
            }
        }
    }
}
```

### Method 55

```java
package org.eclipse.collections.impl.multimap.list;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link SynchronizedPutFastListMultimap}.
 * The benchmarks focus on typical operations: put, get, iteration,
 * select/reject, collect, and flip. Throughput mode is used to measure
 * operations per time unit.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class SynchronizedPutFastListMultimapBenchmark {

    private static final int SIZE = 10_000;

    private SynchronizedPutFastListMultimap<Integer, String> multimap;

    private Pair<Integer, String>[] pairs;

    private Integer lookupKey;

    @SuppressWarnings("unchecked")
    @Setup(Level.Trial)
    public void setUp() {
        // Prepare a multimap filled with deterministic data
        multimap = SynchronizedPutFastListMultimap.newMultimap();
        pairs = new Pair[SIZE];
        for (int i = 0; i < SIZE; i++) {
            // some key collisions to create multi‑values
            int key = i % 1000;
            String value = "value-" + i;
            pairs[i] = Tuples.pair(key, value);
            multimap.put(key, value);
        }
        // Choose a key that is guaranteed to exist for get/iteration benchmarks
        lookupKey = 42;
    }

    @Benchmark
    public void benchmarkPut(Blackhole bh) {
        // Each iteration adds a new entry; the key is chosen to cause contention
        int key = (int) (Math.random() * 1000);
        String value = "new-" + System.nanoTime();
        multimap.put(key, value);
        bh.consume(multimap);
    }

    @Benchmark
    public void benchmarkGet(Blackhole bh) {
        // Retrieve the list of values for a known key
        bh.consume(multimap.get(lookupKey));
    }

    @Benchmark
    public void benchmarkIteration(Blackhole bh) {
        // Iterate over all entries
        multimap.forEachKeyMutableList((k, list) -> {
            bh.consume(k);
            bh.consume(list);
        });
    }

    @Benchmark
    public void benchmarkSelectKeysValues(Blackhole bh) {
        // Select entries where key is even
        var selected = multimap.selectKeysValues((k, v) -> (k & 1) == 0);
        bh.consume(selected);
    }

    @Benchmark
    public void benchmarkRejectKeysValues(Blackhole bh) {
        // Reject entries where key is even
        var rejected = multimap.rejectKeysValues((k, v) -> (k & 1) == 0);
        bh.consume(rejected);
    }

    @Benchmark
    public void benchmarkCollectValues(Blackhole bh) {
        // Transform values to their length
        var collected = multimap.collectValues(String::length);
        bh.consume(collected);
    }

    @Benchmark
    public void benchmarkFlip(Blackhole bh) {
        // Flip key/value direction
        var flipped = multimap.flip();
        bh.consume(flipped);
    }
}
```

### Method 56

```java
package org.eclipse.collections.impl.multimap.set.sorted;

import java.util.Comparator;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Thread)
public class SynchronizedPutTreeSortedSetMultimapBenchmark {

    private static final int SIZE = 10_000;

    private static final int BATCH = 100;

    private SynchronizedPutTreeSortedSetMultimap<Integer, Integer> multimap;

    private final Comparator<Integer> comparator = Comparator.naturalOrder();

    @Setup(Level.Trial)
    public void setUp() {
        multimap = SynchronizedPutTreeSortedSetMultimap.newMultimap(comparator);
        for (int i = 0; i < SIZE; i++) {
            multimap.put(i % (SIZE / 10), i);
        }
    }

    @Benchmark
    public void putSingle() {
        multimap.put(SIZE, SIZE);
        multimap.remove(SIZE, SIZE);
    }

    @Benchmark
    public void putBatch() {
        for (int i = 0; i < BATCH; i++) {
            multimap.put(i, i);
        }
        for (int i = 0; i < BATCH; i++) {
            multimap.remove(i, i);
        }
    }

    @Benchmark
    public void getValues() {
        multimap.get(SIZE / 2);
    }

    @Benchmark
    public void removeSingle() {
        multimap.removeAll(SIZE / 3);
        multimap.put(SIZE / 3, SIZE);
    }

    @Benchmark
    public void iterateAll() {
        multimap.forEachKeyMultiValues((k, values) -> values.forEach(v -> {
            int dummy = v;
        }));
    }

    @Benchmark
    public void toMutable() {
        multimap.toMutable();
    }

    @Benchmark
    public void selectKeysValues() {
        multimap.selectKeysValues((k, v) -> k % 2 == 0);
    }

    @Benchmark
    public void rejectKeysValues() {
        multimap.rejectKeysValues((k, v) -> k % 2 != 0);
    }
}
```

### Method 57

```java
package org.eclipse.collections.impl.multimap.set.sorted;

import java.util.Comparator;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Thread)
public class SynchronizedPutTreeSortedSetMultimapBenchmark {

    private static final int SIZE = 10_000;

    private static final int BATCH = 100;

    private SynchronizedPutTreeSortedSetMultimap<Integer, Integer> multimap;

    private final Comparator<Integer> comparator = Comparator.naturalOrder();

    @Setup(Level.Trial)
    public void setUp() {
        multimap = SynchronizedPutTreeSortedSetMultimap.newMultimap(comparator);
        for (int i = 0; i < SIZE; i++) {
            multimap.put(i % (SIZE / 10), i);
        }
    }

    @Benchmark
    public void putSingle() {
        multimap.put(SIZE, SIZE);
        multimap.remove(SIZE, SIZE);
    }

    @Benchmark
    public void putBatch() {
        for (int i = 0; i < BATCH; i++) {
            multimap.put(i, i);
        }
        for (int i = 0; i < BATCH; i++) {
            multimap.remove(i, i);
        }
    }

    @Benchmark
    public void getValues() {
        multimap.get(SIZE / 2);
    }

    @Benchmark
    public void removeSingle() {
        multimap.removeAll(SIZE / 3);
        multimap.put(SIZE / 3, SIZE);
    }

    @Benchmark
    public void iterateAll() {
        multimap.forEachKeyMultiValues((k, values) -> values.forEach(v -> {
            int dummy = v;
        }));
    }

    @Benchmark
    public void toMutable() {
        multimap.toMutable();
    }

    @Benchmark
    public void selectKeysValues() {
        multimap.selectKeysValues((k, v) -> k % 2 == 0);
    }

    @Benchmark
    public void rejectKeysValues() {
        multimap.rejectKeysValues((k, v) -> k % 2 != 0);
    }
}
```

### Method 58

```java
package org.eclipse.collections.impl.multimap.set.sorted;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Thread)
public class SynchronizedSortedSetMultimapBenchmark {

    private static final String KEY = "key";

    private static final String[] VALUES = { "v1", "v2", "v3", "v4", "v5" };

    private MutableSortedSetMultimap<String, String> unsynchronized;

    private SynchronizedSortedSetMultimap<String, String> synchronizedMap;

    @Setup(Level.Trial)
    public void setUp() {
        // unsynchronized baseline
        unsynchronized = TreeSortedSetMultimap.newMultimap();
        // pre‑populate with some data
        for (int i = 0; i < 1000; i++) {
            unsynchronized.withKeyMultiValues("key" + i, VALUES);
        }
        // synchronized wrapper around a fresh multimap (populated the same way)
        MutableSortedSetMultimap<String, String> delegate = TreeSortedSetMultimap.newMultimap();
        for (int i = 0; i < 1000; i++) {
            delegate.withKeyMultiValues("key" + i, VALUES);
        }
        synchronizedMap = SynchronizedSortedSetMultimap.of(delegate);
    }

    /* --------------------------------------------------------------------- */
    /* Baseline (unsynchronized) benchmarks                                   */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public MutableSortedSet<String> baseline_get() {
        return unsynchronized.get(KEY);
    }

    @Benchmark
    public MutableSortedSetMultimap<String, String> baseline_put() {
        return unsynchronized.withKeyMultiValues(KEY, VALUES);
    }

    @Benchmark
    public MutableSortedSet<String> baseline_removeAll() {
        return unsynchronized.removeAll(KEY);
    }

    /* --------------------------------------------------------------------- */
    /* Synchronized wrapper benchmarks                                        */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public MutableSortedSet<String> sync_get() {
        return synchronizedMap.get(KEY);
    }

    @Benchmark
    public MutableSortedSetMultimap<String, String> sync_put() {
        return synchronizedMap.withKeyMultiValues(KEY, VALUES);
    }

    @Benchmark
    public MutableSortedSet<String> sync_removeAll() {
        return synchronizedMap.removeAll(KEY);
    }
}
```

### Method 59

```java
package org.eclipse.collections.impl.multimap.set.strategy;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link UnifiedSetWithHashingStrategyMultimap}.
 *
 * The benchmarks focus on the most common operations:
 * <ul>
 *   <li>put (insertion)</li>
 *   <li>get (lookup)</li>
 *   <li>flip (key/value inversion)</li>
 *   <li>selectKeysValues (filtering)</li>
 *   <li>rejectKeysValues (filtering)</li>
 * </ul>
 *
 * All benchmarks run in {@link Mode#Throughput} to measure operations per time unit.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Thread)
public class UnifiedSetWithHashingStrategyMultimapBenchmark {

    /**
     * Number of distinct keys in the pre‑populated multimap.
     */
    private static final int KEY_COUNT = 10_000;

    /**
     * Number of values per key in the pre‑populated multimap.
     */
    private static final int VALUES_PER_KEY = 10;

    /**
     * Simple null‑safe hashing strategy based on {@link Object#hashCode()} and {@link Object#equals(Object)}.
     */
    private static final HashingStrategy<Object> DEFAULT_HASHING_STRATEGY = new HashingStrategy<Object>() {

        @Override
        public int computeHashCode(Object object) {
            return object == null ? 0 : object.hashCode();
        }

        @Override
        public boolean equals(Object o1, Object o2) {
            return o1 == null ? o2 == null : o1.equals(o2);
        }
    };

    /**
     * Multimap used for read‑only benchmarks (get, flip, select, reject).
     */
    private UnifiedSetWithHashingStrategyMultimap<Integer, Integer> readOnlyMultimap;

    /**
     * Multimap used for write‑only benchmark (put).
     */
    private UnifiedSetWithHashingStrategyMultimap<Integer, Integer> writeMultimap;

    /**
     * Random generator for keys/values.
     */
    private Random random;

    /**
     * Counter used to generate unique keys for the put benchmark.
     */
    private int putCounter;

    @Setup(Level.Trial)
    public void setUp() {
        random = new Random(12345L);
        // Populate a multimap with a deterministic data set.
        readOnlyMultimap = new UnifiedSetWithHashingStrategyMultimap<>(DEFAULT_HASHING_STRATEGY);
        for (int k = 0; k < KEY_COUNT; k++) {
            for (int v = 0; v < VALUES_PER_KEY; v++) {
                readOnlyMultimap.put(k, k * VALUES_PER_KEY + v);
            }
        }
        // Clone the read‑only map for write benchmark to avoid interference.
        writeMultimap = new UnifiedSetWithHashingStrategyMultimap<>(DEFAULT_HASHING_STRATEGY);
        readOnlyMultimap.forEachKeyValue((k, v) -> writeMultimap.put(k, v));
        putCounter = KEY_COUNT * VALUES_PER_KEY;
    }

    /* --------------------------------------------------------------------- */
    /* Write benchmark: insertion of a new (key, value) pair.               */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void benchmarkPut() {
        int key = random.nextInt(KEY_COUNT);
        int value = putCounter++;
        writeMultimap.put(key, value);
    }

    /* --------------------------------------------------------------------- */
    /* Read benchmark: lookup of the value set for a random key.            */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void benchmarkGet() {
        int key = random.nextInt(KEY_COUNT);
        // Iterate to prevent dead‑code elimination.
        readOnlyMultimap.get(key).forEach(v -> {
            // no‑op
        });
    }

    /* --------------------------------------------------------------------- */
    /* Flip benchmark: invert key/value mapping.                            */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void benchmarkFlip() {
        // Result is discarded; we only measure the operation.
        readOnlyMultimap.flip();
    }

    /* --------------------------------------------------------------------- */
    /* Select benchmark: keep only entries where key is even.               */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void benchmarkSelectKeysValues() {
        Predicate2<Integer, Integer> predicate = (k, v) -> (k & 1) == 0;
        readOnlyMultimap.selectKeysValues(predicate);
    }

    /* --------------------------------------------------------------------- */
    /* Reject benchmark: discard entries where key is odd.                  */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void benchmarkRejectKeysValues() {
        Predicate2<Integer, Integer> predicate = (k, v) -> (k & 1) != 0;
        readOnlyMultimap.rejectKeysValues(predicate);
    }
}
```

### Method 60

```java
package org.eclipse.collections.impl.multimap.set.strategy;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link UnifiedSetWithHashingStrategyMultimap}.
 *
 * The benchmarks focus on the most common operations:
 * <ul>
 *   <li>put (insertion)</li>
 *   <li>get (lookup)</li>
 *   <li>flip (key/value inversion)</li>
 *   <li>selectKeysValues (filtering)</li>
 *   <li>rejectKeysValues (filtering)</li>
 * </ul>
 *
 * All benchmarks run in {@link Mode#Throughput} to measure operations per time unit.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Thread)
public class UnifiedSetWithHashingStrategyMultimapBenchmark {

    /**
     * Number of distinct keys in the pre‑populated multimap.
     */
    private static final int KEY_COUNT = 10_000;

    /**
     * Number of values per key in the pre‑populated multimap.
     */
    private static final int VALUES_PER_KEY = 10;

    /**
     * Simple null‑safe hashing strategy based on {@link Object#hashCode()} and {@link Object#equals(Object)}.
     */
    private static final HashingStrategy<Object> DEFAULT_HASHING_STRATEGY = new HashingStrategy<Object>() {

        @Override
        public int computeHashCode(Object object) {
            return object == null ? 0 : object.hashCode();
        }

        @Override
        public boolean equals(Object o1, Object o2) {
            return o1 == null ? o2 == null : o1.equals(o2);
        }
    };

    /**
     * Multimap used for read‑only benchmarks (get, flip, select, reject).
     */
    private UnifiedSetWithHashingStrategyMultimap<Integer, Integer> readOnlyMultimap;

    /**
     * Multimap used for write‑only benchmark (put).
     */
    private UnifiedSetWithHashingStrategyMultimap<Integer, Integer> writeMultimap;

    /**
     * Random generator for keys/values.
     */
    private Random random;

    /**
     * Counter used to generate unique keys for the put benchmark.
     */
    private int putCounter;

    @Setup(Level.Trial)
    public void setUp() {
        random = new Random(12345L);
        // Populate a multimap with a deterministic data set.
        readOnlyMultimap = new UnifiedSetWithHashingStrategyMultimap<>(DEFAULT_HASHING_STRATEGY);
        for (int k = 0; k < KEY_COUNT; k++) {
            for (int v = 0; v < VALUES_PER_KEY; v++) {
                readOnlyMultimap.put(k, k * VALUES_PER_KEY + v);
            }
        }
        // Clone the read‑only map for write benchmark to avoid interference.
        writeMultimap = new UnifiedSetWithHashingStrategyMultimap<>(DEFAULT_HASHING_STRATEGY);
        readOnlyMultimap.forEachKeyValue((k, v) -> writeMultimap.put(k, v));
        putCounter = KEY_COUNT * VALUES_PER_KEY;
    }

    /* --------------------------------------------------------------------- */
    /* Write benchmark: insertion of a new (key, value) pair.               */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void benchmarkPut() {
        int key = random.nextInt(KEY_COUNT);
        int value = putCounter++;
        writeMultimap.put(key, value);
    }

    /* --------------------------------------------------------------------- */
    /* Read benchmark: lookup of the value set for a random key.            */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void benchmarkGet() {
        int key = random.nextInt(KEY_COUNT);
        // Iterate to prevent dead‑code elimination.
        readOnlyMultimap.get(key).forEach(v -> {
            // no‑op
        });
    }

    /* --------------------------------------------------------------------- */
    /* Flip benchmark: invert key/value mapping.                            */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void benchmarkFlip() {
        // Result is discarded; we only measure the operation.
        readOnlyMultimap.flip();
    }

    /* --------------------------------------------------------------------- */
    /* Select benchmark: keep only entries where key is even.               */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void benchmarkSelectKeysValues() {
        Predicate2<Integer, Integer> predicate = (k, v) -> (k & 1) == 0;
        readOnlyMultimap.selectKeysValues(predicate);
    }

    /* --------------------------------------------------------------------- */
    /* Reject benchmark: discard entries where key is odd.                  */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void benchmarkRejectKeysValues() {
        Predicate2<Integer, Integer> predicate = (k, v) -> (k & 1) != 0;
        readOnlyMultimap.rejectKeysValues(predicate);
    }
}
```

### Method 61

```java
package org.eclipse.collections.impl.multimap.set;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Thread)
public class AbstractMutableSetMultimapBenchmark {

    private static final int SIZE = 10_000;

    private MutableSetMultimap<Integer, Integer> multimap;

    @Setup(Level.Trial)
    public void setUp() {
        multimap = UnifiedSetMultimap.newMultimap();
        for (int i = 0; i < SIZE; i++) {
            // each key maps to a small set of values to exercise set semantics
            multimap.put(i % 1000, i);
            multimap.put(i % 1000, i + SIZE);
        }
    }

    @Benchmark
    public MutableSetMultimap<Integer, Integer> benchmarkToMutable() {
        // toMutable creates a new UnifiedSetMultimap copy
        return multimap.toMutable();
    }

    @Benchmark
    public Object benchmarkToImmutable() {
        // toImmutable returns an immutable view; we treat it as Object to avoid pulling in the concrete type
        return multimap.toImmutable();
    }

    @Benchmark
    public void benchmarkForEachKeyMutableSet() {
        // iterate over each key and its mutable set (as unmodifiable)
        multimap.forEachKeyMutableSet((key, set) -> {
            // simple consumption to prevent dead code elimination
            int size = set.size();
            if (size < 0) {
                throw new AssertionError();
            }
        });
    }

    @Benchmark
    public Object benchmarkCollectKeysValues() {
        // transform each (key, value) pair into a new pair
        return multimap.collectKeysValues((key, value) -> Tuples.pair(key * 2, value + 1));
    }

    @Benchmark
    public Object benchmarkCollectKeyMultiValues() {
        // map keys and values independently using lambda expressions
        return multimap.collectKeyMultiValues(key -> key * 3, value -> value + 5);
    }

    @Benchmark
    public Object benchmarkCollectValues() {
        // transform only the values using a lambda expression
        return multimap.collectValues(value -> value + 10);
    }

    @Benchmark
    public MutableSetMultimap<Integer, Integer> benchmarkAsSynchronized() {
        // obtain a synchronized wrapper
        return multimap.asSynchronized();
    }
}
```

### Method 62

```java
package org.eclipse.collections.impl.parallel;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.block.function.primitive.DoubleFunction;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2, jvmArgsAppend = { "-XX:+UseParallelGC" })
@State(Scope.Benchmark)
public class ParallelIterateBenchmark {

    private static final int ELEMENT_COUNT = 1_000_000;

    private List<Integer> intList;

    private List<BigDecimal> bigDecimalList;

    private static final Predicate<Integer> ALWAYS_TRUE = each -> true;

    private static final Procedure<Integer> NOOP_PROCEDURE = each -> {
        /* no‑op */
    };

    private static final DoubleFunction<Integer> TO_DOUBLE = Integer::doubleValue;

    private static final Function<Integer, Integer> IDENTITY = each -> each;

    private static final Function<BigDecimal, BigDecimal> BD_IDENTITY = each -> each;

    // fixed
    private static final Function0<BigDecimal> ZERO_BD = Functions0.zeroBigDecimal();

    private static final Function2<BigDecimal, BigDecimal, BigDecimal> ADD_BD = (sum, each) -> sum.add(each);

    @Setup(Level.Trial)
    public void setUp() {
        intList = new ArrayList<>(ELEMENT_COUNT);
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            intList.add(i);
        }
        bigDecimalList = new ArrayList<>(ELEMENT_COUNT);
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            bigDecimalList.add(BigDecimal.valueOf(i));
        }
    }

    @Benchmark
    public void parallelForEach() {
        ParallelIterate.forEach(intList, NOOP_PROCEDURE);
    }

    @Benchmark
    public void parallelSumByDouble() {
        ParallelIterate.sumByDouble(intList, IDENTITY, TO_DOUBLE);
    }

    @Benchmark
    public void parallelCollect() {
        ParallelIterate.collect(intList, IDENTITY);
    }

    @Benchmark
    public void parallelAggregateByBigDecimal() {
        ParallelIterate.aggregateBy(bigDecimalList, BD_IDENTITY, ZERO_BD, ADD_BD);
    }

    @Benchmark
    public void parallelGroupBy() {
        // Use a thread‑safe multimap for parallel execution
        MutableMultimap<Integer, Integer> multimap = Multimaps.mutable.list.<Integer, Integer>empty().asSynchronized();
        ParallelIterate.groupBy(intList, IDENTITY, multimap, ParallelIterate.DEFAULT_MIN_FORK_SIZE);
    }

    @Benchmark
    public void parallelSelect() {
        ParallelIterate.select(intList, ALWAYS_TRUE);
    }

    @Benchmark
    public void parallelReject() {
        ParallelIterate.reject(intList, ALWAYS_TRUE);
    }
}
```

### Method 63

```java
package org.eclipse.collections.impl.set.immutable;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2)
@Threads(1)
public class ImmutableUnifiedSetBenchmark {

    @State(Scope.Benchmark)
    public static class BenchmarkState {

        /**
         * Size of the test set – large enough to expose realistic collection behavior.
         */
        private static final int ELEMENT_COUNT = 10_000;

        /**
         * Immutable set under test (concrete type needed for batchForEach).
         */
        ImmutableUnifiedSet<Integer> immutableSet;

        /**
         * Executor used for parallel operations.
         */
        ExecutorService executor;

        /**
         * Simple procedure used for each/batchForEach.
         */
        Procedure<Integer> blackholeProcedure;

        @Setup(Level.Trial)
        public void setUp() {
            // Populate a mutable UnifiedSet and wrap it as immutable.
            Integer[] data = new Integer[ELEMENT_COUNT];
            for (int i = 0; i < ELEMENT_COUNT; i++) {
                data[i] = i;
            }
            // newSetWith returns ImmutableSet, cast to concrete type for batchForEach access.
            immutableSet = (ImmutableUnifiedSet<Integer>) ImmutableUnifiedSet.newSetWith(data);
            // Fixed thread pool for parallel benchmarks (size equals available processors).
            executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
            // No‑op procedure; traversal overhead is what we measure.
            blackholeProcedure = element -> {
                // intentionally empty
            };
        }

        @TearDown(Level.Trial)
        public void tearDown() throws InterruptedException {
            executor.shutdownNow();
            executor.awaitTermination(5, TimeUnit.SECONDS);
        }
    }

    /* --------------------------------------------------------------------- */
    /* Simple read‑only operations                                            */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public int size(BenchmarkState state) {
        return state.immutableSet.size();
    }

    @Benchmark
    public boolean contains(BenchmarkState state) {
        // Probe a value that is guaranteed to be present.
        return state.immutableSet.contains(state.immutableSet.getFirst());
    }

    @Benchmark
    public Integer getFirst(BenchmarkState state) {
        return state.immutableSet.getFirst();
    }

    @Benchmark
    public Integer getLast(BenchmarkState state) {
        return state.immutableSet.getLast();
    }

    @Benchmark
    public Integer getOnly(BenchmarkState state) {
        // Guard against IllegalStateException for sets larger than one element.
        if (state.immutableSet.size() == 1) {
            return state.immutableSet.getOnly();
        }
        return null;
    }

    /* --------------------------------------------------------------------- */
    /* Traversal benchmarks                                                   */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void iteratorTraversal(BenchmarkState state) {
        var iterator = state.immutableSet.iterator();
        while (iterator.hasNext()) {
            iterator.next();
        }
    }

    @Benchmark
    public void eachTraversal(BenchmarkState state) {
        state.immutableSet.each(state.blackholeProcedure);
    }

    /* --------------------------------------------------------------------- */
    /* Parallel traversal benchmarks                                          */
    /* --------------------------------------------------------------------- */
    @Benchmark
    public void asParallelTraversal(BenchmarkState state) throws Exception {
        int batchSize = 256;
        var parallelIterable = state.immutableSet.asParallel(state.executor, batchSize);
        parallelIterable.forEach(state.blackholeProcedure);
    }

    @Benchmark
    public void batchForEachTraversal(BenchmarkState state) {
        // Single batch traversal (equivalent to a full iteration).
        state.immutableSet.batchForEach(state.blackholeProcedure, 0, 1);
    }
}
```

### Method 64

```java
package org.eclipse.collections.impl.set.mutable;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.ThreadLocalRandom;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link UnifiedSet}.
 *
 * The benchmarks focus on the most common operations:
 * - {@code add}
 * - {@code contains}
 * - {@code remove}
 * - iteration via {@code forEach}
 *
 * Best‑practice JMH settings are used:
 * - Warm‑up and measurement iterations
 * - Multiple forks
 * - Throughput mode (operations per time unit)
 * - Blackhole to avoid dead‑code elimination
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 7, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 3, jvmArgsAppend = { "-XX:+UseG1GC", "-Xms2G", "-Xmx2G" })
@State(Scope.Thread)
public class UnifiedSetBenchmark {

    /**
     * Number of elements used for the pre‑filled set.
     */
    private static final int ELEMENT_COUNT = 1_000_000;

    /**
     * Pre‑filled set used for read‑only operations (contains, iteration).
     */
    private UnifiedSet<Integer> filledSet;

    /**
     * Array of random keys used for contains / remove benchmarks.
     */
    private int[] randomKeys;

    /**
     * Empty set used for the add benchmark (re‑used to avoid allocation overhead).
     */
    private UnifiedSet<Integer> emptySet;

    @Setup(Level.Trial)
    public void setUp() {
        // Initialise a filled set with sequential integers.
        filledSet = new UnifiedSet<>(ELEMENT_COUNT);
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            filledSet.add(i);
        }
        // Prepare a shuffled array of keys for random access patterns.
        randomKeys = new int[ELEMENT_COUNT];
        for (int i = 0; i < ELEMENT_COUNT; i++) {
            randomKeys[i] = i;
        }
        // Simple Fisher‑Yates shuffle.
        ThreadLocalRandom rnd = ThreadLocalRandom.current();
        for (int i = ELEMENT_COUNT - 1; i > 0; i--) {
            int j = rnd.nextInt(i + 1);
            int tmp = randomKeys[i];
            randomKeys[i] = randomKeys[j];
            randomKeys[j] = tmp;
        }
        // Empty set for the add benchmark; capacity is pre‑allocated to avoid rehashing.
        emptySet = new UnifiedSet<>(ELEMENT_COUNT);
    }

    /**
     * Benchmark for {@code UnifiedSet.add(Object)}.
     */
    @Benchmark
    public void add(Blackhole bh) {
        // Add a random element and immediately remove it to keep the set size stable.
        int key = ThreadLocalRandom.current().nextInt(ELEMENT_COUNT * 10);
        boolean added = emptySet.add(key);
        bh.consume(added);
        // Remove the element to restore the original state.
        emptySet.remove(key);
    }

    /**
     * Benchmark for {@code UnifiedSet.contains(Object)}.
     */
    @Benchmark
    public void contains(Blackhole bh) {
        // Randomly pick a key from the pre‑generated array.
        int idx = ThreadLocalRandom.current().nextInt(ELEMENT_COUNT);
        int key = randomKeys[idx];
        boolean result = filledSet.contains(key);
        bh.consume(result);
    }

    /**
     * Benchmark for {@code UnifiedSet.remove(Object)}.
     */
    @Benchmark
    public void remove(Blackhole bh) {
        // Remove a random element, then re‑insert it to keep the set size constant.
        int key = ThreadLocalRandom.current().nextInt(ELEMENT_COUNT * 10);
        // Ensure the key is present before removal.
        filledSet.add(key);
        boolean removed = filledSet.remove(key);
        bh.consume(removed);
    }

    /**
     * Benchmark for iterating over the set using {@code forEach}.
     */
    @Benchmark
    public void forEach(Blackhole bh) {
        filledSet.forEach(bh::consume);
    }
}
```

### Method 65

```java
package org.eclipse.collections.impl.set.sorted.immutable;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.block.function.primitive.ObjectIntToObjectFunction;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
@State(Scope.Benchmark)
public class ImmutableTreeSetBenchmark {

    private static final int SIZE = 10_000;

    private SortedSetIterable<Integer> set;

    private SortedSetIterable<Integer> emptySet;

    private ExecutorService executorService;

    @Setup(Level.Trial)
    public void setUp() {
        Integer[] data = new Integer[SIZE];
        for (int i = 0; i < SIZE; i++) {
            data[i] = i;
        }
        set = ImmutableTreeSet.newSetWith(data);
        emptySet = ImmutableTreeSet.newSetWith();
        executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown(Level.Trial)
    public void tearDown() throws InterruptedException {
        executorService.shutdownNow();
        executorService.awaitTermination(5, TimeUnit.SECONDS);
    }

    // -----------------------------------------------------------------
    // Basic read‑only operations
    // -----------------------------------------------------------------
    @Benchmark
    public boolean containsExisting() {
        return set.contains(SIZE / 2);
    }

    @Benchmark
    public boolean containsMissing() {
        return set.contains(-1);
    }

    @Benchmark
    public int size() {
        return set.size();
    }

    @Benchmark
    public Integer first() {
        return set.min();
    }

    @Benchmark
    public Integer last() {
        return set.max();
    }

    @Benchmark
    public void iteratorConsume() {
        set.iterator().forEachRemaining(e -> {
            /* no‑op */
        });
    }

    @Benchmark
    public void eachConsume() {
        set.each(e -> {
            /* no‑op */
        });
    }

    // -----------------------------------------------------------------
    // Transformations
    // -----------------------------------------------------------------
    @Benchmark
    public SortedSetIterable<Integer> takeHalf() {
        return set.take(SIZE / 2);
    }

    @Benchmark
    public SortedSetIterable<Integer> dropHalf() {
        return set.drop(SIZE / 2);
    }

    @Benchmark
    public void collectWithIndex() {
        ObjectIntToObjectFunction<Integer, String> func = (value, index) -> value + ":" + index;
        set.collectWithIndex(func);
    }

    // -----------------------------------------------------------------
    // Parallel iteration (creation only – actual work is delegated to JMH threads)
    // -----------------------------------------------------------------
    @Benchmark
    public void asParallel() {
        set.asParallel(executorService, 1024);
    }

    // -----------------------------------------------------------------
    // Predicate based operations
    // -----------------------------------------------------------------
    private static final Predicate<Integer> IS_EVEN = i -> i % 2 == 0;

    @Benchmark
    public boolean anySatisfyEven() {
        return set.anySatisfy(IS_EVEN);
    }

    @Benchmark
    public boolean allSatisfyEven() {
        return set.allSatisfy(IS_EVEN);
    }

    @Benchmark
    public int countEven() {
        return set.count(IS_EVEN);
    }
}
```

### Method 66

```java
package org.eclipse.collections.impl.set.sorted.mutable;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link TreeSortedSet}.
 * Measures throughput of common operations: add, contains, iteration.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2)
@State(Scope.Thread)
public class TreeSortedSetBenchmark {

    /**
     * Size of the pre‑populated set used for read‑only benchmarks.
     */
    private static final int PREPOPULATED_SIZE = 10_000;

    /**
     * Number of elements added in the add‑benchmark per operation.
     */
    private static final int ADD_BATCH_SIZE = 100;

    private TreeSortedSet<Integer> prepopulatedSet;

    private TreeSortedSet<Integer> mutableSetForAdd;

    private Random random;

    @Setup(Level.Trial)
    public void setUp() {
        random = new Random(12345L);
        prepopulatedSet = TreeSortedSet.newSet();
        for (int i = 0; i < PREPOPULATED_SIZE; i++) {
            prepopulatedSet.add(i);
        }
        // a fresh set for each add benchmark iteration to avoid unbounded growth
        mutableSetForAdd = TreeSortedSet.newSet();
    }

    @Setup(Level.Iteration)
    public void resetAddSet() {
        // Ensure the add benchmark works on an empty set each iteration
        mutableSetForAdd.clear();
    }

    /**
     * Benchmark for {@code add} – adds a batch of random integers.
     */
    @Benchmark
    public void addElements(Blackhole bh) {
        for (int i = 0; i < ADD_BATCH_SIZE; i++) {
            int value = random.nextInt(Integer.MAX_VALUE);
            mutableSetForAdd.add(value);
        }
        // Prevent dead‑code elimination
        bh.consume(mutableSetForAdd);
    }

    /**
     * Benchmark for {@code contains} – checks random elements against a pre‑populated set.
     */
    @Benchmark
    public void containsElements(Blackhole bh) {
        // some misses
        int value = random.nextInt(PREPOPULATED_SIZE * 2);
        boolean result = prepopulatedSet.contains(value);
        bh.consume(result);
    }

    /**
     * Benchmark for iterating over the whole set.
     */
    @Benchmark
    public void iterateElements(Blackhole bh) {
        for (Integer i : prepopulatedSet) {
            bh.consume(i);
        }
    }

    /**
     * Benchmark for {@code remove} – removes random elements from a mutable copy of the pre‑populated set.
     */
    @Benchmark
    public void removeElements(Blackhole bh) {
        // Work on a copy to keep the original set unchanged across iterations
        TreeSortedSet<Integer> copy = TreeSortedSet.newSet(prepopulatedSet);
        int value = random.nextInt(PREPOPULATED_SIZE);
        boolean removed = copy.remove(value);
        bh.consume(removed);
    }
}
```

### Method 67

```java
package org.eclipse.collections.impl.set.sorted.mutable;

import java.util.Random;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link TreeSortedSet}.
 * Measures throughput of common operations: add, contains, iteration.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2)
@State(Scope.Thread)
public class TreeSortedSetBenchmark {

    /**
     * Size of the pre‑populated set used for read‑only benchmarks.
     */
    private static final int PREPOPULATED_SIZE = 10_000;

    /**
     * Number of elements added in the add‑benchmark per operation.
     */
    private static final int ADD_BATCH_SIZE = 100;

    private TreeSortedSet<Integer> prepopulatedSet;

    private TreeSortedSet<Integer> mutableSetForAdd;

    private Random random;

    @Setup(Level.Trial)
    public void setUp() {
        random = new Random(12345L);
        prepopulatedSet = TreeSortedSet.newSet();
        for (int i = 0; i < PREPOPULATED_SIZE; i++) {
            prepopulatedSet.add(i);
        }
        // a fresh set for each add benchmark iteration to avoid unbounded growth
        mutableSetForAdd = TreeSortedSet.newSet();
    }

    @Setup(Level.Iteration)
    public void resetAddSet() {
        // Ensure the add benchmark works on an empty set each iteration
        mutableSetForAdd.clear();
    }

    /**
     * Benchmark for {@code add} – adds a batch of random integers.
     */
    @Benchmark
    public void addElements(Blackhole bh) {
        for (int i = 0; i < ADD_BATCH_SIZE; i++) {
            int value = random.nextInt(Integer.MAX_VALUE);
            mutableSetForAdd.add(value);
        }
        // Prevent dead‑code elimination
        bh.consume(mutableSetForAdd);
    }

    /**
     * Benchmark for {@code contains} – checks random elements against a pre‑populated set.
     */
    @Benchmark
    public void containsElements(Blackhole bh) {
        // some misses
        int value = random.nextInt(PREPOPULATED_SIZE * 2);
        boolean result = prepopulatedSet.contains(value);
        bh.consume(result);
    }

    /**
     * Benchmark for iterating over the whole set.
     */
    @Benchmark
    public void iterateElements(Blackhole bh) {
        for (Integer i : prepopulatedSet) {
            bh.consume(i);
        }
    }

    /**
     * Benchmark for {@code remove} – removes random elements from a mutable copy of the pre‑populated set.
     */
    @Benchmark
    public void removeElements(Blackhole bh) {
        // Work on a copy to keep the original set unchanged across iterations
        TreeSortedSet<Integer> copy = TreeSortedSet.newSet(prepopulatedSet);
        int value = random.nextInt(PREPOPULATED_SIZE);
        boolean removed = copy.remove(value);
        bh.consume(removed);
    }
}
```

### Method 68

```java
package org.eclipse.collections.impl.set.strategy.mutable;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link UnifiedSetWithHashingStrategy}.
 *
 * The benchmarks focus on the most common operations:
 * - add
 * - contains
 * - get
 * - remove
 * - iteration (forEach)
 *
 * A simple integer hashing strategy is used to keep the benchmark deterministic.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2, jvmArgsAppend = { "-XX:+UseG1GC", "-Xms2G", "-Xmx2G" })
@State(Scope.Thread)
public class UnifiedSetWithHashingStrategyBenchmark {

    private static final int ELEMENT_COUNT = 100_000;

    private static final int KEY_RANGE = ELEMENT_COUNT * 10;

    /**
     * Simple hashing strategy for {@code Integer}.
     */
    public static class SimpleIntHashingStrategy implements HashingStrategy<Integer> {

        @Override
        public int computeHashCode(Integer object) {
            // Use the raw int value as hash code (identity hash) to avoid extra indirections.
            return object == null ? 0 : object.intValue();
        }

        @Override
        public boolean equals(Integer one, Integer two) {
            return one == null ? two == null : one.equals(two);
        }
    }

    @State(Scope.Thread)
    public static class BenchmarkState {

        UnifiedSetWithHashingStrategy<Integer> set;

        // pre‑generated keys for contains/get
        int[] keys;

        // keys that are not yet in the set (used for add)
        int[] newKeys;

        // keys that will be removed (used for remove)
        int[] removeKeys;

        // required for asParallel() benchmark (optional)
        ExecutorService executor;

        @Setup(Level.Trial)
        public void setUp() {
            // Initialise the set with a deterministic hashing strategy.
            HashingStrategy<Integer> strategy = new SimpleIntHashingStrategy();
            set = new UnifiedSetWithHashingStrategy<>(strategy);
            // Pre‑populate the set.
            for (int i = 0; i < ELEMENT_COUNT; i++) {
                set.add(i);
            }
            // Prepare key arrays.
            keys = new int[ELEMENT_COUNT];
            for (int i = 0; i < ELEMENT_COUNT; i++) {
                keys[i] = i;
            }
            // Keys that are guaranteed to be absent initially.
            newKeys = new int[ELEMENT_COUNT];
            for (int i = 0; i < ELEMENT_COUNT; i++) {
                newKeys[i] = KEY_RANGE + i;
            }
            // Keys that will be removed (use a subset to keep the set size stable).
            removeKeys = new int[ELEMENT_COUNT / 10];
            for (int i = 0; i < removeKeys.length; i++) {
                // spaced keys to avoid clustering.
                removeKeys[i] = i * 10;
            }
            // Executor for parallel benchmarks (if needed later).
            executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        }

        @TearDown(Level.Trial)
        public void tearDown() {
            executor.shutdownNow();
        }
    }

    @Benchmark
    public void benchmarkAdd(BenchmarkState state, Blackhole bh) {
        // Add a new element that is not present in the set.
        // Use modulo to wrap around the array and avoid unbounded growth.
        int idx = (int) (System.nanoTime() % state.newKeys.length);
        int key = state.newKeys[idx];
        boolean added = state.set.add(key);
        // Consume the result to prevent dead‑code elimination.
        bh.consume(added);
        // Remove the key again to keep the set size constant for subsequent iterations.
        state.set.remove(key);
    }

    @Benchmark
    public void benchmarkContains(BenchmarkState state, Blackhole bh) {
        // Check for an element that is definitely present.
        int idx = (int) (System.nanoTime() % state.keys.length);
        int key = state.keys[idx];
        boolean contains = state.set.contains(key);
        bh.consume(contains);
    }

    @Benchmark
    public void benchmarkGet(BenchmarkState state, Blackhole bh) {
        // Retrieve an element that is present.
        int idx = (int) (System.nanoTime() % state.keys.length);
        int key = state.keys[idx];
        Integer value = state.set.get(key);
        bh.consume(value);
    }

    @Benchmark
    public void benchmarkRemove(BenchmarkState state, Blackhole bh) {
        // Remove an element and immediately re‑add it to keep the set size stable.
        int idx = (int) (System.nanoTime() % state.removeKeys.length);
        int key = state.removeKeys[idx];
        Integer removed = state.set.removeFromPool(key);
        bh.consume(removed);
        // Re‑add the same key so that subsequent iterations see the same state.
        state.set.add(key);
    }

    @Benchmark
    public void benchmarkIteration(BenchmarkState state, Blackhole bh) {
        // Iterate over the set using the built‑in forEach method.
        state.set.forEach(element -> bh.consume(element));
    }

    // Optional: benchmark the parallel forEach to illustrate the parallel API.
    @Benchmark
    public void benchmarkParallelIteration(BenchmarkState state, Blackhole bh) {
        ExecutorService exec = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        try {
            state.set.asParallel(exec, 10_000).forEach(element -> bh.consume(element));
        } finally {
            exec.shutdownNow();
        }
    }
}
```

### Method 69

```java
package org.eclipse.collections.impl.set.strategy.mutable;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link UnifiedSetWithHashingStrategy}.
 *
 * The benchmarks focus on the most common operations:
 * - add
 * - contains
 * - get
 * - remove
 * - iteration (forEach)
 *
 * A simple integer hashing strategy is used to keep the benchmark deterministic.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2, jvmArgsAppend = { "-XX:+UseG1GC", "-Xms2G", "-Xmx2G" })
@State(Scope.Thread)
public class UnifiedSetWithHashingStrategyBenchmark {

    private static final int ELEMENT_COUNT = 100_000;

    private static final int KEY_RANGE = ELEMENT_COUNT * 10;

    /**
     * Simple hashing strategy for {@code Integer}.
     */
    public static class SimpleIntHashingStrategy implements HashingStrategy<Integer> {

        @Override
        public int computeHashCode(Integer object) {
            // Use the raw int value as hash code (identity hash) to avoid extra indirections.
            return object == null ? 0 : object.intValue();
        }

        @Override
        public boolean equals(Integer one, Integer two) {
            return one == null ? two == null : one.equals(two);
        }
    }

    @State(Scope.Thread)
    public static class BenchmarkState {

        UnifiedSetWithHashingStrategy<Integer> set;

        // pre‑generated keys for contains/get
        int[] keys;

        // keys that are not yet in the set (used for add)
        int[] newKeys;

        // keys that will be removed (used for remove)
        int[] removeKeys;

        // required for asParallel() benchmark (optional)
        ExecutorService executor;

        @Setup(Level.Trial)
        public void setUp() {
            // Initialise the set with a deterministic hashing strategy.
            HashingStrategy<Integer> strategy = new SimpleIntHashingStrategy();
            set = new UnifiedSetWithHashingStrategy<>(strategy);
            // Pre‑populate the set.
            for (int i = 0; i < ELEMENT_COUNT; i++) {
                set.add(i);
            }
            // Prepare key arrays.
            keys = new int[ELEMENT_COUNT];
            for (int i = 0; i < ELEMENT_COUNT; i++) {
                keys[i] = i;
            }
            // Keys that are guaranteed to be absent initially.
            newKeys = new int[ELEMENT_COUNT];
            for (int i = 0; i < ELEMENT_COUNT; i++) {
                newKeys[i] = KEY_RANGE + i;
            }
            // Keys that will be removed (use a subset to keep the set size stable).
            removeKeys = new int[ELEMENT_COUNT / 10];
            for (int i = 0; i < removeKeys.length; i++) {
                // spaced keys to avoid clustering.
                removeKeys[i] = i * 10;
            }
            // Executor for parallel benchmarks (if needed later).
            executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        }

        @TearDown(Level.Trial)
        public void tearDown() {
            executor.shutdownNow();
        }
    }

    @Benchmark
    public void benchmarkAdd(BenchmarkState state, Blackhole bh) {
        // Add a new element that is not present in the set.
        // Use modulo to wrap around the array and avoid unbounded growth.
        int idx = (int) (System.nanoTime() % state.newKeys.length);
        int key = state.newKeys[idx];
        boolean added = state.set.add(key);
        // Consume the result to prevent dead‑code elimination.
        bh.consume(added);
        // Remove the key again to keep the set size constant for subsequent iterations.
        state.set.remove(key);
    }

    @Benchmark
    public void benchmarkContains(BenchmarkState state, Blackhole bh) {
        // Check for an element that is definitely present.
        int idx = (int) (System.nanoTime() % state.keys.length);
        int key = state.keys[idx];
        boolean contains = state.set.contains(key);
        bh.consume(contains);
    }

    @Benchmark
    public void benchmarkGet(BenchmarkState state, Blackhole bh) {
        // Retrieve an element that is present.
        int idx = (int) (System.nanoTime() % state.keys.length);
        int key = state.keys[idx];
        Integer value = state.set.get(key);
        bh.consume(value);
    }

    @Benchmark
    public void benchmarkRemove(BenchmarkState state, Blackhole bh) {
        // Remove an element and immediately re‑add it to keep the set size stable.
        int idx = (int) (System.nanoTime() % state.removeKeys.length);
        int key = state.removeKeys[idx];
        Integer removed = state.set.removeFromPool(key);
        bh.consume(removed);
        // Re‑add the same key so that subsequent iterations see the same state.
        state.set.add(key);
    }

    @Benchmark
    public void benchmarkIteration(BenchmarkState state, Blackhole bh) {
        // Iterate over the set using the built‑in forEach method.
        state.set.forEach(element -> bh.consume(element));
    }

    // Optional: benchmark the parallel forEach to illustrate the parallel API.
    @Benchmark
    public void benchmarkParallelIteration(BenchmarkState state, Blackhole bh) {
        ExecutorService exec = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        try {
            state.set.asParallel(exec, 10_000).forEach(element -> bh.consume(element));
        } finally {
            exec.shutdownNow();
        }
    }
}
```

### Method 70

```java
package org.eclipse.collections.impl.stack.immutable;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link ImmutableArrayStack}.
 *
 * The benchmarks focus on the most common operations:
 *   - push
 *   - pop
 *   - peek
 *   - iteration (for‑each)
 *   - select (filter)
 *
 * Best‑practice JMH settings are used:
 *   • Warm‑up and measurement phases
 *   • Single fork (adjustable)
 *   • Throughput mode (operations per time unit)
 *   • Blackhole to avoid dead‑code elimination
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@Threads(1)
@State(Scope.Thread)
public class ImmutableArrayStackBenchmark {

    /**
     * Size of the pre‑populated stack for the benchmarks.
     */
    private static final int STACK_SIZE = 1_000;

    /**
     * The stack used for read‑only operations (peek, iteration, select).
     */
    private ImmutableStack<Integer> baseStack;

    /**
     * A fresh stack for push/pop benchmarks (re‑created each iteration).
     */
    private ImmutableStack<Integer> mutableStack;

    @Setup(Level.Trial)
    public void setUp() {
        // Populate a stack with sequential integers [0, STACK_SIZE)
        Integer[] elements = new Integer[STACK_SIZE];
        for (int i = 0; i < STACK_SIZE; i++) {
            elements[i] = i;
        }
        baseStack = ImmutableArrayStack.newStackWith(elements);
    }

    @Setup(Level.Iteration)
    public void setUpIteration() {
        // For push/pop we start from the same base stack each iteration
        mutableStack = baseStack;
    }

    /**
     * Benchmark the immutable {@code push} operation.
     */
    @Benchmark
    public ImmutableStack<Integer> push(Blackhole bh) {
        ImmutableStack<Integer> result = mutableStack.push(-1);
        bh.consume(result);
        return result;
    }

    /**
     * Benchmark the immutable {@code pop} operation.
     */
    @Benchmark
    public ImmutableStack<Integer> pop(Blackhole bh) {
        // Ensure we have at least one element to pop
        ImmutableStack<Integer> result = mutableStack.pop();
        bh.consume(result);
        return result;
    }

    /**
     * Benchmark the {@code peek} operation (read‑only).
     */
    @Benchmark
    public Integer peek(Blackhole bh) {
        Integer top = baseStack.peek();
        bh.consume(top);
        return top;
    }

    /**
     * Benchmark iterating over the stack using the enhanced for‑loop.
     */
    @Benchmark
    public void iterate(Blackhole bh) {
        for (Integer i : baseStack) {
            bh.consume(i);
        }
    }

    /**
     * Benchmark the {@code select} operation with a simple predicate.
     */
    @Benchmark
    public ImmutableStack<Integer> selectEven(Blackhole bh) {
        ImmutableStack<Integer> result = baseStack.select(i -> (i & 1) == 0);
        bh.consume(result);
        return result;
    }
}
```

### Method 71

```java
package org.eclipse.collections.impl.stack.mutable;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2)
public class ArrayStackBenchmark {

    /**
     * Size of the pre‑filled stack for pop/peek benchmarks.
     */
    private static final int PRE_FILL_SIZE = 1_000;

    /**
     * Element used for push benchmark.
     */
    private static final Integer PUSH_ELEMENT = 42;

    /**
     * Stack used for push benchmark – a fresh instance per invocation.
     */
    @State(Scope.Thread)
    public static class PushState {

        ArrayStack<Integer> stack;

        @Setup(Level.Invocation)
        public void setUp() {
            stack = new ArrayStack<>();
        }
    }

    /**
     * Stack used for pop/peek benchmarks – pre‑filled once per thread.
     */
    @State(Scope.Thread)
    public static class PopPeekState {

        ArrayStack<Integer> stack;

        @Setup(Level.Trial)
        public void setUp() {
            stack = new ArrayStack<>(PRE_FILL_SIZE);
            for (int i = 0; i < PRE_FILL_SIZE; i++) {
                stack.push(i);
            }
        }

        /**
         * Reset the stack to its original size after each pop to keep throughput stable.
         */
        @TearDown(Level.Invocation)
        public void reset() {
            while (stack.size() < PRE_FILL_SIZE) {
                stack.push(stack.size());
            }
        }
    }

    /**
     * Benchmark the push operation (throughput of pushes per millisecond).
     */
    @Benchmark
    public void push(PushState state) {
        state.stack.push(PUSH_ELEMENT);
    }

    /**
     * Benchmark the pop operation (throughput of pops per millisecond).
     */
    @Benchmark
    public void pop(PopPeekState state) {
        state.stack.pop();
    }

    /**
     * Benchmark the peek operation (throughput of peeks per millisecond).
     */
    @Benchmark
    public Integer peek(PopPeekState state) {
        return state.stack.peek();
    }

    /**
     * Benchmark the size operation (throughput of size queries per millisecond).
     */
    @Benchmark
    public int size(PopPeekState state) {
        return state.stack.size();
    }
}
```

### Method 72

```java
package org.eclipse.collections.impl.utility;

import java.util.ArrayList;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link ArrayListIterate}.
 *
 * The benchmarks focus on the most frequently used operations:
 * <ul>
 *   <li>{@code select}</li>
 *   <li>{@code count}</li>
 *   <li>{@code collect}</li>
 *   <li>{@code forEach}</li>
 *   <li>{@code injectInto}</li>
 * </ul>
 *
 * All benchmarks run in {@link Mode#Throughput} to measure operations per second.
 * Warm‑up and measurement iterations are chosen to give stable results on typical CI hardware.
 */
@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 7, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
public class ArrayListIterateBenchmark {

    private static final int LIST_SIZE = 10_000;

    private ArrayList<Integer> sourceList;

    private Predicate<Integer> evenPredicate;

    private Function<Integer, Integer> squareFunction;

    private Procedure<Integer> sumProcedure;

    private int sumResult;

    @Setup
    public void setUp() {
        sourceList = new ArrayList<>(LIST_SIZE);
        for (int i = 0; i < LIST_SIZE; i++) {
            sourceList.add(i);
        }
        evenPredicate = i -> i % 2 == 0;
        squareFunction = i -> i * i;
        sumProcedure = each -> sumResult += each;
    }

    @Benchmark
    public ArrayList<Integer> benchSelect() {
        // Select even numbers
        return ArrayListIterate.select(sourceList, evenPredicate);
    }

    @Benchmark
    public int benchCount() {
        // Count even numbers
        return ArrayListIterate.count(sourceList, evenPredicate);
    }

    @Benchmark
    public ArrayList<Integer> benchCollect() {
        // Collect squares of each element
        return ArrayListIterate.collect(sourceList, squareFunction);
    }

    @Benchmark
    public void benchForEach() {
        // Simple forEach that sums the elements (side‑effect stored in a field to avoid dead‑code elimination)
        sumResult = 0;
        ArrayListIterate.forEach(sourceList, sumProcedure);
    }

    @Benchmark
    public int benchInjectInto() {
        // Sum all elements using injectInto
        return ArrayListIterate.injectInto(0, sourceList, (Integer acc, Integer each) -> acc + each);
    }
}
```

### Method 73

```java
package org.eclipse.collections.impl.utility;

import java.util.Map;
import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Benchmark)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public class MapIterateBenchmark {

    private static final int SIZE = 10_000;

    private Map<Integer, Integer> mutableMap;

    private ImmutableMap<Integer, Integer> immutableMap;

    @Setup(Level.Trial)
    public void setUp() {
        UnifiedMap<Integer, Integer> map = UnifiedMap.newMap(SIZE);
        for (int i = 0; i < SIZE; i++) {
            map.put(i, i);
        }
        this.mutableMap = map;
        this.immutableMap = org.eclipse.collections.impl.factory.Maps.immutable.withAll(map);
    }

    @Benchmark
    public MutableList<Integer> selectValues() {
        Predicate<Integer> isEven = Predicates.attributePredicate(i -> i % 2, Predicates.equal(0));
        return MapIterate.select(mutableMap, isEven);
    }

    @Benchmark
    public MutableList<Integer> collectValues() {
        Function<Integer, Integer> identity = i -> i;
        return MapIterate.collect(mutableMap, identity);
    }

    @Benchmark
    public void forEachValue() {
        Procedure<Integer> sumProcedure = new Procedure<Integer>() {

            private long sum = 0;

            @Override
            public void value(Integer value) {
                sum += value;
            }
        };
        MapIterate.forEachValue(mutableMap, sumProcedure);
    }

    @Benchmark
    public Integer getIfAbsentPut() {
        Function0<Integer> supplier = () -> -1;
        int absentKey = SIZE + 1;
        return MapIterate.getIfAbsentPut(mutableMap, absentKey, supplier);
    }

    @Benchmark
    public Map<Integer, Integer> collectPairs() {
        Function2<Integer, Integer, Pair<Integer, Integer>> pairFunction = (k, v) -> Tuples.pair(k, v);
        return MapIterate.collect(mutableMap, pairFunction);
    }

    @Benchmark
    public Integer detectValue() {
        Predicate<Integer> isZero = i -> i == 0;
        return MapIterate.detect(mutableMap, isZero);
    }

    @Benchmark
    public Map<Integer, Integer> reverseMapping() {
        return MapIterate.reverseMapping(mutableMap);
    }
}
```

## JMH LOOP INSIDE BENCHMARK - Usage of loops in the JMH benchmark function.

### Method 1

```java
/* ---------- Iteration benchmarks ---------- */
@Benchmark
public long iterateMutableForEach() {
    long sum = 0;
    for (int i : mutableList) {
        sum += i;
    }
    return sum;
}
```

### Method 2

```java
/* ---------------- Iteration over entrySet ---------------- */
@Benchmark
public long unsync_iteration() {
    long sum = 0;
    for (Map.Entry<Integer, Integer> entry : unsynchronizedMap.entrySet()) {
        sum += entry.getKey() + entry.getValue();
    }
    return sum;
}
```

### Method 3

```java
/* -------------------- Iteration via primitive iterator -------------------- */
@Benchmark
public void iterateWithIntIteratorSmall(Blackhole bh) {
    var it = smallInterval.intIterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 4

```java
/* ------------------------------------- */
/* Serialization benchmarks */
/* ------------------------------------- */
@Benchmark
public byte[] serializeAdapter() throws IOException {
    try (ByteArrayOutputStream bos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(bos)) {
        oos.writeObject(freshAdapter);
        oos.flush();
        return bos.toByteArray();
    }
}
```

### Method 5

```java
/* --------------------------------------------------------------------- */
/* Benchmark: raw iteration using the Java enhanced for‑loop.           */
/* --------------------------------------------------------------------- */
@Benchmark
public void iterateForEach(Blackhole bh) {
    for (Integer i : composite) {
        bh.consume(i);
    }
}
```

### Method 6

```java
/* --------------------------------------------------------------------- */
/* Iteration                                                             */
/* --------------------------------------------------------------------- */
@Benchmark
public void iterate(Blackhole bh) {
    for (Integer i : doubletonSet) {
        bh.consume(i);
    }
}
```

### Method 7

```java
/* --------------------------------------------------------------------- */
/* Traversal benchmarks                                                   */
/* --------------------------------------------------------------------- */
@Benchmark
public void iteratorTraversal(BenchmarkState state) {
    var iterator = state.immutableSet.iterator();
    while (iterator.hasNext()) {
        iterator.next();
    }
}
```

### Method 8

```java
/* ---------------------------------------------------------------------- */
/* Benchmarks */
/* ---------------------------------------------------------------------- */
@Benchmark
public void benchmarkCharAt(Blackhole bh) {
    for (int idx : randomIndices) {
        bh.consume(codePointList.charAt(idx));
    }
}
```

### Method 9

```java
/**
 * Benchmark for adding a batch of elements.
 */
@Benchmark
public void addBatch() {
    for (int i = 0; i < BATCH_SIZE; i++) {
        mutableBag.add(randomValues[i]);
    }
}
```

### Method 10

```java
/**
 * Benchmark for iterating over entries.
 */
@Benchmark
public long iterateEntries() {
    long sum = 0;
    for (Pair<Integer, String> entry : map.keyValuesView()) {
        sum += entry.getOne() + entry.getTwo().length();
    }
    return sum;
}
```

### Method 11

```java
/**
 * Benchmark for iterating over the whole bag using the iterator.
 */
@Benchmark
public long iterate() {
    long sum = 0L;
    for (Integer i : prepopulatedBag) {
        sum += i;
    }
    // return to prevent dead‑code elimination
    return sum;
}
```

### Method 12

```java
/**
 * Benchmark for iterating over the whole set.
 */
@Benchmark
public void iterateElements(Blackhole bh) {
    for (Integer i : prepopulatedSet) {
        bh.consume(i);
    }
}
```

### Method 13

```java
/**
 * Benchmark for iterating over values.
 */
@Benchmark
public long iterateValues() {
    long sum = 0;
    for (String v : map.values()) {
        sum += v.length();
    }
    return sum;
}
```

### Method 14

```java
/**
 * Benchmark for iterating over {@code entrySet()} and consuming each entry.
 */
@Benchmark
public void benchEntrySetIteration(Blackhole bh) {
    // The entrySet is immutable; iterating over it should be cheap.
    for (var entry : immutableMap.entrySet()) {
        bh.consume(entry.getKey());
        bh.consume(entry.getValue());
    }
}
```

### Method 15

```java
/**
 * Benchmark for removing a batch of elements that are known to exist.
 */
@Benchmark
public void removeBatch() {
    // Ensure we have enough elements to remove; if not, repopulate
    if (mutableBag.size() < BATCH_SIZE) {
        mutableBag.clear();
        for (int i = 0; i < PREPOPULATED_SIZE; i++) {
            mutableBag.add(i);
        }
    }
    for (int i = 0; i < BATCH_SIZE; i++) {
        mutableBag.remove(randomValues[i]);
    }
}
```

### Method 16

```java
/**
 * Benchmark for removing a batch of elements that are known to exist.
 */
@Benchmark
public void removeBatch() {
    // Ensure we have enough elements to remove; if not, repopulate
    if (mutableBag.size() < BATCH_SIZE) {
        mutableBag.clear();
        for (int i = 0; i < PREPOPULATED_SIZE; i++) {
            mutableBag.add(i);
        }
    }
    for (int i = 0; i < BATCH_SIZE; i++) {
        mutableBag.remove(randomValues[i]);
    }
}
```

### Method 17

```java
/**
 * Benchmark for the clear operation.
 */
@Benchmark
public void clear() {
    map.clear();
    // Re‑populate to keep other benchmarks meaningful.
    for (int i = 0; i < SIZE; i++) {
        map.put(keys[i], values[i]);
    }
}
```

### Method 18

```java
/**
 * Benchmark for {@code add} – adds a batch of random integers.
 */
@Benchmark
public void addElements(Blackhole bh) {
    for (int i = 0; i < ADD_BATCH_SIZE; i++) {
        int value = random.nextInt(Integer.MAX_VALUE);
        mutableSetForAdd.add(value);
    }
    // Prevent dead‑code elimination
    bh.consume(mutableSetForAdd);
}
```

### Method 19

```java
/**
 * Benchmark for {@link FlatCollectIterable#iterator()}.
 */
@Benchmark
public long benchmarkIterator(Blackhole bh) {
    long sum = 0;
    for (Integer v : flatCollect) {
        sum += v;
    }
    bh.consume(sum);
    return sum;
}
```

### Method 20

```java
/**
 * Benchmark iterating over the filtered iterable using its iterator.
 */
@Benchmark
public void iteratorTraversal(Blackhole bh) {
    for (Integer i : selectIterable) {
        bh.consume(i);
    }
}
```

### Method 21

```java
/**
 * Benchmark iterating over the full set using the primitive iterator.
 */
@Benchmark
public void iterate(Blackhole bh) {
    var iterator = fullSet.byteIterator();
    while (iterator.hasNext()) {
        bh.consume(iterator.next());
    }
}
```

### Method 22

```java
/**
 * Benchmark iterating over the stack using the enhanced for‑loop.
 */
@Benchmark
public void iterate(Blackhole bh) {
    for (Integer i : baseStack) {
        bh.consume(i);
    }
}
```

### Method 23

```java
/**
 * Benchmark that applies the procedure to every element in the input list.
 */
@Benchmark
public void applyProcedure(BenchmarkState state) {
    for (Integer element : state.data) {
        state.procedure.value(element);
    }
}
```

### Method 24

```java
/**
 * Benchmark that creates a ChunkIterator for the current {@code chunkSize},
 * iterates over all chunks, and consumes each chunk with a Blackhole.
 *
 * Throughput is reported as operations per second (i.e., how many
 * complete iterations of the method can be performed per second).
 */
@Benchmark
public void iterateChunks(Blackhole bh) {
    ChunkIterator<Integer> chunkIterator = new ChunkIterator<>(sourceData, chunkSize);
    while (chunkIterator.hasNext()) {
        RichIterable<Integer> chunk = chunkIterator.next();
        // Consume the chunk to avoid dead‑code elimination.
        bh.consume(chunk);
    }
}
```

### Method 25

```java
/**
 * Benchmark that creates a new FlatCollectIterator for each invocation
 * and iterates over all elements, feeding them into a Blackhole.
 */
@Benchmark
public void iterateFlatCollect(Blackhole bh) {
    FlatCollectIterator<List<Integer>, Integer> iterator = new FlatCollectIterator<>(outerList, flattenFunction);
    while (iterator.hasNext()) {
        bh.consume(iterator.next());
    }
}
```

### Method 26

```java
/**
 * Benchmark that iterates over the {@link ZipIterable} using its {@code iterator()}
 * and consumes each {@link Pair} via {@link Blackhole}.
 */
@Benchmark
public void iterateWithIterator(Blackhole bh) {
    for (Pair<Integer, String> pair : zipIterable) {
        bh.consume(pair);
    }
}
```

### Method 27

```java
/**
 * Benchmark that iterates over the {@link ZipWithIndexIterable} using the
 * standard {@code for‑each} construct and consumes each {@link Pair}
 * with a {@link Blackhole}.
 *
 * @param state   the benchmark state containing the iterable
 * @param bh      blackhole to consume the pairs
 */
@Benchmark
public void iterateWithForEach(BenchmarkState state, Blackhole bh) {
    for (Pair<Integer, Integer> pair : state.zipIterable) {
        // Consume both elements to avoid dead‑code elimination.
        bh.consume(pair.getOne());
        bh.consume(pair.getTwo());
    }
}
```

### Method 28

```java
/**
 * Benchmark the {@code value} method by feeding the pre‑generated data
 * into a fresh {@link BigDecimalSummaryStatistics} instance.
 */
@Benchmark
public void benchmarkValue(Blackhole bh) {
    BigDecimalSummaryStatistics stats = new BigDecimalSummaryStatistics();
    for (BigDecimal bd : data) {
        stats.value(bd);
    }
    bh.consume(stats.getCount());
    bh.consume(stats.getSum());
    bh.consume(stats.getMinOptional());
    bh.consume(stats.getMaxOptional());
    bh.consume(stats.getAverage());
}
```

### Method 29

```java
/**
 * Benchmark the {@code value} method in a tight loop.
 */
@Benchmark
public void benchmarkValue() {
    for (Integer element : data) {
        procedure.value(element);
    }
}
```

### Method 30

```java
// -------------------------------------------------------------
// Benchmarks
// -------------------------------------------------------------
@Benchmark
public boolean benchmarkIntegerIsPositive() {
    boolean result = false;
    for (Integer i : integerList) {
        // XOR to prevent dead‑code elimination.
        result ^= integerIsPositiveFn.booleanValueOf(i);
    }
    return result;
}
```

### Method 31

```java
// Benchmark for a bulk operation that is synchronized internally
@Benchmark
public void putAll(Blackhole bh) {
    MutableMap<Integer, Integer> toPut = UnifiedMap.newMap(100);
    for (int i = 0; i < 100; i++) {
        toPut.put(random.nextInt(size * 10), random.nextInt());
    }
    syncMap.putAll(toPut);
    bh.consume(syncMap);
}
```

### Method 32

```java
// Optional: benchmark the parallel forEach to illustrate the parallel API.
@Benchmark
public void benchmarkParallelIteration(BenchmarkState state, Blackhole bh) {
    ExecutorService exec = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    try {
        state.set.asParallel(exec, 10_000).forEach(element -> bh.consume(element));
    } finally {
        exec.shutdownNow();
    }
}
```

### Method 33

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
public boolean shortCircuit() {
    ObjectIntPredicate<Integer> predicate = (value, occ) -> (value & 1) == 0 && occ == 1;
    for (int i = 0; i < elements.length; i++) {
        if (predicate.accept(elements[i], occurrences[i])) {
            // onShortCircuit == true, expected == true
            return true;
        }
    }
    // atEnd == false
    return false;
}
```

### Method 34

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
public int benchmarkGet() {
    // Sum all elements to prevent dead‑code elimination
    int sum = 0;
    for (int i = 0; i < 6; i++) {
        sum += list.get(i);
    }
    return sum;
}
```

### Method 35

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
public void iterator(Blackhole bh) {
    var it = tripletonSet.iterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 36

```java
@Benchmark
@Group("mixed")
@GroupThreads(1)
public void mixedOperations(Blackhole bh) {
    int op = ThreadLocalRandom.current().nextInt(4);
    int key = ThreadLocalRandom.current().nextInt(size * 2);
    switch(op) {
        case 0:
            bh.consume(map.put(key, key));
            break;
        case 1:
            bh.consume(map.get(key));
            break;
        case 2:
            bh.consume(map.getIfAbsentPut(key, () -> key));
            break;
        case 3:
            bh.consume(map.updateValue(key, () -> 0, old -> old + 1));
            break;
    }
}
```

### Method 37

```java
@Benchmark
@Group("mixed")
@GroupThreads(1)
public void mixedOperations(Blackhole bh) {
    int op = ThreadLocalRandom.current().nextInt(4);
    int key = ThreadLocalRandom.current().nextInt(size * 2);
    switch(op) {
        case 0:
            bh.consume(map.put(key, key));
            break;
        case 1:
            bh.consume(map.get(key));
            break;
        case 2:
            bh.consume(map.getIfAbsentPut(key, () -> key));
            break;
        case 3:
            bh.consume(map.updateValue(key, () -> 0, old -> old + 1));
            break;
    }
}
```

### Method 38

```java
@Benchmark
@Group("mixed")
@GroupThreads(1)
public void mixedOperations(Blackhole bh) {
    int op = ThreadLocalRandom.current().nextInt(4);
    int key = ThreadLocalRandom.current().nextInt(size * 2);
    switch(op) {
        case 0:
            bh.consume(map.put(key, key));
            break;
        case 1:
            bh.consume(map.get(key));
            break;
        case 2:
            bh.consume(map.getIfAbsentPut(key, () -> key));
            break;
        case 3:
            bh.consume(map.updateValue(key, () -> 0, old -> old + 1));
            break;
    }
}
```

### Method 39

```java
@Benchmark
public ArrayAdapter<Integer> deserializeAdapter() throws IOException, ClassNotFoundException {
    try (ByteArrayInputStream bis = new ByteArrayInputStream(serializedForm);
        ObjectInputStream ois = new ObjectInputStream(bis)) {
        @SuppressWarnings("unchecked")
        ArrayAdapter<Integer> deserialized = (ArrayAdapter<Integer>) ois.readObject();
        return deserialized;
    }
}
```

### Method 40

```java
@Benchmark
public ImmutableListMultimap<Integer, Integer> createMultimap() {
    var mutable = new org.eclipse.collections.impl.multimap.list.FastListMultimap<Integer, Integer>();
    for (int k = 0; k < keyCount; k++) {
        for (int v = 0; v < valuesPerKey; v++) {
            mutable.put(k, v);
        }
    }
    return mutable.toImmutable();
}
```

### Method 41

```java
@Benchmark
public ImmutableListMultimap<Integer, Integer> createMultimap() {
    var mutable = new org.eclipse.collections.impl.multimap.list.FastListMultimap<Integer, Integer>();
    for (int k = 0; k < keyCount; k++) {
        for (int v = 0; v < valuesPerKey; v++) {
            mutable.put(k, v);
        }
    }
    return mutable.toImmutable();
}
```

### Method 42

```java
@Benchmark
public LazyIterable<Pair<Integer, Integer>> cartesianProduct(Blackhole bh) {
    LazyIterable<Pair<Integer, Integer>> result = SetIterables.cartesianProduct(setA, setB);
    // Force evaluation of a few elements to avoid dead‑code elimination.
    int count = 0;
    for (Pair<Integer, Integer> p : result) {
        bh.consume(p);
        if (++count >= 10)
            break;
    }
    return result;
}
```

### Method 43

```java
@Benchmark
public LazyIterable<Pair<Integer, Integer>> cartesianProduct(Blackhole bh) {
    LazyIterable<Pair<Integer, Integer>> result = SetIterables.cartesianProduct(setA, setB);
    // Force evaluation of a few elements to avoid dead‑code elimination.
    int count = 0;
    for (Pair<Integer, Integer> p : result) {
        bh.consume(p);
        if (++count >= 10)
            break;
    }
    return result;
}
```

### Method 44

```java
@Benchmark
public LazyIterable<String> cartesianProductWithFunction(Blackhole bh) {
    Function2<Integer, Integer, String> concat = (a, b) -> a + ":" + b;
    LazyIterable<String> result = SetIterables.cartesianProduct(setA, setB, concat);
    int count = 0;
    for (String s : result) {
        bh.consume(s);
        if (++count >= 10)
            break;
    }
    return result;
}
```

### Method 45

```java
@Benchmark
public LazyIterable<String> cartesianProductWithFunction(Blackhole bh) {
    Function2<Integer, Integer, String> concat = (a, b) -> a + ":" + b;
    LazyIterable<String> result = SetIterables.cartesianProduct(setA, setB, concat);
    int count = 0;
    for (String s : result) {
        bh.consume(s);
        if (++count >= 10)
            break;
    }
    return result;
}
```

### Method 46

```java
@Benchmark
public MultiReaderHashBagMultimap<Integer, String> putBenchmark() {
    MultiReaderHashBagMultimap<Integer, String> map = MultiReaderHashBagMultimap.newMultimap();
    for (int i = 0; i < ELEMENT_COUNT; i++) {
        map.put(i % KEY_RANGE, "v-" + i);
    }
    return map;
}
```

### Method 47

```java
@Benchmark
public MultiReaderUnifiedSetMultimap<Integer, Integer> put() {
    MultiReaderUnifiedSetMultimap<Integer, Integer> map = MultiReaderUnifiedSetMultimap.newMultimap();
    for (Pair<Integer, Integer> entry : entries) {
        map.put(entry.getOne(), entry.getTwo());
    }
    return map;
}
```

### Method 48

```java
@Benchmark
public MutableBag<Integer> addElements() {
    for (int e : elements) {
        bag.add(e);
    }
    return bag;
}
```

### Method 49

```java
@Benchmark
public MutableBag<Integer> removeElements() {
    // first fill the bag
    for (int e : elements) {
        bag.add(e);
    }
    // then remove the same elements
    for (int e : elements) {
        bag.remove(e);
    }
    return bag;
}
```

### Method 50

```java
@Benchmark
public MutableBag<Integer> removeElements() {
    // first fill the bag
    for (int e : elements) {
        bag.add(e);
    }
    // then remove the same elements
    for (int e : elements) {
        bag.remove(e);
    }
    return bag;
}
```

### Method 51

```java
@Benchmark
public MutableBag<Integer> selectByOccurrences() {
    // populate the bag with duplicate elements to create varying occurrence counts
    for (int i = 0; i < elements.length; i++) {
        // 1..5 occurrences
        int repetitions = (i % 5) + 1;
        for (int j = 0; j < repetitions; j++) {
            bag.add(elements[i]);
        }
    }
    // benchmark the selection based on occurrence predicate
    return bag.selectByOccurrences(OCCURRENCE_PREDICATE);
}
```

### Method 52

```java
@Benchmark
public MutableBag<Integer> selectByOccurrences() {
    // populate the bag with duplicate elements to create varying occurrence counts
    for (int i = 0; i < elements.length; i++) {
        // 1..5 occurrences
        int repetitions = (i % 5) + 1;
        for (int j = 0; j < repetitions; j++) {
            bag.add(elements[i]);
        }
    }
    // benchmark the selection based on occurrence predicate
    return bag.selectByOccurrences(OCCURRENCE_PREDICATE);
}
```

### Method 53

```java
@Benchmark
public MutableBag<Integer> trimToSize() {
    // fill the bag to trigger internal resizing
    for (int e : elements) {
        bag.add(e);
    }
    // benchmark the trim operation
    ((HashBag<Integer>) bag).trimToSize();
    return bag;
}
```

### Method 54

```java
@Benchmark
public MutableObjectDoubleMap<String> benchmarkSumByDoubleFunction() {
    MutableObjectDoubleMap<String> map = ObjectDoubleMaps.mutable.empty();
    for (Integer i : integerList) {
        map = sumByDoubleFn.value(map, i);
    }
    return map;
}
```

### Method 55

```java
@Benchmark
public MutableObjectDoubleMap<String> benchmarkSumByFloatFunction() {
    MutableObjectDoubleMap<String> map = ObjectDoubleMaps.mutable.empty();
    for (Integer i : integerList) {
        map = sumByFloatFn.value(map, i);
    }
    return map;
}
```

### Method 56

```java
@Benchmark
public MutableObjectLongMap<String> benchmarkSumByIntFunction() {
    MutableObjectLongMap<String> map = ObjectLongMaps.mutable.empty();
    for (Integer i : integerList) {
        map = sumByIntFn.value(map, i);
    }
    return map;
}
```

### Method 57

```java
@Benchmark
public boolean benchmarkContains() {
    // Use a code point that is guaranteed to be present in the sample strings
    // (the letter 'o' for ASCII, or the musical G‑clef U+1D11E for the third case)
    int codePoint = source.indexOf('o') >= 0 ? 'o' : 0x1D11E;
    return adapter.contains(codePoint);
}
```

### Method 58

```java
@Benchmark
public boolean contains() {
    // check for a value that is present and one that is not
    return list.contains(3) && !list.contains(99);
}
```

### Method 59

```java
@Benchmark
public int benchmarkUnboxIntegerToInt() {
    int sum = 0;
    for (Integer i : integerList) {
        sum += unboxIntegerToIntFn.intValueOf(i);
    }
    return sum;
}
```

### Method 60

```java
@Benchmark
public int benchmarkUnboxNumberToInt() {
    int sum = 0;
    for (Number n : numberList) {
        sum += unboxNumberToIntFn.intValueOf(n);
    }
    return sum;
}
```

### Method 61

```java
@Benchmark
public int detectAbsent() {
    Integer result = bag.detect(i -> i == absentElement);
    return result == null ? -1 : result;
}
```

### Method 62

```java
@Benchmark
public int detectPresent() {
    Integer result = bag.detect(i -> i == presentElement);
    return result == null ? -1 : result;
}
```

### Method 63

```java
@Benchmark
public int iterate() {
    int sum = 0;
    for (Integer i : bag) {
        sum += i;
    }
    return sum;
}
```

### Method 64

```java
@Benchmark
public int iterate(BenchmarkState state) {
    int sum = 0;
    Iterator<Integer> it = state.bag.iterator();
    while (it.hasNext()) {
        sum += it.next();
    }
    // return to prevent dead‑code elimination
    return sum;
}
```

### Method 65

```java
@Benchmark
public int iterate(IterateState state) {
    int sum = 0;
    var it = state.bag.booleanIterator();
    while (it.hasNext()) {
        sum += it.next() ? 1 : 0;
    }
    return sum;
}
```

### Method 66

```java
@Benchmark
public int iterateBag(BenchmarkState state) {
    int sum = 0;
    for (Integer i : state.bag) {
        sum += i;
    }
    return sum;
}
```

### Method 67

```java
@Benchmark
public int iterateTakeWhile(Blackhole bh) {
    TakeWhileIterator<Integer> iterator = new TakeWhileIterator<>(data, predicate);
    int count = 0;
    while (iterator.hasNext()) {
        bh.consume(iterator.next());
        count++;
    }
    return count;
}
```

### Method 68

```java
@Benchmark
public int plainIteration() {
    int sum = 0;
    while (plainIterator.hasNext()) {
        sum += plainIterator.next();
    }
    // Prevent dead‑code elimination
    return sum;
}
```

### Method 69

```java
@Benchmark
public int tapIteration() {
    int sum = 0;
    while (tapIterator.hasNext()) {
        sum += tapIterator.next();
    }
    // Prevent dead‑code elimination
    return sum;
}
```

### Method 70

```java
@Benchmark
public long benchIteration() {
    long sum = 0;
    for (Map.Entry<Integer, Integer> entry : readOnlyMap.entrySet()) {
        sum += entry.getValue();
    }
    return sum;
}
```

### Method 71

```java
@Benchmark
public long benchmarkIterateEntries() {
    long sum = 0;
    for (ObjectBooleanPair<Integer> entry : map.keyValuesView()) {
        sum += entry.getTwo() ? 1 : 0;
    }
    return sum;
}
```

### Method 72

```java
@Benchmark
public long benchmarkIterateEntries() {
    long sum = 0;
    for (ObjectBooleanPair<Integer> entry : map.keyValuesView()) {
        sum += entry.getTwo() ? 1 : 0;
    }
    return sum;
}
```

### Method 73

```java
@Benchmark
public long benchmarkIterateKeys() {
    long sum = 0;
    for (Integer key : map.keySet()) {
        sum += key;
    }
    return sum;
}
```

### Method 74

```java
@Benchmark
public long benchmarkIterateValues() {
    long trueCount = 0;
    for (boolean v : map.values().toArray()) {
        if (v)
            trueCount++;
    }
    return trueCount;
}
```

### Method 75

```java
@Benchmark
public long benchmarkIterator() {
    LongIterator it = interval.longIterator();
    long last = 0;
    while (it.hasNext()) {
        last = it.next();
    }
    return last;
}
```

### Method 76

```java
@Benchmark
public long iterate() {
    long sum = 0L;
    while (iterator.hasNext()) {
        sum += iterator.next();
    }
    // Return a value to prevent dead‑code elimination.
    return sum;
}
```

### Method 77

```java
@Benchmark
public long iterate(ThreadState state) {
    long sum = 0L;
    for (Integer i : state.syncSet) {
        sum += i;
    }
    return sum;
}
```

### Method 78

```java
@Benchmark
public long iterateUnmodifiableForEach() {
    long sum = 0;
    for (int i : unmodifiableList) {
        sum += i;
    }
    return sum;
}
```

### Method 79

```java
@Benchmark
public long iterateUnmodifiableJavaForEach() {
    long sum = 0;
    for (int i : unmodifiableJavaList) {
        sum += i;
    }
    return sum;
}
```

### Method 80

```java
@Benchmark
public long iteratorTraversal() {
    long sum = 0;
    for (Integer v : lazyIterable) {
        sum += v;
    }
    return sum;
}
```

### Method 81

```java
@Benchmark
public long sync_iteration() {
    long sum = 0;
    for (Map.Entry<Integer, Integer> entry : synchronizedMap.entrySet()) {
        sum += entry.getKey() + entry.getValue();
    }
    return sum;
}
```

### Method 82

```java
@Benchmark
public void add(Blackhole bh) {
    FastList<Integer> local = FastList.newList();
    for (int i = 0; i < size; i++) {
        local.add(i);
    }
    bh.consume(local);
}
```

### Method 83

```java
@Benchmark
public void benchPut() {
    // put a new key each time to avoid overwriting existing entries
    int key = (int) (Math.random() * Integer.MAX_VALUE);
    map.put(key, key % 2 == 0);
}
```

### Method 84

```java
@Benchmark
public void benchmarkBooleanIterator(Blackhole bh) {
    var iterator = this.booleanIterable.booleanIterator();
    while (iterator.hasNext()) {
        bh.consume(iterator.next());
    }
}
```

### Method 85

```java
@Benchmark
public void benchmarkIterate(Blackhole bh) {
    // Iterate over the whole composite list.
    for (Integer i : compositeList) {
        bh.consume(i);
    }
}
```

### Method 86

```java
@Benchmark
public void benchmarkIterator(Blackhole bh) {
    for (Integer element : tapIterable) {
        bh.consume(element);
    }
}
```

### Method 87

```java
@Benchmark
public void benchmarkIterator(Blackhole bh) {
    for (Integer i : quadSet) {
        bh.consume(i);
    }
}
```

### Method 88

```java
@Benchmark
public void benchmarkIterator(Blackhole bh) {
    for (String v : lazyIterable) {
        bh.consume(v);
    }
}
```

### Method 89

```java
@Benchmark
public void benchmarkIterator(Blackhole bh) {
    var it = distinctIterable.iterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 90

```java
@Benchmark
public void benchmarkIteratorTraversal(BenchmarkState state, Blackhole bh) {
    for (Integer elem : state.takeIterable) {
        bh.consume(elem);
    }
}
```

### Method 91

```java
@Benchmark
public void benchmarkReadExternal(Blackhole bh) throws IOException, ClassNotFoundException {
    HashBagMultimap<Integer, Integer> newMap = HashBagMultimap.newMultimap();
    try (ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(serializedForm))) {
        newMap.readExternal(ois);
    }
    bh.consume(newMap);
}
```

### Method 92

```java
@Benchmark
public void benchmarkReadExternal(Blackhole bh) throws IOException, ClassNotFoundException {
    HashBagMultimap<Integer, Integer> newMap = HashBagMultimap.newMultimap();
    try (ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(serializedForm))) {
        newMap.readExternal(ois);
    }
    bh.consume(newMap);
}
```

### Method 93

```java
@Benchmark
public void benchmarkValueMethod(Blackhole bh) {
    // Clear the target list to ensure each iteration processes the same amount of work.
    targetList.clear();
    // Apply the procedure to each element.
    for (Integer value : inputData) {
        procedure.value(value);
    }
    // Consume the resulting list size to avoid dead‑code elimination.
    bh.consume(targetList.size());
}
```

### Method 94

```java
@Benchmark
public void benchmarkWriteExternal(Blackhole bh) throws IOException {
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        mutableMultimap.writeExternal(oos);
    }
    bh.consume(baos.toByteArray());
}
```

### Method 95

```java
@Benchmark
public void benchmarkWriteExternal(Blackhole bh) throws IOException {
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        mutableMultimap.writeExternal(oos);
    }
    bh.consume(baos.toByteArray());
}
```

### Method 96

```java
@Benchmark
public void countProcedureThroughput(Blackhole bh) {
    // Create a fresh CountProcedure for each benchmark invocation to avoid state leakage
    CountProcedure<Integer> countProcedure = new CountProcedure<>(predicate);
    for (Integer value : data) {
        countProcedure.value(value);
    }
    // Consume the result to prevent dead‑code elimination
    bh.consume(countProcedure.getCount());
}
```

### Method 97

```java
@Benchmark
public void deserialize(Blackhole bh) throws IOException, ClassNotFoundException {
    ImmutableSetWithHashingStrategySerializationProxy<Integer> proxy = new ImmutableSetWithHashingStrategySerializationProxy<>();
    try (ByteArrayInputStream bais = new ByteArrayInputStream(this.serializedBytes);
        ObjectInputStream ois = new ObjectInputStream(bais)) {
        proxy.readExternal(ois);
        // the actual immutable set
        Object result = proxy.readResolve();
        bh.consume(result);
    }
}
```

### Method 98

```java
@Benchmark
public void deserialize(Blackhole bh) throws IOException, ClassNotFoundException {
    ImmutableSetWithHashingStrategySerializationProxy<Integer> proxy = new ImmutableSetWithHashingStrategySerializationProxy<>();
    try (ByteArrayInputStream bais = new ByteArrayInputStream(this.serializedBytes);
        ObjectInputStream ois = new ObjectInputStream(bais)) {
        proxy.readExternal(ois);
        // the actual immutable set
        Object result = proxy.readResolve();
        bh.consume(result);
    }
}
```

### Method 99

```java
@Benchmark
public void get(Blackhole bh) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += list.get(i);
    }
    bh.consume(sum);
}
```

### Method 100

```java
@Benchmark
public void getValues(Blackhole bh) {
    for (int key = 0; key < KEY_COUNT; key++) {
        bh.consume(multimap.get(key));
    }
}
```

### Method 101

```java
@Benchmark
public void iterate() {
    // Simple iteration using the primitive iterator.
    var iterator = list.booleanIterator();
    while (iterator.hasNext()) {
        iterator.next();
    }
}
```

### Method 102

```java
@Benchmark
public void iterate(BenchmarkState state, Blackhole bh) {
    for (Integer i : state.stack) {
        bh.consume(i);
    }
}
```

### Method 103

```java
@Benchmark
public void iterate(Blackhole bh) {
    // Enhanced‑for loop uses iterator()
    for (Integer i : dropWhileIterable) {
        bh.consume(i);
    }
}
```

### Method 104

```java
@Benchmark
public void iterateAll(BenchmarkState state, Blackhole bh) {
    for (Integer i : state.rejectIterable) {
        bh.consume(i);
    }
}
```

### Method 105

```java
@Benchmark
public void iterateAll(Blackhole bh) {
    var iterator = setAll.booleanIterator();
    while (iterator.hasNext()) {
        bh.consume(iterator.next());
    }
}
```

### Method 106

```java
@Benchmark
public void iterateChunks(BenchmarkState state, Blackhole bh) {
    // Iterate over all chunks and feed each chunk to the Blackhole.
    for (RichIterable<Integer> chunk : state.chunkIterable) {
        // Consume the chunk itself.
        bh.consume(chunk);
        // Iterate inside the chunk to ensure full traversal.
        for (Integer i : chunk) {
            bh.consume(i);
        }
    }
}
```

### Method 107

```java
@Benchmark
public void iterateChunks(BenchmarkState state, Blackhole bh) {
    // Iterate over all chunks and feed each chunk to the Blackhole.
    for (RichIterable<Integer> chunk : state.chunkIterable) {
        // Consume the chunk itself.
        bh.consume(chunk);
        // Iterate inside the chunk to ensure full traversal.
        for (Integer i : chunk) {
            bh.consume(i);
        }
    }
}
```

### Method 108

```java
@Benchmark
public void iterateDistinct(Blackhole bh) {
    while (distinctIterator.hasNext()) {
        bh.consume(distinctIterator.next());
    }
}
```

### Method 109

```java
@Benchmark
public void iterateEntrySet(BenchmarkState state, Blackhole bh) {
    // Use keyValuesView() which yields Pair<K,V>
    for (Pair<Integer, Integer> entry : state.map.keyValuesView()) {
        bh.consume(entry.getOne());
        bh.consume(entry.getTwo());
    }
}
```

### Method 110

```java
@Benchmark
public void iterateEntrySet(Blackhole bh) {
    for (MutableMap.Entry<Integer, Integer> entry : syncMap.entrySet()) {
        bh.consume(entry.getKey());
        bh.consume(entry.getValue());
    }
}
```

### Method 111

```java
@Benchmark
public void iterateKeySet(BenchmarkState state, Blackhole bh) {
    // Use keysView() which is available on ImmutableSortedMap
    for (Integer key : state.map.keysView()) {
        bh.consume(key);
    }
}
```

### Method 112

```java
@Benchmark
public void iterateKeySet(Blackhole bh) {
    for (Integer key : syncMap.keySet()) {
        bh.consume(key);
    }
}
```

### Method 113

```java
@Benchmark
public void iterateValues(Blackhole bh) {
    for (Integer value : syncMap.values()) {
        bh.consume(value);
    }
}
```

### Method 114

```java
@Benchmark
public void iterateWithIntIteratorLarge(Blackhole bh) {
    var it = largeInterval.intIterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 115

```java
@Benchmark
public void iterator() {
    Iterator<Integer> it = bag.iterator();
    while (it.hasNext()) {
        it.next();
    }
}
```

### Method 116

```java
@Benchmark
public void partition(Blackhole bh) {
    for (Integer value : data) {
        procedure.value(value);
    }
    bh.consume(procedure);
}
```

### Method 117

```java
@Benchmark
public void partitionStrings() {
    for (String s : data) {
        procedure.value(s);
    }
}
```

### Method 118

```java
@Benchmark
public void putBatch() {
    for (int i = 0; i < BATCH; i++) {
        multimap.put(i, i);
    }
    for (int i = 0; i < BATCH; i++) {
        multimap.remove(i, i);
    }
}
```

### Method 119

```java
@Benchmark
public void putBatch() {
    for (int i = 0; i < BATCH; i++) {
        multimap.put(i, i);
    }
    for (int i = 0; i < BATCH; i++) {
        multimap.remove(i, i);
    }
}
```

### Method 120

```java
@Benchmark
public void putBatch(BenchmarkState state) {
    // Apply the procedure to each element in the pre‑generated batch.
    for (String value : state.values) {
        state.procedure.value(value);
    }
}
```

### Method 121

```java
@Benchmark
public void putBatch(Blackhole bh) {
    // Insert a batch of entries in a tight loop.
    for (int i = 0; i < BATCH_SIZE; i++) {
        int key = PREPOPULATED_SIZE + i;
        mutableMultimap.put(key, valueFor(key));
    }
    bh.consume(mutableMultimap);
}
```

### Method 122

```java
@Benchmark
public void putNewMap(Blackhole bh) {
    TreeBagMultimap<Integer, Integer> map = new TreeBagMultimap<>();
    for (int i = 0; i < VALUE_COUNT; i++) {
        int key = i % KEY_COUNT;
        map.put(key, i);
    }
    bh.consume(map);
}
```

### Method 123

```java
@Benchmark
public void removeByIndex(Blackhole bh) {
    // Remove from the end to avoid shifting cost dominating the benchmark
    FastList<Integer> local = FastList.newList(listForRemove);
    while (!local.isEmpty()) {
        local.remove(local.size() - 1);
    }
    bh.consume(local);
}
```

### Method 124

```java
@Benchmark
public void serialize(Blackhole bh) throws IOException {
    ImmutableSetWithHashingStrategySerializationProxy<Integer> proxy = new ImmutableSetWithHashingStrategySerializationProxy<>(this.immutableSet, this.hashingStrategy);
    try (ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        proxy.writeExternal(oos);
        oos.flush();
        // prevent dead‑code elimination
        bh.consume(baos.toByteArray());
    }
}
```

### Method 125

```java
@Benchmark
public void serialize(Blackhole bh) throws IOException {
    ImmutableSetWithHashingStrategySerializationProxy<Integer> proxy = new ImmutableSetWithHashingStrategySerializationProxy<>(this.immutableSet, this.hashingStrategy);
    try (ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        proxy.writeExternal(oos);
        oos.flush();
        // prevent dead‑code elimination
        bh.consume(baos.toByteArray());
    }
}
```

### Method 126

```java
@Benchmark
public void serializeDeserialize(Blackhole bh) throws IOException, ClassNotFoundException {
    // Serialize into a fresh byte array each iteration.
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        oos.writeObject(immutableMap);
        oos.flush();
    }
    // Deserialize from the freshly created byte array.
    try (ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(baos.toByteArray()))) {
        @SuppressWarnings("unchecked")
        ImmutableSortedMap<Integer, String> deserialized = (ImmutableSortedMap<Integer, String>) ois.readObject();
        bh.consume(deserialized);
    }
}
```

### Method 127

```java
@Benchmark
public void serializeDeserialize(Blackhole bh) throws IOException, ClassNotFoundException {
    // Serialize into a fresh byte array each iteration.
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        oos.writeObject(immutableMap);
        oos.flush();
    }
    // Deserialize from the freshly created byte array.
    try (ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(baos.toByteArray()))) {
        @SuppressWarnings("unchecked")
        ImmutableSortedMap<Integer, String> deserialized = (ImmutableSortedMap<Integer, String>) ois.readObject();
        bh.consume(deserialized);
    }
}
```

### Method 128

```java
@Benchmark
public void serializeDeserialize(Blackhole bh) throws IOException, ClassNotFoundException {
    // Serialize into a fresh byte array each iteration.
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        oos.writeObject(immutableMap);
        oos.flush();
    }
    // Deserialize from the freshly created byte array.
    try (ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(baos.toByteArray()))) {
        @SuppressWarnings("unchecked")
        ImmutableSortedMap<Integer, String> deserialized = (ImmutableSortedMap<Integer, String>) ois.readObject();
        bh.consume(deserialized);
    }
}
```

### Method 129

```java
@Benchmark
public void serializeDeserialize(Blackhole bh) throws IOException, ClassNotFoundException {
    // Serialize into a fresh byte array each iteration.
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        oos.writeObject(immutableMap);
        oos.flush();
    }
    // Deserialize from the freshly created byte array.
    try (ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(baos.toByteArray()))) {
        @SuppressWarnings("unchecked")
        ImmutableSortedMap<Integer, String> deserialized = (ImmutableSortedMap<Integer, String>) ois.readObject();
        bh.consume(deserialized);
    }
}
```

### Method 130

```java
@Benchmark
public void zipWithIndex() {
    // Simulate a typical usage pattern: feed each element to the procedure.
    for (String element : inputs) {
        procedure.value(element);
    }
}
```

## JMH UNSINKED VARIABLE - Unsinked variable inside benchmark method

### Method 1

```java
/* ---------- Iteration benchmarks ---------- */
@Benchmark
public long iterateMutableForEach() {
    long sum = 0;
    for (int i : mutableList) {
        sum += i;
    }
    return sum;
}
```

### Method 2

```java
/* ---------------- Iteration over entrySet ---------------- */
@Benchmark
public long unsync_iteration() {
    long sum = 0;
    for (Map.Entry<Integer, Integer> entry : unsynchronizedMap.entrySet()) {
        sum += entry.getKey() + entry.getValue();
    }
    return sum;
}
```

### Method 3

```java
/* -------------------- Iteration via primitive iterator -------------------- */
@Benchmark
public void iterateWithIntIteratorSmall(Blackhole bh) {
    var it = smallInterval.intIterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 4

```java
/* -------------------- Traversal using Spliterator -------------------- */
@Benchmark
public void spliteratorSmall(Blackhole bh) {
    var spliterator = smallInterval.spliterator();
    spliterator.forEachRemaining((IntConsumer) bh::consume);
}
```

### Method 5

```java
/* ------------------------------------- */
/*  Iteration benchmarks                */
/* ------------------------------------- */
@Benchmark
public long benchmarkForEach() {
    final long[] holder = new long[1];
    // consume last value to avoid dead code elimination
    interval.each(value -> holder[0] = value);
    return holder[0];
}
```

### Method 6

```java
/* --------------------------------------------------------------------- */
/* Parallel traversal benchmarks                                          */
/* --------------------------------------------------------------------- */
@Benchmark
public void asParallelTraversal(BenchmarkState state) throws Exception {
    int batchSize = 256;
    var parallelIterable = state.immutableSet.asParallel(state.executor, batchSize);
    parallelIterable.forEach(state.blackholeProcedure);
}
```

### Method 7

```java
/* --------------------------------------------------------------------- */
/* Traversal benchmarks                                                   */
/* --------------------------------------------------------------------- */
@Benchmark
public void iteratorTraversal(BenchmarkState state) {
    var iterator = state.immutableSet.iterator();
    while (iterator.hasNext()) {
        iterator.next();
    }
}
```

### Method 8

```java
/**
 * Benchmark adding a byte to a mutable set.
 */
@Benchmark
public void add(Blackhole bh) {
    int idx = counter.getAndIncrement() & 0xFF;
    byte value = ALL_BYTES[idx];
    // ensure the set is cleared periodically to keep size bounded
    if (mutableSet.size() == 256) {
        mutableSet.clear();
    }
    boolean added = mutableSet.add(value);
    bh.consume(added);
}
```

### Method 9

```java
/**
 * Benchmark checking containment in a fully populated set.
 */
@Benchmark
public void contains(Blackhole bh) {
    int idx = counter.getAndIncrement() & 0xFF;
    byte value = ALL_BYTES[idx];
    boolean contains = fullSet.contains(value);
    bh.consume(contains);
}
```

### Method 10

```java
/**
 * Benchmark for a single get operation.
 */
@Benchmark
public String get() {
    int idx = (int) (Math.random() * SIZE);
    return map.get(keys[idx]);
}
```

### Method 11

```java
/**
 * Benchmark for a single put operation that updates an existing key.
 */
@Benchmark
public void putExistingKey() {
    int idx = (int) (Math.random() * SIZE);
    int key = keys[idx];
    map.put(key, "updated-" + key);
}
```

### Method 12

```java
/**
 * Benchmark for a single remove operation.
 */
@Benchmark
public void remove() {
    int idx = (int) (Math.random() * SIZE);
    map.remove(keys[idx]);
}
```

### Method 13

```java
/**
 * Benchmark for iterating over entries.
 */
@Benchmark
public long iterateEntries() {
    long sum = 0;
    for (Pair<Integer, String> entry : map.keyValuesView()) {
        sum += entry.getOne() + entry.getTwo().length();
    }
    return sum;
}
```

### Method 14

```java
/**
 * Benchmark for iterating over the whole bag using the iterator.
 */
@Benchmark
public long iterate() {
    long sum = 0L;
    for (Integer i : prepopulatedBag) {
        sum += i;
    }
    // return to prevent dead‑code elimination
    return sum;
}
```

### Method 15

```java
/**
 * Benchmark for iterating over values.
 */
@Benchmark
public long iterateValues() {
    long sum = 0;
    for (String v : map.values()) {
        sum += v.length();
    }
    return sum;
}
```

### Method 16

```java
/**
 * Benchmark for iterating over {@code entrySet()} and consuming each entry.
 */
@Benchmark
public void benchEntrySetIteration(Blackhole bh) {
    // The entrySet is immutable; iterating over it should be cheap.
    for (var entry : immutableMap.entrySet()) {
        bh.consume(entry.getKey());
        bh.consume(entry.getValue());
    }
}
```

### Method 17

```java
/**
 * Benchmark for the forEach method that processes each element.
 */
@Benchmark
public long forEach() {
    final long[] sum = { 0L };
    prepopulatedBag.each(item -> sum[0] += item);
    return sum[0];
}
```

### Method 18

```java
/**
 * Benchmark for the inverse view lookup (value → key).
 */
@Benchmark
public Integer inverseLookup() {
    int idx = (int) (Math.random() * SIZE);
    return map.inverse().get(values[idx]);
}
```

### Method 19

```java
/**
 * Benchmark for {@code UnifiedSet.contains(Object)}.
 */
@Benchmark
public void contains(Blackhole bh) {
    // Randomly pick a key from the pre‑generated array.
    int idx = ThreadLocalRandom.current().nextInt(ELEMENT_COUNT);
    int key = randomKeys[idx];
    boolean result = filledSet.contains(key);
    bh.consume(result);
}
```

### Method 20

```java
/**
 * Benchmark for {@code remove} – removes random elements from a mutable copy of the pre‑populated set.
 */
@Benchmark
public void removeElements(Blackhole bh) {
    // Work on a copy to keep the original set unchanged across iterations
    TreeSortedSet<Integer> copy = TreeSortedSet.newSet(prepopulatedSet);
    int value = random.nextInt(PREPOPULATED_SIZE);
    boolean removed = copy.remove(value);
    bh.consume(removed);
}
```

### Method 21

```java
/**
 * Benchmark for {@link FlatCollectIterable#iterator()}.
 */
@Benchmark
public long benchmarkIterator(Blackhole bh) {
    long sum = 0;
    for (Integer v : flatCollect) {
        sum += v;
    }
    bh.consume(sum);
    return sum;
}
```

### Method 22

```java
/**
 * Benchmark iterating over the full set using the primitive iterator.
 */
@Benchmark
public void iterate(Blackhole bh) {
    var iterator = fullSet.byteIterator();
    while (iterator.hasNext()) {
        bh.consume(iterator.next());
    }
}
```

### Method 23

```java
/**
 * Benchmark removing a byte from a mutable set.
 */
@Benchmark
public void remove(Blackhole bh) {
    // ensure the set contains the element before removal
    if (mutableSet.isEmpty()) {
        mutableSet.addAll(ALL_BYTES);
    }
    int idx = counter.getAndIncrement() & 0xFF;
    byte value = ALL_BYTES[idx];
    boolean removed = mutableSet.remove(value);
    bh.consume(removed);
}
```

### Method 24

```java
/**
 * Benchmark that creates a ChunkIterator for the current {@code chunkSize},
 * iterates over all chunks, and consumes each chunk with a Blackhole.
 *
 * Throughput is reported as operations per second (i.e., how many
 * complete iterations of the method can be performed per second).
 */
@Benchmark
public void iterateChunks(Blackhole bh) {
    ChunkIterator<Integer> chunkIterator = new ChunkIterator<>(sourceData, chunkSize);
    while (chunkIterator.hasNext()) {
        RichIterable<Integer> chunk = chunkIterator.next();
        // Consume the chunk to avoid dead‑code elimination.
        bh.consume(chunk);
    }
}
```

### Method 25

```java
/**
 * Benchmark that creates a new FlatCollectIterator for each invocation
 * and iterates over all elements, feeding them into a Blackhole.
 */
@Benchmark
public void iterateFlatCollect(Blackhole bh) {
    FlatCollectIterator<List<Integer>, Integer> iterator = new FlatCollectIterator<>(outerList, flattenFunction);
    while (iterator.hasNext()) {
        bh.consume(iterator.next());
    }
}
```

### Method 26

```java
/**
 * Benchmark that iterates over the {@link ZipWithIndexIterable} using the
 * standard {@code for‑each} construct and consumes each {@link Pair}
 * with a {@link Blackhole}.
 *
 * @param state   the benchmark state containing the iterable
 * @param bh      blackhole to consume the pairs
 */
@Benchmark
public void iterateWithForEach(BenchmarkState state, Blackhole bh) {
    for (Pair<Integer, Integer> pair : state.zipIterable) {
        // Consume both elements to avoid dead‑code elimination.
        bh.consume(pair.getOne());
        bh.consume(pair.getTwo());
    }
}
```

### Method 27

```java
/**
 * Benchmark the deserialization (readExternal) throughput.
 */
@Benchmark
public void deserialize(ReadBufferState bufferState, Blackhole bh) throws IOException, ClassNotFoundException {
    HashBagWithHashingStrategySerializationProxy<String> proxy = new HashBagWithHashingStrategySerializationProxy<>();
    proxy.readExternal(bufferState.ois);
    // Resolve the proxy to obtain the actual bag instance.
    Object result = proxy.readResolve();
    bh.consume(result);
}
```

### Method 28

```java
/**
 * Benchmark the serialization (writeExternal) throughput.
 */
@Benchmark
public void serialize(WriteBufferState bufferState, BagState bagState, Blackhole bh) throws IOException {
    // The proxy holds a reference to the bag; we reuse it for each iteration.
    HashBagWithHashingStrategySerializationProxy<String> proxy = new HashBagWithHashingStrategySerializationProxy<>(bagState.bag);
    proxy.writeExternal(bufferState.oos);
    // Ensure the serialized bytes are consumed so the JIT cannot eliminate the call.
    bh.consume(bufferState.baos.toByteArray());
}
```

### Method 29

```java
/**
 * Benchmark the {@code merge} method by merging two already populated
 * statistics objects.
 */
@Benchmark
public void benchmarkMerge(Blackhole bh) {
    BigDecimalSummaryStatistics leftCopy = new BigDecimalSummaryStatistics();
    leftCopy.merge(left);
    leftCopy.merge(right);
    bh.consume(leftCopy.getCount());
    bh.consume(leftCopy.getSum());
    bh.consume(leftCopy.getMinOptional());
    bh.consume(leftCopy.getMaxOptional());
    bh.consume(leftCopy.getAverage());
}
```

### Method 30

```java
/**
 * Benchmark the {@code value} method by feeding the pre‑generated data
 * into a fresh {@link BigDecimalSummaryStatistics} instance.
 */
@Benchmark
public void benchmarkValue(Blackhole bh) {
    BigDecimalSummaryStatistics stats = new BigDecimalSummaryStatistics();
    for (BigDecimal bd : data) {
        stats.value(bd);
    }
    bh.consume(stats.getCount());
    bh.consume(stats.getSum());
    bh.consume(stats.getMinOptional());
    bh.consume(stats.getMaxOptional());
    bh.consume(stats.getAverage());
}
```

### Method 31

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
public boolean shortCircuit() {
    ObjectIntPredicate<Integer> predicate = (value, occ) -> (value & 1) == 0 && occ == 1;
    for (int i = 0; i < elements.length; i++) {
        if (predicate.accept(elements[i], occurrences[i])) {
            // onShortCircuit == true, expected == true
            return true;
        }
    }
    // atEnd == false
    return false;
}
```

### Method 32

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
public void iterator(Blackhole bh) {
    var it = tripletonSet.iterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 33

```java
@Benchmark
@Group("iterate")
@GroupThreads(1)
public long iterateSingleThread() {
    final long[] sum = new long[1];
    multimap.forEachKeyValue((k, v) -> sum[0] += k + v);
    return sum[0];
}
```

### Method 34

```java
@Benchmark
@Group("iterate")
@GroupThreads(3)
public long iterateConcurrent() {
    final long[] sum = new long[1];
    multimap.forEachKeyValue((k, v) -> sum[0] += k + v);
    return sum[0];
}
```

### Method 35

```java
@Benchmark
@Group("mixed")
@GroupThreads(1)
public void mixedOperations(Blackhole bh) {
    int op = ThreadLocalRandom.current().nextInt(4);
    int key = ThreadLocalRandom.current().nextInt(size * 2);
    switch(op) {
        case 0:
            bh.consume(map.put(key, key));
            break;
        case 1:
            bh.consume(map.get(key));
            break;
        case 2:
            bh.consume(map.getIfAbsentPut(key, () -> key));
            break;
        case 3:
            bh.consume(map.updateValue(key, () -> 0, old -> old + 1));
            break;
    }
}
```

### Method 36

```java
@Benchmark
@Group("write")
@GroupThreads(2)
public void sort() {
    // Sorting acquires a write lock; we sort a copy to keep the original order.
    // This mimics a realistic workload where sorting is occasional.
    MultiReaderList<Integer> copy = list.clone();
    copy.sortThis();
}
```

### Method 37

```java
@Benchmark
public BooleanArrayList reverseThis() {
    // Reverse the list in‑place.
    // Clone to avoid mutating the shared state for other benchmarks.
    BooleanArrayList copy = BooleanArrayList.newList(list);
    return copy.reverseThis();
}
```

### Method 38

```java
@Benchmark
public ImmutableListMultimap<Integer, Integer> createMultimap() {
    var mutable = new org.eclipse.collections.impl.multimap.list.FastListMultimap<Integer, Integer>();
    for (int k = 0; k < keyCount; k++) {
        for (int v = 0; v < valuesPerKey; v++) {
            mutable.put(k, v);
        }
    }
    return mutable.toImmutable();
}
```

### Method 39

```java
@Benchmark
public Integer iteratorNext() {
    var it = doubletonSet.iterator();
    Integer first = it.next();
    Integer second = it.next();
    return second;
}
```

### Method 40

```java
@Benchmark
public MultiReaderUnifiedSetMultimap<Integer, Integer> put() {
    MultiReaderUnifiedSetMultimap<Integer, Integer> map = MultiReaderUnifiedSetMultimap.newMultimap();
    for (Pair<Integer, Integer> entry : entries) {
        map.put(entry.getOne(), entry.getTwo());
    }
    return map;
}
```

### Method 41

```java
@Benchmark
public boolean addFalseToEmpty() {
    BooleanHashSet s = new BooleanHashSet();
    return s.add(false);
}
```

### Method 42

```java
@Benchmark
public boolean addTrueToEmpty() {
    BooleanHashSet s = new BooleanHashSet();
    return s.add(true);
}
```

### Method 43

```java
@Benchmark
public boolean benchContainsKey() {
    int idx = (int) (Math.random() * SIZE);
    return map.containsKey(keys[idx]);
}
```

### Method 44

```java
@Benchmark
public boolean benchGet() {
    // random existing key
    int idx = (int) (Math.random() * SIZE);
    return map.get(keys[idx]);
}
```

### Method 45

```java
@Benchmark
public boolean remove() {
    // Remove a single key‑value pair; copy the multimap to avoid side effects
    MultiReaderUnifiedSetMultimap<Integer, Integer> copy = MultiReaderUnifiedSetMultimap.newMultimap(multimap);
    return copy.remove(keyToRemove, keyToRemove);
}
```

### Method 46

```java
@Benchmark
public int benchEntryIteration() {
    // count true values (same as benchIteration) using the public API
    final int[] trueCount = { 0 };
    mapForIteration.forEachKeyValue((k, v) -> {
        if (v) {
            trueCount[0]++;
        }
    });
    return trueCount[0];
}
```

### Method 47

```java
@Benchmark
public int benchIteration() {
    // count true values using the public API
    final int[] sum = { 0 };
    mapForIteration.forEachKeyValue((k, v) -> {
        if (v) {
            sum[0]++;
        }
    });
    return sum[0];
}
```

### Method 48

```java
@Benchmark
public int benchKeyIteration() {
    // count keys using the public API
    final int[] count = { 0 };
    mapForIteration.forEachKey(k -> count[0]++);
    return count[0];
}
```

### Method 49

```java
@Benchmark
public int iterate() {
    int sum = 0;
    for (Integer i : bag) {
        sum += i;
    }
    return sum;
}
```

### Method 50

```java
@Benchmark
public int iterate(BenchmarkState state) {
    int sum = 0;
    Iterator<Integer> it = state.bag.iterator();
    while (it.hasNext()) {
        sum += it.next();
    }
    // return to prevent dead‑code elimination
    return sum;
}
```

### Method 51

```java
@Benchmark
public int iterate(IterateState state) {
    int sum = 0;
    var it = state.bag.booleanIterator();
    while (it.hasNext()) {
        sum += it.next() ? 1 : 0;
    }
    return sum;
}
```

### Method 52

```java
@Benchmark
public int iterateBag(BenchmarkState state) {
    int sum = 0;
    for (Integer i : state.bag) {
        sum += i;
    }
    return sum;
}
```

### Method 53

```java
@Benchmark
public int iterateTakeWhile(Blackhole bh) {
    TakeWhileIterator<Integer> iterator = new TakeWhileIterator<>(data, predicate);
    int count = 0;
    while (iterator.hasNext()) {
        bh.consume(iterator.next());
        count++;
    }
    return count;
}
```

### Method 54

```java
@Benchmark
public int iterateViaSpliterator() {
    int[] sum = new int[1];
    Spliterator<Integer> spliterator = freshAdapter.spliterator();
    // Simple forEachRemaining to keep the benchmark focused on traversal cost.
    spliterator.forEachRemaining(v -> sum[0] += v);
    return sum[0];
}
```

### Method 55

```java
@Benchmark
public int readIterateAndCount() {
    final int[] sum = new int[1];
    bag.withReadLockAndDelegate(delegate -> {
        for (Integer i : delegate) {
            sum[0] += i;
        }
    });
    return sum[0];
}
```

### Method 56

```java
@Benchmark
public long benchIteration() {
    long sum = 0;
    for (Map.Entry<Integer, Integer> entry : readOnlyMap.entrySet()) {
        sum += entry.getValue();
    }
    return sum;
}
```

### Method 57

```java
@Benchmark
public long benchmarkIterateEntries() {
    long sum = 0;
    for (ObjectBooleanPair<Integer> entry : map.keyValuesView()) {
        sum += entry.getTwo() ? 1 : 0;
    }
    return sum;
}
```

### Method 58

```java
@Benchmark
public long benchmarkIterateKeys() {
    long sum = 0;
    for (Integer key : map.keySet()) {
        sum += key;
    }
    return sum;
}
```

### Method 59

```java
@Benchmark
public long benchmarkIterator() {
    LongIterator it = interval.longIterator();
    long last = 0;
    while (it.hasNext()) {
        last = it.next();
    }
    return last;
}
```

### Method 60

```java
@Benchmark
public long benchmarkSpliterator() {
    var spliterator = interval.spliterator();
    final long[] holder = new long[1];
    // Explicitly use a LongConsumer to avoid ambiguity
    spliterator.forEachRemaining((long v) -> holder[0] = v);
    return holder[0];
}
```

### Method 61

```java
@Benchmark
public long iterate() {
    // Iterate over all entries and sum the values to prevent dead‑code elimination
    final long[] sum = new long[1];
    multimap.forEachKeyValue((k, v) -> sum[0] += v);
    return sum[0];
}
```

### Method 62

```java
@Benchmark
public long iterateUnmodifiableForEach() {
    long sum = 0;
    for (int i : unmodifiableList) {
        sum += i;
    }
    return sum;
}
```

### Method 63

```java
@Benchmark
public long iterateUnmodifiableJavaForEach() {
    long sum = 0;
    for (int i : unmodifiableJavaList) {
        sum += i;
    }
    return sum;
}
```

### Method 64

```java
@Benchmark
public long iteratorTraversal() {
    long sum = 0;
    for (Integer v : lazyIterable) {
        sum += v;
    }
    return sum;
}
```

### Method 65

```java
@Benchmark
public long sync_iteration() {
    long sum = 0;
    for (Map.Entry<Integer, Integer> entry : synchronizedMap.entrySet()) {
        sum += entry.getKey() + entry.getValue();
    }
    return sum;
}
```

### Method 66

```java
@Benchmark
public void benchRemove() {
    // remove a random key; re‑insert to keep map size stable
    int idx = (int) (Math.random() * SIZE);
    Integer key = keys[idx];
    map.remove(key);
    map.put(key, values[idx]);
}
```

### Method 67

```java
@Benchmark
public void benchmarkAdd(BenchmarkState state, Blackhole bh) {
    // Add a new element that is not present in the set.
    // Use modulo to wrap around the array and avoid unbounded growth.
    int idx = (int) (System.nanoTime() % state.newKeys.length);
    int key = state.newKeys[idx];
    boolean added = state.set.add(key);
    // Consume the result to prevent dead‑code elimination.
    bh.consume(added);
    // Remove the key again to keep the set size constant for subsequent iterations.
    state.set.remove(key);
}
```

### Method 68

```java
@Benchmark
public void benchmarkBooleanIterator(Blackhole bh) {
    var iterator = this.booleanIterable.booleanIterator();
    while (iterator.hasNext()) {
        bh.consume(iterator.next());
    }
}
```

### Method 69

```java
@Benchmark
public void benchmarkContains(BenchmarkState state, Blackhole bh) {
    // Check for an element that is definitely present.
    int idx = (int) (System.nanoTime() % state.keys.length);
    int key = state.keys[idx];
    boolean contains = state.set.contains(key);
    bh.consume(contains);
}
```

### Method 70

```java
@Benchmark
public void benchmarkGet(BenchmarkState state, Blackhole bh) {
    // Retrieve an element that is present.
    int idx = (int) (System.nanoTime() % state.keys.length);
    int key = state.keys[idx];
    Integer value = state.set.get(key);
    bh.consume(value);
}
```

### Method 71

```java
@Benchmark
public void benchmarkIterator(Blackhole bh) {
    var it = distinctIterable.iterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 72

```java
@Benchmark
public void benchmarkRemove(BenchmarkState state, Blackhole bh) {
    // Remove an element and immediately re‑add it to keep the set size stable.
    int idx = (int) (System.nanoTime() % state.removeKeys.length);
    int key = state.removeKeys[idx];
    Integer removed = state.set.removeFromPool(key);
    bh.consume(removed);
    // Re‑add the same key so that subsequent iterations see the same state.
    state.set.add(key);
}
```

### Method 73

```java
@Benchmark
public void countProcedureThroughput(Blackhole bh) {
    // Create a fresh CountProcedure for each benchmark invocation to avoid state leakage
    CountProcedure<Integer> countProcedure = new CountProcedure<>(predicate);
    for (Integer value : data) {
        countProcedure.value(value);
    }
    // Consume the result to prevent dead‑code elimination
    bh.consume(countProcedure.getCount());
}
```

### Method 74

```java
@Benchmark
public void deserialize(Blackhole bh) throws IOException, ClassNotFoundException {
    ImmutableSetWithHashingStrategySerializationProxy<Integer> proxy = new ImmutableSetWithHashingStrategySerializationProxy<>();
    try (ByteArrayInputStream bais = new ByteArrayInputStream(this.serializedBytes);
        ObjectInputStream ois = new ObjectInputStream(bais)) {
        proxy.readExternal(ois);
        // the actual immutable set
        Object result = proxy.readResolve();
        bh.consume(result);
    }
}
```

### Method 75

```java
@Benchmark
public void iterate() {
    // Simple iteration using the primitive iterator.
    var iterator = list.booleanIterator();
    while (iterator.hasNext()) {
        iterator.next();
    }
}
```

### Method 76

```java
@Benchmark
public void iterateEntrySet(BenchmarkState state, Blackhole bh) {
    // Use keyValuesView() which yields Pair<K,V>
    for (Pair<Integer, Integer> entry : state.map.keyValuesView()) {
        bh.consume(entry.getOne());
        bh.consume(entry.getTwo());
    }
}
```

### Method 77

```java
@Benchmark
public void iterateEntrySet(Blackhole bh) {
    for (MutableMap.Entry<Integer, Integer> entry : syncMap.entrySet()) {
        bh.consume(entry.getKey());
        bh.consume(entry.getValue());
    }
}
```

### Method 78

```java
@Benchmark
public void iterateForEach(Blackhole bh) {
    final int[] sum = new int[1];
    list.forEach(item -> sum[0] += item);
    bh.consume(sum[0]);
}
```

### Method 79

```java
@Benchmark
public void iterateWithIntIteratorLarge(Blackhole bh) {
    var it = largeInterval.intIterator();
    while (it.hasNext()) {
        bh.consume(it.next());
    }
}
```

### Method 80

```java
@Benchmark
public void iterator() {
    Iterator<Integer> it = bag.iterator();
    while (it.hasNext()) {
        it.next();
    }
}
```

### Method 81

```java
@Benchmark
public void iteratorHasNext(Blackhole bh) {
    var it = set.booleanIterator();
    bh.consume(it.hasNext());
}
```

### Method 82

```java
@Benchmark
public void iteratorNext(Blackhole bh) {
    var it = set.booleanIterator();
    bh.consume(it.next());
}
```

### Method 83

```java
@Benchmark
public void serialize(Blackhole bh) throws IOException {
    ImmutableSetWithHashingStrategySerializationProxy<Integer> proxy = new ImmutableSetWithHashingStrategySerializationProxy<>(this.immutableSet, this.hashingStrategy);
    try (ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        proxy.writeExternal(oos);
        oos.flush();
        // prevent dead‑code elimination
        bh.consume(baos.toByteArray());
    }
}
```

### Method 84

```java
@Benchmark
public void serializeDeserialize(Blackhole bh) throws IOException, ClassNotFoundException {
    // Serialize into a fresh byte array each iteration.
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        oos.writeObject(immutableMap);
        oos.flush();
    }
    // Deserialize from the freshly created byte array.
    try (ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(baos.toByteArray()))) {
        @SuppressWarnings("unchecked")
        ImmutableSortedMap<Integer, String> deserialized = (ImmutableSortedMap<Integer, String>) ois.readObject();
        bh.consume(deserialized);
    }
}
```

### Method 85

```java
@Benchmark
public void spliteratorLarge(Blackhole bh) {
    var spliterator = largeInterval.spliterator();
    spliterator.forEachRemaining((IntConsumer) bh::consume);
}
```

## JMH IGNORED METHOD RETURN - Method return not used or consumed by a Blackhole.

### Method 1

```java
/* ---------------- Put Operations ---------------- */
@Benchmark
public MutableBiMap<Integer, Integer> unsync_put() {
    unsynchronizedMap.put(-1, -1);
    unsynchronizedMap.removeKey(-1);
    return unsynchronizedMap;
}
```

### Method 2

```java
/* ---------------- Put Operations ---------------- */
@Benchmark
public MutableBiMap<Integer, Integer> unsync_put() {
    unsynchronizedMap.put(-1, -1);
    unsynchronizedMap.removeKey(-1);
    return unsynchronizedMap;
}
```

### Method 3

```java
/* ---------------- Remove Operations ---------------- */
@Benchmark
public MutableBiMap<Integer, Integer> unsync_remove() {
    unsynchronizedMap.removeKey(size / 2);
    unsynchronizedMap.put(size / 2, size / 2);
    return unsynchronizedMap;
}
```

### Method 4

```java
/* ---------------- Remove Operations ---------------- */
@Benchmark
public MutableBiMap<Integer, Integer> unsync_remove() {
    unsynchronizedMap.removeKey(size / 2);
    unsynchronizedMap.put(size / 2, size / 2);
    return unsynchronizedMap;
}
```

### Method 5

```java
/* ------------------------------------- */
/* Mutating benchmarks */
/* ------------------------------------- */
@Benchmark
public ArrayAdapter<Integer> setElement() {
    // Mutate a middle element; returns the previous value (ignored).
    freshAdapter.set(500, -1);
    return freshAdapter;
}
```

### Method 6

```java
/* --------------------------------------------------------------------- */
/*  Write operations                                                    */
/* --------------------------------------------------------------------- */
@Benchmark
@Group("write")
// 2 concurrent writers
@GroupThreads(2)
public void addElement() {
    // Adding at the end; the list grows, but we keep the size bounded
    // by removing the first element to avoid unbounded memory growth.
    list.add(random.nextInt());
    list.remove(0);
}
```

### Method 7

```java
/* --------------------------------------------------------------------- */
/*  Write operations                                                    */
/* --------------------------------------------------------------------- */
@Benchmark
@Group("write")
// 2 concurrent writers
@GroupThreads(2)
public void addElement() {
    // Adding at the end; the list grows, but we keep the size bounded
    // by removing the first element to avoid unbounded memory growth.
    list.add(random.nextInt());
    list.remove(0);
}
```

### Method 8

```java
/* --------------------------------------------------------------------- */
/* Flip benchmark: invert key/value mapping.                            */
/* --------------------------------------------------------------------- */
@Benchmark
public void benchmarkFlip() {
    // Result is discarded; we only measure the operation.
    readOnlyMultimap.flip();
}
```

### Method 9

```java
/* --------------------------------------------------------------------- */
/* Reject benchmark: discard entries where key is odd.                  */
/* --------------------------------------------------------------------- */
@Benchmark
public void benchmarkRejectKeysValues() {
    Predicate2<Integer, Integer> predicate = (k, v) -> (k & 1) != 0;
    readOnlyMultimap.rejectKeysValues(predicate);
}
```

### Method 10

```java
/* --------------------------------------------------------------------- */
/* Select benchmark: keep only entries where key is even.               */
/* --------------------------------------------------------------------- */
@Benchmark
public void benchmarkSelectKeysValues() {
    Predicate2<Integer, Integer> predicate = (k, v) -> (k & 1) == 0;
    readOnlyMultimap.selectKeysValues(predicate);
}
```

### Method 11

```java
/* --------------------------------------------------------------------- */
/* Traversal benchmarks                                                   */
/* --------------------------------------------------------------------- */
@Benchmark
public void iteratorTraversal(BenchmarkState state) {
    var iterator = state.immutableSet.iterator();
    while (iterator.hasNext()) {
        iterator.next();
    }
}
```

### Method 12

```java
/* --------------------------------------------------------------------- */
/* Write benchmark: insertion of a new (key, value) pair.               */
/* --------------------------------------------------------------------- */
@Benchmark
public void benchmarkPut() {
    int key = random.nextInt(KEY_COUNT);
    int value = putCounter++;
    writeMultimap.put(key, value);
}
```

### Method 13

```java
/* --------------------------------------------------------------------- */
/* Write benchmarks */
/* --------------------------------------------------------------------- */
@Benchmark
public void putSingle(Blackhole bh) {
    // Use a fresh key to avoid collisions that could bias the measurement.
    int key = PREPOPULATED_SIZE + (int) (Math.random() * BATCH_SIZE);
    String value = valueFor(key);
    mutableMultimap.put(key, value);
    // Prevent dead‑code elimination.
    bh.consume(mutableMultimap);
}
```

### Method 14

```java
/**
 * Benchmark for a single put operation (new key).
 */
@Benchmark
public void putNewKey() {
    // Use a key that is not present to avoid overwriting.
    int newKey = SIZE + (int) (Math.random() * SIZE);
    map.put(newKey, "new-" + newKey);
}
```

### Method 15

```java
/**
 * Benchmark for a single put operation that updates an existing key.
 */
@Benchmark
public void putExistingKey() {
    int idx = (int) (Math.random() * SIZE);
    int key = keys[idx];
    map.put(key, "updated-" + key);
}
```

### Method 16

```java
/**
 * Benchmark for a single put operation.
 */
@Benchmark
public void putOne(BenchmarkState state) {
    int key = ThreadLocalRandom.current().nextInt(KEY_COUNT);
    int value = ThreadLocalRandom.current().nextInt();
    state.multimap.put(key, value);
}
```

### Method 17

```java
/**
 * Benchmark for a single remove operation.
 */
@Benchmark
public void remove() {
    int idx = (int) (Math.random() * SIZE);
    map.remove(keys[idx]);
}
```

### Method 18

```java
/**
 * Benchmark for addOccurrences – adds multiple copies of a single element.
 */
@Benchmark
public void addOccurrences() {
    mutableBag.addOccurrences(randomValues[0], 5);
}
```

### Method 19

```java
/**
 * Benchmark for adding a batch of elements.
 */
@Benchmark
public void addBatch() {
    for (int i = 0; i < BATCH_SIZE; i++) {
        mutableBag.add(randomValues[i]);
    }
}
```

### Method 20

```java
/**
 * Benchmark for flipping the multimap (producing a bag‑multimap).
 */
@Benchmark
public void flip(BenchmarkState state) {
    state.multimap.flip();
}
```

### Method 21

```java
/**
 * Benchmark for merging two pre‑populated {@link BigIntegerSummaryStatistics}.
 */
@Benchmark
public void mergeStatistics(MergeState state, Blackhole bh) {
    // The merge method mutates the left instance; we clone it to keep the benchmark idempotent.
    BigIntegerSummaryStatistics leftCopy = // copy left content
    new BigIntegerSummaryStatistics().// copy left content
    merge(state.left);
    leftCopy.merge(state.right);
    bh.consume(leftCopy);
}
```

### Method 22

```java
/**
 * Benchmark for rejecting key‑value pairs where the key is even.
 */
@Benchmark
public void rejectKeysValuesEven(BenchmarkState state) {
    state.multimap.rejectKeysValues((k, v) -> (k & 1) == 0);
}
```

### Method 23

```java
/**
 * Benchmark for removeOccurrences – removes multiple copies of a single element.
 */
@Benchmark
public void removeOccurrences() {
    mutableBag.removeOccurrences(randomValues[0], 3);
}
```

### Method 24

```java
/**
 * Benchmark for removing a batch of elements that are known to exist.
 */
@Benchmark
public void removeBatch() {
    // Ensure we have enough elements to remove; if not, repopulate
    if (mutableBag.size() < BATCH_SIZE) {
        mutableBag.clear();
        for (int i = 0; i < PREPOPULATED_SIZE; i++) {
            mutableBag.add(i);
        }
    }
    for (int i = 0; i < BATCH_SIZE; i++) {
        mutableBag.remove(randomValues[i]);
    }
}
```

### Method 25

```java
/**
 * Benchmark for removing a batch of elements that are known to exist.
 */
@Benchmark
public void removeBatch() {
    // Ensure we have enough elements to remove; if not, repopulate
    if (mutableBag.size() < BATCH_SIZE) {
        mutableBag.clear();
        for (int i = 0; i < PREPOPULATED_SIZE; i++) {
            mutableBag.add(i);
        }
    }
    for (int i = 0; i < BATCH_SIZE; i++) {
        mutableBag.remove(randomValues[i]);
    }
}
```

### Method 26

```java
/**
 * Benchmark for retrieving the collection associated with a key.
 */
@Benchmark
public void get(BenchmarkState state) {
    int key = state.keys[ThreadLocalRandom.current().nextInt(KEY_COUNT)];
    state.multimap.get(key);
}
```

### Method 27

```java
/**
 * Benchmark for selecting key‑value pairs where the key is even.
 */
@Benchmark
public void selectKeysValuesEven(BenchmarkState state) {
    state.multimap.selectKeysValues((k, v) -> (k & 1) == 0);
}
```

### Method 28

```java
/**
 * Benchmark for the clear operation.
 */
@Benchmark
public void clear() {
    map.clear();
    // Re‑populate to keep other benchmarks meaningful.
    for (int i = 0; i < SIZE; i++) {
        map.put(keys[i], values[i]);
    }
}
```

### Method 29

```java
/**
 * Benchmark for the flip operation (produces a Multimap).
 */
@Benchmark
public void flip() {
    map.flip();
}
```

### Method 30

```java
/**
 * Benchmark for {@code UnifiedSet.add(Object)}.
 */
@Benchmark
public void add(Blackhole bh) {
    // Add a random element and immediately remove it to keep the set size stable.
    int key = ThreadLocalRandom.current().nextInt(ELEMENT_COUNT * 10);
    boolean added = emptySet.add(key);
    bh.consume(added);
    // Remove the element to restore the original state.
    emptySet.remove(key);
}
```

### Method 31

```java
/**
 * Benchmark for {@code UnifiedSet.remove(Object)}.
 */
@Benchmark
public void remove(Blackhole bh) {
    // Remove a random element, then re‑insert it to keep the set size constant.
    int key = ThreadLocalRandom.current().nextInt(ELEMENT_COUNT * 10);
    // Ensure the key is present before removal.
    filledSet.add(key);
    boolean removed = filledSet.remove(key);
    bh.consume(removed);
}
```

### Method 32

```java
/**
 * Benchmark for {@code add} – adds a batch of random integers.
 */
@Benchmark
public void addElements(Blackhole bh) {
    for (int i = 0; i < ADD_BATCH_SIZE; i++) {
        int value = random.nextInt(Integer.MAX_VALUE);
        mutableSetForAdd.add(value);
    }
    // Prevent dead‑code elimination
    bh.consume(mutableSetForAdd);
}
```

### Method 33

```java
/**
 * Benchmark for {@code put} – inserting a new key/value pair.
 */
@Benchmark
public void put(Blackhole bh) {
    // ensure new key
    int key = size + random.nextInt(1000);
    int value = random.nextInt();
    multimap.put(key, value);
    bh.consume(multimap);
}
```

### Method 34

```java
/**
 * Benchmark removing a byte from a mutable set.
 */
@Benchmark
public void remove(Blackhole bh) {
    // ensure the set contains the element before removal
    if (mutableSet.isEmpty()) {
        mutableSet.addAll(ALL_BYTES);
    }
    int idx = counter.getAndIncrement() & 0xFF;
    byte value = ALL_BYTES[idx];
    boolean removed = mutableSet.remove(value);
    bh.consume(removed);
}
```

### Method 35

```java
/**
 * Benchmark the pop operation (throughput of pops per millisecond).
 */
@Benchmark
public void pop(PopPeekState state) {
    state.stack.pop();
}
```

### Method 36

```java
/**
 * Benchmark the {@code merge} method by merging two already populated
 * statistics objects.
 */
@Benchmark
public void benchmarkMerge(Blackhole bh) {
    BigDecimalSummaryStatistics leftCopy = new BigDecimalSummaryStatistics();
    leftCopy.merge(left);
    leftCopy.merge(right);
    bh.consume(leftCopy.getCount());
    bh.consume(leftCopy.getSum());
    bh.consume(leftCopy.getMinOptional());
    bh.consume(leftCopy.getMaxOptional());
    bh.consume(leftCopy.getAverage());
}
```

### Method 37

```java
/**
 * Benchmark the {@code merge} method by merging two already populated
 * statistics objects.
 */
@Benchmark
public void benchmarkMerge(Blackhole bh) {
    BigDecimalSummaryStatistics leftCopy = new BigDecimalSummaryStatistics();
    leftCopy.merge(left);
    leftCopy.merge(right);
    bh.consume(leftCopy.getCount());
    bh.consume(leftCopy.getSum());
    bh.consume(leftCopy.getMinOptional());
    bh.consume(leftCopy.getMaxOptional());
    bh.consume(leftCopy.getAverage());
}
```

### Method 38

```java
/**
 * Write operation: adds a new element to the set.
 */
@Benchmark
@Group("rw")
// one writer per group
@GroupThreads(1)
public void add(SharedState shared, ThreadState thread) {
    shared.set.add(thread.writeValue);
}
```

### Method 39

```java
/**
 * Write operation: removes an element from the set (to keep size bounded).
 */
@Benchmark
@Group("rw")
// one remover per group
@GroupThreads(1)
public void remove(SharedState shared, ThreadState thread) {
    // Remove a previously added element to avoid unbounded growth.
    shared.set.remove(thread.writeValue - 1);
}
```

### Method 40

```java
// -----------------------------------------------------------------
// Parallel iteration (creation only – actual work is delegated to JMH threads)
// -----------------------------------------------------------------
@Benchmark
public void asParallel() {
    set.asParallel(executorService, 1024);
}
```

### Method 41

```java
// Benchmark for a bulk operation that is synchronized internally
@Benchmark
public void putAll(Blackhole bh) {
    MutableMap<Integer, Integer> toPut = UnifiedMap.newMap(100);
    for (int i = 0; i < 100; i++) {
        toPut.put(random.nextInt(size * 10), random.nextInt());
    }
    syncMap.putAll(toPut);
    bh.consume(syncMap);
}
```

### Method 42

```java
// Optional: benchmark the parallel forEach to illustrate the parallel API.
@Benchmark
public void benchmarkParallelIteration(BenchmarkState state, Blackhole bh) {
    ExecutorService exec = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    try {
        state.set.asParallel(exec, 10_000).forEach(element -> bh.consume(element));
    } finally {
        exec.shutdownNow();
    }
}
```

### Method 43

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(java.util.concurrent.TimeUnit.MILLISECONDS)
public void benchPut() {
    map.put(ThreadLocalRandom.current().nextInt(), ThreadLocalRandom.current().nextInt());
}
```

### Method 44

```java
@Benchmark
@Group("put")
@GroupThreads(1)
public void putSingleThread() {
    int key = keyGenerator.incrementAndGet();
    multimap.put(key, key);
}
```

### Method 45

```java
@Benchmark
@Group("put")
@GroupThreads(3)
public void putConcurrent() {
    int key = keyGenerator.incrementAndGet();
    multimap.put(key, key);
}
```

### Method 46

```java
@Benchmark
@Group("write")
@GroupThreads(2)
public void sort() {
    // Sorting acquires a write lock; we sort a copy to keep the original order.
    // This mimics a realistic workload where sorting is occasional.
    MultiReaderList<Integer> copy = list.clone();
    copy.sortThis();
}
```

### Method 47

```java
@Benchmark
public ImmutableListMultimap<Integer, Integer> createMultimap() {
    var mutable = new org.eclipse.collections.impl.multimap.list.FastListMultimap<Integer, Integer>();
    for (int k = 0; k < keyCount; k++) {
        for (int v = 0; v < valuesPerKey; v++) {
            mutable.put(k, v);
        }
    }
    return mutable.toImmutable();
}
```

### Method 48

```java
@Benchmark
public Integer benchRemove() {
    int key = random.nextInt(size);
    Integer old = map.remove(key);
    map.put(key, key);
    return old;
}
```

### Method 49

```java
@Benchmark
public MultiReaderHashBagMultimap<Integer, String> putBenchmark() {
    MultiReaderHashBagMultimap<Integer, String> map = MultiReaderHashBagMultimap.newMultimap();
    for (int i = 0; i < ELEMENT_COUNT; i++) {
        map.put(i % KEY_RANGE, "v-" + i);
    }
    return map;
}
```

### Method 50

```java
@Benchmark
public MultiReaderUnifiedSetMultimap<Integer, Integer> put() {
    MultiReaderUnifiedSetMultimap<Integer, Integer> map = MultiReaderUnifiedSetMultimap.newMultimap();
    for (Pair<Integer, Integer> entry : entries) {
        map.put(entry.getOne(), entry.getTwo());
    }
    return map;
}
```

### Method 51

```java
@Benchmark
public MutableBag<Integer> addElements() {
    for (int e : elements) {
        bag.add(e);
    }
    return bag;
}
```

### Method 52

```java
@Benchmark
public MutableBag<Integer> removeElements() {
    // first fill the bag
    for (int e : elements) {
        bag.add(e);
    }
    // then remove the same elements
    for (int e : elements) {
        bag.remove(e);
    }
    return bag;
}
```

### Method 53

```java
@Benchmark
public MutableBag<Integer> removeElements() {
    // first fill the bag
    for (int e : elements) {
        bag.add(e);
    }
    // then remove the same elements
    for (int e : elements) {
        bag.remove(e);
    }
    return bag;
}
```

### Method 54

```java
@Benchmark
public MutableBag<Integer> selectByOccurrences() {
    // populate the bag with duplicate elements to create varying occurrence counts
    for (int i = 0; i < elements.length; i++) {
        // 1..5 occurrences
        int repetitions = (i % 5) + 1;
        for (int j = 0; j < repetitions; j++) {
            bag.add(elements[i]);
        }
    }
    // benchmark the selection based on occurrence predicate
    return bag.selectByOccurrences(OCCURRENCE_PREDICATE);
}
```

### Method 55

```java
@Benchmark
public MutableBag<Integer> trimToSize() {
    // fill the bag to trigger internal resizing
    for (int e : elements) {
        bag.add(e);
    }
    // benchmark the trim operation
    ((HashBag<Integer>) bag).trimToSize();
    return bag;
}
```

### Method 56

```java
@Benchmark
public MutableBiMap<Integer, Integer> sync_put() {
    synchronizedMap.put(-1, -1);
    synchronizedMap.removeKey(-1);
    return synchronizedMap;
}
```

### Method 57

```java
@Benchmark
public MutableBiMap<Integer, Integer> sync_put() {
    synchronizedMap.put(-1, -1);
    synchronizedMap.removeKey(-1);
    return synchronizedMap;
}
```

### Method 58

```java
@Benchmark
public MutableBiMap<Integer, Integer> sync_remove() {
    synchronizedMap.removeKey(size / 2);
    synchronizedMap.put(size / 2, size / 2);
    return synchronizedMap;
}
```

### Method 59

```java
@Benchmark
public MutableBiMap<Integer, Integer> sync_remove() {
    synchronizedMap.removeKey(size / 2);
    synchronizedMap.put(size / 2, size / 2);
    return synchronizedMap;
}
```

### Method 60

```java
@Benchmark
public boolean removeAtIndex() {
    // Remove element at a random valid index.
    if (list.isEmpty()) {
        return false;
    }
    int index = random.nextInt(list.size());
    list.removeAtIndex(index);
    return true;
}
```

### Method 61

```java
@Benchmark
public void add(Blackhole bh) {
    FastList<Integer> local = FastList.newList();
    for (int i = 0; i < size; i++) {
        local.add(i);
    }
    bh.consume(local);
}
```

### Method 62

```java
@Benchmark
public void addElement(BenchmarkState state) {
    state.bag.add(state.nextAdd);
}
```

### Method 63

```java
@Benchmark
public void benchPut() {
    map.put(putCounter++, putCounter);
}
```

### Method 64

```java
@Benchmark
public void benchmarkAdd(BenchmarkState state, Blackhole bh) {
    // Add a new element that is not present in the set.
    // Use modulo to wrap around the array and avoid unbounded growth.
    int idx = (int) (System.nanoTime() % state.newKeys.length);
    int key = state.newKeys[idx];
    boolean added = state.set.add(key);
    // Consume the result to prevent dead‑code elimination.
    bh.consume(added);
    // Remove the key again to keep the set size constant for subsequent iterations.
    state.set.remove(key);
}
```

### Method 65

```java
@Benchmark
public void benchmarkAdd(Blackhole bh) {
    // Adding a single element at the end of the composite list.
    // The element is removed immediately to keep the list size constant.
    compositeList.add(elementToAdd.getFirst());
    // Remove the element we just added to avoid side‑effects on subsequent iterations.
    compositeList.remove(compositeList.size() - 1);
    bh.consume(compositeList);
}
```

### Method 66

```java
@Benchmark
public void benchmarkAdd(Blackhole bh) {
    // Adding a single element at the end of the composite list.
    // The element is removed immediately to keep the list size constant.
    compositeList.add(elementToAdd.getFirst());
    // Remove the element we just added to avoid side‑effects on subsequent iterations.
    compositeList.remove(compositeList.size() - 1);
    bh.consume(compositeList);
}
```

### Method 67

```java
@Benchmark
public void benchmarkPartitionPredicate2Procedure() {
    source.forEach(predicate2Procedure);
    // Consume results to prevent dead‑code elimination
    partitionStack.getSelected().size();
    partitionStack.getRejected().size();
}
```

### Method 68

```java
@Benchmark
public void benchmarkPartitionPredicate2Procedure() {
    source.forEach(predicate2Procedure);
    // Consume results to prevent dead‑code elimination
    partitionStack.getSelected().size();
    partitionStack.getRejected().size();
}
```

### Method 69

```java
@Benchmark
public void benchmarkPartitionProcedure() {
    source.forEach(procedure);
    // Consume results to prevent dead‑code elimination
    partitionStack.getSelected().size();
    partitionStack.getRejected().size();
}
```

### Method 70

```java
@Benchmark
public void benchmarkPartitionProcedure() {
    source.forEach(procedure);
    // Consume results to prevent dead‑code elimination
    partitionStack.getSelected().size();
    partitionStack.getRejected().size();
}
```

### Method 71

```java
@Benchmark
public void benchmarkPut() {
    int key = random.nextInt(1_000);
    String value = "new-" + random.nextInt();
    multimap.put(key, value);
}
```

### Method 72

```java
@Benchmark
public void benchmarkPut(Blackhole bh) {
    // Each iteration adds a new entry; the key is chosen to cause contention
    int key = (int) (Math.random() * 1000);
    String value = "new-" + System.nanoTime();
    multimap.put(key, value);
    bh.consume(multimap);
}
```

### Method 73

```java
@Benchmark
public void benchmarkPut(Blackhole bh) {
    // Insert a new key/value pair; keys are generated sequentially to avoid collisions.
    int key = putKeyCounter++;
    int value = key * 31;
    putMap.put(key, value);
    // Consume the map to prevent dead‑code elimination.
    bh.consume(putMap);
}
```

### Method 74

```java
@Benchmark
public void benchmarkRemove(BenchmarkState state, Blackhole bh) {
    // Remove an element and immediately re‑add it to keep the set size stable.
    int idx = (int) (System.nanoTime() % state.removeKeys.length);
    int key = state.removeKeys[idx];
    Integer removed = state.set.removeFromPool(key);
    bh.consume(removed);
    // Re‑add the same key so that subsequent iterations see the same state.
    state.set.add(key);
}
```

### Method 75

```java
@Benchmark
public void collectValues() {
    Function<String, Integer> toLength = s -> s.length();
    multimap.collectValues(toLength);
}
```

### Method 76

```java
@Benchmark
public void collectValues() {
    multimap.collectValues(v -> v * v);
}
```

### Method 77

```java
@Benchmark
public void collectWithIndex() {
    ObjectIntToObjectFunction<Integer, String> func = (value, index) -> value + ":" + index;
    set.collectWithIndex(func);
}
```

### Method 78

```java
@Benchmark
public void flip() {
    multimap.flip();
}
```

### Method 79

```java
@Benchmark
public void flipMultimap() {
    multimap.flip();
}
```

### Method 80

```java
@Benchmark
public void getBag() {
    multimap.get(sampleKey);
}
```

### Method 81

```java
@Benchmark
public void getBagForKey() {
    int key = keys.get(0);
    multimap.get(key);
}
```

### Method 82

```java
@Benchmark
public void getValues() {
    multimap.get(SIZE / 2);
}
```

### Method 83

```java
@Benchmark
public void iterate() {
    // Simple iteration using the primitive iterator.
    var iterator = list.booleanIterator();
    while (iterator.hasNext()) {
        iterator.next();
    }
}
```

### Method 84

```java
@Benchmark
public void iterator() {
    Iterator<Integer> it = bag.iterator();
    while (it.hasNext()) {
        it.next();
    }
}
```

### Method 85

```java
@Benchmark
public void put() {
    multimap.put(benchmarkKey, benchmarkValue);
}
```

### Method 86

```java
@Benchmark
public void put(Blackhole bh) {
    int key = random.nextInt(size * 10);
    int value = random.nextInt();
    syncMap.put(key, value);
    bh.consume(syncMap);
}
```

### Method 87

```java
@Benchmark
public void putBatch() {
    for (int i = 0; i < BATCH; i++) {
        multimap.put(i, i);
    }
    for (int i = 0; i < BATCH; i++) {
        multimap.remove(i, i);
    }
}
```

### Method 88

```java
@Benchmark
public void putBatch() {
    for (int i = 0; i < BATCH; i++) {
        multimap.put(i, i);
    }
    for (int i = 0; i < BATCH; i++) {
        multimap.remove(i, i);
    }
}
```

### Method 89

```java
@Benchmark
public void putBatch(Blackhole bh) {
    // Insert a batch of entries in a tight loop.
    for (int i = 0; i < BATCH_SIZE; i++) {
        int key = PREPOPULATED_SIZE + i;
        mutableMultimap.put(key, valueFor(key));
    }
    bh.consume(mutableMultimap);
}
```

### Method 90

```java
@Benchmark
public void putNewMap(Blackhole bh) {
    TreeBagMultimap<Integer, Integer> map = new TreeBagMultimap<>();
    for (int i = 0; i < VALUE_COUNT; i++) {
        int key = i % KEY_COUNT;
        map.put(key, i);
    }
    bh.consume(map);
}
```

### Method 91

```java
@Benchmark
public void putNewValues() {
    syncMap.withKeyMultiValues(newKey, 1, 2, 3);
}
```

### Method 92

```java
@Benchmark
public void putSingle() {
    multimap.put(SIZE, SIZE);
    multimap.remove(SIZE, SIZE);
}
```

### Method 93

```java
@Benchmark
public void putSingle() {
    multimap.put(SIZE, SIZE);
    multimap.remove(SIZE, SIZE);
}
```

### Method 94

```java
@Benchmark
public void putSingle() {
    multimap.put(sampleKey, sampleValue);
}
```

### Method 95

```java
@Benchmark
public void putSingleEntry() {
    int key = keys.get(0);
    multimap.put(key, "new-value");
}
```

### Method 96

```java
@Benchmark
public void rejectKeysValues() {
    Predicate2<Integer, String> keyIsOdd = (k, v) -> k % 2 != 0;
    multimap.rejectKeysValues(keyIsOdd);
}
```

### Method 97

```java
@Benchmark
public void rejectKeysValues() {
    multimap.rejectKeysValues((k, v) -> k % 2 != 0);
}
```

### Method 98

```java
@Benchmark
public void remove() {
    multimap.remove(benchmarkKey, benchmarkValue);
}
```

### Method 99

```java
@Benchmark
public void removeByIndex(Blackhole bh) {
    // Remove from the end to avoid shifting cost dominating the benchmark
    FastList<Integer> local = FastList.newList(listForRemove);
    while (!local.isEmpty()) {
        local.remove(local.size() - 1);
    }
    bh.consume(local);
}
```

### Method 100

```java
@Benchmark
public void removeElement(BenchmarkState state) {
    state.bag.remove(state.nextRemove);
}
```

### Method 101

```java
@Benchmark
public void removeSingle() {
    multimap.removeAll(SIZE / 3);
    multimap.put(SIZE / 3, SIZE);
}
```

### Method 102

```java
@Benchmark
public void removeSingle() {
    multimap.removeAll(SIZE / 3);
    multimap.put(SIZE / 3, SIZE);
}
```

### Method 103

```java
@Benchmark
public void removeSingle(Blackhole bh) {
    // Remove a key that is guaranteed to exist.
    int key = (int) (Math.random() * (PREPOPULATED_SIZE / 10));
    mutableMultimap.removeAll(key);
    bh.consume(mutableMultimap);
}
```

### Method 104

```java
@Benchmark
public void selectKeysValues() {
    Predicate2<Integer, String> keyIsEven = (k, v) -> k % 2 == 0;
    multimap.selectKeysValues(keyIsEven);
}
```

### Method 105

```java
@Benchmark
public void selectKeysValues() {
    multimap.selectKeysValues((k, v) -> (k & 1) == 0 && (v & 1) == 0);
}
```

### Method 106

```java
@Benchmark
public void selectKeysValues() {
    multimap.selectKeysValues((k, v) -> k % 2 == 0);
}
```

### Method 107

```java
@Benchmark
public void set() {
    // set each position with a new value; values are deterministic
    list.set(0, 10);
    list.set(1, 20);
    list.set(2, 30);
    list.set(3, 40);
    list.set(4, 50);
}
```

### Method 108

```java
@Benchmark
public void set() {
    // set each position with a new value; values are deterministic
    list.set(0, 10);
    list.set(1, 20);
    list.set(2, 30);
    list.set(3, 40);
    list.set(4, 50);
}
```

### Method 109

```java
@Benchmark
public void set() {
    // set each position with a new value; values are deterministic
    list.set(0, 10);
    list.set(1, 20);
    list.set(2, 30);
    list.set(3, 40);
    list.set(4, 50);
}
```

### Method 110

```java
@Benchmark
public void set() {
    // set each position with a new value; values are deterministic
    list.set(0, 10);
    list.set(1, 20);
    list.set(2, 30);
    list.set(3, 40);
    list.set(4, 50);
}
```

### Method 111

```java
@Benchmark
public void set() {
    // set each position with a new value; values are deterministic
    list.set(0, 10);
    list.set(1, 20);
    list.set(2, 30);
    list.set(3, 40);
    list.set(4, 50);
}
```

### Method 112

```java
@Benchmark
public void toMutable() {
    multimap.toMutable();
}
```

### Method 113

```java
@Benchmark
public void writeAddOccurrence() {
    bag.addOccurrences(WRITE_KEY, 1);
}
```

### Method 114

```java
@Benchmark
public void writeRemove() {
    bag.removeOccurrences(WRITE_KEY, 1);
}
```

## JMH UNSAFELOOP INSIDE BENCHMARK - Suspicious numeric accumulation inside a loop in the JMH benchmark function.

### Method 1

```java
/* ---------- Iteration benchmarks ---------- */
@Benchmark
public long iterateMutableForEach() {
    long sum = 0;
    for (int i : mutableList) {
        sum += i;
    }
    return sum;
}
```

### Method 2

```java
/* ---------------- Iteration over entrySet ---------------- */
@Benchmark
public long unsync_iteration() {
    long sum = 0;
    for (Map.Entry<Integer, Integer> entry : unsynchronizedMap.entrySet()) {
        sum += entry.getKey() + entry.getValue();
    }
    return sum;
}
```

### Method 3

```java
/**
 * Benchmark for iterating over entries.
 */
@Benchmark
public long iterateEntries() {
    long sum = 0;
    for (Pair<Integer, String> entry : map.keyValuesView()) {
        sum += entry.getOne() + entry.getTwo().length();
    }
    return sum;
}
```

### Method 4

```java
/**
 * Benchmark for iterating over the whole bag using the iterator.
 */
@Benchmark
public long iterate() {
    long sum = 0L;
    for (Integer i : prepopulatedBag) {
        sum += i;
    }
    // return to prevent dead‑code elimination
    return sum;
}
```

### Method 5

```java
/**
 * Benchmark for iterating over values.
 */
@Benchmark
public long iterateValues() {
    long sum = 0;
    for (String v : map.values()) {
        sum += v.length();
    }
    return sum;
}
```

### Method 6

```java
/**
 * Benchmark for {@link FlatCollectIterable#iterator()}.
 */
@Benchmark
public long benchmarkIterator(Blackhole bh) {
    long sum = 0;
    for (Integer v : flatCollect) {
        sum += v;
    }
    bh.consume(sum);
    return sum;
}
```

### Method 7

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
public int benchmarkGet() {
    // Sum all elements to prevent dead‑code elimination
    int sum = 0;
    for (int i = 0; i < 6; i++) {
        sum += list.get(i);
    }
    return sum;
}
```

### Method 8

```java
@Benchmark
public int benchmarkUnboxIntegerToInt() {
    int sum = 0;
    for (Integer i : integerList) {
        sum += unboxIntegerToIntFn.intValueOf(i);
    }
    return sum;
}
```

### Method 9

```java
@Benchmark
public int benchmarkUnboxNumberToInt() {
    int sum = 0;
    for (Number n : numberList) {
        sum += unboxNumberToIntFn.intValueOf(n);
    }
    return sum;
}
```

### Method 10

```java
@Benchmark
public int iterate() {
    int sum = 0;
    for (Integer i : bag) {
        sum += i;
    }
    return sum;
}
```

### Method 11

```java
@Benchmark
public int iterate(BenchmarkState state) {
    int sum = 0;
    Iterator<Integer> it = state.bag.iterator();
    while (it.hasNext()) {
        sum += it.next();
    }
    // return to prevent dead‑code elimination
    return sum;
}
```

### Method 12

```java
@Benchmark
public int iterate(IterateState state) {
    int sum = 0;
    var it = state.bag.booleanIterator();
    while (it.hasNext()) {
        sum += it.next() ? 1 : 0;
    }
    return sum;
}
```

### Method 13

```java
@Benchmark
public int iterateBag(BenchmarkState state) {
    int sum = 0;
    for (Integer i : state.bag) {
        sum += i;
    }
    return sum;
}
```

### Method 14

```java
@Benchmark
public int plainIteration() {
    int sum = 0;
    while (plainIterator.hasNext()) {
        sum += plainIterator.next();
    }
    // Prevent dead‑code elimination
    return sum;
}
```

### Method 15

```java
@Benchmark
public int tapIteration() {
    int sum = 0;
    while (tapIterator.hasNext()) {
        sum += tapIterator.next();
    }
    // Prevent dead‑code elimination
    return sum;
}
```

### Method 16

```java
@Benchmark
public long benchIteration() {
    long sum = 0;
    for (Map.Entry<Integer, Integer> entry : readOnlyMap.entrySet()) {
        sum += entry.getValue();
    }
    return sum;
}
```

### Method 17

```java
@Benchmark
public long benchmarkIterateEntries() {
    long sum = 0;
    for (ObjectBooleanPair<Integer> entry : map.keyValuesView()) {
        sum += entry.getTwo() ? 1 : 0;
    }
    return sum;
}
```

### Method 18

```java
@Benchmark
public long benchmarkIterateKeys() {
    long sum = 0;
    for (Integer key : map.keySet()) {
        sum += key;
    }
    return sum;
}
```

### Method 19

```java
@Benchmark
public long benchmarkIterateValues() {
    long trueCount = 0;
    for (boolean v : map.values().toArray()) {
        if (v)
            trueCount++;
    }
    return trueCount;
}
```

### Method 20

```java
@Benchmark
public long iterate() {
    long sum = 0L;
    while (iterator.hasNext()) {
        sum += iterator.next();
    }
    // Return a value to prevent dead‑code elimination.
    return sum;
}
```

### Method 21

```java
@Benchmark
public long iterate(ThreadState state) {
    long sum = 0L;
    for (Integer i : state.syncSet) {
        sum += i;
    }
    return sum;
}
```

### Method 22

```java
@Benchmark
public long iterateUnmodifiableForEach() {
    long sum = 0;
    for (int i : unmodifiableList) {
        sum += i;
    }
    return sum;
}
```

### Method 23

```java
@Benchmark
public long iterateUnmodifiableJavaForEach() {
    long sum = 0;
    for (int i : unmodifiableJavaList) {
        sum += i;
    }
    return sum;
}
```

### Method 24

```java
@Benchmark
public long iteratorTraversal() {
    long sum = 0;
    for (Integer v : lazyIterable) {
        sum += v;
    }
    return sum;
}
```

### Method 25

```java
@Benchmark
public long sync_iteration() {
    long sum = 0;
    for (Map.Entry<Integer, Integer> entry : synchronizedMap.entrySet()) {
        sum += entry.getKey() + entry.getValue();
    }
    return sum;
}
```

### Method 26

```java
@Benchmark
public void get(Blackhole bh) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += list.get(i);
    }
    bh.consume(sum);
}
```

## JMH FIXTURE USING INVOCATION SCOPE - Fixture methods configured with Invocation scope. 

### Method 1

```java
/**
 * Clear the map after each benchmark invocation to keep the workload constant.
 */
@TearDown(Level.Invocation)
public void clearMap() {
    map.clear();
}
```

### Method 2

```java
/**
 * Initialise the list before each benchmark invocation to guarantee a clean state.
 */
@Setup(Level.Invocation)
public void setUp() {
    list = new DoubletonList<>(1, 2);
}
```

### Method 3

```java
/**
 * Reset the stack to its original size after each pop to keep throughput stable.
 */
@TearDown(Level.Invocation)
public void reset() {
    while (stack.size() < PRE_FILL_SIZE) {
        stack.push(stack.size());
    }
}
```

### Method 4

```java
@Setup(Level.Invocation)
public void clearPartition() {
    // Ensure each benchmark iteration starts with empty selected/rejected collections.
    partition.getSelected().clear();
    partition.getRejected().clear();
}
```

### Method 5

```java
@Setup(Level.Invocation)
public void reset() {
    // ensure the bag is in the same state before each remove operation
    // (re‑populate if it became empty)
    if (bag.isEmpty()) {
        setUp();
    }
}
```

### Method 6

```java
@Setup(Level.Invocation)
public void resetPartitionStack() {
    // Clear previous results before each invocation to avoid side‑effects
    partitionStack = new PartitionArrayStack<>();
    procedure = new PartitionProcedure<>(EVEN_PREDICATE, partitionStack);
    predicate2Procedure = new PartitionPredicate2Procedure<>(MOD_PREDICATE, 2, partitionStack);
}
```

### Method 7

```java
@Setup(Level.Invocation)
public void setUp() {
    // Use a fresh map for each invocation to avoid side‑effects from previous runs
    map = new HashMap<>();
    // Simple identity key function; replace with more complex logic if needed
    keyFunction = new Function<Integer, Integer>() {

        @Override
        public Integer valueOf(Integer obj) {
            return obj;
        }
    };
    // Create the procedure under test
    procedure = new GroupByUniqueKeyProcedure<>(map, keyFunction);
    // Generate a random element for each invocation to simulate realistic usage
    element = ThreadLocalRandom.current().nextInt();
}
```

### Method 8

```java
@Setup(Level.Invocation)
public void setUp() {
    bag.clear();
}
```

### Method 9

```java
@Setup(Level.Invocation)
public void setUp() {
    map = OrderedMapAdapter.adapt(new LinkedHashMap<>(size));
    for (int i = 0; i < size; i++) {
        map.put(i, i);
    }
}
```

### Method 10

```java
@Setup(Level.Invocation)
public void setUp() {
    stack = new ArrayStack<>();
}
```

### Method 11

```java
@Setup(Level.Invocation)
public void setUpInvocation() {
    // Create a fresh iterator for each benchmark invocation.
    iterator = new ImmutableIterator<>(data);
}
```

### Method 12

```java
@Setup(Level.Invocation)
public void setUpInvocation() {
    // Re‑create iterators for each benchmark invocation to avoid state carry‑over
    plainIterator = data.iterator();
    tapIterator = new TapIterator<>(data.iterator(), noopProcedure);
}
```

### Method 13

```java
@Setup(Level.Invocation)
public void setUpInvocation() {
    // start each benchmark with an empty bag
    bag = HashBag.newBag();
}
```

### Method 14

```java
@Setup(Level.Invocation)
public void setUpIteration() {
    // Create a new DistinctIterator for each benchmark invocation to avoid state carry‑over.
    distinctIterator = new DistinctIterator<>(sourceData);
}
```

### Method 15

```java
@Setup(Level.Trial)
public void setUp() throws IOException {
    bag = new HashBagWithHashingStrategy<>(STRING_HASHING_STRATEGY);
    // Populate with a realistic workload (e.g., 10 000 distinct strings, each with random multiplicity)
    for (int i = 0; i < 10_000; i++) {
        String element = "elem-" + i;
        // 1‑5 occurrences
        int occurrences = (i % 5) + 1;
        bag.addOccurrences(element, occurrences);
    }
    // Pre‑serialize once so the read benchmark can reuse the same byte array without re‑serializing each iteration.
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        new HashBagWithHashingStrategySerializationProxy<>(bag).writeExternal(oos);
        oos.flush();
        serializedData = baos.toByteArray();
    }
}
```

### Method 16

```java
@Setup(Level.Trial)
public void setUp() throws IOException {
    bag = new HashBagWithHashingStrategy<>(STRING_HASHING_STRATEGY);
    // Populate with a realistic workload (e.g., 10 000 distinct strings, each with random multiplicity)
    for (int i = 0; i < 10_000; i++) {
        String element = "elem-" + i;
        // 1‑5 occurrences
        int occurrences = (i % 5) + 1;
        bag.addOccurrences(element, occurrences);
    }
    // Pre‑serialize once so the read benchmark can reuse the same byte array without re‑serializing each iteration.
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        new HashBagWithHashingStrategySerializationProxy<>(bag).writeExternal(oos);
        oos.flush();
        serializedData = baos.toByteArray();
    }
}
```

### Method 17

```java
@TearDown(Level.Invocation)
public void tearDown() throws IOException {
    oos.close();
    baos.close();
}
```

### Method 18

```java
@TearDown(Level.Invocation)
public void tearDown() throws IOException {
    oos.close();
    baos.close();
}
```

### Method 19

```java
@TearDown(Level.Invocation)
public void tearDown() {
    map = null;
}
```

## JMH IGNORED STATIC METHOD RETURN - Static method return not used or consumed by a Blackhole.

### Method 1

```java
/* -------------------- Traversal using Spliterator -------------------- */
@Benchmark
public void spliteratorSmall(Blackhole bh) {
    var spliterator = smallInterval.spliterator();
    spliterator.forEachRemaining((IntConsumer) bh::consume);
}
```

### Method 2

```java
/* --------------------------------------------------------------------- */
/*  Parallel iteration (optional)                                       */
/* --------------------------------------------------------------------- */
@Benchmark
@Group("parallel")
@GroupThreads(4)
public void parallelForEach(Blackhole bh) {
    // Demonstrates the parallel view provided by the collection.
    list.asParallel(executor, 1_000).forEach(bh::consume);
}
```

### Method 3

```java
/* --------------------------------------------------------------------- */
/* Benchmark: Eclipse Collections {@code each} method.                  */
/* --------------------------------------------------------------------- */
@Benchmark
public void each(Blackhole bh) {
    composite.each(bh::consume);
}
```

### Method 4

```java
/**
 * Benchmark for iterating over the set using {@code forEach}.
 */
@Benchmark
public void forEach(Blackhole bh) {
    filledSet.forEach(bh::consume);
}
```

### Method 5

```java
/**
 * Benchmark for {@link FlatCollectIterable#each(org.eclipse.collections.api.block.procedure.Procedure)}.
 */
@Benchmark
public void benchmarkEach(Blackhole bh) {
    flatCollect.each(bh::consume);
}
```

### Method 6

```java
/**
 * Benchmark the {@code each} method which internally uses {@code Iterate.forEach}.
 */
@Benchmark
public void each(Blackhole bh) {
    selectIterable.each(bh::consume);
}
```

### Method 7

```java
// -------------------------------------------------------------------------
// Bulk write: getIfAbsentPutAll()
// -------------------------------------------------------------------------
@Benchmark
public MutableBag<String> getIfAbsentPutAll(BenchmarkState state) {
    return state.syncMultimap.getIfAbsentPutAll(state.key, java.util.Arrays.asList(state.values));
}
```

### Method 8

```java
// -------------------------------------------------------------------------
// Multi‑threaded scenario: 4 concurrent threads
// -------------------------------------------------------------------------
@Benchmark
@Threads(4)
public MutableBag<String> concurrentGet(BenchmarkState state) {
    return state.syncMultimap.get(state.key);
}
```

### Method 9

```java
// -------------------------------------------------------------------------
// Remove operation: removeAll()
// -------------------------------------------------------------------------
@Benchmark
public MutableBag<String> removeAll(BenchmarkState state) {
    return state.syncMultimap.removeAll(state.key);
}
```

### Method 10

```java
// -------------------------------------------------------------------------
// Simple read operation: get()
// -------------------------------------------------------------------------
@Benchmark
public MutableBag<String> get(BenchmarkState state) {
    return state.syncMultimap.get(state.key);
}
```

### Method 11

```java
// -------------------------------------------------------------------------
// Write operation: putOccurrences()
// -------------------------------------------------------------------------
@Benchmark
public void putOccurrences(BenchmarkState state) {
    state.syncMultimap.putOccurrences(state.key, "new-value", 1);
}
```

### Method 12

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
public void benchEach(Blackhole bh) {
    bag.each(bh::consume);
}
```

### Method 13

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
public void benchmarkEach(Blackhole bh) {
    // Use Blackhole to consume each element
    list.each((Procedure<Integer>) bh::consume);
}
```

### Method 14

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
public void each(Blackhole bh) {
    tripletonSet.each(bh::consume);
}
```

### Method 15

```java
@Benchmark
@Group("iteration")
@GroupThreads(1)
public void iterateValues(Blackhole bh) {
    map.forEachValue(bh::consume);
}
```

### Method 16

```java
@Benchmark
@Group("read")
@GroupThreads(4)
public void iterate(Blackhole bh) {
    // The internal iteration uses a read lock; we simply consume each element.
    list.forEach(bh::consume);
}
```

### Method 17

```java
@Benchmark
public MutableSet<MutableSet<Integer>> powerSet() {
    // powerSet grows exponentially; limit to small size to keep benchmark realistic
    Set<Integer> smallSet = new HashSet<>();
    IntStream.range(0, Math.min(12, size)).forEach(smallSet::add);
    return Sets.powerSet(smallSet);
}
```

### Method 18

```java
@Benchmark
public void benchmarkEach(BenchmarkState state, Blackhole bh) {
    state.takeIterable.each(bh::consume);
}
```

### Method 19

```java
@Benchmark
public void benchmarkEach(Blackhole bh) {
    integerIterable.each(bh::consume);
}
```

### Method 20

```java
@Benchmark
public void benchmarkEach(Blackhole bh) {
    lazyIterable.each(bh::consume);
}
```

### Method 21

```java
@Benchmark
public void benchmarkEach(Blackhole bh) {
    quadSet.each(bh::consume);
}
```

### Method 22

```java
@Benchmark
public void benchmarkEach(Blackhole bh) {
    singletonSet.each(bh::consume);
}
```

### Method 23

```java
@Benchmark
public void benchmarkEach(Blackhole bh) {
    this.booleanIterable.each((BooleanProcedure) bh::consume);
}
```

### Method 24

```java
@Benchmark
public void benchmarkForEach(Blackhole bh) {
    this.booleanIterable.forEach((BooleanProcedure) bh::consume);
}
```

### Method 25

```java
@Benchmark
public void benchmarkIterator(Blackhole bh) {
    integerIterable.iterator().forEachRemaining(bh::consume);
}
```

### Method 26

```java
@Benchmark
public void benchmarkIterator(Blackhole bh) {
    singletonSet.iterator().forEachRemaining(bh::consume);
}
```

### Method 27

```java
@Benchmark
public void each(Blackhole bh) {
    // Direct call to the each method
    dropWhileIterable.each(bh::consume);
}
```

### Method 28

```java
@Benchmark
public void each(Blackhole bh) {
    // invoke the each method; consume the values via Blackhole
    list.each(bh::consume);
}
```

### Method 29

```java
@Benchmark
public void each(Blackhole bh) {
    dropIterable.each(bh::consume);
}
```

### Method 30

```java
@Benchmark
public void each(Blackhole bh) {
    list.each(bh::consume);
}
```

### Method 31

```java
@Benchmark
public void each(Blackhole bh) {
    list.each(bh::consume);
}
```

### Method 32

```java
@Benchmark
public void eachProcedure(BenchmarkState state, Blackhole bh) {
    state.rejectIterable.each(bh::consume);
}
```

### Method 33

```java
@Benchmark
public void forEach(Blackhole bh) {
    batch.forEach((Procedure<Integer>) bh::consume);
}
```

### Method 34

```java
@Benchmark
public void iterate(BenchmarkState state, Blackhole bh) {
    state.set.iterator().forEachRemaining(bh::consume);
}
```

### Method 35

```java
@Benchmark
public void iteratePlain(Blackhole bh) {
    plainIterable.forEach(bh::consume);
}
```

### Method 36

```java
@Benchmark
public void iterateSynchronized(Blackhole bh) {
    synchronizedIterable.forEach(bh::consume);
}
```

### Method 37

```java
@Benchmark
public void iterator(Blackhole bh) {
    dropIterable.iterator().forEachRemaining(bh::consume);
}
```

### Method 38

```java
@Benchmark
public void keySetIteration(Blackhole bh) {
    tripletonMap.keySet().forEach(bh::consume);
}
```

### Method 39

```java
@Benchmark
public void spliteratorLarge(Blackhole bh) {
    var spliterator = largeInterval.spliterator();
    spliterator.forEachRemaining((IntConsumer) bh::consume);
}
```

### Method 40

```java
@Benchmark
public void valuesIteration(Blackhole bh) {
    tripletonMap.values().forEach(bh::consume);
}
```

## JMH STATE FINAL PRIMITIVE - JMH State primitive field declared final.

### Method 1

```java
package org.eclipse.collections.impl.multimap.bag;

import java.util.concurrent.TimeUnit;
import org.eclipse.collections.api.*;
import org.eclipse.collections.api.annotation.*;
import org.eclipse.collections.api.bag.*;
import org.eclipse.collections.api.bag.sorted.*;
import org.eclipse.collections.api.bimap.*;
import org.eclipse.collections.api.block.*;
import org.eclipse.collections.api.block.comparator.*;
import org.eclipse.collections.api.block.factory.*;
import org.eclipse.collections.api.block.function.*;
import org.eclipse.collections.api.block.predicate.*;
import org.eclipse.collections.api.block.procedure.*;
import org.eclipse.collections.api.collection.*;
import org.eclipse.collections.api.factory.*;
import org.eclipse.collections.api.factory.bag.*;
import org.eclipse.collections.api.factory.bag.sorted.*;
import org.eclipse.collections.api.factory.bag.strategy.*;
import org.eclipse.collections.api.factory.bimap.*;
import org.eclipse.collections.api.factory.list.*;
import org.eclipse.collections.api.factory.map.*;
import org.eclipse.collections.api.factory.map.sorted.*;
import org.eclipse.collections.api.factory.map.strategy.*;
import org.eclipse.collections.api.factory.set.*;
import org.eclipse.collections.api.factory.set.sorted.*;
import org.eclipse.collections.api.factory.set.strategy.*;
import org.eclipse.collections.api.factory.stack.*;
import org.eclipse.collections.api.list.*;
import org.eclipse.collections.api.map.*;
import org.eclipse.collections.api.map.primitive.*;
import org.eclipse.collections.api.map.sorted.*;
import org.eclipse.collections.api.multimap.*;
import org.eclipse.collections.api.multimap.bag.*;
import org.eclipse.collections.api.multimap.list.*;
import org.eclipse.collections.api.multimap.ordered.*;
import org.eclipse.collections.api.multimap.set.*;
import org.eclipse.collections.api.multimap.sortedbag.*;
import org.eclipse.collections.api.multimap.sortedset.*;
import org.eclipse.collections.api.ordered.*;
import org.eclipse.collections.api.partition.*;
import org.eclipse.collections.api.partition.bag.*;
import org.eclipse.collections.api.partition.bag.sorted.*;
import org.eclipse.collections.api.partition.list.*;
import org.eclipse.collections.api.partition.ordered.*;
import org.eclipse.collections.api.partition.set.*;
import org.eclipse.collections.api.partition.set.sorted.*;
import org.eclipse.collections.api.partition.stack.*;
import org.eclipse.collections.api.set.*;
import org.eclipse.collections.api.set.sorted.*;
import org.eclipse.collections.api.stack.*;
import org.eclipse.collections.api.tuple.*;
import org.eclipse.collections.impl.*;
import org.eclipse.collections.impl.bag.*;
import org.eclipse.collections.impl.bag.immutable.*;
import org.eclipse.collections.impl.bag.mutable.*;
import org.eclipse.collections.impl.bag.mutable.primitive.*;
import org.eclipse.collections.impl.bag.sorted.immutable.*;
import org.eclipse.collections.impl.bag.sorted.mutable.*;
import org.eclipse.collections.impl.bag.strategy.mutable.*;
import org.eclipse.collections.impl.bimap.*;
import org.eclipse.collections.impl.bimap.immutable.*;
import org.eclipse.collections.impl.bimap.mutable.*;
import org.eclipse.collections.impl.block.comparator.*;
import org.eclipse.collections.impl.block.factory.*;
import org.eclipse.collections.impl.block.factory.primitive.*;
import org.eclipse.collections.impl.block.function.*;
import org.eclipse.collections.impl.block.function.checked.*;
import org.eclipse.collections.impl.block.function.primitive.*;
import org.eclipse.collections.impl.block.predicate.*;
import org.eclipse.collections.impl.block.predicate.checked.*;
import org.eclipse.collections.impl.block.predicate.primitive.*;
import org.eclipse.collections.impl.block.procedure.*;
import org.eclipse.collections.impl.block.procedure.checked.*;
import org.eclipse.collections.impl.block.procedure.checked.primitive.*;
import org.eclipse.collections.impl.block.procedure.primitive.*;
import org.eclipse.collections.impl.collection.*;
import org.eclipse.collections.impl.collection.immutable.*;
import org.eclipse.collections.impl.collection.mutable.*;
import org.eclipse.collections.impl.collector.*;
import org.eclipse.collections.impl.factory.*;
import org.eclipse.collections.impl.forkjoin.*;
import org.eclipse.collections.impl.lazy.*;
import org.eclipse.collections.impl.lazy.iterator.*;
import org.eclipse.collections.impl.lazy.parallel.*;
import org.eclipse.collections.impl.lazy.parallel.bag.*;
import org.eclipse.collections.impl.lazy.parallel.list.*;
import org.eclipse.collections.impl.lazy.parallel.set.*;
import org.eclipse.collections.impl.lazy.parallel.set.sorted.*;
import org.eclipse.collections.impl.lazy.primitive.*;
import org.eclipse.collections.impl.list.*;
import org.eclipse.collections.impl.list.fixed.*;
import org.eclipse.collections.impl.list.immutable.*;
import org.eclipse.collections.impl.list.immutable.primitive.*;
import org.eclipse.collections.impl.list.mutable.*;
import org.eclipse.collections.impl.list.mutable.primitive.*;
import org.eclipse.collections.impl.list.primitive.*;
import org.eclipse.collections.impl.map.*;
import org.eclipse.collections.impl.map.fixed.*;
import org.eclipse.collections.impl.map.immutable.*;
import org.eclipse.collections.impl.map.mutable.*;
import org.eclipse.collections.impl.map.mutable.primitive.*;
import org.eclipse.collections.impl.map.ordered.mutable.*;
import org.eclipse.collections.impl.map.sorted.immutable.*;
import org.eclipse.collections.impl.map.sorted.mutable.*;
import org.eclipse.collections.impl.map.strategy.immutable.*;
import org.eclipse.collections.impl.map.strategy.mutable.*;
import org.eclipse.collections.impl.multimap.*;
import org.eclipse.collections.impl.multimap.bag.*;
import org.eclipse.collections.impl.multimap.bag.sorted.*;
import org.eclipse.collections.impl.multimap.bag.sorted.immutable.*;
import org.eclipse.collections.impl.multimap.bag.sorted.mutable.*;
import org.eclipse.collections.impl.multimap.bag.strategy.*;
import org.eclipse.collections.impl.multimap.list.*;
import org.eclipse.collections.impl.multimap.set.*;
import org.eclipse.collections.impl.multimap.set.sorted.*;
import org.eclipse.collections.impl.multimap.set.strategy.*;
import org.eclipse.collections.impl.parallel.*;
import org.eclipse.collections.impl.partition.bag.*;
import org.eclipse.collections.impl.partition.bag.sorted.*;
import org.eclipse.collections.impl.partition.list.*;
import org.eclipse.collections.impl.partition.set.*;
import org.eclipse.collections.impl.partition.set.sorted.*;
import org.eclipse.collections.impl.partition.set.strategy.*;
import org.eclipse.collections.impl.partition.stack.*;
import org.eclipse.collections.impl.set.*;
import org.eclipse.collections.impl.set.fixed.*;
import org.eclipse.collections.impl.set.immutable.*;
import org.eclipse.collections.impl.set.immutable.primitive.*;
import org.eclipse.collections.impl.set.mutable.*;
import org.eclipse.collections.impl.set.mutable.primitive.*;
import org.eclipse.collections.impl.set.sorted.immutable.*;
import org.eclipse.collections.impl.set.sorted.mutable.*;
import org.eclipse.collections.impl.set.strategy.immutable.*;
import org.eclipse.collections.impl.set.strategy.mutable.*;
import org.eclipse.collections.impl.stack.immutable.*;
import org.eclipse.collections.impl.stack.mutable.*;
import org.eclipse.collections.impl.stream.*;
import org.eclipse.collections.impl.string.immutable.*;
import org.eclipse.collections.impl.tuple.*;
import org.eclipse.collections.impl.tuple.primitive.*;
import org.eclipse.collections.impl.utility.*;
import org.eclipse.collections.impl.utility.internal.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public class SynchronizedBagMultimapBenchmark {

    @State(Scope.Benchmark)
    public static class BenchmarkState {

        // Underlying mutable multimap (unsynchronized) used as delegate
        MutableBagMultimap<Integer, String> delegate;

        // Synchronized wrapper under test
        SynchronizedBagMultimap<Integer, String> syncMultimap;

        // Keys and values used in benchmarks
        final int key = 42;

        final String[] values = { "a", "b", "c", "d", "e" };

        @Setup(Level.Trial)
        public void setUp() {
            // Populate delegate with a moderate amount of data
            delegate = new HashBagMultimap<>();
            for (int i = 0; i < 10_000; i++) {
                delegate.put(i % 100, "value-" + i);
            }
            // Create synchronized view
            syncMultimap = SynchronizedBagMultimap.of(delegate);
        }

        @TearDown(Level.Trial)
        public void tearDown() {
            delegate = null;
            syncMultimap = null;
        }
    }

    // -------------------------------------------------------------------------
    // Simple read operation: get()
    // -------------------------------------------------------------------------
    @Benchmark
    public MutableBag<String> get(BenchmarkState state) {
        return state.syncMultimap.get(state.key);
    }

    // -------------------------------------------------------------------------
    // Write operation: putOccurrences()
    // -------------------------------------------------------------------------
    @Benchmark
    public void putOccurrences(BenchmarkState state) {
        state.syncMultimap.putOccurrences(state.key, "new-value", 1);
    }

    // -------------------------------------------------------------------------
    // Bulk write: getIfAbsentPutAll()
    // -------------------------------------------------------------------------
    @Benchmark
    public MutableBag<String> getIfAbsentPutAll(BenchmarkState state) {
        return state.syncMultimap.getIfAbsentPutAll(state.key, java.util.Arrays.asList(state.values));
    }

    // -------------------------------------------------------------------------
    // Remove operation: removeAll()
    // -------------------------------------------------------------------------
    @Benchmark
    public MutableBag<String> removeAll(BenchmarkState state) {
        return state.syncMultimap.removeAll(state.key);
    }

    // -------------------------------------------------------------------------
    // Transformation operation: collectValues()
    // -------------------------------------------------------------------------
    @Benchmark
    public MutableBagMultimap<Integer, Integer> collectValues(BenchmarkState state) {
        return state.syncMultimap.collectValues(v -> v.length());
    }

    // -------------------------------------------------------------------------
    // Multi‑threaded scenario: 4 concurrent threads
    // -------------------------------------------------------------------------
    @Benchmark
    @Threads(4)
    public MutableBag<String> concurrentGet(BenchmarkState state) {
        return state.syncMultimap.get(state.key);
    }
}
```

## JMH DEAD STORE VARIABLE - Dead store to local variable in JMH benchmark

### Method 1

```java
@Benchmark
public Integer iteratorNext() {
    var it = doubletonSet.iterator();
    Integer first = it.next();
    Integer second = it.next();
    return second;
}
```

