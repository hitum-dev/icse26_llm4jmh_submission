## JMH STATE FINAL STATIC PRIMITIVE - JMH State primitive static field declared final.

### Method 1

```java
/*
 * Copyright (c) 2023 The Bank of New York Mellon.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.list;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.LongAdder;

import org.eclipse.collections.api.list.ImmutableList;
import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.Counter;
import org.eclipse.collections.impl.factory.Lists;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.primitive.LongInterval;
import org.eclipse.collections.impl.utility.ArrayListIterate;
import org.eclipse.collections.impl.utility.Iterate;
import org.eclipse.collections.impl.utility.ListIterate;
import org.junit.After;
import org.junit.Before;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 3)
@Measurement(iterations = 10, time = 3)
public class JDKListIterationTest
{
    private static final int SIZE = 100_000;

    private final List<Long> longs = LongInterval.zeroTo(SIZE).collect(Long::valueOf).castToList();
    private final ArrayList<Long> arrayList = new ArrayList<>(this.longs);
    private final List<Long> synchArrayList = Collections.synchronizedList(new ArrayList<>(this.longs));
    private final CopyOnWriteArrayList<Long> cowaList = new CopyOnWriteArrayList<>(this.longs);

    @Before
    @Setup
    public void setUp()
    {
    }

    @After
    @TearDown
    public void tearDown() throws InterruptedException
    {
    }

    @Benchmark
    public long arrayList_iterate_forEach()
    {
        LongAdder adder = new LongAdder();
        Iterate.forEach(this.arrayList, adder::add);
        return adder.longValue();
    }

    @Benchmark
    public long arrayList_arrayListIterate_forEach()
    {
        LongAdder adder = new LongAdder();
        ArrayListIterate.forEach(this.arrayList, adder::add);
        return adder.longValue();
    }

    @Benchmark
    public long cowal_iterate_forEach()
    {
        LongAdder adder = new LongAdder();
        Iterate.forEach(this.cowaList, adder::add);
        return adder.longValue();
    }

    @Benchmark
    public long cowal_listIterate_forEach()
    {
        LongAdder adder = new LongAdder();
        ListIterate.forEach(this.cowaList, adder::add);
        return adder.longValue();
    }

    @Benchmark
    public long synchArrayList_iterate_forEach()
    {
        LongAdder adder = new LongAdder();
        Iterate.forEach(this.synchArrayList, adder::add);
        return adder.longValue();
    }

    @Benchmark
    public long synchArrayList_listIterate_forEach()
    {
        LongAdder adder = new LongAdder();
        ListIterate.forEach(this.synchArrayList, adder::add);
        return adder.longValue();
    }
}
```

### Method 2

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.list;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.api.list.ImmutableList;
import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.factory.Lists;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.junit.After;
import org.junit.Before;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class ListIterationTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    private final MutableList<Integer> ecMutable = Lists.mutable.withAll(Interval.zeroTo(SIZE));
    private final ImmutableList<Integer> ecImmutable = Lists.immutable.withAll(Interval.zeroTo(SIZE));

    private ExecutorService executorService;

    @Before
    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @After
    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_mutable_ec()
    {
        int count = this.ecMutable
                .asLazy()
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void serial_immutable_ec()
    {
        int count = this.ecImmutable
                .asLazy()
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void parallel_mutable_ec()
    {
        int count = this.ecMutable
                .asParallel(this.executorService, BATCH_SIZE)
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void parallel_immutable_ec()
    {
        int count = this.ecImmutable
                .asParallel(this.executorService, BATCH_SIZE)
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void serial_mutable_scala()
    {
        ScalaListIterationTest.serial_mutable_scala();
    }

    @Benchmark
    public void parallel_mutable_scala()
    {
        ScalaListIterationTest.parallel_mutable_scala();
    }
}
```

### Method 3

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.list;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.api.list.ImmutableList;
import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.factory.Lists;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.junit.After;
import org.junit.Before;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class ListIterationTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    private final MutableList<Integer> ecMutable = Lists.mutable.withAll(Interval.zeroTo(SIZE));
    private final ImmutableList<Integer> ecImmutable = Lists.immutable.withAll(Interval.zeroTo(SIZE));

    private ExecutorService executorService;

    @Before
    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @After
    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_mutable_ec()
    {
        int count = this.ecMutable
                .asLazy()
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void serial_immutable_ec()
    {
        int count = this.ecImmutable
                .asLazy()
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void parallel_mutable_ec()
    {
        int count = this.ecMutable
                .asParallel(this.executorService, BATCH_SIZE)
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void parallel_immutable_ec()
    {
        int count = this.ecImmutable
                .asParallel(this.executorService, BATCH_SIZE)
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void serial_mutable_scala()
    {
        ScalaListIterationTest.serial_mutable_scala();
    }

    @Benchmark
    public void parallel_mutable_scala()
    {
        ScalaListIterationTest.parallel_mutable_scala();
    }
}
```

### Method 4

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.carrotsearch.hppc.Containers;
import com.carrotsearch.hppc.ObjectObjectHashMap;
import com.carrotsearch.hppc.ObjectObjectMap;
import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.map.MutableMap;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.map.mutable.UnifiedMap;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;
import scala.collection.mutable.HashTable;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class ChainMapPutTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    @Param({"true", "false"})
    public boolean isPresized;
    @Param({"0.70f", "0.75f", "0.80f"})
    public float loadFactor;
    private String[] elements;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            this.elements[i] = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
        }
    }

    @Benchmark
    public MutableMap<String, String> ec()
    {
        int localSize = this.size;
        float localLoadFactor = this.loadFactor;
        String[] localElements = this.elements;
        /**
         * @see UnifiedMap#DEFAULT_INITIAL_CAPACITY
         */
        int defaultInitialCapacity = 8;

        MutableMap<String, String> ec = this.isPresized
                ? UnifiedMap.newMap(localSize, localLoadFactor)
                : UnifiedMap.newMap(defaultInitialCapacity, localLoadFactor);

        for (int i = 0; i < localSize; i++)
        {
            ec.put(localElements[i], "dummy");
        }
        return ec;
    }

    @Benchmark
    public ObjectObjectMap<String, String> hppc()
    {
        int localSize = this.size;
        float localLoadFactor = this.loadFactor;
        String[] localElements = this.elements;
        int defaultInitialCapacity = Containers.DEFAULT_EXPECTED_ELEMENTS;

        ObjectObjectMap<String, String> hppc = this.isPresized
                ? new ObjectObjectHashMap<>(localSize, localLoadFactor)
                : new ObjectObjectHashMap<>(defaultInitialCapacity, localLoadFactor);

        for (int i = 0; i < localSize; i++)
        {
            hppc.put(localElements[i], "dummy");
        }
        return hppc;
    }

    @Benchmark
    public Map<String, String> jdk()
    {
        int localSize = this.size;
        float localLoadFactor = this.loadFactor;
        String[] localElements = this.elements;

        /**
         * @see HashMap#DEFAULT_INITIAL_CAPACITY
         */
        int defaultInitialCapacity = 16;

        Map<String, String> jdk = this.isPresized
                ? new HashMap<>(localSize, localLoadFactor)
                : new HashMap<>(defaultInitialCapacity, localLoadFactor);

        for (int i = 0; i < localSize; i++)
        {
            jdk.put(localElements[i], "dummy");
        }
        return jdk;
    }

    @Benchmark
    public scala.collection.mutable.HashMap<String, String> scala()
    {
        int localSize = this.size;
        if (Float.compare(this.loadFactor, 0.75f) != 0)
        {
            throw new IllegalArgumentException();
        }
        String[] localElements = this.elements;

        /**
         * @see HashTable#initialSize()
         */
        int defaultInitialSize = 16;

        scala.collection.mutable.HashMap<String, String> scala = this.isPresized
                ? new PresizableHashMap<>(localSize)
                : new PresizableHashMap<>(defaultInitialSize);

        for (int i = 0; i < localSize; i++)
        {
            scala.put(localElements[i], "dummy");
        }
        return scala;
    }
}
```

### Method 5

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.TimeUnit;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class JdkMutableMapGetTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    private String[] elements;
    private Map<String, String> jdkMap;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];
        this.jdkMap = new HashMap<>(this.size);

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            String element = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
            this.elements[i] = element;
            this.jdkMap.put(element, "dummy");
        }
    }

    @Benchmark
    public void get()
    {
        int localSize = this.size;
        String[] localElements = this.elements;
        Map<String, String> localJdkMap = this.jdkMap;

        for (int i = 0; i < localSize; i++)
        {
            if (localJdkMap.get(localElements[i]) == null)
            {
                throw new AssertionError(i);
            }
        }
    }
}
```

### Method 6

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.carrotsearch.hppc.ObjectObjectHashMap;
import com.carrotsearch.hppc.ObjectObjectMap;
import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class HppcMutableMapGetTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    private String[] elements;
    private ObjectObjectMap<String, String> hppcMap;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];
        this.hppcMap = new ObjectObjectHashMap<>(this.size);

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            String element = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
            this.elements[i] = element;
            this.hppcMap.put(element, "dummy");
        }
    }

    @Benchmark
    public void get()
    {
        int localSize = this.size;
        String[] localElements = this.elements;
        ObjectObjectMap<String, String> localHppcMap = this.hppcMap;

        for (int i = 0; i < localSize; i++)
        {
            if (localHppcMap.get(localElements[i]) == null)
            {
                throw new AssertionError(i);
            }
        }
    }
}
```

### Method 7

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.ObjObjMap;
import com.koloboke.collect.map.hash.HashObjObjMaps;
import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class KolobokeMapPutTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    @Param({"true", "false"})
    public boolean isPresized;
    @Param("0.75")
    public float loadFactor; //Adding a loadFactor for only ease of data plots
    private String[] elements;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            this.elements[i] = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
        }
    }

    @Benchmark
    public ObjObjMap<String, String> koloboke()
    {
        int localSize = this.size;
        String[] localElements = this.elements;

        ObjObjMap<String, String> koloboke = this.isPresized
                ? HashObjObjMaps.newMutableMap(localSize)
                : HashObjObjMaps.newMutableMap();

        for (int i = 0; i < localSize; i++)
        {
            koloboke.put(localElements[i], "dummy");
        }
        return koloboke;
    }
}
```

### Method 8

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.ObjObjMap;
import com.koloboke.collect.map.hash.HashObjObjMaps;
import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class KolobokeMutableMapGetTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    private String[] elements;
    private ObjObjMap<String, String> kolobokeMap;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];
        this.kolobokeMap = HashObjObjMaps.newMutableMap(this.size);

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            String element = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
            this.elements[i] = element;
            this.kolobokeMap.put(element, "dummy");
        }
    }

    @Benchmark
    public void get()
    {
        int localSize = this.size;
        String[] localElements = this.elements;
        ObjObjMap<String, String> localKolobokeMap = this.kolobokeMap;

        for (int i = 0; i < localSize; i++)
        {
            if (localKolobokeMap.get(localElements[i]) == null)
            {
                throw new AssertionError(i);
            }
        }
    }
}
```

### Method 9

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import gnu.trove.impl.Constants;
import gnu.trove.map.TMap;
import gnu.trove.map.hash.THashMap;
import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class TroveMapPutTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    @Param({"true", "false"})
    public boolean isPresized;
    @Param({"0.45", "0.50", "0.55"})
    public float loadFactor;
    private String[] elements;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            this.elements[i] = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
        }
    }

    @Benchmark
    public TMap<String, String> trove()
    {
        int localSize = this.size;
        float localLoadFactor = this.loadFactor;
        String[] localElements = this.elements;
        int defaultInitialCapacity = Constants.DEFAULT_CAPACITY;

        TMap<String, String> trove = this.isPresized
                ? new THashMap<>(localSize, localLoadFactor)
                : new THashMap<>(defaultInitialCapacity, localLoadFactor);

        for (int i = 0; i < localSize; i++)
        {
            trove.put(localElements[i], "dummy");
        }
        return trove;
    }
}
```

### Method 10

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import gnu.trove.map.TMap;
import gnu.trove.map.hash.THashMap;
import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class TroveMutableMapGetTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    private String[] elements;
    private TMap<String, String> troveMap;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];
        this.troveMap = new THashMap<>(this.size);

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            String element = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
            this.elements[i] = element;
            this.troveMap.put(element, "dummy");
        }
    }

    @Benchmark
    public void get()
    {
        int localSize = this.size;
        String[] localElements = this.elements;
        TMap<String, String> localTroveMap = this.troveMap;

        for (int i = 0; i < localSize; i++)
        {
            if (localTroveMap.get(localElements[i]) == null)
            {
                throw new AssertionError(i);
            }
        }
    }
}
```

### Method 11

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.map.ImmutableMap;
import org.eclipse.collections.api.map.MutableMap;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.map.mutable.UnifiedMap;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class EcImmutableMapGetTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    private String[] elements;
    private ImmutableMap<String, String> ecMap;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];
        MutableMap<String, String> map = UnifiedMap.newMap(this.size);

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            String element = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
            this.elements[i] = element;
            map.put(element, "dummy");
        }

        this.ecMap = map.toImmutable();
    }

    @Benchmark
    public void get()
    {
        int localSize = this.size;
        String[] localElements = this.elements;
        ImmutableMap<String, String> localEcMap = this.ecMap;

        for (int i = 0; i < localSize; i++)
        {
            if (localEcMap.get(localElements[i]) == null)
            {
                throw new AssertionError(i);
            }
        }
    }
}
```

### Method 12

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.map.MutableMap;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.map.mutable.UnifiedMap;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class EcMutableMapGetTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    private String[] elements;
    private MutableMap<String, String> ecMap;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];
        this.ecMap = UnifiedMap.newMap(this.size);

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            String element = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
            this.elements[i] = element;
            this.ecMap.put(element, "dummy");
        }
    }

    @Benchmark
    public void get()
    {
        int localSize = this.size;
        String[] localElements = this.elements;
        MutableMap<String, String> localEcMap = this.ecMap;

        for (int i = 0; i < localSize; i++)
        {
            if (localEcMap.get(localElements[i]) == null)
            {
                throw new AssertionError(i);
            }
        }
    }
}
```

### Method 13

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.map.MutableMap;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.map.mutable.UnifiedMap;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;
import scala.collection.immutable.HashMap$;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MapGrowthTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;

    private String[] elements;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            this.elements[i] = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
        }
    }

    @Benchmark
    public MutableMap<String, String> mutableEcPut()
    {
        int localSize = this.size;
        /**
         * @see UnifiedMap#DEFAULT_LOAD_FACTOR
         */
        float localLoadFactor = 0.75f;
        String[] localElements = this.elements;

        MutableMap<String, String> map = UnifiedMap.newMap(localSize, localLoadFactor);

        for (int i = 0; i < localSize; i++)
        {
            map.put(localElements[i], "dummy");
        }
        return map;
    }

    @Benchmark
    public scala.collection.mutable.HashMap<String, String> mutableScalaPut()
    {
        int localSize = this.size;
        String[] localElements = this.elements;

        scala.collection.mutable.HashMap<String, String> map = new PresizableHashMap<>(localSize);

        for (int i = 0; i < localSize; i++)
        {
            map.put(localElements[i], "dummy");
        }
        return map;
    }

    @Benchmark
    public scala.collection.immutable.Map<String, String> immutableScalaPut()
    {
        int localSize = this.size;
        String[] localElements = this.elements;

        scala.collection.immutable.Map<String, String> map = HashMap$.MODULE$.empty();

        for (int i = 0; i < localSize; i++)
        {
            map = map.updated(localElements[i], "dummy");
        }
        return map;
    }
}
```

### Method 14

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;
import scala.collection.immutable.HashMap$;
import scala.collection.immutable.Map;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class ScalaImmutableMapGetTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    private String[] elements;
    private Map<String, String> scalaMap;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];
        Map<String, String> map = HashMap$.MODULE$.empty();

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            String element = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
            this.elements[i] = element;
            map = map.updated(element, "dummy");
        }

        this.scalaMap = map;
    }

    @Benchmark
    public void get()
    {
        int localSize = this.size;
        String[] localElements = this.elements;
        Map<String, String> localScalaMap = this.scalaMap;

        for (int i = 0; i < localSize; i++)
        {
            if (!localScalaMap.get(localElements[i]).isDefined())
            {
                throw new AssertionError(i);
            }
        }
    }
}
```

### Method 15

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;
import scala.collection.mutable.AnyRefMap;
import scala.collection.mutable.Map;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class ScalaAnyRefMapGetTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    private String[] elements;
    private Map<String, String> scalaAnyRefMap;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];
        this.scalaAnyRefMap = new AnyRefMap<>(this.size);

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            String element = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
            this.elements[i] = element;
            this.scalaAnyRefMap.put(element, "dummy");
        }
    }

    @Benchmark
    public void get()
    {
        int localSize = this.size;
        String[] localElements = this.elements;
        Map<String, String> localScalaAnyRefMap = this.scalaAnyRefMap;

        for (int i = 0; i < localSize; i++)
        {
            if (!localScalaAnyRefMap.get(localElements[i]).isDefined())
            {
                throw new AssertionError(i);
            }
        }
    }
}
```

### Method 16

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;
import scala.collection.mutable.AnyRefMap;
import scala.collection.mutable.Map;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class ScalaAnyRefMapPutTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    @Param({"true", "false"})
    public boolean isPresized;
    @Param("0.75")
    public float loadFactor; //Adding a loadFactor for only ease of data plots
    private String[] elements;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            this.elements[i] = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
        }
    }

    @Benchmark
    public Map<String, String> scalaAnyRef()
    {
        int localSize = this.size;
        String[] localElements = this.elements;

        Map<String, String> scalaAnyRefMap = this.isPresized ? new AnyRefMap<>(localSize) : new AnyRefMap<>();

        for (int i = 0; i < localSize; i++)
        {
            scalaAnyRefMap.put(localElements[i], "dummy");
        }
        return scalaAnyRefMap;
    }
}
```

### Method 17

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.map;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;
import scala.collection.mutable.Map;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class ScalaMutableMapGetTest
{
    private static final int RANDOM_COUNT = 9;

    @Param({"250000", "500000", "750000", "1000000", "1250000", "1500000", "1750000", "2000000", "2250000", "2500000", "2750000", "3000000",
            "3250000", "3500000", "3750000", "4000000", "4250000", "4500000", "4750000", "5000000", "5250000", "5500000", "5750000", "6000000",
            "6250000", "6500000", "6750000", "7000000", "7250000", "7500000", "7750000", "8000000", "8250000", "8500000", "8750000", "9000000",
            "9250000", "9500000", "9750000", "10000000"})
    public int size;
    private String[] elements;
    private Map<String, String> scalaMap;

    @Setup
    public void setUp()
    {
        this.elements = new String[this.size];
        this.scalaMap = new PresizableHashMap<>(this.size);

        Random random = new Random(123456789012345L);
        for (int i = 0; i < this.size; i++)
        {
            String element = RandomStringUtils.random(RANDOM_COUNT, 0, 0, false, true, null, random);
            this.elements[i] = element;
            this.scalaMap.put(element, "dummy");
        }
    }

    @Benchmark
    public void get()
    {
        int localSize = this.size;
        String[] localElements = this.elements;
        Map<String, String> localScalaMap = this.scalaMap;

        for (int i = 0; i < localSize; i++)
        {
            if (!localScalaMap.get(localElements[i]).isDefined())
            {
                throw new AssertionError(i);
            }
        }
    }
}
```

### Method 18

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.set.sorted;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.api.set.sorted.ImmutableSortedSet;
import org.eclipse.collections.api.set.sorted.MutableSortedSet;
import org.eclipse.collections.impl.factory.SortedSets;
import org.eclipse.collections.impl.list.Interval;
import org.junit.After;
import org.junit.Before;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class SortedSetIterationTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    private final MutableSortedSet<Integer> ecMutable = SortedSets.mutable.withAll(Interval.zeroTo(SIZE));
    private final ImmutableSortedSet<Integer> ecImmutable = SortedSets.immutable.withAll(Interval.zeroTo(SIZE));

    private ExecutorService executorService;

    @Before
    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @After
    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_mutable_ec()
    {
        int count = this.ecMutable
                .asLazy()
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void serial_immutable_ec()
    {
        int count = this.ecImmutable
                .asLazy()
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void parallel_mutable_ec()
    {
        int count = this.ecMutable
                .asParallel(this.executorService, BATCH_SIZE)
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void parallel_immutable_ec()
    {
        int count = this.ecImmutable
                .asParallel(this.executorService, BATCH_SIZE)
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void serial_mutable_scala()
    {
        ScalaSortedSetIterationTest.serial_mutable_scala();
    }

    @Benchmark
    public void serial_immutable_scala()
    {
        ScalaSortedSetIterationTest.serial_immutable_scala();
    }

    @Benchmark
    public void parallel_mutable_scala()
    {
        ScalaSortedSetIterationTest.parallel_mutable_scala();
    }

    @Benchmark
    public void parallel_immutable_scala()
    {
        ScalaSortedSetIterationTest.parallel_immutable_scala();
    }
}
```

### Method 19

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.set.sorted;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.api.set.sorted.ImmutableSortedSet;
import org.eclipse.collections.api.set.sorted.MutableSortedSet;
import org.eclipse.collections.impl.factory.SortedSets;
import org.eclipse.collections.impl.list.Interval;
import org.junit.After;
import org.junit.Before;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class SortedSetIterationTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    private final MutableSortedSet<Integer> ecMutable = SortedSets.mutable.withAll(Interval.zeroTo(SIZE));
    private final ImmutableSortedSet<Integer> ecImmutable = SortedSets.immutable.withAll(Interval.zeroTo(SIZE));

    private ExecutorService executorService;

    @Before
    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @After
    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_mutable_ec()
    {
        int count = this.ecMutable
                .asLazy()
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void serial_immutable_ec()
    {
        int count = this.ecImmutable
                .asLazy()
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void parallel_mutable_ec()
    {
        int count = this.ecMutable
                .asParallel(this.executorService, BATCH_SIZE)
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void parallel_immutable_ec()
    {
        int count = this.ecImmutable
                .asParallel(this.executorService, BATCH_SIZE)
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .count(each -> (each + 1) % 10_000 != 0);
        if (count != 999_800)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void serial_mutable_scala()
    {
        ScalaSortedSetIterationTest.serial_mutable_scala();
    }

    @Benchmark
    public void serial_immutable_scala()
    {
        ScalaSortedSetIterationTest.serial_immutable_scala();
    }

    @Benchmark
    public void parallel_mutable_scala()
    {
        ScalaSortedSetIterationTest.parallel_mutable_scala();
    }

    @Benchmark
    public void parallel_immutable_scala()
    {
        ScalaSortedSetIterationTest.parallel_immutable_scala();
    }
}
```

### Method 20

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh.set.sorted;

import java.util.concurrent.TimeUnit;

import org.eclipse.collections.api.set.sorted.ImmutableSortedSet;
import org.eclipse.collections.api.set.sorted.MutableSortedSet;
import org.eclipse.collections.impl.factory.SortedSets;
import org.eclipse.collections.impl.list.Interval;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class SortedSetContainsTest
{
    private static final int SIZE = 2_000_000;

    private final MutableSortedSet<Integer> ecMutable = SortedSets.mutable.withAll(Interval.zeroToBy(SIZE, 2));
    private final ImmutableSortedSet<Integer> ecImmutable = SortedSets.immutable.withAll(Interval.zeroToBy(SIZE, 2));

    @Benchmark
    public void contains_mutable_ec()
    {
        int size = SIZE;
        MutableSortedSet<Integer> localEcMutable = this.ecMutable;

        for (int i = 0; i < size; i += 2)
        {
            if (!localEcMutable.contains(i))
            {
                throw new AssertionError(i);
            }
        }

        for (int i = 1; i < size; i += 2)
        {
            if (localEcMutable.contains(i))
            {
                throw new AssertionError(i);
            }
        }
    }

    @Benchmark
    public void contains_immutable_ec()
    {
        int size = SIZE;
        ImmutableSortedSet<Integer> localEcImmutable = this.ecImmutable;

        for (int i = 0; i < size; i += 2)
        {
            if (!localEcImmutable.contains(i))
            {
                throw new AssertionError(i);
            }
        }

        for (int i = 1; i < size; i += 2)
        {
            if (localEcImmutable.contains(i))
            {
                throw new AssertionError(i);
            }
        }
    }

    @Benchmark
    public void contains_mutable_scala()
    {
        SortedSetContainsScalaTest.contains_mutable_scala();
    }

    @Benchmark
    public void contains_immutable_scala()
    {
        SortedSetContainsScalaTest.contains_immutable_scala();
    }
}
```

### Method 21

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.RichIterable;
import org.eclipse.collections.api.multimap.MutableMultimap;
import org.eclipse.collections.api.multimap.list.MutableListMultimap;
import org.eclipse.collections.impl.block.factory.Comparators;
import org.eclipse.collections.impl.block.factory.Procedures;
import org.eclipse.collections.impl.forkjoin.FJIterate;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AnagramListTest
{
    private static final int SIZE = 1_000_000;

    private static final int SIZE_THRESHOLD = 10;
    private final FastList<String> ecWords = FastList.newWithNValues(SIZE, () -> RandomStringUtils.randomAlphabetic(5).toUpperCase());
    private final ArrayList<String> jdkWords = new ArrayList<>(this.ecWords);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableListMultimap<Alphagram, String> groupBy = this.ecWords.groupBy(Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = ParallelIterate.groupBy(this.ecWords, Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_forkjoin_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = FJIterate.groupBy(this.ecWords, Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        Map<Alphagram, List<String>> groupBy = this.jdkWords.stream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        Map<Alphagram, List<String>> groupBy = this.ecWords.stream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        Map<Alphagram, List<String>> groupBy = this.jdkWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        Map<Alphagram, List<String>> groupBy = this.ecWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    private static final class Alphagram
    {
        private final char[] key;

        private Alphagram(String string)
        {
            this.key = string.toCharArray();
            Arrays.sort(this.key);
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }
            Alphagram alphagram = (Alphagram) o;
            return Arrays.equals(this.key, alphagram.key);
        }

        @Override
        public int hashCode()
        {
            return Arrays.hashCode(this.key);
        }

        @Override
        public String toString()
        {
            return new String(this.key);
        }
    }
}
```

### Method 22

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.RichIterable;
import org.eclipse.collections.api.multimap.MutableMultimap;
import org.eclipse.collections.api.multimap.list.MutableListMultimap;
import org.eclipse.collections.impl.block.factory.Comparators;
import org.eclipse.collections.impl.block.factory.Procedures;
import org.eclipse.collections.impl.forkjoin.FJIterate;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AnagramListTest
{
    private static final int SIZE = 1_000_000;

    private static final int SIZE_THRESHOLD = 10;
    private final FastList<String> ecWords = FastList.newWithNValues(SIZE, () -> RandomStringUtils.randomAlphabetic(5).toUpperCase());
    private final ArrayList<String> jdkWords = new ArrayList<>(this.ecWords);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableListMultimap<Alphagram, String> groupBy = this.ecWords.groupBy(Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = ParallelIterate.groupBy(this.ecWords, Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_forkjoin_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = FJIterate.groupBy(this.ecWords, Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        Map<Alphagram, List<String>> groupBy = this.jdkWords.stream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        Map<Alphagram, List<String>> groupBy = this.ecWords.stream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        Map<Alphagram, List<String>> groupBy = this.jdkWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        Map<Alphagram, List<String>> groupBy = this.ecWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    private static final class Alphagram
    {
        private final char[] key;

        private Alphagram(String string)
        {
            this.key = string.toCharArray();
            Arrays.sort(this.key);
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }
            Alphagram alphagram = (Alphagram) o;
            return Arrays.equals(this.key, alphagram.key);
        }

        @Override
        public int hashCode()
        {
            return Arrays.hashCode(this.key);
        }

        @Override
        public String toString()
        {
            return new String(this.key);
        }
    }
}
```

### Method 23

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import org.eclipse.collections.api.bag.MutableBag;
import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.set.MutableSet;
import org.eclipse.collections.impl.bag.mutable.HashBag;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.CompositeFastList;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.eclipse.collections.impl.test.Verify;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class FunctionalInterfaceTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    @Param({"0", "1", "2", "3"})
    public int megamorphicWarmupLevel;

    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = new FastList<>(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Before
    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @Before
    @Setup(Level.Trial)
    public void setUp_megamorphic()
    {
        this.setUp();

        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate1 = each -> (each + 2) % 10_000 != 0;
        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate2 = each -> (each + 3) % 10_000 != 0;
        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate3 = each -> (each + 4) % 10_000 != 0;
        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate4 = each -> (each + 5) % 10_000 != 0;

        org.eclipse.collections.api.block.function.Function<Integer, String> function1 = each ->
        {
            Assert.assertNotNull(each);
            return String.valueOf(each);
        };

        org.eclipse.collections.api.block.function.Function<String, Integer> function2 = each -> {
            Assert.assertNotNull(each);
            return Integer.valueOf(each);
        };

        org.eclipse.collections.api.block.function.Function<Integer, String> function3 = each ->
        {
            Assert.assertSame(each, each);
            return String.valueOf(each);
        };

        org.eclipse.collections.api.block.function.Function<String, Integer> function4 = each -> {
            Assert.assertSame(each, each);
            return Integer.valueOf(each);
        };

        if (this.megamorphicWarmupLevel > 0)
        {
            Predicate<Integer> predicateJDK1 = each -> (each + 2) % 10_000 != 0;
            Predicate<Integer> predicateJDK2 = each -> (each + 3) % 10_000 != 0;
            Predicate<Integer> predicateJDK3 = each -> (each + 4) % 10_000 != 0;
            Predicate<Integer> predicateJDK4 = each -> (each + 5) % 10_000 != 0;

            Function<Integer, String> mapper1 = each ->
            {
                Assert.assertNotNull(each);
                return String.valueOf(each);
            };

            Function<String, Integer> mapper2 = each -> {
                Assert.assertNotNull(each);
                return Integer.valueOf(each);
            };

            Function<Integer, String> mapper3 = each ->
            {
                Assert.assertSame(each, each);
                return String.valueOf(each);
            };

            Function<String, Integer> mapper4 = each -> {
                Assert.assertSame(each, each);
                return Integer.valueOf(each);
            };

            // serial, lazy, JDK
            {
                Set<Integer> set = this.integersJDK.stream()
                        .filter(predicateJDK1)
                        .map(mapper1)
                        .map(mapper2)
                        .filter(predicateJDK2)
                        .collect(Collectors.toSet());
                Verify.assertSize(999_800, set);

                List<Integer> collection = this.integersJDK.stream()
                        .filter(predicateJDK3)
                        .map(mapper3)
                        .map(mapper4)
                        .filter(predicateJDK4)
                        .collect(Collectors.toCollection(ArrayList::new));
                Verify.assertSize(999_800, collection);
            }

            // parallel, lazy, JDK
            {
                Set<Integer> set = this.integersJDK.parallelStream()
                        .filter(predicateJDK1)
                        .map(mapper1)
                        .map(mapper2)
                        .filter(predicateJDK2)
                        .collect(Collectors.toSet());
                Verify.assertSize(999_800, set);

                List<Integer> collection = this.integersJDK.parallelStream()
                        .filter(predicateJDK3)
                        .map(mapper3)
                        .map(mapper4)
                        .filter(predicateJDK4)
                        .collect(Collectors.toCollection(ArrayList::new));
                Verify.assertSize(999_800, collection);
            }

            // serial, lazy, EC
            {
                MutableSet<Integer> set = this.integersEC.asLazy()
                        .select(predicate1)
                        .collect(function1)
                        .collect(function2)
                        .select(predicate2)
                        .toSet();
                Verify.assertSize(999_800, set);

                MutableBag<Integer> bag = this.integersEC.asLazy()
                        .select(predicate3)
                        .collect(function3)
                        .collect(function4)
                        .select(predicate4)
                        .toBag();
                Verify.assertIterableSize(999_800, bag);
            }

            // parallel, lazy, EC
            {
                MutableSet<Integer> set = this.integersEC.asParallel(this.executorService, BATCH_SIZE)
                        .select(predicate1)
                        .collect(function1)
                        .collect(function2)
                        .select(predicate2)
                        .toSet();
                Verify.assertSize(999_800, set);

                MutableBag<Integer> bag = this.integersEC.asParallel(this.executorService, BATCH_SIZE)
                        .select(predicate3)
                        .collect(function3)
                        .collect(function4)
                        .select(predicate4)
                        .toBag();
                Verify.assertIterableSize(999_800, bag);
            }

            // serial, eager, EC
            MutableSet<Integer> set = this.integersEC
                    .select(predicate1)
                    .collect(function1)
                    .collect(function2)
                    .select(predicate2)
                    .toSet();
            Verify.assertSize(999_800, set);

            MutableBag<Integer> bag = this.integersEC
                    .select(predicate3)
                    .collect(function3)
                    .collect(function4)
                    .select(predicate4)
                    .toBag();
            Verify.assertIterableSize(999_800, bag);
        }

        if (this.megamorphicWarmupLevel > 1)
        {
            // parallel, eager, EC
            Collection<Integer> select1 = ParallelIterate.select(this.integersEC, predicate1, new UnifiedSet<>(), true);
            Collection<String> collect1 = ParallelIterate.collect(select1, function1, new UnifiedSet<>(), true);
            Collection<Integer> collect2 = ParallelIterate.collect(collect1, function2, new UnifiedSet<>(), true);
            UnifiedSet<Integer> set = ParallelIterate.select(collect2, predicate2, new UnifiedSet<>(), true);
            Verify.assertSize(999_800, set);

            Collection<Integer> select3 = ParallelIterate.select(this.integersEC, predicate3, new HashBag<>(), true);
            Collection<String> collect3 = ParallelIterate.collect(select3, function3, new HashBag<>(), true);
            Collection<Integer> collect4 = ParallelIterate.collect(collect3, function4, new HashBag<>(), true);
            HashBag<Integer> bag = ParallelIterate.select(collect4, predicate4, new HashBag<>(), true);
            Verify.assertSize(999_800, bag);
        }

        if (this.megamorphicWarmupLevel > 2)
        {
            // parallel, eager, EC, executorService
            UnifiedSet<Integer> select1 = ParallelIterate.select(this.integersEC, predicate1, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            UnifiedSet<String> collect1 = ParallelIterate.collect(select1, function1, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            UnifiedSet<Integer> collect2 = ParallelIterate.collect(collect1, function2, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            UnifiedSet<Integer> set = ParallelIterate.select(collect2, predicate2, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            Verify.assertSize(999_800, set);

            HashBag<Integer> select3 = ParallelIterate.select(this.integersEC, predicate3, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            HashBag<String> collect3 = ParallelIterate.collect(select3, function3, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            HashBag<Integer> collect4 = ParallelIterate.collect(collect3, function4, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            HashBag<Integer> bag = ParallelIterate.select(collect4, predicate4, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            Verify.assertSize(999_800, bag);
        }

        FunctionalInterfaceScalaTest.megamorphic(this.megamorphicWarmupLevel);
    }

    @After
    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public List<Integer> serial_lazy_jdk()
    {
        List<Integer> list = this.integersJDK.stream()
                .filter(each -> each % 10_000 != 0)
                .map(String::valueOf)
                .map(Integer::valueOf)
                .filter(each -> (each + 1) % 10_000 != 0)
                .collect(Collectors.toList());
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_serial_lazy_jdk()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.serial_lazy_jdk());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public List<Integer> parallel_lazy_jdk()
    {
        List<Integer> list = this.integersJDK.parallelStream()
                .filter(each -> each % 10_000 != 0)
                .map(String::valueOf)
                .map(Integer::valueOf)
                .filter(each -> (each + 1) % 10_000 != 0)
                .collect(Collectors.toList());
        Verify.assertSize(999_800, list);
        return list;
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Test
    public void test_parallel_lazy_jdk()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.parallel_lazy_jdk());
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public MutableList<Integer> serial_eager_ec()
    {
        FastList<Integer> select1 = this.integersEC.select(each -> each % 10_000 != 0);
        FastList<String> collect1 = select1.collect(String::valueOf);
        FastList<Integer> collect2 = collect1.collect(Integer::valueOf);
        FastList<Integer> list = collect2.select(each -> (each + 1) % 10_000 != 0);
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_serial_eager_ec()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.serial_eager_ec());
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public MutableList<Integer> serial_eager_ec_hand_coded()
    {
        FastList<Integer> list = new FastList<>();
        int size = this.integersEC.size();
        for (int i = 0; i < size; i++)
        {
            Integer integer = this.integersEC.get(i);
            if (integer % 10_000 != 0 && (Integer.valueOf(String.valueOf(integer)) + 1) % 10_000 != 0)
            {
                list.add(integer);
            }
        }
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_serial_eager_ec_hand_coded()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.serial_eager_ec_hand_coded());
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public MutableList<Integer> serial_lazy_ec()
    {
        MutableList<Integer> list = this.integersEC
                .asLazy()
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .select(each -> (each + 1) % 10_000 != 0)
                .toList();
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_serial_lazy_ec()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.serial_lazy_ec());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public MutableList<Integer> parallel_eager_ec()
    {
        MutableList<Integer> select1 = ParallelIterate.select(this.integersEC, each -> each % 10_000 != 0, new CompositeFastList<>(), BATCH_SIZE, this.executorService, false);
        MutableList<String> collect1 = ParallelIterate.collect(select1, String::valueOf, new CompositeFastList<>(), BATCH_SIZE, this.executorService, false);
        MutableList<Integer> collect2 = ParallelIterate.collect(collect1, Integer::valueOf, new CompositeFastList<>(), BATCH_SIZE, this.executorService, false);
        MutableList<Integer> list = ParallelIterate.select(collect2, each -> (each + 1) % 10_000 != 0, new CompositeFastList<>(), BATCH_SIZE, this.executorService, false);
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_parallel_eager_ec()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.parallel_eager_ec());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public MutableList<Integer> parallel_lazy_ec()
    {
        MutableList<Integer> list = this.integersEC
                .asParallel(this.executorService, BATCH_SIZE)
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .select(each -> (each + 1) % 10_000 != 0)
                .toList();
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_parallel_lazy_ec()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.parallel_lazy_ec());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public CompositeFastList<Integer> parallel_eager_ec_hand_coded()
    {
        CompositeFastList<Integer> list = ParallelIterate.select(
                this.integersEC,
                integer -> integer % 10_000 != 0 && (Integer.valueOf(String.valueOf(integer)) + 1) % 10_000 != 0,
                new CompositeFastList<>(),
                BATCH_SIZE,
                this.executorService,
                false);
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_parallel_eager_ec_hand_coded()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.parallel_eager_ec_hand_coded());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public MutableList<Integer> parallel_lazy_ec_hand_coded()
    {
        MutableList<Integer> list = this.integersEC
                .asParallel(this.executorService, BATCH_SIZE)
                .select(integer -> integer % 10_000 != 0 && (Integer.valueOf(String.valueOf(integer)) + 1) % 10_000 != 0).toList();
        Verify.assertSize(999_800, list);
        return list;
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Test
    public void test_parallel_lazy_ec_hand_coded()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.parallel_lazy_ec_hand_coded());
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public void serial_eager_scala()
    {
        FunctionalInterfaceScalaTest.serial_eager_scala();
    }

    @Test
    public void test_serial_eager_scala()
    {
        FunctionalInterfaceScalaTest.test_serial_eager_scala();
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public void serial_lazy_scala()
    {
        FunctionalInterfaceScalaTest.serial_lazy_scala();
    }

    @Test
    public void test_serial_lazy_scala()
    {
        FunctionalInterfaceScalaTest.test_serial_lazy_scala();
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public void parallel_lazy_scala()
    {
        FunctionalInterfaceScalaTest.parallel_lazy_scala();
    }

    @Test
    public void test_parallel_lazy_scala()
    {
        FunctionalInterfaceScalaTest.test_parallel_lazy_scala();
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public void parallel_lazy_scala_hand_coded()
    {
        FunctionalInterfaceScalaTest.parallel_lazy_scala_hand_coded();
    }

    @Test
    public void test_parallel_lazy_scala_hand_coded()
    {
        FunctionalInterfaceScalaTest.test_parallel_lazy_scala_hand_coded();
    }
}
```

### Method 24

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import org.eclipse.collections.api.bag.MutableBag;
import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.set.MutableSet;
import org.eclipse.collections.impl.bag.mutable.HashBag;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.CompositeFastList;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.eclipse.collections.impl.test.Verify;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class FunctionalInterfaceTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    @Param({"0", "1", "2", "3"})
    public int megamorphicWarmupLevel;

    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = new FastList<>(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Before
    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @Before
    @Setup(Level.Trial)
    public void setUp_megamorphic()
    {
        this.setUp();

        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate1 = each -> (each + 2) % 10_000 != 0;
        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate2 = each -> (each + 3) % 10_000 != 0;
        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate3 = each -> (each + 4) % 10_000 != 0;
        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate4 = each -> (each + 5) % 10_000 != 0;

        org.eclipse.collections.api.block.function.Function<Integer, String> function1 = each ->
        {
            Assert.assertNotNull(each);
            return String.valueOf(each);
        };

        org.eclipse.collections.api.block.function.Function<String, Integer> function2 = each -> {
            Assert.assertNotNull(each);
            return Integer.valueOf(each);
        };

        org.eclipse.collections.api.block.function.Function<Integer, String> function3 = each ->
        {
            Assert.assertSame(each, each);
            return String.valueOf(each);
        };

        org.eclipse.collections.api.block.function.Function<String, Integer> function4 = each -> {
            Assert.assertSame(each, each);
            return Integer.valueOf(each);
        };

        if (this.megamorphicWarmupLevel > 0)
        {
            Predicate<Integer> predicateJDK1 = each -> (each + 2) % 10_000 != 0;
            Predicate<Integer> predicateJDK2 = each -> (each + 3) % 10_000 != 0;
            Predicate<Integer> predicateJDK3 = each -> (each + 4) % 10_000 != 0;
            Predicate<Integer> predicateJDK4 = each -> (each + 5) % 10_000 != 0;

            Function<Integer, String> mapper1 = each ->
            {
                Assert.assertNotNull(each);
                return String.valueOf(each);
            };

            Function<String, Integer> mapper2 = each -> {
                Assert.assertNotNull(each);
                return Integer.valueOf(each);
            };

            Function<Integer, String> mapper3 = each ->
            {
                Assert.assertSame(each, each);
                return String.valueOf(each);
            };

            Function<String, Integer> mapper4 = each -> {
                Assert.assertSame(each, each);
                return Integer.valueOf(each);
            };

            // serial, lazy, JDK
            {
                Set<Integer> set = this.integersJDK.stream()
                        .filter(predicateJDK1)
                        .map(mapper1)
                        .map(mapper2)
                        .filter(predicateJDK2)
                        .collect(Collectors.toSet());
                Verify.assertSize(999_800, set);

                List<Integer> collection = this.integersJDK.stream()
                        .filter(predicateJDK3)
                        .map(mapper3)
                        .map(mapper4)
                        .filter(predicateJDK4)
                        .collect(Collectors.toCollection(ArrayList::new));
                Verify.assertSize(999_800, collection);
            }

            // parallel, lazy, JDK
            {
                Set<Integer> set = this.integersJDK.parallelStream()
                        .filter(predicateJDK1)
                        .map(mapper1)
                        .map(mapper2)
                        .filter(predicateJDK2)
                        .collect(Collectors.toSet());
                Verify.assertSize(999_800, set);

                List<Integer> collection = this.integersJDK.parallelStream()
                        .filter(predicateJDK3)
                        .map(mapper3)
                        .map(mapper4)
                        .filter(predicateJDK4)
                        .collect(Collectors.toCollection(ArrayList::new));
                Verify.assertSize(999_800, collection);
            }

            // serial, lazy, EC
            {
                MutableSet<Integer> set = this.integersEC.asLazy()
                        .select(predicate1)
                        .collect(function1)
                        .collect(function2)
                        .select(predicate2)
                        .toSet();
                Verify.assertSize(999_800, set);

                MutableBag<Integer> bag = this.integersEC.asLazy()
                        .select(predicate3)
                        .collect(function3)
                        .collect(function4)
                        .select(predicate4)
                        .toBag();
                Verify.assertIterableSize(999_800, bag);
            }

            // parallel, lazy, EC
            {
                MutableSet<Integer> set = this.integersEC.asParallel(this.executorService, BATCH_SIZE)
                        .select(predicate1)
                        .collect(function1)
                        .collect(function2)
                        .select(predicate2)
                        .toSet();
                Verify.assertSize(999_800, set);

                MutableBag<Integer> bag = this.integersEC.asParallel(this.executorService, BATCH_SIZE)
                        .select(predicate3)
                        .collect(function3)
                        .collect(function4)
                        .select(predicate4)
                        .toBag();
                Verify.assertIterableSize(999_800, bag);
            }

            // serial, eager, EC
            MutableSet<Integer> set = this.integersEC
                    .select(predicate1)
                    .collect(function1)
                    .collect(function2)
                    .select(predicate2)
                    .toSet();
            Verify.assertSize(999_800, set);

            MutableBag<Integer> bag = this.integersEC
                    .select(predicate3)
                    .collect(function3)
                    .collect(function4)
                    .select(predicate4)
                    .toBag();
            Verify.assertIterableSize(999_800, bag);
        }

        if (this.megamorphicWarmupLevel > 1)
        {
            // parallel, eager, EC
            Collection<Integer> select1 = ParallelIterate.select(this.integersEC, predicate1, new UnifiedSet<>(), true);
            Collection<String> collect1 = ParallelIterate.collect(select1, function1, new UnifiedSet<>(), true);
            Collection<Integer> collect2 = ParallelIterate.collect(collect1, function2, new UnifiedSet<>(), true);
            UnifiedSet<Integer> set = ParallelIterate.select(collect2, predicate2, new UnifiedSet<>(), true);
            Verify.assertSize(999_800, set);

            Collection<Integer> select3 = ParallelIterate.select(this.integersEC, predicate3, new HashBag<>(), true);
            Collection<String> collect3 = ParallelIterate.collect(select3, function3, new HashBag<>(), true);
            Collection<Integer> collect4 = ParallelIterate.collect(collect3, function4, new HashBag<>(), true);
            HashBag<Integer> bag = ParallelIterate.select(collect4, predicate4, new HashBag<>(), true);
            Verify.assertSize(999_800, bag);
        }

        if (this.megamorphicWarmupLevel > 2)
        {
            // parallel, eager, EC, executorService
            UnifiedSet<Integer> select1 = ParallelIterate.select(this.integersEC, predicate1, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            UnifiedSet<String> collect1 = ParallelIterate.collect(select1, function1, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            UnifiedSet<Integer> collect2 = ParallelIterate.collect(collect1, function2, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            UnifiedSet<Integer> set = ParallelIterate.select(collect2, predicate2, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            Verify.assertSize(999_800, set);

            HashBag<Integer> select3 = ParallelIterate.select(this.integersEC, predicate3, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            HashBag<String> collect3 = ParallelIterate.collect(select3, function3, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            HashBag<Integer> collect4 = ParallelIterate.collect(collect3, function4, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            HashBag<Integer> bag = ParallelIterate.select(collect4, predicate4, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            Verify.assertSize(999_800, bag);
        }

        FunctionalInterfaceScalaTest.megamorphic(this.megamorphicWarmupLevel);
    }

    @After
    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public List<Integer> serial_lazy_jdk()
    {
        List<Integer> list = this.integersJDK.stream()
                .filter(each -> each % 10_000 != 0)
                .map(String::valueOf)
                .map(Integer::valueOf)
                .filter(each -> (each + 1) % 10_000 != 0)
                .collect(Collectors.toList());
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_serial_lazy_jdk()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.serial_lazy_jdk());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public List<Integer> parallel_lazy_jdk()
    {
        List<Integer> list = this.integersJDK.parallelStream()
                .filter(each -> each % 10_000 != 0)
                .map(String::valueOf)
                .map(Integer::valueOf)
                .filter(each -> (each + 1) % 10_000 != 0)
                .collect(Collectors.toList());
        Verify.assertSize(999_800, list);
        return list;
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Test
    public void test_parallel_lazy_jdk()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.parallel_lazy_jdk());
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public MutableList<Integer> serial_eager_ec()
    {
        FastList<Integer> select1 = this.integersEC.select(each -> each % 10_000 != 0);
        FastList<String> collect1 = select1.collect(String::valueOf);
        FastList<Integer> collect2 = collect1.collect(Integer::valueOf);
        FastList<Integer> list = collect2.select(each -> (each + 1) % 10_000 != 0);
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_serial_eager_ec()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.serial_eager_ec());
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public MutableList<Integer> serial_eager_ec_hand_coded()
    {
        FastList<Integer> list = new FastList<>();
        int size = this.integersEC.size();
        for (int i = 0; i < size; i++)
        {
            Integer integer = this.integersEC.get(i);
            if (integer % 10_000 != 0 && (Integer.valueOf(String.valueOf(integer)) + 1) % 10_000 != 0)
            {
                list.add(integer);
            }
        }
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_serial_eager_ec_hand_coded()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.serial_eager_ec_hand_coded());
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public MutableList<Integer> serial_lazy_ec()
    {
        MutableList<Integer> list = this.integersEC
                .asLazy()
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .select(each -> (each + 1) % 10_000 != 0)
                .toList();
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_serial_lazy_ec()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.serial_lazy_ec());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public MutableList<Integer> parallel_eager_ec()
    {
        MutableList<Integer> select1 = ParallelIterate.select(this.integersEC, each -> each % 10_000 != 0, new CompositeFastList<>(), BATCH_SIZE, this.executorService, false);
        MutableList<String> collect1 = ParallelIterate.collect(select1, String::valueOf, new CompositeFastList<>(), BATCH_SIZE, this.executorService, false);
        MutableList<Integer> collect2 = ParallelIterate.collect(collect1, Integer::valueOf, new CompositeFastList<>(), BATCH_SIZE, this.executorService, false);
        MutableList<Integer> list = ParallelIterate.select(collect2, each -> (each + 1) % 10_000 != 0, new CompositeFastList<>(), BATCH_SIZE, this.executorService, false);
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_parallel_eager_ec()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.parallel_eager_ec());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public MutableList<Integer> parallel_lazy_ec()
    {
        MutableList<Integer> list = this.integersEC
                .asParallel(this.executorService, BATCH_SIZE)
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .select(each -> (each + 1) % 10_000 != 0)
                .toList();
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_parallel_lazy_ec()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.parallel_lazy_ec());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public CompositeFastList<Integer> parallel_eager_ec_hand_coded()
    {
        CompositeFastList<Integer> list = ParallelIterate.select(
                this.integersEC,
                integer -> integer % 10_000 != 0 && (Integer.valueOf(String.valueOf(integer)) + 1) % 10_000 != 0,
                new CompositeFastList<>(),
                BATCH_SIZE,
                this.executorService,
                false);
        Verify.assertSize(999_800, list);
        return list;
    }

    @Test
    public void test_parallel_eager_ec_hand_coded()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.parallel_eager_ec_hand_coded());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public MutableList<Integer> parallel_lazy_ec_hand_coded()
    {
        MutableList<Integer> list = this.integersEC
                .asParallel(this.executorService, BATCH_SIZE)
                .select(integer -> integer % 10_000 != 0 && (Integer.valueOf(String.valueOf(integer)) + 1) % 10_000 != 0).toList();
        Verify.assertSize(999_800, list);
        return list;
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Test
    public void test_parallel_lazy_ec_hand_coded()
    {
        Verify.assertListsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toList(),
                this.parallel_lazy_ec_hand_coded());
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public void serial_eager_scala()
    {
        FunctionalInterfaceScalaTest.serial_eager_scala();
    }

    @Test
    public void test_serial_eager_scala()
    {
        FunctionalInterfaceScalaTest.test_serial_eager_scala();
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public void serial_lazy_scala()
    {
        FunctionalInterfaceScalaTest.serial_lazy_scala();
    }

    @Test
    public void test_serial_lazy_scala()
    {
        FunctionalInterfaceScalaTest.test_serial_lazy_scala();
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public void parallel_lazy_scala()
    {
        FunctionalInterfaceScalaTest.parallel_lazy_scala();
    }

    @Test
    public void test_parallel_lazy_scala()
    {
        FunctionalInterfaceScalaTest.test_parallel_lazy_scala();
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public void parallel_lazy_scala_hand_coded()
    {
        FunctionalInterfaceScalaTest.parallel_lazy_scala_hand_coded();
    }

    @Test
    public void test_parallel_lazy_scala_hand_coded()
    {
        FunctionalInterfaceScalaTest.test_parallel_lazy_scala_hand_coded();
    }
}
```

### Method 25

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import org.eclipse.collections.api.bag.MutableBag;
import org.eclipse.collections.api.set.MutableSet;
import org.eclipse.collections.impl.bag.mutable.HashBag;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.eclipse.collections.impl.test.Verify;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@SuppressWarnings({"Convert2Lambda", "Anonymous2MethodRef"})
@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class FunctionalInterfaceSetTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    @Param({"0", "1", "2", "3"})
    public int megamorphicWarmupLevel;

    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = new FastList<>(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Before
    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @Before
    @Setup(Level.Trial)
    public void setUp_megamorphic()
    {
        this.setUp();

        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate1 = each -> (each + 2) % 10_000 != 0;
        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate2 = each -> (each + 3) % 10_000 != 0;
        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate3 = each -> (each + 4) % 10_000 != 0;
        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate4 = each -> (each + 5) % 10_000 != 0;

        org.eclipse.collections.api.block.function.Function<Integer, String> function1 = each ->
        {
            Assert.assertNotNull(each);
            return String.valueOf(each);
        };

        org.eclipse.collections.api.block.function.Function<String, Integer> function2 = each -> {
            Assert.assertNotNull(each);
            return Integer.valueOf(each);
        };

        org.eclipse.collections.api.block.function.Function<Integer, String> function3 = each ->
        {
            Assert.assertSame(each, each);
            return String.valueOf(each);
        };

        org.eclipse.collections.api.block.function.Function<String, Integer> function4 = each -> {
            Assert.assertSame(each, each);
            return Integer.valueOf(each);
        };

        if (this.megamorphicWarmupLevel > 0)
        {
            Predicate<Integer> predicateJDK1 = each -> (each + 2) % 10_000 != 0;
            Predicate<Integer> predicateJDK2 = each -> (each + 3) % 10_000 != 0;
            Predicate<Integer> predicateJDK3 = each -> (each + 4) % 10_000 != 0;
            Predicate<Integer> predicateJDK4 = each -> (each + 5) % 10_000 != 0;

            Function<Integer, String> mapper1 = each ->
            {
                Assert.assertNotNull(each);
                return String.valueOf(each);
            };

            Function<String, Integer> mapper2 = each -> {
                Assert.assertNotNull(each);
                return Integer.valueOf(each);
            };

            Function<Integer, String> mapper3 = each ->
            {
                Assert.assertSame(each, each);
                return String.valueOf(each);
            };

            Function<String, Integer> mapper4 = each -> {
                Assert.assertSame(each, each);
                return Integer.valueOf(each);
            };

            // serial, lazy, JDK
            {
                Set<Integer> set = this.integersJDK.stream()
                        .filter(predicateJDK1)
                        .map(mapper1)
                        .map(mapper2)
                        .filter(predicateJDK2)
                        .collect(Collectors.toSet());
                Verify.assertSize(999_800, set);

                List<Integer> collection = this.integersJDK.stream()
                        .filter(predicateJDK3)
                        .map(mapper3)
                        .map(mapper4)
                        .filter(predicateJDK4)
                        .collect(Collectors.toCollection(ArrayList::new));
                Verify.assertSize(999_800, collection);
            }

            // parallel, lazy, JDK
            {
                Set<Integer> set = this.integersJDK.parallelStream()
                        .filter(predicateJDK1)
                        .map(mapper1)
                        .map(mapper2)
                        .filter(predicateJDK2)
                        .collect(Collectors.toSet());
                Verify.assertSize(999_800, set);

                List<Integer> collection = this.integersJDK.parallelStream()
                        .filter(predicateJDK3)
                        .map(mapper3)
                        .map(mapper4)
                        .filter(predicateJDK4)
                        .collect(Collectors.toCollection(ArrayList::new));
                Verify.assertSize(999_800, collection);
            }

            // serial, lazy, EC
            {
                MutableSet<Integer> set = this.integersEC.asLazy()
                        .select(predicate1)
                        .collect(function1)
                        .collect(function2)
                        .select(predicate2)
                        .toSet();
                Verify.assertSize(999_800, set);

                MutableBag<Integer> bag = this.integersEC.asLazy()
                        .select(predicate3)
                        .collect(function3)
                        .collect(function4)
                        .select(predicate4)
                        .toBag();
                Verify.assertIterableSize(999_800, bag);
            }

            // parallel, lazy, EC
            {
                MutableSet<Integer> set = this.integersEC.asParallel(this.executorService, BATCH_SIZE)
                        .select(predicate1)
                        .collect(function1)
                        .collect(function2)
                        .select(predicate2)
                        .toSet();
                Verify.assertSize(999_800, set);

                MutableBag<Integer> bag = this.integersEC.asParallel(this.executorService, BATCH_SIZE)
                        .select(predicate3)
                        .collect(function3)
                        .collect(function4)
                        .select(predicate4)
                        .toBag();
                Verify.assertIterableSize(999_800, bag);
            }

            // serial, eager, EC
            MutableSet<Integer> set = this.integersEC
                    .select(predicate1)
                    .collect(function1)
                    .collect(function2)
                    .select(predicate2)
                    .toSet();
            Verify.assertSize(999_800, set);

            MutableBag<Integer> bag = this.integersEC
                    .select(predicate3)
                    .collect(function3)
                    .collect(function4)
                    .select(predicate4)
                    .toBag();
            Verify.assertIterableSize(999_800, bag);
        }

        if (this.megamorphicWarmupLevel > 1)
        {
            // parallel, eager, EC
            Collection<Integer> select1 = ParallelIterate.select(this.integersEC, predicate1, new UnifiedSet<>(), true);
            Collection<String> collect1 = ParallelIterate.collect(select1, function1, new UnifiedSet<>(), true);
            Collection<Integer> collect2 = ParallelIterate.collect(collect1, function2, new UnifiedSet<>(), true);
            UnifiedSet<Integer> set = ParallelIterate.select(collect2, predicate2, new UnifiedSet<>(), true);
            Verify.assertSize(999_800, set);

            Collection<Integer> select3 = ParallelIterate.select(this.integersEC, predicate3, new HashBag<>(), true);
            Collection<String> collect3 = ParallelIterate.collect(select3, function3, new HashBag<>(), true);
            Collection<Integer> collect4 = ParallelIterate.collect(collect3, function4, new HashBag<>(), true);
            HashBag<Integer> bag = ParallelIterate.select(collect4, predicate4, new HashBag<>(), true);
            Verify.assertSize(999_800, bag);
        }

        if (this.megamorphicWarmupLevel > 2)
        {
            // parallel, eager, EC, executorService
            UnifiedSet<Integer> select1 = ParallelIterate.select(this.integersEC, predicate1, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            UnifiedSet<String> collect1 = ParallelIterate.collect(select1, function1, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            UnifiedSet<Integer> collect2 = ParallelIterate.collect(collect1, function2, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            UnifiedSet<Integer> set = ParallelIterate.select(collect2, predicate2, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            Verify.assertSize(999_800, set);

            HashBag<Integer> select3 = ParallelIterate.select(this.integersEC, predicate3, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            HashBag<String> collect3 = ParallelIterate.collect(select3, function3, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            HashBag<Integer> collect4 = ParallelIterate.collect(collect3, function4, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            HashBag<Integer> bag = ParallelIterate.select(collect4, predicate4, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            Verify.assertSize(999_800, bag);
        }

        FunctionalInterfaceScalaTest.megamorphic(this.megamorphicWarmupLevel);
    }

    @After
    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public Set<Integer> serial_lazy_jdk()
    {
        Set<Integer> set = this.integersJDK.stream()
                .filter(each -> each % 10_000 != 0)
                .map(String::valueOf)
                .map(Integer::valueOf)
                .filter(each -> (each + 1) % 10_000 != 0)
                .collect(Collectors.toSet());
        Verify.assertSize(999_800, set);
        return set;
    }

    @Test
    public void test_serial_lazy_jdk()
    {
        Verify.assertSetsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toSet(),
                this.serial_lazy_jdk());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public Set<Integer> parallel_lazy_jdk()
    {
        Set<Integer> set = this.integersJDK.parallelStream()
                .filter(each -> each % 10_000 != 0)
                .map(String::valueOf)
                .map(Integer::valueOf)
                .filter(each -> (each + 1) % 10_000 != 0)
                .collect(Collectors.toSet());
        Verify.assertSize(999_800, set);
        return set;
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Test
    public void test_parallel_lazy_jdk()
    {
        Verify.assertSetsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toSet(),
                this.parallel_lazy_jdk());
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public MutableSet<Integer> serial_eager_ec()
    {
        FastList<Integer> select1 = this.integersEC.select(each -> each % 10_000 != 0);
        FastList<String> collect1 = select1.collect(String::valueOf);
        FastList<Integer> collect2 = collect1.collect(Integer::valueOf);
        UnifiedSet<Integer> set = collect2.select(each -> (each + 1) % 10_000 != 0, UnifiedSet.newSet());
        Verify.assertSize(999_800, set);
        return set;
    }

    @Test
    public void test_serial_eager_ec()
    {
        Verify.assertSetsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toSet(),
                this.serial_eager_ec());
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public MutableSet<Integer> serial_lazy_ec()
    {
        MutableSet<Integer> set = this.integersEC
                .asLazy()
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .select(each -> (each + 1) % 10_000 != 0)
                .toSet();
        Verify.assertSize(999_800, set);
        return set;
    }

    @Test
    public void test_serial_lazy_ec()
    {
        Verify.assertSetsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toSet(),
                this.serial_lazy_ec());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public MutableSet<Integer> parallel_lazy_ec()
    {
        MutableSet<Integer> set = this.integersEC
                .asParallel(this.executorService, BATCH_SIZE)
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .select(each -> (each + 1) % 10_000 != 0)
                .toSet();
        Verify.assertSize(999_800, set);
        return set;
    }

    @Test
    public void test_parallel_lazy_ec()
    {
        Verify.assertSetsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toSet(),
                this.parallel_lazy_ec());
    }
}
```

### Method 26

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import org.eclipse.collections.api.bag.MutableBag;
import org.eclipse.collections.api.set.MutableSet;
import org.eclipse.collections.impl.bag.mutable.HashBag;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.eclipse.collections.impl.test.Verify;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@SuppressWarnings({"Convert2Lambda", "Anonymous2MethodRef"})
@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class FunctionalInterfaceSetTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    @Param({"0", "1", "2", "3"})
    public int megamorphicWarmupLevel;

    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = new FastList<>(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Before
    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @Before
    @Setup(Level.Trial)
    public void setUp_megamorphic()
    {
        this.setUp();

        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate1 = each -> (each + 2) % 10_000 != 0;
        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate2 = each -> (each + 3) % 10_000 != 0;
        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate3 = each -> (each + 4) % 10_000 != 0;
        org.eclipse.collections.api.block.predicate.Predicate<Integer> predicate4 = each -> (each + 5) % 10_000 != 0;

        org.eclipse.collections.api.block.function.Function<Integer, String> function1 = each ->
        {
            Assert.assertNotNull(each);
            return String.valueOf(each);
        };

        org.eclipse.collections.api.block.function.Function<String, Integer> function2 = each -> {
            Assert.assertNotNull(each);
            return Integer.valueOf(each);
        };

        org.eclipse.collections.api.block.function.Function<Integer, String> function3 = each ->
        {
            Assert.assertSame(each, each);
            return String.valueOf(each);
        };

        org.eclipse.collections.api.block.function.Function<String, Integer> function4 = each -> {
            Assert.assertSame(each, each);
            return Integer.valueOf(each);
        };

        if (this.megamorphicWarmupLevel > 0)
        {
            Predicate<Integer> predicateJDK1 = each -> (each + 2) % 10_000 != 0;
            Predicate<Integer> predicateJDK2 = each -> (each + 3) % 10_000 != 0;
            Predicate<Integer> predicateJDK3 = each -> (each + 4) % 10_000 != 0;
            Predicate<Integer> predicateJDK4 = each -> (each + 5) % 10_000 != 0;

            Function<Integer, String> mapper1 = each ->
            {
                Assert.assertNotNull(each);
                return String.valueOf(each);
            };

            Function<String, Integer> mapper2 = each -> {
                Assert.assertNotNull(each);
                return Integer.valueOf(each);
            };

            Function<Integer, String> mapper3 = each ->
            {
                Assert.assertSame(each, each);
                return String.valueOf(each);
            };

            Function<String, Integer> mapper4 = each -> {
                Assert.assertSame(each, each);
                return Integer.valueOf(each);
            };

            // serial, lazy, JDK
            {
                Set<Integer> set = this.integersJDK.stream()
                        .filter(predicateJDK1)
                        .map(mapper1)
                        .map(mapper2)
                        .filter(predicateJDK2)
                        .collect(Collectors.toSet());
                Verify.assertSize(999_800, set);

                List<Integer> collection = this.integersJDK.stream()
                        .filter(predicateJDK3)
                        .map(mapper3)
                        .map(mapper4)
                        .filter(predicateJDK4)
                        .collect(Collectors.toCollection(ArrayList::new));
                Verify.assertSize(999_800, collection);
            }

            // parallel, lazy, JDK
            {
                Set<Integer> set = this.integersJDK.parallelStream()
                        .filter(predicateJDK1)
                        .map(mapper1)
                        .map(mapper2)
                        .filter(predicateJDK2)
                        .collect(Collectors.toSet());
                Verify.assertSize(999_800, set);

                List<Integer> collection = this.integersJDK.parallelStream()
                        .filter(predicateJDK3)
                        .map(mapper3)
                        .map(mapper4)
                        .filter(predicateJDK4)
                        .collect(Collectors.toCollection(ArrayList::new));
                Verify.assertSize(999_800, collection);
            }

            // serial, lazy, EC
            {
                MutableSet<Integer> set = this.integersEC.asLazy()
                        .select(predicate1)
                        .collect(function1)
                        .collect(function2)
                        .select(predicate2)
                        .toSet();
                Verify.assertSize(999_800, set);

                MutableBag<Integer> bag = this.integersEC.asLazy()
                        .select(predicate3)
                        .collect(function3)
                        .collect(function4)
                        .select(predicate4)
                        .toBag();
                Verify.assertIterableSize(999_800, bag);
            }

            // parallel, lazy, EC
            {
                MutableSet<Integer> set = this.integersEC.asParallel(this.executorService, BATCH_SIZE)
                        .select(predicate1)
                        .collect(function1)
                        .collect(function2)
                        .select(predicate2)
                        .toSet();
                Verify.assertSize(999_800, set);

                MutableBag<Integer> bag = this.integersEC.asParallel(this.executorService, BATCH_SIZE)
                        .select(predicate3)
                        .collect(function3)
                        .collect(function4)
                        .select(predicate4)
                        .toBag();
                Verify.assertIterableSize(999_800, bag);
            }

            // serial, eager, EC
            MutableSet<Integer> set = this.integersEC
                    .select(predicate1)
                    .collect(function1)
                    .collect(function2)
                    .select(predicate2)
                    .toSet();
            Verify.assertSize(999_800, set);

            MutableBag<Integer> bag = this.integersEC
                    .select(predicate3)
                    .collect(function3)
                    .collect(function4)
                    .select(predicate4)
                    .toBag();
            Verify.assertIterableSize(999_800, bag);
        }

        if (this.megamorphicWarmupLevel > 1)
        {
            // parallel, eager, EC
            Collection<Integer> select1 = ParallelIterate.select(this.integersEC, predicate1, new UnifiedSet<>(), true);
            Collection<String> collect1 = ParallelIterate.collect(select1, function1, new UnifiedSet<>(), true);
            Collection<Integer> collect2 = ParallelIterate.collect(collect1, function2, new UnifiedSet<>(), true);
            UnifiedSet<Integer> set = ParallelIterate.select(collect2, predicate2, new UnifiedSet<>(), true);
            Verify.assertSize(999_800, set);

            Collection<Integer> select3 = ParallelIterate.select(this.integersEC, predicate3, new HashBag<>(), true);
            Collection<String> collect3 = ParallelIterate.collect(select3, function3, new HashBag<>(), true);
            Collection<Integer> collect4 = ParallelIterate.collect(collect3, function4, new HashBag<>(), true);
            HashBag<Integer> bag = ParallelIterate.select(collect4, predicate4, new HashBag<>(), true);
            Verify.assertSize(999_800, bag);
        }

        if (this.megamorphicWarmupLevel > 2)
        {
            // parallel, eager, EC, executorService
            UnifiedSet<Integer> select1 = ParallelIterate.select(this.integersEC, predicate1, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            UnifiedSet<String> collect1 = ParallelIterate.collect(select1, function1, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            UnifiedSet<Integer> collect2 = ParallelIterate.collect(collect1, function2, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            UnifiedSet<Integer> set = ParallelIterate.select(collect2, predicate2, new UnifiedSet<>(), BATCH_SIZE, this.executorService, true);
            Verify.assertSize(999_800, set);

            HashBag<Integer> select3 = ParallelIterate.select(this.integersEC, predicate3, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            HashBag<String> collect3 = ParallelIterate.collect(select3, function3, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            HashBag<Integer> collect4 = ParallelIterate.collect(collect3, function4, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            HashBag<Integer> bag = ParallelIterate.select(collect4, predicate4, new HashBag<>(), BATCH_SIZE, this.executorService, true);
            Verify.assertSize(999_800, bag);
        }

        FunctionalInterfaceScalaTest.megamorphic(this.megamorphicWarmupLevel);
    }

    @After
    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public Set<Integer> serial_lazy_jdk()
    {
        Set<Integer> set = this.integersJDK.stream()
                .filter(each -> each % 10_000 != 0)
                .map(String::valueOf)
                .map(Integer::valueOf)
                .filter(each -> (each + 1) % 10_000 != 0)
                .collect(Collectors.toSet());
        Verify.assertSize(999_800, set);
        return set;
    }

    @Test
    public void test_serial_lazy_jdk()
    {
        Verify.assertSetsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toSet(),
                this.serial_lazy_jdk());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public Set<Integer> parallel_lazy_jdk()
    {
        Set<Integer> set = this.integersJDK.parallelStream()
                .filter(each -> each % 10_000 != 0)
                .map(String::valueOf)
                .map(Integer::valueOf)
                .filter(each -> (each + 1) % 10_000 != 0)
                .collect(Collectors.toSet());
        Verify.assertSize(999_800, set);
        return set;
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Test
    public void test_parallel_lazy_jdk()
    {
        Verify.assertSetsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toSet(),
                this.parallel_lazy_jdk());
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public MutableSet<Integer> serial_eager_ec()
    {
        FastList<Integer> select1 = this.integersEC.select(each -> each % 10_000 != 0);
        FastList<String> collect1 = select1.collect(String::valueOf);
        FastList<Integer> collect2 = collect1.collect(Integer::valueOf);
        UnifiedSet<Integer> set = collect2.select(each -> (each + 1) % 10_000 != 0, UnifiedSet.newSet());
        Verify.assertSize(999_800, set);
        return set;
    }

    @Test
    public void test_serial_eager_ec()
    {
        Verify.assertSetsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toSet(),
                this.serial_eager_ec());
    }

    @Warmup(iterations = 20)
    @Measurement(iterations = 10)
    @Benchmark
    public MutableSet<Integer> serial_lazy_ec()
    {
        MutableSet<Integer> set = this.integersEC
                .asLazy()
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .select(each -> (each + 1) % 10_000 != 0)
                .toSet();
        Verify.assertSize(999_800, set);
        return set;
    }

    @Test
    public void test_serial_lazy_ec()
    {
        Verify.assertSetsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toSet(),
                this.serial_lazy_ec());
    }

    @Warmup(iterations = 50)
    @Measurement(iterations = 25)
    @Benchmark
    public MutableSet<Integer> parallel_lazy_ec()
    {
        MutableSet<Integer> set = this.integersEC
                .asParallel(this.executorService, BATCH_SIZE)
                .select(each -> each % 10_000 != 0)
                .collect(String::valueOf)
                .collect(Integer::valueOf)
                .select(each -> (each + 1) % 10_000 != 0)
                .toSet();
        Verify.assertSize(999_800, set);
        return set;
    }

    @Test
    public void test_parallel_lazy_ec()
    {
        Verify.assertSetsEqual(
                Interval.oneToBy(1_000_000, 10_000).flatCollect(each -> Interval.fromTo(each, each + 9_997)).toSet(),
                this.parallel_lazy_ec());
    }
}
```

### Method 27

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.CompositeFastList;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.test.Verify;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class CollectTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = new FastList<>(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        List<String> strings = this.integersJDK.stream().map(Object::toString).collect(Collectors.toList());
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        List<String> strings = this.integersEC.stream().map(Object::toString).collect(Collectors.toList());
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        List<String> strings = this.integersJDK.parallelStream().map(Object::toString).collect(Collectors.toList());
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        List<String> strings = this.integersEC.parallelStream().map(Object::toString).collect(Collectors.toList());
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void serial_eager_scala()
    {
        CollectScalaTest.serial_eager_scala();
    }

    @Benchmark
    public void serial_lazy_scala()
    {
        CollectScalaTest.serial_lazy_scala();
    }

    @Benchmark
    public void parallel_lazy_scala()
    {
        CollectScalaTest.parallel_lazy_scala();
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableList<String> strings = this.integersEC.collect(Object::toString);
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        Collection<String> strings = ParallelIterate.collect(this.integersEC, Object::toString);
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void parallel_eager_fixed_pool_ec()
    {
        Collection<String> strings = ParallelIterate.collect(
                this.integersEC,
                Object::toString,
                new CompositeFastList<>(),
                BATCH_SIZE,
                this.executorService,
                false);
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void serial_lazy_ec()
    {
        MutableList<String> strings = this.integersEC.asLazy().collect(Object::toString).toList();
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        MutableList<String> strings = this.integersEC.asParallel(this.executorService, BATCH_SIZE).collect(Object::toString).toList();
        Verify.assertSize(SIZE, strings);
    }
}
```

### Method 28

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.CompositeFastList;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.test.Verify;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class CollectTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = new FastList<>(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        List<String> strings = this.integersJDK.stream().map(Object::toString).collect(Collectors.toList());
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        List<String> strings = this.integersEC.stream().map(Object::toString).collect(Collectors.toList());
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        List<String> strings = this.integersJDK.parallelStream().map(Object::toString).collect(Collectors.toList());
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        List<String> strings = this.integersEC.parallelStream().map(Object::toString).collect(Collectors.toList());
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void serial_eager_scala()
    {
        CollectScalaTest.serial_eager_scala();
    }

    @Benchmark
    public void serial_lazy_scala()
    {
        CollectScalaTest.serial_lazy_scala();
    }

    @Benchmark
    public void parallel_lazy_scala()
    {
        CollectScalaTest.parallel_lazy_scala();
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableList<String> strings = this.integersEC.collect(Object::toString);
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        Collection<String> strings = ParallelIterate.collect(this.integersEC, Object::toString);
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void parallel_eager_fixed_pool_ec()
    {
        Collection<String> strings = ParallelIterate.collect(
                this.integersEC,
                Object::toString,
                new CompositeFastList<>(),
                BATCH_SIZE,
                this.executorService,
                false);
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void serial_lazy_ec()
    {
        MutableList<String> strings = this.integersEC.asLazy().collect(Object::toString).toList();
        Verify.assertSize(SIZE, strings);
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        MutableList<String> strings = this.integersEC.asParallel(this.executorService, BATCH_SIZE).collect(Object::toString).toList();
        Verify.assertSize(SIZE, strings);
    }
}
```

### Method 29

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.ParallelListIterable;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class CollectIfTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final ExecutorService service = ParallelIterate.newPooledExecutor(CollectTest.class.getSimpleName(), true);
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = FastList.newList(Interval.oneTo(SIZE));

    @Benchmark
    public void serial_lazy_jdk()
    {
        List<String> evenStrings = this.integersJDK.stream().filter(e -> e % 2 == 0).map(Object::toString).collect(Collectors.toList());
        List<String> oddStrings = this.integersJDK.stream().filter(e -> e % 2 == 1).map(Object::toString).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        List<String> evenStrings = this.integersEC.stream().filter(e -> e % 2 == 0).map(Object::toString).collect(Collectors.toList());
        List<String> oddStrings = this.integersEC.stream().filter(e -> e % 2 == 1).map(Object::toString).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        List<String> evenStrings = this.integersJDK.parallelStream().filter(e -> e % 2 == 0).map(Object::toString).collect(Collectors.toList());
        List<String> oddStrings = this.integersJDK.parallelStream().filter(e -> e % 2 == 1).map(Object::toString).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        List<String> evenStrings = this.integersEC.parallelStream().filter(e -> e % 2 == 0).map(Object::toString).collect(Collectors.toList());
        List<String> oddStrings = this.integersEC.parallelStream().filter(e -> e % 2 == 1).map(Object::toString).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableList<String> evenStrings = this.integersEC.collectIf(e -> e % 2 == 0, Object::toString);
        MutableList<String> oddStrings = this.integersEC.collectIf(e -> e % 2 == 1, Object::toString);
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        Collection<String> evenStrings = ParallelIterate.collectIf(this.integersEC, e -> e % 2 == 0, Object::toString);
        Collection<String> oddStrings = ParallelIterate.collectIf(this.integersEC, e -> e % 2 == 1, Object::toString);
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void serial_lazy_ec()
    {
        MutableList<String> evenStrings = this.integersEC.asLazy().select(e -> e % 2 == 0).collect(Object::toString).toList();
        MutableList<String> oddStrings = this.integersEC.asLazy().select(e -> e % 2 == 1).collect(Object::toString).toList();
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        ParallelListIterable<Integer> parallelListIterable = this.integersEC.asParallel(this.service, BATCH_SIZE);
        MutableList<String> evenStrings = parallelListIterable.select(e -> e % 2 == 0).collect(Object::toString).toList();
        MutableList<String> oddStrings = parallelListIterable.select(e -> e % 2 == 1).collect(Object::toString).toList();
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }
}
```

### Method 30

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.ParallelListIterable;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class CollectIfTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final ExecutorService service = ParallelIterate.newPooledExecutor(CollectTest.class.getSimpleName(), true);
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = FastList.newList(Interval.oneTo(SIZE));

    @Benchmark
    public void serial_lazy_jdk()
    {
        List<String> evenStrings = this.integersJDK.stream().filter(e -> e % 2 == 0).map(Object::toString).collect(Collectors.toList());
        List<String> oddStrings = this.integersJDK.stream().filter(e -> e % 2 == 1).map(Object::toString).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        List<String> evenStrings = this.integersEC.stream().filter(e -> e % 2 == 0).map(Object::toString).collect(Collectors.toList());
        List<String> oddStrings = this.integersEC.stream().filter(e -> e % 2 == 1).map(Object::toString).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        List<String> evenStrings = this.integersJDK.parallelStream().filter(e -> e % 2 == 0).map(Object::toString).collect(Collectors.toList());
        List<String> oddStrings = this.integersJDK.parallelStream().filter(e -> e % 2 == 1).map(Object::toString).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        List<String> evenStrings = this.integersEC.parallelStream().filter(e -> e % 2 == 0).map(Object::toString).collect(Collectors.toList());
        List<String> oddStrings = this.integersEC.parallelStream().filter(e -> e % 2 == 1).map(Object::toString).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableList<String> evenStrings = this.integersEC.collectIf(e -> e % 2 == 0, Object::toString);
        MutableList<String> oddStrings = this.integersEC.collectIf(e -> e % 2 == 1, Object::toString);
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        Collection<String> evenStrings = ParallelIterate.collectIf(this.integersEC, e -> e % 2 == 0, Object::toString);
        Collection<String> oddStrings = ParallelIterate.collectIf(this.integersEC, e -> e % 2 == 1, Object::toString);
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void serial_lazy_ec()
    {
        MutableList<String> evenStrings = this.integersEC.asLazy().select(e -> e % 2 == 0).collect(Object::toString).toList();
        MutableList<String> oddStrings = this.integersEC.asLazy().select(e -> e % 2 == 1).collect(Object::toString).toList();
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        ParallelListIterable<Integer> parallelListIterable = this.integersEC.asParallel(this.service, BATCH_SIZE);
        MutableList<String> evenStrings = parallelListIterable.select(e -> e % 2 == 0).collect(Object::toString).toList();
        MutableList<String> oddStrings = parallelListIterable.select(e -> e % 2 == 1).collect(Object::toString).toList();
        Assert.assertEquals(SIZE / 2, evenStrings.size());
        Assert.assertEquals(SIZE / 2, oddStrings.size());
    }
}
```

### Method 31

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.ParallelListIterable;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class SelectTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final ExecutorService service = ParallelIterate.newPooledExecutor(SelectTest.class.getSimpleName(), true);
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = FastList.newList(Interval.oneTo(SIZE));

    @Benchmark
    public void serial_lazy_jdk()
    {
        List<Integer> evens = this.integersJDK.stream().filter(each -> each % 2 == 0).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        List<Integer> evens = this.integersEC.stream().filter(each -> each % 2 == 0).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        List<Integer> evens = this.integersJDK.parallelStream().filter(each -> each % 2 == 0).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        List<Integer> evens = this.integersEC.parallelStream().filter(each -> each % 2 == 0).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableList<Integer> evens = this.integersEC.select(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        Collection<Integer> evens = ParallelIterate.select(this.integersEC, each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void serial_lazy_ec()
    {
        MutableList<Integer> evens = this.integersEC.asLazy().select(each -> each % 2 == 0).toList();
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        ParallelListIterable<Integer> parallelListIterable = this.integersEC.asParallel(this.service, BATCH_SIZE);
        MutableList<Integer> evens = parallelListIterable.select(each -> each % 2 == 0).toList();
        Assert.assertEquals(SIZE / 2, evens.size());
    }
}
```

### Method 32

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.ParallelListIterable;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class SelectTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final ExecutorService service = ParallelIterate.newPooledExecutor(SelectTest.class.getSimpleName(), true);
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = FastList.newList(Interval.oneTo(SIZE));

    @Benchmark
    public void serial_lazy_jdk()
    {
        List<Integer> evens = this.integersJDK.stream().filter(each -> each % 2 == 0).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        List<Integer> evens = this.integersEC.stream().filter(each -> each % 2 == 0).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        List<Integer> evens = this.integersJDK.parallelStream().filter(each -> each % 2 == 0).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        List<Integer> evens = this.integersEC.parallelStream().filter(each -> each % 2 == 0).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableList<Integer> evens = this.integersEC.select(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        Collection<Integer> evens = ParallelIterate.select(this.integersEC, each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void serial_lazy_ec()
    {
        MutableList<Integer> evens = this.integersEC.asLazy().select(each -> each % 2 == 0).toList();
        Assert.assertEquals(SIZE / 2, evens.size());
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        ParallelListIterable<Integer> parallelListIterable = this.integersEC.asParallel(this.service, BATCH_SIZE);
        MutableList<Integer> evens = parallelListIterable.select(each -> each % 2 == 0).toList();
        Assert.assertEquals(SIZE / 2, evens.size());
    }
}
```

### Method 33

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class FlatCollectTest
{
    private static final int COUNT = 10_000;
    private static final int LIST_SIZE = 100;
    private final List<List<Integer>> integersJDK = new ArrayList<>(FastList.<List<Integer>>newWithNValues(COUNT, () -> new ArrayList<>(Interval.oneTo(LIST_SIZE))));
    private final MutableList<MutableList<Integer>> integersEC = FastList.newWithNValues(COUNT, () -> Interval.oneTo(LIST_SIZE).toList());

    @Benchmark
    public List<Integer> serial_lazy_jdk()
    {
        return this.integersJDK.stream().flatMap(Collection::stream).collect(Collectors.toList());
    }

    @Benchmark
    public List<Integer> serial_lazy_streams_ec()
    {
        return this.integersEC.stream().flatMap(Collection::stream).collect(Collectors.toList());
    }

    @Benchmark
    public MutableList<Integer> serial_eager_ec()
    {
        return this.integersEC.flatCollect(e -> e);
    }

    @Benchmark
    public MutableList<Integer> serial_lazy_ec()
    {
        return this.integersEC.asLazy().flatCollect(e -> e).toList();
    }
}
```

### Method 34

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class FlatCollectTest
{
    private static final int COUNT = 10_000;
    private static final int LIST_SIZE = 100;
    private final List<List<Integer>> integersJDK = new ArrayList<>(FastList.<List<Integer>>newWithNValues(COUNT, () -> new ArrayList<>(Interval.oneTo(LIST_SIZE))));
    private final MutableList<MutableList<Integer>> integersEC = FastList.newWithNValues(COUNT, () -> Interval.oneTo(LIST_SIZE).toList());

    @Benchmark
    public List<Integer> serial_lazy_jdk()
    {
        return this.integersJDK.stream().flatMap(Collection::stream).collect(Collectors.toList());
    }

    @Benchmark
    public List<Integer> serial_lazy_streams_ec()
    {
        return this.integersEC.stream().flatMap(Collection::stream).collect(Collectors.toList());
    }

    @Benchmark
    public MutableList<Integer> serial_eager_ec()
    {
        return this.integersEC.flatCollect(e -> e);
    }

    @Benchmark
    public MutableList<Integer> serial_lazy_ec()
    {
        return this.integersEC.asLazy().flatCollect(e -> e).toList();
    }
}
```

### Method 35

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collections;
import java.util.DoubleSummaryStatistics;
import java.util.Map;
import java.util.PrimitiveIterator;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.map.MapIterable;
import org.eclipse.collections.api.map.MutableMap;
import org.eclipse.collections.api.set.Pool;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.eclipse.collections.impl.test.Verify;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AggregateByTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private static final Random RANDOM = new Random(System.currentTimeMillis());
    private static final PrimitiveIterator.OfInt INTS = RANDOM.ints(1, 10).iterator();
    private static final PrimitiveIterator.OfDouble DOUBLES = RANDOM.doubles(1.0d, 100.0d).iterator();
    private final Pool<Account> accountPool = UnifiedSet.newSet();
    private final Pool<Product> productPool = UnifiedSet.newSet();
    private final Pool<String> categoryPool = UnifiedSet.newSet();
    private final FastList<Position> ecPositions = FastList.newWithNValues(SIZE, Position::new);
    private final ArrayList<Position> jdkPositions = new ArrayList<>(this.ecPositions);

    private ExecutorService executorService;

    @Before
    @Setup(Level.Iteration)
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        this.ecPositions.shuffleThis();
        Collections.shuffle(this.jdkPositions);
    }

    @After
    @TearDown(Level.Iteration)
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public Map<Product, DoubleSummaryStatistics> aggregateByProduct_serial_lazy_jdk()
    {
        Map<Product, DoubleSummaryStatistics> result =
                this.jdkPositions.stream().collect(
                        Collectors.groupingBy(
                                Position::getProduct,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<Product, DoubleSummaryStatistics> aggregateByProduct_serial_lazy_streams_ec()
    {
        Map<Product, DoubleSummaryStatistics> result =
                this.ecPositions.stream().collect(
                        Collectors.groupingBy(
                                Position::getProduct,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<Account, DoubleSummaryStatistics> aggregateByAccount_serial_lazy_jdk()
    {
        Map<Account, DoubleSummaryStatistics> accountDoubleMap =
                this.jdkPositions.stream().collect(
                        Collectors.groupingBy(
                                Position::getAccount,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(accountDoubleMap);
        return accountDoubleMap;
    }

    @Benchmark
    public Map<Account, DoubleSummaryStatistics> aggregateByAccount_serial_lazy_streams_ec()
    {
        Map<Account, DoubleSummaryStatistics> accountDoubleMap =
                this.ecPositions.stream().collect(
                        Collectors.groupingBy(
                                Position::getAccount,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(accountDoubleMap);
        return accountDoubleMap;
    }

    @Benchmark
    public Map<String, DoubleSummaryStatistics> aggregateByCategory_serial_lazy_jdk()
    {
        Map<String, DoubleSummaryStatistics> categoryDoubleMap =
                this.jdkPositions.stream().collect(
                        Collectors.groupingBy(
                                Position::getCategory,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(categoryDoubleMap);
        return categoryDoubleMap;
    }

    @Benchmark
    public Map<String, DoubleSummaryStatistics> aggregateByCategory_serial_lazy_streams_ec()
    {
        Map<String, DoubleSummaryStatistics> categoryDoubleMap =
                this.ecPositions.stream().collect(
                        Collectors.groupingBy(
                                Position::getCategory,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(categoryDoubleMap);
        return categoryDoubleMap;
    }

    @Benchmark
    public Map<Product, DoubleSummaryStatistics> aggregateByProduct_parallel_lazy_jdk()
    {
        Map<Product, DoubleSummaryStatistics> result =
                this.jdkPositions.parallelStream().collect(
                        Collectors.groupingBy(
                                Position::getProduct,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<Product, DoubleSummaryStatistics> aggregateByProduct_parallel_lazy_streams_ec()
    {
        Map<Product, DoubleSummaryStatistics> result =
                this.ecPositions.parallelStream().collect(
                        Collectors.groupingBy(
                                Position::getProduct,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<Account, DoubleSummaryStatistics> aggregateByAccount_parallel_lazy_jdk()
    {
        Map<Account, DoubleSummaryStatistics> result =
                this.jdkPositions.parallelStream().collect(
                        Collectors.groupingBy(
                                Position::getAccount,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<Account, DoubleSummaryStatistics> aggregateByAccount_parallel_lazy_streams_ec()
    {
        Map<Account, DoubleSummaryStatistics> result =
                this.ecPositions.parallelStream().collect(
                        Collectors.groupingBy(
                                Position::getAccount,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<String, DoubleSummaryStatistics> aggregateByCategory_parallel_lazy_jdk()
    {
        Map<String, DoubleSummaryStatistics> result =
                this.jdkPositions.parallelStream().collect(
                        Collectors.groupingBy(Position::getCategory, Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<String, DoubleSummaryStatistics> aggregateByCategory_parallel_lazy_streams_ec()
    {
        Map<String, DoubleSummaryStatistics> result =
                this.ecPositions.parallelStream().collect(
                        Collectors.groupingBy(Position::getCategory, Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Product, ImmutableMarketValueStatistics> aggregateByProduct_serial_eager_ec()
    {
        MutableMap<Product, ImmutableMarketValueStatistics> result =
                this.ecPositions.aggregateBy(
                        Position::getProduct,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Account, ImmutableMarketValueStatistics> aggregateByAccount_serial_eager_ec()
    {
        MutableMap<Account, ImmutableMarketValueStatistics> result =
                this.ecPositions.aggregateBy(
                        Position::getAccount,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<String, ImmutableMarketValueStatistics> aggregateByCategory_serial_eager_ec()
    {
        MutableMap<String, ImmutableMarketValueStatistics> result =
                this.ecPositions.aggregateBy(
                        Position::getCategory,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Product, ImmutableMarketValueStatistics> aggregateByProduct_parallel_eager_ec()
    {
        MutableMap<Product, ImmutableMarketValueStatistics> result =
                ParallelIterate.aggregateBy(
                        this.ecPositions,
                        Position::getProduct,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Account, ImmutableMarketValueStatistics> aggregateByAccount_parallel_eager_ec()
    {
        MutableMap<Account, ImmutableMarketValueStatistics> result =
                ParallelIterate.aggregateBy(
                        this.ecPositions,
                        Position::getAccount,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<String, ImmutableMarketValueStatistics> aggregateByCategory_parallel_eager_ec()
    {
        MutableMap<String, ImmutableMarketValueStatistics> result =
                ParallelIterate.aggregateBy(
                        this.ecPositions,
                        Position::getCategory,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MapIterable<Product, ImmutableMarketValueStatistics> aggregateByProduct_serial_lazy_ec()
    {
        MapIterable<Product, ImmutableMarketValueStatistics> result =
                this.ecPositions.asLazy().aggregateBy(
                        Position::getProduct,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MapIterable<Account, ImmutableMarketValueStatistics> aggregateByAccount_serial_lazy_ec()
    {
        MapIterable<Account, ImmutableMarketValueStatistics> result =
                this.ecPositions.asLazy().aggregateBy(
                        Position::getAccount,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MapIterable<String, ImmutableMarketValueStatistics> aggregateByCategory_serial_lazy_ec()
    {
        MapIterable<String, ImmutableMarketValueStatistics> result =
                this.ecPositions.asLazy().aggregateBy(
                        Position::getCategory,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MapIterable<Product, ImmutableMarketValueStatistics> aggregateByProduct_parallel_lazy_ec()
    {
        MapIterable<Product, ImmutableMarketValueStatistics> result =
                this.ecPositions.asParallel(this.executorService, BATCH_SIZE)
                        .aggregateBy(
                                Position::getProduct,
                                ImmutableMarketValueStatistics::getZero,
                                ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Test
    public void test_aggregateByProduct_parallel_lazy_ec()
    {
        MapIterable<Product, ImmutableMarketValueStatistics> actual = this.aggregateByProduct_parallel_lazy_ec();
        MapIterable<Product, ImmutableMarketValueStatistics> expected = this.aggregateByProduct_serial_lazy_ec();
        Assert.assertEquals(expected, expected);
        Verify.assertMapsEqual((Map<Product, ImmutableMarketValueStatistics>) expected, (Map<Product, ImmutableMarketValueStatistics>) actual);
    }

    @Benchmark
    public MapIterable<Account, ImmutableMarketValueStatistics> aggregateByAccount_parallel_lazy_ec()
    {
        MapIterable<Account, ImmutableMarketValueStatistics> result =
                this.ecPositions.asParallel(this.executorService, BATCH_SIZE)
                        .aggregateBy(
                                Position::getAccount,
                                ImmutableMarketValueStatistics::new,
                                ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Test
    public void test_aggregateByAccount_parallel_lazy_ec()
    {
        MapIterable<Account, ImmutableMarketValueStatistics> actual = this.aggregateByAccount_parallel_lazy_ec();
        MapIterable<Account, ImmutableMarketValueStatistics> expected = this.aggregateByAccount_serial_lazy_ec();
        Assert.assertEquals(expected, expected);
        Verify.assertMapsEqual((Map<Account, ImmutableMarketValueStatistics>) expected, (Map<Account, ImmutableMarketValueStatistics>) actual);
    }

    @Benchmark
    public MapIterable<String, ImmutableMarketValueStatistics> aggregateByCategory_parallel_lazy_ec()
    {
        MapIterable<String, ImmutableMarketValueStatistics> result =
                this.ecPositions.asParallel(this.executorService, BATCH_SIZE)
                        .aggregateBy(
                                Position::getCategory,
                                ImmutableMarketValueStatistics::new,
                                ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Test
    public void test_aggregateByCategory_parallel_lazy_ec()
    {
        MapIterable<String, ImmutableMarketValueStatistics> actual = this.aggregateByCategory_parallel_lazy_ec();
        MapIterable<String, ImmutableMarketValueStatistics> expected = this.aggregateByCategory_serial_lazy_ec();
        Assert.assertEquals(expected, expected);
        Verify.assertMapsEqual((Map<String, ImmutableMarketValueStatistics>) expected, (Map<String, ImmutableMarketValueStatistics>) actual);
    }

    @Benchmark
    public MutableMap<Product, MarketValueStatistics> aggregateInPlaceByProduct_serial_eager_ec()
    {
        MutableMap<Product, MarketValueStatistics> result =
                this.ecPositions.aggregateInPlaceBy(
                        Position::getProduct,
                        MarketValueStatistics::new,
                        MarketValueStatistics::accept);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Account, MarketValueStatistics> aggregateInPlaceByAccount_serial_eager_ec()
    {
        MutableMap<Account, MarketValueStatistics> result =
                this.ecPositions.aggregateInPlaceBy(
                        Position::getAccount,
                        MarketValueStatistics::new,
                        MarketValueStatistics::accept);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<String, MarketValueStatistics> aggregateInPlaceByCategory_serial_eager_ec()
    {
        MutableMap<String, MarketValueStatistics> result =
                this.ecPositions.aggregateInPlaceBy(
                        Position::getCategory,
                        MarketValueStatistics::new,
                        MarketValueStatistics::accept);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Product, MarketValueStatistics> aggregateInPlaceByProduct_parallel_eager_ec()
    {
        MutableMap<Product, MarketValueStatistics> result =
                ParallelIterate.aggregateInPlaceBy(
                        this.ecPositions,
                        Position::getProduct,
                        MarketValueStatistics::new,
                        MarketValueStatistics::syncAccept);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Account, MarketValueStatistics> aggregateInPlaceByAccount_parallel_eager_ec()
    {
        MutableMap<Account, MarketValueStatistics> result =
                ParallelIterate.aggregateInPlaceBy(
                        this.ecPositions,
                        Position::getAccount,
                        MarketValueStatistics::new,
                        MarketValueStatistics::syncAccept);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<String, MarketValueStatistics> aggregateInPlaceByCategory_parallel_eager_ec()
    {
        MutableMap<String, MarketValueStatistics> result =
                ParallelIterate.aggregateInPlaceBy(
                        this.ecPositions,
                        Position::getCategory,
                        MarketValueStatistics::new,
                        MarketValueStatistics::syncAccept);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MapIterable<Product, MarketValueStatistics> aggregateInPlaceByProduct_parallel_lazy_ec()
    {
        MapIterable<Product, MarketValueStatistics> result =
                this.ecPositions.asParallel(this.executorService, BATCH_SIZE)
                        .aggregateInPlaceBy(
                                Position::getProduct,
                                MarketValueStatistics::new,
                                MarketValueStatistics::syncAccept);
        Assert.assertNotNull(result);
        return result;
    }

    @Test
    public void test_aggregateInPlaceByProduct_parallel_lazy_ec()
    {
        MapIterable<Product, MarketValueStatistics> actual = this.aggregateInPlaceByProduct_parallel_lazy_ec();
        MapIterable<Product, MarketValueStatistics> expected = this.aggregateInPlaceByProduct_serial_eager_ec();
        Assert.assertEquals(expected, expected);
        Verify.assertMapsEqual((Map<Product, MarketValueStatistics>) expected, (Map<Product, MarketValueStatistics>) actual);
    }

    @Benchmark
    public MapIterable<Account, MarketValueStatistics> aggregateInPlaceByAccount_parallel_lazy_ec()
    {
        MapIterable<Account, MarketValueStatistics> result =
                this.ecPositions.asParallel(this.executorService, BATCH_SIZE)
                        .aggregateInPlaceBy(
                                Position::getAccount,
                                MarketValueStatistics::new,
                                MarketValueStatistics::syncAccept);
        Assert.assertNotNull(result);
        return result;
    }

    @Test
    public void test_aggregateInPlaceByAccount_parallel_lazy_ec()
    {
        MapIterable<Account, MarketValueStatistics> actual = this.aggregateInPlaceByAccount_parallel_lazy_ec();
        MapIterable<Account, MarketValueStatistics> expected = this.aggregateInPlaceByAccount_serial_eager_ec();
        Assert.assertEquals(expected, expected);
        Verify.assertMapsEqual((Map<Account, MarketValueStatistics>) expected, (Map<Account, MarketValueStatistics>) actual);
    }

    @Benchmark
    public MapIterable<String, MarketValueStatistics> aggregateInPlaceByCategory_parallel_lazy_ec()
    {
        MapIterable<String, MarketValueStatistics> result =
                this.ecPositions.asParallel(this.executorService, BATCH_SIZE)
                        .aggregateInPlaceBy(
                                Position::getCategory,
                                MarketValueStatistics::new,
                                MarketValueStatistics::syncAccept);
        Assert.assertNotNull(result);
        return result;
    }

    @Test
    public void test_aggregateInPlaceByCategory_parallel_lazy_ec()
    {
        MapIterable<String, MarketValueStatistics> actual = this.aggregateInPlaceByCategory_parallel_lazy_ec();
        MapIterable<String, MarketValueStatistics> expected = this.aggregateInPlaceByCategory_serial_eager_ec();
        Assert.assertEquals(expected, expected);
        Verify.assertMapsEqual((Map<String, MarketValueStatistics>) expected, (Map<String, MarketValueStatistics>) actual);
    }

    private static boolean isCloseTo(double a, double b, double delta)
    {
        return a - b < delta || b - a < delta;
    }

    private static final class ImmutableMarketValueStatistics
    {
        private static final ImmutableMarketValueStatistics ZERO = new ImmutableMarketValueStatistics();

        private final long count;
        private final double sum;
        private final double min;
        private final double max;

        private ImmutableMarketValueStatistics()
        {
            this(0, 0.0, Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY);
        }

        private ImmutableMarketValueStatistics(long count, double sum, double min, double max)
        {
            this.count = count;
            this.sum = sum;
            this.min = min;
            this.max = max;
        }

        public ImmutableMarketValueStatistics add(Position position)
        {
            double marketValue = position.getMarketValue();
            return new ImmutableMarketValueStatistics(
                    this.count + 1,
                    this.sum + marketValue,
                    Math.min(this.min, marketValue),
                    Math.max(this.max, marketValue));
        }

        public static ImmutableMarketValueStatistics getZero()
        {
            return ZERO;
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }

            ImmutableMarketValueStatistics that = (ImmutableMarketValueStatistics) o;

            if (this.count != that.count)
            {
                return false;
            }
            if (Double.compare(that.max, this.max) != 0)
            {
                return false;
            }
            if (Double.compare(that.min, this.min) != 0)
            {
                return false;
            }
            return AggregateByTest.isCloseTo(that.sum, this.sum, 0.0001);
        }

        @Override
        public int hashCode()
        {
            int result = (int) (this.count ^ (this.count >>> 32));
            long temp = Double.doubleToLongBits(this.sum);
            result = 31 * result + (int) (temp ^ (temp >>> 32));
            temp = Double.doubleToLongBits(this.min);
            result = 31 * result + (int) (temp ^ (temp >>> 32));
            temp = Double.doubleToLongBits(this.max);
            result = 31 * result + (int) (temp ^ (temp >>> 32));
            return result;
        }

        @Override
        public String toString()
        {
            return "ImmutableMarketValueStatistics{"
                    + "count=" + this.count
                    + ", sum=" + this.sum
                    + ", min=" + this.min
                    + ", max=" + this.max
                    + '}';
        }
    }

    private static final class MarketValueStatistics extends DoubleSummaryStatistics
    {
        public void accept(Position position)
        {
            this.accept(position.getMarketValue());
        }

        public synchronized void syncAccept(Position position)
        {
            this.accept(position);
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }

            MarketValueStatistics that = (MarketValueStatistics) o;

            if (this.getCount() != that.getCount())
            {
                return false;
            }
            if (Double.compare(that.getMax(), this.getMax()) != 0)
            {
                return false;
            }
            if (Double.compare(that.getMin(), this.getMin()) != 0)
            {
                return false;
            }
            return AggregateByTest.isCloseTo(that.getSum(), this.getSum(), 0.01);
        }

        @Override
        public int hashCode()
        {
            int result = (int) (this.getCount() ^ (this.getCount() >>> 32));
            long temp = Double.doubleToLongBits(this.getSum());
            result = 31 * result + (int) (temp ^ (temp >>> 32));
            temp = Double.doubleToLongBits(this.getMin());
            result = 31 * result + (int) (temp ^ (temp >>> 32));
            temp = Double.doubleToLongBits(this.getMax());
            result = 31 * result + (int) (temp ^ (temp >>> 32));
            return result;
        }
    }

    private final class Position
    {
        private final Account account = AggregateByTest.this.accountPool.put(new Account());
        private final Product product = AggregateByTest.this.productPool.put(new Product());
        private final int quantity = INTS.nextInt();

        public Account getAccount()
        {
            return this.account;
        }

        public Product getProduct()
        {
            return this.product;
        }

        public String getCategory()
        {
            return this.product.getCategory();
        }

        public int getQuantity()
        {
            return this.quantity;
        }

        public double getMarketValue()
        {
            return this.quantity * this.product.getPrice();
        }
    }

    private static final class Account
    {
        private final String name = RandomStringUtils.randomNumeric(5);

        public String getName()
        {
            return this.name;
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }

            Account account = (Account) o;

            return this.name.equals(account.name);
        }

        @Override
        public int hashCode()
        {
            return this.name.hashCode();
        }
    }

    private final class Product
    {
        private final String name = RandomStringUtils.randomNumeric(3);
        private final String category = AggregateByTest.this.categoryPool.put(RandomStringUtils.randomAlphabetic(1).toUpperCase());
        private final double price = DOUBLES.nextDouble();

        public String getName()
        {
            return this.name;
        }

        public double getPrice()
        {
            return this.price;
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }

            Product account = (Product) o;

            return this.name.equals(account.name);
        }

        public String getCategory()
        {
            return this.category;
        }

        @Override
        public int hashCode()
        {
            return this.name.hashCode();
        }

        @Override
        public String toString()
        {
            return "Product{"
                    + "name='" + this.name + '\''
                    + ", category='" + this.category + '\''
                    + ", price=" + this.price
                    + '}';
        }
    }
}
```

### Method 36

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Collections;
import java.util.DoubleSummaryStatistics;
import java.util.Map;
import java.util.PrimitiveIterator;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.map.MapIterable;
import org.eclipse.collections.api.map.MutableMap;
import org.eclipse.collections.api.set.Pool;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.eclipse.collections.impl.test.Verify;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AggregateByTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private static final Random RANDOM = new Random(System.currentTimeMillis());
    private static final PrimitiveIterator.OfInt INTS = RANDOM.ints(1, 10).iterator();
    private static final PrimitiveIterator.OfDouble DOUBLES = RANDOM.doubles(1.0d, 100.0d).iterator();
    private final Pool<Account> accountPool = UnifiedSet.newSet();
    private final Pool<Product> productPool = UnifiedSet.newSet();
    private final Pool<String> categoryPool = UnifiedSet.newSet();
    private final FastList<Position> ecPositions = FastList.newWithNValues(SIZE, Position::new);
    private final ArrayList<Position> jdkPositions = new ArrayList<>(this.ecPositions);

    private ExecutorService executorService;

    @Before
    @Setup(Level.Iteration)
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        this.ecPositions.shuffleThis();
        Collections.shuffle(this.jdkPositions);
    }

    @After
    @TearDown(Level.Iteration)
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public Map<Product, DoubleSummaryStatistics> aggregateByProduct_serial_lazy_jdk()
    {
        Map<Product, DoubleSummaryStatistics> result =
                this.jdkPositions.stream().collect(
                        Collectors.groupingBy(
                                Position::getProduct,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<Product, DoubleSummaryStatistics> aggregateByProduct_serial_lazy_streams_ec()
    {
        Map<Product, DoubleSummaryStatistics> result =
                this.ecPositions.stream().collect(
                        Collectors.groupingBy(
                                Position::getProduct,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<Account, DoubleSummaryStatistics> aggregateByAccount_serial_lazy_jdk()
    {
        Map<Account, DoubleSummaryStatistics> accountDoubleMap =
                this.jdkPositions.stream().collect(
                        Collectors.groupingBy(
                                Position::getAccount,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(accountDoubleMap);
        return accountDoubleMap;
    }

    @Benchmark
    public Map<Account, DoubleSummaryStatistics> aggregateByAccount_serial_lazy_streams_ec()
    {
        Map<Account, DoubleSummaryStatistics> accountDoubleMap =
                this.ecPositions.stream().collect(
                        Collectors.groupingBy(
                                Position::getAccount,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(accountDoubleMap);
        return accountDoubleMap;
    }

    @Benchmark
    public Map<String, DoubleSummaryStatistics> aggregateByCategory_serial_lazy_jdk()
    {
        Map<String, DoubleSummaryStatistics> categoryDoubleMap =
                this.jdkPositions.stream().collect(
                        Collectors.groupingBy(
                                Position::getCategory,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(categoryDoubleMap);
        return categoryDoubleMap;
    }

    @Benchmark
    public Map<String, DoubleSummaryStatistics> aggregateByCategory_serial_lazy_streams_ec()
    {
        Map<String, DoubleSummaryStatistics> categoryDoubleMap =
                this.ecPositions.stream().collect(
                        Collectors.groupingBy(
                                Position::getCategory,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(categoryDoubleMap);
        return categoryDoubleMap;
    }

    @Benchmark
    public Map<Product, DoubleSummaryStatistics> aggregateByProduct_parallel_lazy_jdk()
    {
        Map<Product, DoubleSummaryStatistics> result =
                this.jdkPositions.parallelStream().collect(
                        Collectors.groupingBy(
                                Position::getProduct,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<Product, DoubleSummaryStatistics> aggregateByProduct_parallel_lazy_streams_ec()
    {
        Map<Product, DoubleSummaryStatistics> result =
                this.ecPositions.parallelStream().collect(
                        Collectors.groupingBy(
                                Position::getProduct,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<Account, DoubleSummaryStatistics> aggregateByAccount_parallel_lazy_jdk()
    {
        Map<Account, DoubleSummaryStatistics> result =
                this.jdkPositions.parallelStream().collect(
                        Collectors.groupingBy(
                                Position::getAccount,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<Account, DoubleSummaryStatistics> aggregateByAccount_parallel_lazy_streams_ec()
    {
        Map<Account, DoubleSummaryStatistics> result =
                this.ecPositions.parallelStream().collect(
                        Collectors.groupingBy(
                                Position::getAccount,
                                Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<String, DoubleSummaryStatistics> aggregateByCategory_parallel_lazy_jdk()
    {
        Map<String, DoubleSummaryStatistics> result =
                this.jdkPositions.parallelStream().collect(
                        Collectors.groupingBy(Position::getCategory, Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public Map<String, DoubleSummaryStatistics> aggregateByCategory_parallel_lazy_streams_ec()
    {
        Map<String, DoubleSummaryStatistics> result =
                this.ecPositions.parallelStream().collect(
                        Collectors.groupingBy(Position::getCategory, Collectors.summarizingDouble(Position::getMarketValue)));
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Product, ImmutableMarketValueStatistics> aggregateByProduct_serial_eager_ec()
    {
        MutableMap<Product, ImmutableMarketValueStatistics> result =
                this.ecPositions.aggregateBy(
                        Position::getProduct,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Account, ImmutableMarketValueStatistics> aggregateByAccount_serial_eager_ec()
    {
        MutableMap<Account, ImmutableMarketValueStatistics> result =
                this.ecPositions.aggregateBy(
                        Position::getAccount,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<String, ImmutableMarketValueStatistics> aggregateByCategory_serial_eager_ec()
    {
        MutableMap<String, ImmutableMarketValueStatistics> result =
                this.ecPositions.aggregateBy(
                        Position::getCategory,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Product, ImmutableMarketValueStatistics> aggregateByProduct_parallel_eager_ec()
    {
        MutableMap<Product, ImmutableMarketValueStatistics> result =
                ParallelIterate.aggregateBy(
                        this.ecPositions,
                        Position::getProduct,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Account, ImmutableMarketValueStatistics> aggregateByAccount_parallel_eager_ec()
    {
        MutableMap<Account, ImmutableMarketValueStatistics> result =
                ParallelIterate.aggregateBy(
                        this.ecPositions,
                        Position::getAccount,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<String, ImmutableMarketValueStatistics> aggregateByCategory_parallel_eager_ec()
    {
        MutableMap<String, ImmutableMarketValueStatistics> result =
                ParallelIterate.aggregateBy(
                        this.ecPositions,
                        Position::getCategory,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MapIterable<Product, ImmutableMarketValueStatistics> aggregateByProduct_serial_lazy_ec()
    {
        MapIterable<Product, ImmutableMarketValueStatistics> result =
                this.ecPositions.asLazy().aggregateBy(
                        Position::getProduct,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MapIterable<Account, ImmutableMarketValueStatistics> aggregateByAccount_serial_lazy_ec()
    {
        MapIterable<Account, ImmutableMarketValueStatistics> result =
                this.ecPositions.asLazy().aggregateBy(
                        Position::getAccount,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MapIterable<String, ImmutableMarketValueStatistics> aggregateByCategory_serial_lazy_ec()
    {
        MapIterable<String, ImmutableMarketValueStatistics> result =
                this.ecPositions.asLazy().aggregateBy(
                        Position::getCategory,
                        ImmutableMarketValueStatistics::new,
                        ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MapIterable<Product, ImmutableMarketValueStatistics> aggregateByProduct_parallel_lazy_ec()
    {
        MapIterable<Product, ImmutableMarketValueStatistics> result =
                this.ecPositions.asParallel(this.executorService, BATCH_SIZE)
                        .aggregateBy(
                                Position::getProduct,
                                ImmutableMarketValueStatistics::getZero,
                                ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Test
    public void test_aggregateByProduct_parallel_lazy_ec()
    {
        MapIterable<Product, ImmutableMarketValueStatistics> actual = this.aggregateByProduct_parallel_lazy_ec();
        MapIterable<Product, ImmutableMarketValueStatistics> expected = this.aggregateByProduct_serial_lazy_ec();
        Assert.assertEquals(expected, expected);
        Verify.assertMapsEqual((Map<Product, ImmutableMarketValueStatistics>) expected, (Map<Product, ImmutableMarketValueStatistics>) actual);
    }

    @Benchmark
    public MapIterable<Account, ImmutableMarketValueStatistics> aggregateByAccount_parallel_lazy_ec()
    {
        MapIterable<Account, ImmutableMarketValueStatistics> result =
                this.ecPositions.asParallel(this.executorService, BATCH_SIZE)
                        .aggregateBy(
                                Position::getAccount,
                                ImmutableMarketValueStatistics::new,
                                ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Test
    public void test_aggregateByAccount_parallel_lazy_ec()
    {
        MapIterable<Account, ImmutableMarketValueStatistics> actual = this.aggregateByAccount_parallel_lazy_ec();
        MapIterable<Account, ImmutableMarketValueStatistics> expected = this.aggregateByAccount_serial_lazy_ec();
        Assert.assertEquals(expected, expected);
        Verify.assertMapsEqual((Map<Account, ImmutableMarketValueStatistics>) expected, (Map<Account, ImmutableMarketValueStatistics>) actual);
    }

    @Benchmark
    public MapIterable<String, ImmutableMarketValueStatistics> aggregateByCategory_parallel_lazy_ec()
    {
        MapIterable<String, ImmutableMarketValueStatistics> result =
                this.ecPositions.asParallel(this.executorService, BATCH_SIZE)
                        .aggregateBy(
                                Position::getCategory,
                                ImmutableMarketValueStatistics::new,
                                ImmutableMarketValueStatistics::add);
        Assert.assertNotNull(result);
        return result;
    }

    @Test
    public void test_aggregateByCategory_parallel_lazy_ec()
    {
        MapIterable<String, ImmutableMarketValueStatistics> actual = this.aggregateByCategory_parallel_lazy_ec();
        MapIterable<String, ImmutableMarketValueStatistics> expected = this.aggregateByCategory_serial_lazy_ec();
        Assert.assertEquals(expected, expected);
        Verify.assertMapsEqual((Map<String, ImmutableMarketValueStatistics>) expected, (Map<String, ImmutableMarketValueStatistics>) actual);
    }

    @Benchmark
    public MutableMap<Product, MarketValueStatistics> aggregateInPlaceByProduct_serial_eager_ec()
    {
        MutableMap<Product, MarketValueStatistics> result =
                this.ecPositions.aggregateInPlaceBy(
                        Position::getProduct,
                        MarketValueStatistics::new,
                        MarketValueStatistics::accept);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Account, MarketValueStatistics> aggregateInPlaceByAccount_serial_eager_ec()
    {
        MutableMap<Account, MarketValueStatistics> result =
                this.ecPositions.aggregateInPlaceBy(
                        Position::getAccount,
                        MarketValueStatistics::new,
                        MarketValueStatistics::accept);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<String, MarketValueStatistics> aggregateInPlaceByCategory_serial_eager_ec()
    {
        MutableMap<String, MarketValueStatistics> result =
                this.ecPositions.aggregateInPlaceBy(
                        Position::getCategory,
                        MarketValueStatistics::new,
                        MarketValueStatistics::accept);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Product, MarketValueStatistics> aggregateInPlaceByProduct_parallel_eager_ec()
    {
        MutableMap<Product, MarketValueStatistics> result =
                ParallelIterate.aggregateInPlaceBy(
                        this.ecPositions,
                        Position::getProduct,
                        MarketValueStatistics::new,
                        MarketValueStatistics::syncAccept);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<Account, MarketValueStatistics> aggregateInPlaceByAccount_parallel_eager_ec()
    {
        MutableMap<Account, MarketValueStatistics> result =
                ParallelIterate.aggregateInPlaceBy(
                        this.ecPositions,
                        Position::getAccount,
                        MarketValueStatistics::new,
                        MarketValueStatistics::syncAccept);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MutableMap<String, MarketValueStatistics> aggregateInPlaceByCategory_parallel_eager_ec()
    {
        MutableMap<String, MarketValueStatistics> result =
                ParallelIterate.aggregateInPlaceBy(
                        this.ecPositions,
                        Position::getCategory,
                        MarketValueStatistics::new,
                        MarketValueStatistics::syncAccept);
        Assert.assertNotNull(result);
        return result;
    }

    @Benchmark
    public MapIterable<Product, MarketValueStatistics> aggregateInPlaceByProduct_parallel_lazy_ec()
    {
        MapIterable<Product, MarketValueStatistics> result =
                this.ecPositions.asParallel(this.executorService, BATCH_SIZE)
                        .aggregateInPlaceBy(
                                Position::getProduct,
                                MarketValueStatistics::new,
                                MarketValueStatistics::syncAccept);
        Assert.assertNotNull(result);
        return result;
    }

    @Test
    public void test_aggregateInPlaceByProduct_parallel_lazy_ec()
    {
        MapIterable<Product, MarketValueStatistics> actual = this.aggregateInPlaceByProduct_parallel_lazy_ec();
        MapIterable<Product, MarketValueStatistics> expected = this.aggregateInPlaceByProduct_serial_eager_ec();
        Assert.assertEquals(expected, expected);
        Verify.assertMapsEqual((Map<Product, MarketValueStatistics>) expected, (Map<Product, MarketValueStatistics>) actual);
    }

    @Benchmark
    public MapIterable<Account, MarketValueStatistics> aggregateInPlaceByAccount_parallel_lazy_ec()
    {
        MapIterable<Account, MarketValueStatistics> result =
                this.ecPositions.asParallel(this.executorService, BATCH_SIZE)
                        .aggregateInPlaceBy(
                                Position::getAccount,
                                MarketValueStatistics::new,
                                MarketValueStatistics::syncAccept);
        Assert.assertNotNull(result);
        return result;
    }

    @Test
    public void test_aggregateInPlaceByAccount_parallel_lazy_ec()
    {
        MapIterable<Account, MarketValueStatistics> actual = this.aggregateInPlaceByAccount_parallel_lazy_ec();
        MapIterable<Account, MarketValueStatistics> expected = this.aggregateInPlaceByAccount_serial_eager_ec();
        Assert.assertEquals(expected, expected);
        Verify.assertMapsEqual((Map<Account, MarketValueStatistics>) expected, (Map<Account, MarketValueStatistics>) actual);
    }

    @Benchmark
    public MapIterable<String, MarketValueStatistics> aggregateInPlaceByCategory_parallel_lazy_ec()
    {
        MapIterable<String, MarketValueStatistics> result =
                this.ecPositions.asParallel(this.executorService, BATCH_SIZE)
                        .aggregateInPlaceBy(
                                Position::getCategory,
                                MarketValueStatistics::new,
                                MarketValueStatistics::syncAccept);
        Assert.assertNotNull(result);
        return result;
    }

    @Test
    public void test_aggregateInPlaceByCategory_parallel_lazy_ec()
    {
        MapIterable<String, MarketValueStatistics> actual = this.aggregateInPlaceByCategory_parallel_lazy_ec();
        MapIterable<String, MarketValueStatistics> expected = this.aggregateInPlaceByCategory_serial_eager_ec();
        Assert.assertEquals(expected, expected);
        Verify.assertMapsEqual((Map<String, MarketValueStatistics>) expected, (Map<String, MarketValueStatistics>) actual);
    }

    private static boolean isCloseTo(double a, double b, double delta)
    {
        return a - b < delta || b - a < delta;
    }

    private static final class ImmutableMarketValueStatistics
    {
        private static final ImmutableMarketValueStatistics ZERO = new ImmutableMarketValueStatistics();

        private final long count;
        private final double sum;
        private final double min;
        private final double max;

        private ImmutableMarketValueStatistics()
        {
            this(0, 0.0, Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY);
        }

        private ImmutableMarketValueStatistics(long count, double sum, double min, double max)
        {
            this.count = count;
            this.sum = sum;
            this.min = min;
            this.max = max;
        }

        public ImmutableMarketValueStatistics add(Position position)
        {
            double marketValue = position.getMarketValue();
            return new ImmutableMarketValueStatistics(
                    this.count + 1,
                    this.sum + marketValue,
                    Math.min(this.min, marketValue),
                    Math.max(this.max, marketValue));
        }

        public static ImmutableMarketValueStatistics getZero()
        {
            return ZERO;
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }

            ImmutableMarketValueStatistics that = (ImmutableMarketValueStatistics) o;

            if (this.count != that.count)
            {
                return false;
            }
            if (Double.compare(that.max, this.max) != 0)
            {
                return false;
            }
            if (Double.compare(that.min, this.min) != 0)
            {
                return false;
            }
            return AggregateByTest.isCloseTo(that.sum, this.sum, 0.0001);
        }

        @Override
        public int hashCode()
        {
            int result = (int) (this.count ^ (this.count >>> 32));
            long temp = Double.doubleToLongBits(this.sum);
            result = 31 * result + (int) (temp ^ (temp >>> 32));
            temp = Double.doubleToLongBits(this.min);
            result = 31 * result + (int) (temp ^ (temp >>> 32));
            temp = Double.doubleToLongBits(this.max);
            result = 31 * result + (int) (temp ^ (temp >>> 32));
            return result;
        }

        @Override
        public String toString()
        {
            return "ImmutableMarketValueStatistics{"
                    + "count=" + this.count
                    + ", sum=" + this.sum
                    + ", min=" + this.min
                    + ", max=" + this.max
                    + '}';
        }
    }

    private static final class MarketValueStatistics extends DoubleSummaryStatistics
    {
        public void accept(Position position)
        {
            this.accept(position.getMarketValue());
        }

        public synchronized void syncAccept(Position position)
        {
            this.accept(position);
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }

            MarketValueStatistics that = (MarketValueStatistics) o;

            if (this.getCount() != that.getCount())
            {
                return false;
            }
            if (Double.compare(that.getMax(), this.getMax()) != 0)
            {
                return false;
            }
            if (Double.compare(that.getMin(), this.getMin()) != 0)
            {
                return false;
            }
            return AggregateByTest.isCloseTo(that.getSum(), this.getSum(), 0.01);
        }

        @Override
        public int hashCode()
        {
            int result = (int) (this.getCount() ^ (this.getCount() >>> 32));
            long temp = Double.doubleToLongBits(this.getSum());
            result = 31 * result + (int) (temp ^ (temp >>> 32));
            temp = Double.doubleToLongBits(this.getMin());
            result = 31 * result + (int) (temp ^ (temp >>> 32));
            temp = Double.doubleToLongBits(this.getMax());
            result = 31 * result + (int) (temp ^ (temp >>> 32));
            return result;
        }
    }

    private final class Position
    {
        private final Account account = AggregateByTest.this.accountPool.put(new Account());
        private final Product product = AggregateByTest.this.productPool.put(new Product());
        private final int quantity = INTS.nextInt();

        public Account getAccount()
        {
            return this.account;
        }

        public Product getProduct()
        {
            return this.product;
        }

        public String getCategory()
        {
            return this.product.getCategory();
        }

        public int getQuantity()
        {
            return this.quantity;
        }

        public double getMarketValue()
        {
            return this.quantity * this.product.getPrice();
        }
    }

    private static final class Account
    {
        private final String name = RandomStringUtils.randomNumeric(5);

        public String getName()
        {
            return this.name;
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }

            Account account = (Account) o;

            return this.name.equals(account.name);
        }

        @Override
        public int hashCode()
        {
            return this.name.hashCode();
        }
    }

    private final class Product
    {
        private final String name = RandomStringUtils.randomNumeric(3);
        private final String category = AggregateByTest.this.categoryPool.put(RandomStringUtils.randomAlphabetic(1).toUpperCase());
        private final double price = DOUBLES.nextDouble();

        public String getName()
        {
            return this.name;
        }

        public double getPrice()
        {
            return this.price;
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }

            Product account = (Product) o;

            return this.name.equals(account.name);
        }

        public String getCategory()
        {
            return this.category;
        }

        @Override
        public int hashCode()
        {
            return this.name.hashCode();
        }

        @Override
        public String toString()
        {
            return "Product{"
                    + "name='" + this.name + '\''
                    + ", category='" + this.category + '\''
                    + ", price=" + this.price
                    + '}';
        }
    }
}
```

### Method 37

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MaxTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;

    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final MutableList<Integer> integersEC = Interval.oneTo(SIZE).toList();

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public int serial_lazy_jdk()
    {
        return this.integersJDK.stream().max(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int serial_lazy_reverse_jdk()
    {
        return this.integersJDK.stream().max(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int serial_lazy_reverse_streams_ec()
    {
        return this.integersEC.stream().max(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int serial_lazy_intstream_jdk()
    {
        return this.integersJDK.stream().mapToInt(Integer::intValue).max().getAsInt();
    }

    @Benchmark
    public int serial_lazy_intstream_streams_ec()
    {
        return this.integersEC.stream().mapToInt(Integer::intValue).max().getAsInt();
    }

    @Benchmark
    public int parallel_lazy_jdk()
    {
        return this.integersJDK.parallelStream().max(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_streams_ec()
    {
        return this.integersEC.parallelStream().max(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_reverse_jdk()
    {
        return this.integersJDK.parallelStream().max(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_reverse_streams_ec()
    {
        return this.integersEC.parallelStream().max(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_intstream_jdk()
    {
        return this.integersJDK.parallelStream().mapToInt(Integer::intValue).max().getAsInt();
    }

    @Benchmark
    public int parallel_lazy_intstream_streams_ec()
    {
        return this.integersEC.parallelStream().mapToInt(Integer::intValue).max().getAsInt();
    }

    @Benchmark
    public int serial_eager_ec()
    {
        return this.integersEC.max(Comparator.naturalOrder());
    }

    @Benchmark
    public int serial_eager_reverse_ec()
    {
        return this.integersEC.max(Comparator.reverseOrder());
    }

    @Benchmark
    public int serial_lazy_ec()
    {
        return this.integersEC.asLazy().max(Comparator.naturalOrder());
    }

    @Benchmark
    public int serial_lazy_reverse_ec()
    {
        return this.integersEC.asLazy().max(Comparator.reverseOrder());
    }

    @Benchmark
    public int parallel_lazy_ec()
    {
        return this.integersEC.asParallel(this.executorService, BATCH_SIZE).max(Comparator.naturalOrder());
    }

    @Benchmark
    public int parallel_lazy_reverse_ec()
    {
        return this.integersEC.asParallel(this.executorService, BATCH_SIZE).max(Comparator.reverseOrder());
    }
}
```

### Method 38

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MaxTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;

    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final MutableList<Integer> integersEC = Interval.oneTo(SIZE).toList();

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public int serial_lazy_jdk()
    {
        return this.integersJDK.stream().max(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int serial_lazy_reverse_jdk()
    {
        return this.integersJDK.stream().max(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int serial_lazy_reverse_streams_ec()
    {
        return this.integersEC.stream().max(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int serial_lazy_intstream_jdk()
    {
        return this.integersJDK.stream().mapToInt(Integer::intValue).max().getAsInt();
    }

    @Benchmark
    public int serial_lazy_intstream_streams_ec()
    {
        return this.integersEC.stream().mapToInt(Integer::intValue).max().getAsInt();
    }

    @Benchmark
    public int parallel_lazy_jdk()
    {
        return this.integersJDK.parallelStream().max(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_streams_ec()
    {
        return this.integersEC.parallelStream().max(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_reverse_jdk()
    {
        return this.integersJDK.parallelStream().max(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_reverse_streams_ec()
    {
        return this.integersEC.parallelStream().max(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_intstream_jdk()
    {
        return this.integersJDK.parallelStream().mapToInt(Integer::intValue).max().getAsInt();
    }

    @Benchmark
    public int parallel_lazy_intstream_streams_ec()
    {
        return this.integersEC.parallelStream().mapToInt(Integer::intValue).max().getAsInt();
    }

    @Benchmark
    public int serial_eager_ec()
    {
        return this.integersEC.max(Comparator.naturalOrder());
    }

    @Benchmark
    public int serial_eager_reverse_ec()
    {
        return this.integersEC.max(Comparator.reverseOrder());
    }

    @Benchmark
    public int serial_lazy_ec()
    {
        return this.integersEC.asLazy().max(Comparator.naturalOrder());
    }

    @Benchmark
    public int serial_lazy_reverse_ec()
    {
        return this.integersEC.asLazy().max(Comparator.reverseOrder());
    }

    @Benchmark
    public int parallel_lazy_ec()
    {
        return this.integersEC.asParallel(this.executorService, BATCH_SIZE).max(Comparator.naturalOrder());
    }

    @Benchmark
    public int parallel_lazy_reverse_ec()
    {
        return this.integersEC.asParallel(this.executorService, BATCH_SIZE).max(Comparator.reverseOrder());
    }
}
```

### Method 39

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MinTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;

    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final MutableList<Integer> integersEC = Interval.oneTo(SIZE).toList();

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public int serial_lazy_jdk()
    {
        return this.integersJDK.stream().min(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int serial_lazy_streams_ec()
    {
        return this.integersEC.stream().min(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int serial_lazy_reverse_jdk()
    {
        return this.integersJDK.stream().min(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int serial_lazy_reverse_streams_ec()
    {
        return this.integersEC.stream().min(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int serial_lazy_intstream_jdk()
    {
        return this.integersJDK.stream().mapToInt(Integer::intValue).min().getAsInt();
    }

    @Benchmark
    public int serial_lazy_intstream_streams_ec()
    {
        return this.integersEC.stream().mapToInt(Integer::intValue).min().getAsInt();
    }

    @Benchmark
    public int parallel_lazy_jdk()
    {
        return this.integersJDK.parallelStream().min(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_streams_ec()
    {
        return this.integersEC.parallelStream().min(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_reverse_jdk()
    {
        return this.integersJDK.parallelStream().min(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_reverse_streams_ec()
    {
        return this.integersEC.parallelStream().min(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_intstream_jdk()
    {
        return this.integersJDK.parallelStream().mapToInt(Integer::intValue).min().getAsInt();
    }

    @Benchmark
    public int parallel_lazy_intstream_streams_ec()
    {
        return this.integersEC.parallelStream().mapToInt(Integer::intValue).min().getAsInt();
    }

    @Benchmark
    public int serial_eager_ec()
    {
        return this.integersEC.min(Comparator.naturalOrder());
    }

    @Benchmark
    public int serial_eager_reverse_ec()
    {
        return this.integersEC.min(Comparator.reverseOrder());
    }

    @Benchmark
    public int serial_lazy_ec()
    {
        return this.integersEC.asLazy().min(Comparator.naturalOrder());
    }

    @Benchmark
    public int serial_lazy_reverse_ec()
    {
        return this.integersEC.asLazy().min(Comparator.reverseOrder());
    }

    @Benchmark
    public int parallel_lazy_ec()
    {
        return this.integersEC.asParallel(this.executorService, BATCH_SIZE).min(Comparator.naturalOrder());
    }

    @Benchmark
    public int parallel_lazy_reverse_ec()
    {
        return this.integersEC.asParallel(this.executorService, BATCH_SIZE).min(Comparator.reverseOrder());
    }
}
```

### Method 40

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MinTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;

    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final MutableList<Integer> integersEC = Interval.oneTo(SIZE).toList();

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public int serial_lazy_jdk()
    {
        return this.integersJDK.stream().min(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int serial_lazy_streams_ec()
    {
        return this.integersEC.stream().min(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int serial_lazy_reverse_jdk()
    {
        return this.integersJDK.stream().min(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int serial_lazy_reverse_streams_ec()
    {
        return this.integersEC.stream().min(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int serial_lazy_intstream_jdk()
    {
        return this.integersJDK.stream().mapToInt(Integer::intValue).min().getAsInt();
    }

    @Benchmark
    public int serial_lazy_intstream_streams_ec()
    {
        return this.integersEC.stream().mapToInt(Integer::intValue).min().getAsInt();
    }

    @Benchmark
    public int parallel_lazy_jdk()
    {
        return this.integersJDK.parallelStream().min(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_streams_ec()
    {
        return this.integersEC.parallelStream().min(Comparator.naturalOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_reverse_jdk()
    {
        return this.integersJDK.parallelStream().min(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_reverse_streams_ec()
    {
        return this.integersEC.parallelStream().min(Comparator.reverseOrder()).get();
    }

    @Benchmark
    public int parallel_lazy_intstream_jdk()
    {
        return this.integersJDK.parallelStream().mapToInt(Integer::intValue).min().getAsInt();
    }

    @Benchmark
    public int parallel_lazy_intstream_streams_ec()
    {
        return this.integersEC.parallelStream().mapToInt(Integer::intValue).min().getAsInt();
    }

    @Benchmark
    public int serial_eager_ec()
    {
        return this.integersEC.min(Comparator.naturalOrder());
    }

    @Benchmark
    public int serial_eager_reverse_ec()
    {
        return this.integersEC.min(Comparator.reverseOrder());
    }

    @Benchmark
    public int serial_lazy_ec()
    {
        return this.integersEC.asLazy().min(Comparator.naturalOrder());
    }

    @Benchmark
    public int serial_lazy_reverse_ec()
    {
        return this.integersEC.asLazy().min(Comparator.reverseOrder());
    }

    @Benchmark
    public int parallel_lazy_ec()
    {
        return this.integersEC.asParallel(this.executorService, BATCH_SIZE).min(Comparator.naturalOrder());
    }

    @Benchmark
    public int parallel_lazy_reverse_ec()
    {
        return this.integersEC.asParallel(this.executorService, BATCH_SIZE).min(Comparator.reverseOrder());
    }
}
```

### Method 41

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.partition.PartitionIterable;
import org.eclipse.collections.api.partition.list.PartitionMutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class PartitionTest
{
    private static final int SIZE = 1_000_000;
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final MutableList<Integer> integersEC = Interval.oneTo(SIZE).toList();

    @Benchmark
    public Map<Boolean, List<Integer>> serial_lazy_jdk()
    {
        return this.integersJDK.stream().collect(Collectors.partitioningBy(each -> each % 2 == 0));
    }

    @Benchmark
    public Map<Boolean, List<Integer>> serial_lazy_streams_ec()
    {
        return this.integersEC.stream().collect(Collectors.partitioningBy(each -> each % 2 == 0));
    }

    @Benchmark
    public PartitionMutableList<Integer> serial_eager_ec()
    {
        return this.integersEC.partition(each -> each % 2 == 0);
    }

    @Benchmark
    public PartitionIterable<Integer> serial_lazy_ec()
    {
        return this.integersEC.asLazy().partition(each -> each % 2 == 0);
    }
}
```

### Method 42

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.impl.block.factory.Procedures;
import org.eclipse.collections.impl.block.procedure.CountProcedure;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class CountTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    @Param({"0", "1", "2", "3"})
    public int megamorphicWarmupLevel;

    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = new FastList<>(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Setup(Level.Trial)
    public void setUp_megamorphic()
    {
        if (this.megamorphicWarmupLevel > 0)
        {
            // serial, lazy, JDK
            {
                long evens = this.integersJDK.stream().filter(each -> each % 2 == 0).count();
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersJDK.stream().filter(each -> each % 2 == 1).count();
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersJDK.stream().filter(each -> (each & 1) == 0).count();
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // parallel, lazy, JDK
            {
                long evens = this.integersJDK.parallelStream().filter(each -> each % 2 == 0).count();
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersJDK.parallelStream().filter(each -> each % 2 == 1).count();
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersJDK.parallelStream().filter(each -> (each & 1) == 0).count();
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // serial, lazy, EC
            {
                long evens = this.integersEC.asLazy().count(each -> each % 2 == 0);
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersEC.asLazy().count(each -> each % 2 == 1);
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersEC.asLazy().count(each -> (each & 1) == 0);
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // parallel, lazy, EC
            {
                long evens = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> each % 2 == 0);
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> each % 2 == 1);
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> (each & 1) == 0);
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // serial, eager, EC
            {
                long evens = this.integersEC.count(each -> each % 2 == 0);
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersEC.count(each -> each % 2 == 1);
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersEC.count(each -> (each & 1) == 0);
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // parallel, eager, EC
            long evens = ParallelIterate.count(this.integersEC, each -> each % 2 == 0);
            Assert.assertEquals(SIZE / 2, evens);
            long odds = ParallelIterate.count(this.integersEC, each -> each % 2 == 1);
            Assert.assertEquals(SIZE / 2, odds);
            long evens2 = ParallelIterate.count(this.integersEC, each -> (each & 1) == 0);
            Assert.assertEquals(SIZE / 2, evens2);
        }

        if (this.megamorphicWarmupLevel > 1)
        {
            // stream().mapToLong().reduce()
            Assert.assertEquals(
                    500001500000L,
                    this.integersJDK.stream().mapToLong(each -> each + 1).reduce(0, (accum, each) -> accum + each));

            Assert.assertEquals(
                    500002500000L,
                    this.integersJDK.stream().mapToLong(each -> each + 2).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));

            Assert.assertEquals(
                    500003500000L,
                    this.integersJDK.stream().mapToLong(each -> each + 3).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));

            // parallelStream().mapToLong().reduce()
            Assert.assertEquals(
                    500001500000L,
                    this.integersJDK.parallelStream().mapToLong(each -> each + 1).reduce(0, (accum, each) -> accum + each));

            Assert.assertEquals(
                    500002500000L,
                    this.integersJDK.parallelStream().mapToLong(each -> each + 2).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));

            Assert.assertEquals(
                    500003500000L,
                    this.integersJDK.parallelStream().mapToLong(each -> each + 3).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));
        }

        if (this.megamorphicWarmupLevel > 2)
        {
            this.integersEC.asLazy().forEach(Procedures.cast(Assert::assertNotNull));
            this.integersEC.asLazy().forEach(Procedures.cast(each -> Assert.assertEquals(each, each)));
            this.integersEC.asLazy().forEach(new CountProcedure<>());

            this.integersEC.asParallel(this.executorService, BATCH_SIZE).forEach(Assert::assertNotNull);
            this.integersEC.asParallel(this.executorService, BATCH_SIZE).forEach(each -> Assert.assertEquals(each, each));
            this.integersEC.asParallel(this.executorService, BATCH_SIZE).forEach(new CountProcedure<>());

            this.integersJDK.stream().forEach(Assert::assertNotNull);
            this.integersJDK.stream().forEach(each -> Assert.assertEquals(each, each));

            this.integersJDK.parallelStream().forEach(Assert::assertNotNull);
            this.integersJDK.parallelStream().forEach(each -> Assert.assertEquals(each, each));
        }

        CountScalaTest.megamorphic(this.megamorphicWarmupLevel);
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        long evens = this.integersJDK.stream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        long evens = this.integersEC.stream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        long evens = this.integersJDK.parallelStream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        long evens = this.integersEC.parallelStream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_eager_ec()
    {
        int evens = this.integersEC.count(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_lazy_ec()
    {
        int evens = this.integersEC.asLazy().count(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        int evens = ParallelIterate.count(this.integersEC, each -> each % 2 == 0, BATCH_SIZE, this.executorService);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        int evens = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_eager_scala()
    {
        CountScalaTest.serial_eager_scala();
    }

    @Benchmark
    public void serial_lazy_scala()
    {
        CountScalaTest.serial_lazy_scala();
    }

    @Benchmark
    public void parallel_lazy_scala()
    {
        CountScalaTest.parallel_lazy_scala();
    }
}
```

### Method 43

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.impl.block.factory.Procedures;
import org.eclipse.collections.impl.block.procedure.CountProcedure;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class CountTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    @Param({"0", "1", "2", "3"})
    public int megamorphicWarmupLevel;

    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = new FastList<>(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Setup(Level.Trial)
    public void setUp_megamorphic()
    {
        if (this.megamorphicWarmupLevel > 0)
        {
            // serial, lazy, JDK
            {
                long evens = this.integersJDK.stream().filter(each -> each % 2 == 0).count();
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersJDK.stream().filter(each -> each % 2 == 1).count();
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersJDK.stream().filter(each -> (each & 1) == 0).count();
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // parallel, lazy, JDK
            {
                long evens = this.integersJDK.parallelStream().filter(each -> each % 2 == 0).count();
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersJDK.parallelStream().filter(each -> each % 2 == 1).count();
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersJDK.parallelStream().filter(each -> (each & 1) == 0).count();
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // serial, lazy, EC
            {
                long evens = this.integersEC.asLazy().count(each -> each % 2 == 0);
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersEC.asLazy().count(each -> each % 2 == 1);
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersEC.asLazy().count(each -> (each & 1) == 0);
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // parallel, lazy, EC
            {
                long evens = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> each % 2 == 0);
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> each % 2 == 1);
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> (each & 1) == 0);
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // serial, eager, EC
            {
                long evens = this.integersEC.count(each -> each % 2 == 0);
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersEC.count(each -> each % 2 == 1);
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersEC.count(each -> (each & 1) == 0);
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // parallel, eager, EC
            long evens = ParallelIterate.count(this.integersEC, each -> each % 2 == 0);
            Assert.assertEquals(SIZE / 2, evens);
            long odds = ParallelIterate.count(this.integersEC, each -> each % 2 == 1);
            Assert.assertEquals(SIZE / 2, odds);
            long evens2 = ParallelIterate.count(this.integersEC, each -> (each & 1) == 0);
            Assert.assertEquals(SIZE / 2, evens2);
        }

        if (this.megamorphicWarmupLevel > 1)
        {
            // stream().mapToLong().reduce()
            Assert.assertEquals(
                    500001500000L,
                    this.integersJDK.stream().mapToLong(each -> each + 1).reduce(0, (accum, each) -> accum + each));

            Assert.assertEquals(
                    500002500000L,
                    this.integersJDK.stream().mapToLong(each -> each + 2).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));

            Assert.assertEquals(
                    500003500000L,
                    this.integersJDK.stream().mapToLong(each -> each + 3).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));

            // parallelStream().mapToLong().reduce()
            Assert.assertEquals(
                    500001500000L,
                    this.integersJDK.parallelStream().mapToLong(each -> each + 1).reduce(0, (accum, each) -> accum + each));

            Assert.assertEquals(
                    500002500000L,
                    this.integersJDK.parallelStream().mapToLong(each -> each + 2).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));

            Assert.assertEquals(
                    500003500000L,
                    this.integersJDK.parallelStream().mapToLong(each -> each + 3).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));
        }

        if (this.megamorphicWarmupLevel > 2)
        {
            this.integersEC.asLazy().forEach(Procedures.cast(Assert::assertNotNull));
            this.integersEC.asLazy().forEach(Procedures.cast(each -> Assert.assertEquals(each, each)));
            this.integersEC.asLazy().forEach(new CountProcedure<>());

            this.integersEC.asParallel(this.executorService, BATCH_SIZE).forEach(Assert::assertNotNull);
            this.integersEC.asParallel(this.executorService, BATCH_SIZE).forEach(each -> Assert.assertEquals(each, each));
            this.integersEC.asParallel(this.executorService, BATCH_SIZE).forEach(new CountProcedure<>());

            this.integersJDK.stream().forEach(Assert::assertNotNull);
            this.integersJDK.stream().forEach(each -> Assert.assertEquals(each, each));

            this.integersJDK.parallelStream().forEach(Assert::assertNotNull);
            this.integersJDK.parallelStream().forEach(each -> Assert.assertEquals(each, each));
        }

        CountScalaTest.megamorphic(this.megamorphicWarmupLevel);
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        long evens = this.integersJDK.stream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        long evens = this.integersEC.stream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        long evens = this.integersJDK.parallelStream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        long evens = this.integersEC.parallelStream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_eager_ec()
    {
        int evens = this.integersEC.count(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_lazy_ec()
    {
        int evens = this.integersEC.asLazy().count(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        int evens = ParallelIterate.count(this.integersEC, each -> each % 2 == 0, BATCH_SIZE, this.executorService);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        int evens = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_eager_scala()
    {
        CountScalaTest.serial_eager_scala();
    }

    @Benchmark
    public void serial_lazy_scala()
    {
        CountScalaTest.serial_lazy_scala();
    }

    @Benchmark
    public void parallel_lazy_scala()
    {
        CountScalaTest.parallel_lazy_scala();
    }
}
```

### Method 44

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AllSatisfyTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = FastList.newList(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_jdk()
    {
        Assert.assertFalse(this.integersJDK.stream().allMatch(each -> each < SIZE / 2));
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_streams_ec()
    {
        Assert.assertFalse(this.integersEC.stream().allMatch(each -> each < SIZE / 2));
    }

    @Benchmark
    public void process_all_serial_lazy_jdk()
    {
        Assert.assertTrue(this.integersJDK.stream().allMatch(each -> each > 0));
    }

    @Benchmark
    public void process_all_serial_lazy_streams_ec()
    {
        Assert.assertTrue(this.integersEC.stream().allMatch(each -> each > 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_eager_ec()
    {
        Assert.assertFalse(this.integersEC.allSatisfy(each -> each < SIZE / 2));
    }

    @Benchmark
    public void process_all_serial_eager_ec()
    {
        Assert.assertTrue(this.integersEC.allSatisfy(each -> each > 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_ec()
    {
        Assert.assertFalse(this.integersEC.asLazy().allSatisfy(each -> each < SIZE / 2));
    }

    @Benchmark
    public void process_all_serial_lazy_ec()
    {
        Assert.assertTrue(this.integersEC.asLazy().allSatisfy(each -> each > 0));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_jdk()
    {
        Assert.assertFalse(this.integersJDK.parallelStream().allMatch(each -> each != SIZE / 2 - 1));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_streams_ec()
    {
        Assert.assertFalse(this.integersEC.parallelStream().allMatch(each -> each != SIZE / 2 - 1));
    }

    @Benchmark
    public void process_all_parallel_lazy_jdk()
    {
        Assert.assertTrue(this.integersJDK.parallelStream().allMatch(each -> each > 0));
    }

    @Benchmark
    public void process_all_parallel_lazy_streams_ec()
    {
        Assert.assertTrue(this.integersEC.parallelStream().allMatch(each -> each > 0));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_ec()
    {
        Assert.assertFalse(this.integersEC.asParallel(this.executorService, BATCH_SIZE).allSatisfy(each -> each != SIZE / 2 - 1));
    }

    @Benchmark
    public void process_all_parallel_lazy_ec()
    {
        Assert.assertTrue(this.integersEC.asParallel(this.executorService, BATCH_SIZE).allSatisfy(each -> each > 0));
    }
}
```

### Method 45

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AllSatisfyTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = FastList.newList(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_jdk()
    {
        Assert.assertFalse(this.integersJDK.stream().allMatch(each -> each < SIZE / 2));
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_streams_ec()
    {
        Assert.assertFalse(this.integersEC.stream().allMatch(each -> each < SIZE / 2));
    }

    @Benchmark
    public void process_all_serial_lazy_jdk()
    {
        Assert.assertTrue(this.integersJDK.stream().allMatch(each -> each > 0));
    }

    @Benchmark
    public void process_all_serial_lazy_streams_ec()
    {
        Assert.assertTrue(this.integersEC.stream().allMatch(each -> each > 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_eager_ec()
    {
        Assert.assertFalse(this.integersEC.allSatisfy(each -> each < SIZE / 2));
    }

    @Benchmark
    public void process_all_serial_eager_ec()
    {
        Assert.assertTrue(this.integersEC.allSatisfy(each -> each > 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_ec()
    {
        Assert.assertFalse(this.integersEC.asLazy().allSatisfy(each -> each < SIZE / 2));
    }

    @Benchmark
    public void process_all_serial_lazy_ec()
    {
        Assert.assertTrue(this.integersEC.asLazy().allSatisfy(each -> each > 0));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_jdk()
    {
        Assert.assertFalse(this.integersJDK.parallelStream().allMatch(each -> each != SIZE / 2 - 1));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_streams_ec()
    {
        Assert.assertFalse(this.integersEC.parallelStream().allMatch(each -> each != SIZE / 2 - 1));
    }

    @Benchmark
    public void process_all_parallel_lazy_jdk()
    {
        Assert.assertTrue(this.integersJDK.parallelStream().allMatch(each -> each > 0));
    }

    @Benchmark
    public void process_all_parallel_lazy_streams_ec()
    {
        Assert.assertTrue(this.integersEC.parallelStream().allMatch(each -> each > 0));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_ec()
    {
        Assert.assertFalse(this.integersEC.asParallel(this.executorService, BATCH_SIZE).allSatisfy(each -> each != SIZE / 2 - 1));
    }

    @Benchmark
    public void process_all_parallel_lazy_ec()
    {
        Assert.assertTrue(this.integersEC.asParallel(this.executorService, BATCH_SIZE).allSatisfy(each -> each > 0));
    }
}
```

### Method 46

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AnySatisfyTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = FastList.newList(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_jdk()
    {
        Assert.assertTrue(this.integersJDK.stream().anyMatch(each -> each > SIZE / 2));
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_streams_ec()
    {
        Assert.assertTrue(this.integersEC.stream().anyMatch(each -> each > SIZE / 2));
    }

    @Benchmark
    public void process_all_serial_lazy_jdk()
    {
        Assert.assertFalse(this.integersJDK.stream().anyMatch(each -> each < 0));
    }

    @Benchmark
    public void process_all_serial_lazy_streams_ec()
    {
        Assert.assertFalse(this.integersEC.stream().anyMatch(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_eager_ec()
    {
        Assert.assertTrue(this.integersEC.anySatisfy(each -> each > SIZE / 2));
    }

    @Benchmark
    public void process_all_serial_eager_ec()
    {
        Assert.assertFalse(this.integersEC.anySatisfy(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_ec()
    {
        Assert.assertTrue(this.integersEC.asLazy().anySatisfy(each -> each > SIZE / 2));
    }

    @Benchmark
    public void process_all_serial_lazy_ec()
    {
        Assert.assertFalse(this.integersEC.asLazy().anySatisfy(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_eager_scala()
    {
        AnySatisfyScalaTest.short_circuit_middle_serial_eager_scala();
    }

    @Benchmark
    public void process_all_serial_eager_scala()
    {
        AnySatisfyScalaTest.process_all_serial_eager_scala();
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_scala()
    {
        AnySatisfyScalaTest.short_circuit_middle_serial_lazy_scala();
    }

    @Benchmark
    public void process_all_serial_lazy_scala()
    {
        AnySatisfyScalaTest.process_all_serial_lazy_scala();
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_jdk()
    {
        Assert.assertTrue(this.integersJDK.parallelStream().anyMatch(each -> each == SIZE / 2 - 1));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_streams_ec()
    {
        Assert.assertTrue(this.integersEC.parallelStream().anyMatch(each -> each == SIZE / 2 - 1));
    }

    @Benchmark
    public void process_all_parallel_lazy_jdk()
    {
        Assert.assertFalse(this.integersJDK.parallelStream().anyMatch(each -> each < 0));
    }

    @Benchmark
    public void process_all_parallel_lazy_streams_ec()
    {
        Assert.assertFalse(this.integersEC.parallelStream().anyMatch(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_ec()
    {
        Assert.assertTrue(this.integersEC.asParallel(this.executorService, BATCH_SIZE).anySatisfy(each -> each == SIZE / 2 - 1));
    }

    @Benchmark
    public void process_all_parallel_lazy_ec()
    {
        Assert.assertFalse(this.integersEC.asParallel(this.executorService, BATCH_SIZE).anySatisfy(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_scala()
    {
        AnySatisfyScalaTest.short_circuit_middle_parallel_lazy_scala();
    }

    @Benchmark
    public void process_all_parallel_lazy_scala()
    {
        AnySatisfyScalaTest.process_all_parallel_lazy_scala();
    }
}
```

### Method 47

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AnySatisfyTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = FastList.newList(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_jdk()
    {
        Assert.assertTrue(this.integersJDK.stream().anyMatch(each -> each > SIZE / 2));
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_streams_ec()
    {
        Assert.assertTrue(this.integersEC.stream().anyMatch(each -> each > SIZE / 2));
    }

    @Benchmark
    public void process_all_serial_lazy_jdk()
    {
        Assert.assertFalse(this.integersJDK.stream().anyMatch(each -> each < 0));
    }

    @Benchmark
    public void process_all_serial_lazy_streams_ec()
    {
        Assert.assertFalse(this.integersEC.stream().anyMatch(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_eager_ec()
    {
        Assert.assertTrue(this.integersEC.anySatisfy(each -> each > SIZE / 2));
    }

    @Benchmark
    public void process_all_serial_eager_ec()
    {
        Assert.assertFalse(this.integersEC.anySatisfy(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_ec()
    {
        Assert.assertTrue(this.integersEC.asLazy().anySatisfy(each -> each > SIZE / 2));
    }

    @Benchmark
    public void process_all_serial_lazy_ec()
    {
        Assert.assertFalse(this.integersEC.asLazy().anySatisfy(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_eager_scala()
    {
        AnySatisfyScalaTest.short_circuit_middle_serial_eager_scala();
    }

    @Benchmark
    public void process_all_serial_eager_scala()
    {
        AnySatisfyScalaTest.process_all_serial_eager_scala();
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_scala()
    {
        AnySatisfyScalaTest.short_circuit_middle_serial_lazy_scala();
    }

    @Benchmark
    public void process_all_serial_lazy_scala()
    {
        AnySatisfyScalaTest.process_all_serial_lazy_scala();
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_jdk()
    {
        Assert.assertTrue(this.integersJDK.parallelStream().anyMatch(each -> each == SIZE / 2 - 1));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_streams_ec()
    {
        Assert.assertTrue(this.integersEC.parallelStream().anyMatch(each -> each == SIZE / 2 - 1));
    }

    @Benchmark
    public void process_all_parallel_lazy_jdk()
    {
        Assert.assertFalse(this.integersJDK.parallelStream().anyMatch(each -> each < 0));
    }

    @Benchmark
    public void process_all_parallel_lazy_streams_ec()
    {
        Assert.assertFalse(this.integersEC.parallelStream().anyMatch(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_ec()
    {
        Assert.assertTrue(this.integersEC.asParallel(this.executorService, BATCH_SIZE).anySatisfy(each -> each == SIZE / 2 - 1));
    }

    @Benchmark
    public void process_all_parallel_lazy_ec()
    {
        Assert.assertFalse(this.integersEC.asParallel(this.executorService, BATCH_SIZE).anySatisfy(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_scala()
    {
        AnySatisfyScalaTest.short_circuit_middle_parallel_lazy_scala();
    }

    @Benchmark
    public void process_all_parallel_lazy_scala()
    {
        AnySatisfyScalaTest.process_all_parallel_lazy_scala();
    }
}
```

### Method 48

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class NoneSatisfyTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = new FastList<>(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_jdk()
    {
        Assert.assertFalse(this.integersJDK.stream().noneMatch(each -> each > SIZE / 2));
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_streams_ec()
    {
        Assert.assertFalse(this.integersEC.stream().noneMatch(each -> each > SIZE / 2));
    }

    @Benchmark
    public void process_none_serial_lazy_jdk()
    {
        Assert.assertTrue(this.integersJDK.stream().noneMatch(each -> each < 0));
    }

    @Benchmark
    public void process_none_serial_lazy_streams_ec()
    {
        Assert.assertTrue(this.integersEC.stream().noneMatch(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_eager_ec()
    {
        Assert.assertFalse(this.integersEC.noneSatisfy(each -> each > SIZE / 2));
    }

    @Benchmark
    public void process_none_serial_eager_ec()
    {
        Assert.assertTrue(this.integersEC.noneSatisfy(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_ec()
    {
        Assert.assertFalse(this.integersEC.asLazy().noneSatisfy(each -> each > SIZE / 2));
    }

    @Benchmark
    public void process_none_serial_lazy_ec()
    {
        Assert.assertTrue(this.integersEC.asLazy().noneSatisfy(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_jdk()
    {
        Assert.assertFalse(this.integersJDK.parallelStream().noneMatch(each -> each == SIZE / 2 - 1));
    }

    @Benchmark
    public void process_all_parallel_lazy_jdk()
    {
        Assert.assertTrue(this.integersJDK.parallelStream().noneMatch(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_ec()
    {
        Assert.assertFalse(this.integersEC.asParallel(this.executorService, BATCH_SIZE).noneSatisfy(each -> each == SIZE / 2 - 1));
    }

    @Benchmark
    public void process_all_parallel_lazy_ec()
    {
        Assert.assertTrue(this.integersEC.asParallel(this.executorService, BATCH_SIZE).noneSatisfy(each -> each < 0));
    }
}
```

### Method 49

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class NoneSatisfyTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final FastList<Integer> integersEC = new FastList<>(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_jdk()
    {
        Assert.assertFalse(this.integersJDK.stream().noneMatch(each -> each > SIZE / 2));
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_streams_ec()
    {
        Assert.assertFalse(this.integersEC.stream().noneMatch(each -> each > SIZE / 2));
    }

    @Benchmark
    public void process_none_serial_lazy_jdk()
    {
        Assert.assertTrue(this.integersJDK.stream().noneMatch(each -> each < 0));
    }

    @Benchmark
    public void process_none_serial_lazy_streams_ec()
    {
        Assert.assertTrue(this.integersEC.stream().noneMatch(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_eager_ec()
    {
        Assert.assertFalse(this.integersEC.noneSatisfy(each -> each > SIZE / 2));
    }

    @Benchmark
    public void process_none_serial_eager_ec()
    {
        Assert.assertTrue(this.integersEC.noneSatisfy(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_serial_lazy_ec()
    {
        Assert.assertFalse(this.integersEC.asLazy().noneSatisfy(each -> each > SIZE / 2));
    }

    @Benchmark
    public void process_none_serial_lazy_ec()
    {
        Assert.assertTrue(this.integersEC.asLazy().noneSatisfy(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_jdk()
    {
        Assert.assertFalse(this.integersJDK.parallelStream().noneMatch(each -> each == SIZE / 2 - 1));
    }

    @Benchmark
    public void process_all_parallel_lazy_jdk()
    {
        Assert.assertTrue(this.integersJDK.parallelStream().noneMatch(each -> each < 0));
    }

    @Benchmark
    public void short_circuit_middle_parallel_lazy_ec()
    {
        Assert.assertFalse(this.integersEC.asParallel(this.executorService, BATCH_SIZE).noneSatisfy(each -> each == SIZE / 2 - 1));
    }

    @Benchmark
    public void process_all_parallel_lazy_ec()
    {
        Assert.assertTrue(this.integersEC.asParallel(this.executorService, BATCH_SIZE).noneSatisfy(each -> each < 0));
    }
}
```

### Method 50

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class ListAddAllTest
{
    private static final int SIZE = 1000;
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final MutableList<Integer> integersEC = FastList.newList(Interval.oneTo(SIZE));

    @Benchmark
    public void jdk()
    {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < 1000; i++)
        {
            result.addAll(this.integersJDK);
        }
        if (result.size() != 1_000_000)
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void ec()
    {
        MutableList<Integer> result = FastList.newList();
        for (int i = 0; i < 1000; i++)
        {
            result.addAll(this.integersEC);
        }
        if (result.size() != 1_000_000)
        {
            throw new AssertionError();
        }
    }
}
```

### Method 51

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class ListEqualTest
{
    private static final int SIZE = 1_000_000;
    private final List<Integer> integersJDK1 = new ArrayList<>(Interval.oneTo(SIZE));
    private final List<Integer> integersJDK2 = new ArrayList<>(Interval.oneTo(SIZE));
    private final List<Integer> integersJDK3 = new ArrayList<>(Interval.oneTo(SIZE / 2));
    private final MutableList<Integer> integersEC1 = Interval.oneTo(SIZE).toList();
    private final MutableList<Integer> integersEC2 = Interval.oneTo(SIZE).toList();
    private final MutableList<Integer> integersEC3 = Interval.oneTo(SIZE / 2).toList();

    @Benchmark
    public void jdk()
    {
        if (!this.integersJDK1.equals(this.integersJDK1))
        {
            throw new AssertionError();
        }
        if (!this.integersJDK1.equals(this.integersJDK2))
        {
            throw new AssertionError();
        }
        if (this.integersJDK1.equals(this.integersJDK3))
        {
            throw new AssertionError();
        }
        if (!this.integersJDK1.equals(this.integersEC1))
        {
            throw new AssertionError();
        }
        if (this.integersJDK1.equals(this.integersEC3))
        {
            throw new AssertionError();
        }
    }

    @Benchmark
    public void ec()
    {
        if (!this.integersEC1.equals(this.integersEC1))
        {
            throw new AssertionError();
        }
        if (!this.integersEC1.equals(this.integersEC2))
        {
            throw new AssertionError();
        }
        if (this.integersEC1.equals(this.integersEC3))
        {
            throw new AssertionError();
        }
        if (!this.integersEC1.equals(this.integersJDK1))
        {
            throw new AssertionError();
        }
        if (this.integersEC1.equals(this.integersJDK3))
        {
            throw new AssertionError();
        }
    }
}
```

### Method 52

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.block.factory.Predicates;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class RejectTest
{
    private static final int SIZE = 1_000_000;
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final MutableList<Integer> integersEC = Interval.oneTo(SIZE).toList();

    @Benchmark
    public void serial_lazy_jdk_lambda_not()
    {
        List<Integer> evens = this.integersJDK.stream().filter(each -> each % 2 != 1).collect(Collectors.toList());
        List<Integer> odds = this.integersJDK.stream().filter(each -> each % 2 != 0).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evens.size());
        Assert.assertEquals(SIZE / 2, odds.size());
    }

    @Benchmark
    public void serial_lazy_streams_ec_lambda_not()
    {
        List<Integer> evens = this.integersEC.stream().filter(each -> each % 2 != 1).collect(Collectors.toList());
        List<Integer> odds = this.integersEC.stream().filter(each -> each % 2 != 0).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evens.size());
        Assert.assertEquals(SIZE / 2, odds.size());
    }

    @Benchmark
    public void serial_lazy_jdk_lambda_negate()
    {
        Predicate<Integer> predicate1 = each -> each % 2 == 1;
        List<Integer> evens = this.integersJDK.stream().filter(predicate1.negate()).collect(Collectors.toList());
        Predicate<Integer> predicate2 = each -> each % 2 == 0;
        List<Integer> odds = this.integersJDK.stream().filter(predicate2.negate()).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evens.size());
        Assert.assertEquals(SIZE / 2, odds.size());
    }

    @Benchmark
    public void serial_lazy_streams_ec_lambda_negate()
    {
        Predicate<Integer> predicate1 = each -> each % 2 == 1;
        List<Integer> evens = this.integersEC.stream().filter(predicate1.negate()).collect(Collectors.toList());
        Predicate<Integer> predicate2 = each -> each % 2 == 0;
        List<Integer> odds = this.integersEC.stream().filter(predicate2.negate()).collect(Collectors.toList());
        Assert.assertEquals(SIZE / 2, evens.size());
        Assert.assertEquals(SIZE / 2, odds.size());
    }

    @Benchmark
    public void serial_eager_ec_select_predicates_not()
    {
        MutableList<Integer> evens = this.integersEC.select(Predicates.not(each -> each % 2 == 1));
        MutableList<Integer> odds = this.integersEC.select(Predicates.not(each -> each % 2 == 0));
        Assert.assertEquals(SIZE / 2, evens.size());
        Assert.assertEquals(SIZE / 2, odds.size());
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableList<Integer> evens = this.integersEC.reject(each -> each % 2 == 1);
        MutableList<Integer> odds = this.integersEC.reject(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens.size());
        Assert.assertEquals(SIZE / 2, odds.size());
    }

    @Benchmark
    public void serial_lazy_ec()
    {
        MutableList<Integer> evens = this.integersEC.asLazy().reject(each -> each % 2 == 1).toList();
        MutableList<Integer> odds = this.integersEC.asLazy().reject(each -> each % 2 == 0).toList();
        Assert.assertEquals(SIZE / 2, evens.size());
        Assert.assertEquals(SIZE / 2, odds.size());
    }
}
```

### Method 53

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import com.google.common.collect.Multimaps;
import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.test.Verify;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class GroupByListTest
{
    private static final int SIZE = 1_000_000;
    private final List<Integer> integersJDK = new ArrayList<>(Interval.oneTo(SIZE));
    private final MutableList<Integer> integersEC = Interval.oneTo(SIZE).toList();

    @Benchmark
    public void groupBy_2_keys_serial_lazy_jdk()
    {
        Verify.assertSize(2, this.integersJDK.stream().collect(Collectors.groupingBy(each -> each % 2 == 0)));
    }

    @Benchmark
    public void groupBy_2_keys_serial_lazy_streams_ec()
    {
        Verify.assertSize(2, this.integersEC.stream().collect(Collectors.groupingBy(each -> each % 2 == 0)));
    }

    @Benchmark
    public void groupBy_100_keys_serial_lazy_jdk()
    {
        Verify.assertSize(100, this.integersJDK.stream().collect(Collectors.groupingBy(each -> each % 100)));
    }

    @Benchmark
    public void groupBy_100_keys_serial_lazy_streams_ec()
    {
        Verify.assertSize(100, this.integersEC.stream().collect(Collectors.groupingBy(each -> each % 100)));
    }

    @Benchmark
    public void groupBy_10000_keys_serial_lazy_jdk()
    {
        Verify.assertSize(10_000, this.integersJDK.stream().collect(Collectors.groupingBy(each -> each % 10_000)));
    }

    @Benchmark
    public void groupBy_10000_keys_serial_lazy_streams_ec()
    {
        Verify.assertSize(10_000, this.integersEC.stream().collect(Collectors.groupingBy(each -> each % 10_000)));
    }

    @Benchmark
    public void groupBy_2_keys_serial_eager_guava()
    {
        Verify.assertSize(2, Multimaps.index(this.integersJDK, each -> each % 2 == 0).asMap());
    }

    @Benchmark
    public void groupBy_100_keys_serial_eager_guava()
    {
        Verify.assertSize(100, Multimaps.index(this.integersJDK, each -> each % 100).asMap());
    }

    @Benchmark
    public void groupBy_10000_keys_serial_eager_guava()
    {
        Verify.assertSize(10_000, Multimaps.index(this.integersJDK, each -> each % 10000).asMap());
    }

    @Benchmark
    public void groupBy_2_keys_serial_eager_ec()
    {
        Assert.assertEquals(2, this.integersEC.groupBy(each -> each % 2 == 0).sizeDistinct());
    }

    @Benchmark
    public void groupBy_100_keys_serial_eager_ec()
    {
        Assert.assertEquals(100, this.integersEC.groupBy(each -> each % 100).sizeDistinct());
    }

    @Benchmark
    public void groupBy_10000_keys_serial_eager_ec()
    {
        Assert.assertEquals(10_000, this.integersEC.groupBy(each -> each % 10_000).sizeDistinct());
    }

    @Benchmark
    public void groupBy_2_keys_serial_lazy_ec()
    {
        Assert.assertEquals(2, this.integersEC.asLazy().groupBy(each -> each % 2 == 0).sizeDistinct());
    }

    @Benchmark
    public void groupBy_100_keys_serial_lazy_ec()
    {
        Assert.assertEquals(100, this.integersEC.asLazy().groupBy(each -> each % 100).sizeDistinct());
    }

    @Benchmark
    public void groupBy_10000_keys_serial_lazy_ec()
    {
        Assert.assertEquals(10_000, this.integersEC.asLazy().groupBy(each -> each % 10_000).sizeDistinct());
    }

    @Benchmark
    public void groupBy_2_keys_serial_eager_scala()
    {
        GroupByScalaTest.groupBy_2_keys_serial_eager_scala();
    }

    @Benchmark
    public void groupBy_100_keys_serial_eager_scala()
    {
        GroupByScalaTest.groupBy_100_keys_serial_eager_scala();
    }

    @Benchmark
    public void groupBy_10000_keys_serial_eager_scala()
    {
        GroupByScalaTest.groupBy_10000_keys_serial_eager_scala();
    }

    @Benchmark
    public void groupBy_2_keys_serial_lazy_scala()
    {
        GroupByScalaTest.groupBy_2_keys_serial_lazy_scala();
    }

    @Benchmark
    public void groupBy_100_keys_serial_lazy_scala()
    {
        GroupByScalaTest.groupBy_100_keys_serial_lazy_scala();
    }

    @Benchmark
    public void groupBy_10000_keys_serial_lazy_scala()
    {
        GroupByScalaTest.groupBy_10000_keys_serial_lazy_scala();
    }
}
```

### Method 54

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.RichIterable;
import org.eclipse.collections.api.multimap.MutableMultimap;
import org.eclipse.collections.api.multimap.set.MutableSetMultimap;
import org.eclipse.collections.api.multimap.set.UnsortedSetMultimap;
import org.eclipse.collections.api.tuple.Pair;
import org.eclipse.collections.impl.block.factory.Comparators;
import org.eclipse.collections.impl.block.factory.Procedures;
import org.eclipse.collections.impl.forkjoin.FJIterate;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.CompositeFastList;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.eclipse.collections.impl.tuple.Tuples;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AnagramSetTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    private static final int SIZE_THRESHOLD = 10;
    private final UnifiedSet<String> ecWords = UnifiedSet.newSet(FastList.newWithNValues(SIZE, () -> RandomStringUtils.randomAlphabetic(5).toUpperCase()));
    private final Set<String> jdkWords = new HashSet<>(this.ecWords);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_eager_scala()
    {
        AnagramSetScalaTest.serial_eager_scala();
    }

    @Benchmark
    public void serial_lazy_scala()
    {
        AnagramSetScalaTest.serial_lazy_scala();
    }

    @Benchmark
    public void parallel_lazy_scala()
    {
        AnagramSetScalaTest.parallel_lazy_scala();
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableSetMultimap<Alphagram, String> groupBy = this.ecWords.groupBy(Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = ParallelIterate.groupBy(this.ecWords, Alphagram::new);
        CompositeFastList<RichIterable<String>> select = ParallelIterate.select(groupBy.multiValuesView(), iterable -> iterable.size() >= SIZE_THRESHOLD, new CompositeFastList<>(), false);
        Collection<String> collect = ParallelIterate.collect(select
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed(), iterable -> iterable.size() + ": " + iterable);
        ParallelIterate.forEach(collect, Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        UnsortedSetMultimap<Alphagram, String> multimap = this.ecWords.asParallel(this.executorService, BATCH_SIZE)
                .groupBy(Alphagram::new);
        FastList<Pair<Integer, String>> pairs = (FastList<Pair<Integer, String>>) FastList.newList(multimap.multiValuesView()).asParallel(this.executorService, BATCH_SIZE)
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .collect(iterable -> Tuples.pair(iterable.size(), iterable.size() + ": " + iterable))
                .toSortedList((pair1, pair2) -> Integer.compare(pair2.getOne(), pair1.getOne()));
        pairs.asParallel(this.executorService, BATCH_SIZE)
                .collect(Pair::getTwo)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_forkjoin_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = FJIterate.groupBy(this.ecWords, Alphagram::new);
        CompositeFastList<RichIterable<String>> select = FJIterate.select(groupBy.multiValuesView(), iterable -> iterable.size() >= SIZE_THRESHOLD, new CompositeFastList<>(), false);
        Collection<String> collect = FJIterate.collect(select
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed(), iterable -> iterable.size() + ": " + iterable);
        FJIterate.forEach(collect, Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        Map<Alphagram, Set<String>> groupBy = this.jdkWords.stream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        Map<Alphagram, Set<String>> groupBy = this.ecWords.stream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        Map<Alphagram, Set<String>> groupBy = this.jdkWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed())
                .parallel()
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        Map<Alphagram, Set<String>> groupBy = this.ecWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed())
                .parallel()
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    private static final class Alphagram
    {
        private final char[] key;

        private Alphagram(String string)
        {
            this.key = string.toCharArray();
            Arrays.sort(this.key);
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }
            Alphagram alphagram = (Alphagram) o;
            return Arrays.equals(this.key, alphagram.key);
        }

        @Override
        public int hashCode()
        {
            return Arrays.hashCode(this.key);
        }

        @Override
        public String toString()
        {
            return new String(this.key);
        }
    }
}
```

### Method 55

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.RichIterable;
import org.eclipse.collections.api.multimap.MutableMultimap;
import org.eclipse.collections.api.multimap.set.MutableSetMultimap;
import org.eclipse.collections.api.multimap.set.UnsortedSetMultimap;
import org.eclipse.collections.api.tuple.Pair;
import org.eclipse.collections.impl.block.factory.Comparators;
import org.eclipse.collections.impl.block.factory.Procedures;
import org.eclipse.collections.impl.forkjoin.FJIterate;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.CompositeFastList;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.eclipse.collections.impl.tuple.Tuples;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AnagramSetTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    private static final int SIZE_THRESHOLD = 10;
    private final UnifiedSet<String> ecWords = UnifiedSet.newSet(FastList.newWithNValues(SIZE, () -> RandomStringUtils.randomAlphabetic(5).toUpperCase()));
    private final Set<String> jdkWords = new HashSet<>(this.ecWords);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_eager_scala()
    {
        AnagramSetScalaTest.serial_eager_scala();
    }

    @Benchmark
    public void serial_lazy_scala()
    {
        AnagramSetScalaTest.serial_lazy_scala();
    }

    @Benchmark
    public void parallel_lazy_scala()
    {
        AnagramSetScalaTest.parallel_lazy_scala();
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableSetMultimap<Alphagram, String> groupBy = this.ecWords.groupBy(Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = ParallelIterate.groupBy(this.ecWords, Alphagram::new);
        CompositeFastList<RichIterable<String>> select = ParallelIterate.select(groupBy.multiValuesView(), iterable -> iterable.size() >= SIZE_THRESHOLD, new CompositeFastList<>(), false);
        Collection<String> collect = ParallelIterate.collect(select
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed(), iterable -> iterable.size() + ": " + iterable);
        ParallelIterate.forEach(collect, Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        UnsortedSetMultimap<Alphagram, String> multimap = this.ecWords.asParallel(this.executorService, BATCH_SIZE)
                .groupBy(Alphagram::new);
        FastList<Pair<Integer, String>> pairs = (FastList<Pair<Integer, String>>) FastList.newList(multimap.multiValuesView()).asParallel(this.executorService, BATCH_SIZE)
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .collect(iterable -> Tuples.pair(iterable.size(), iterable.size() + ": " + iterable))
                .toSortedList((pair1, pair2) -> Integer.compare(pair2.getOne(), pair1.getOne()));
        pairs.asParallel(this.executorService, BATCH_SIZE)
                .collect(Pair::getTwo)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_forkjoin_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = FJIterate.groupBy(this.ecWords, Alphagram::new);
        CompositeFastList<RichIterable<String>> select = FJIterate.select(groupBy.multiValuesView(), iterable -> iterable.size() >= SIZE_THRESHOLD, new CompositeFastList<>(), false);
        Collection<String> collect = FJIterate.collect(select
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed(), iterable -> iterable.size() + ": " + iterable);
        FJIterate.forEach(collect, Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        Map<Alphagram, Set<String>> groupBy = this.jdkWords.stream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        Map<Alphagram, Set<String>> groupBy = this.ecWords.stream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        Map<Alphagram, Set<String>> groupBy = this.jdkWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed())
                .parallel()
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        Map<Alphagram, Set<String>> groupBy = this.ecWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed())
                .parallel()
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    private static final class Alphagram
    {
        private final char[] key;

        private Alphagram(String string)
        {
            this.key = string.toCharArray();
            Arrays.sort(this.key);
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }
            Alphagram alphagram = (Alphagram) o;
            return Arrays.equals(this.key, alphagram.key);
        }

        @Override
        public int hashCode()
        {
            return Arrays.hashCode(this.key);
        }

        @Override
        public String toString()
        {
            return new String(this.key);
        }
    }
}
```

### Method 56

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.RichIterable;
import org.eclipse.collections.api.multimap.MutableMultimap;
import org.eclipse.collections.api.multimap.set.MutableSetMultimap;
import org.eclipse.collections.api.multimap.set.UnsortedSetMultimap;
import org.eclipse.collections.api.tuple.Pair;
import org.eclipse.collections.impl.block.factory.Comparators;
import org.eclipse.collections.impl.block.factory.Procedures;
import org.eclipse.collections.impl.forkjoin.FJIterate;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.CompositeFastList;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.eclipse.collections.impl.tuple.Tuples;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AnagramSetTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    private static final int SIZE_THRESHOLD = 10;
    private final UnifiedSet<String> ecWords = UnifiedSet.newSet(FastList.newWithNValues(SIZE, () -> RandomStringUtils.randomAlphabetic(5).toUpperCase()));
    private final Set<String> jdkWords = new HashSet<>(this.ecWords);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_eager_scala()
    {
        AnagramSetScalaTest.serial_eager_scala();
    }

    @Benchmark
    public void serial_lazy_scala()
    {
        AnagramSetScalaTest.serial_lazy_scala();
    }

    @Benchmark
    public void parallel_lazy_scala()
    {
        AnagramSetScalaTest.parallel_lazy_scala();
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableSetMultimap<Alphagram, String> groupBy = this.ecWords.groupBy(Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = ParallelIterate.groupBy(this.ecWords, Alphagram::new);
        CompositeFastList<RichIterable<String>> select = ParallelIterate.select(groupBy.multiValuesView(), iterable -> iterable.size() >= SIZE_THRESHOLD, new CompositeFastList<>(), false);
        Collection<String> collect = ParallelIterate.collect(select
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed(), iterable -> iterable.size() + ": " + iterable);
        ParallelIterate.forEach(collect, Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        UnsortedSetMultimap<Alphagram, String> multimap = this.ecWords.asParallel(this.executorService, BATCH_SIZE)
                .groupBy(Alphagram::new);
        FastList<Pair<Integer, String>> pairs = (FastList<Pair<Integer, String>>) FastList.newList(multimap.multiValuesView()).asParallel(this.executorService, BATCH_SIZE)
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .collect(iterable -> Tuples.pair(iterable.size(), iterable.size() + ": " + iterable))
                .toSortedList((pair1, pair2) -> Integer.compare(pair2.getOne(), pair1.getOne()));
        pairs.asParallel(this.executorService, BATCH_SIZE)
                .collect(Pair::getTwo)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_forkjoin_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = FJIterate.groupBy(this.ecWords, Alphagram::new);
        CompositeFastList<RichIterable<String>> select = FJIterate.select(groupBy.multiValuesView(), iterable -> iterable.size() >= SIZE_THRESHOLD, new CompositeFastList<>(), false);
        Collection<String> collect = FJIterate.collect(select
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed(), iterable -> iterable.size() + ": " + iterable);
        FJIterate.forEach(collect, Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        Map<Alphagram, Set<String>> groupBy = this.jdkWords.stream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        Map<Alphagram, Set<String>> groupBy = this.ecWords.stream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        Map<Alphagram, Set<String>> groupBy = this.jdkWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed())
                .parallel()
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        Map<Alphagram, Set<String>> groupBy = this.ecWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed())
                .parallel()
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    private static final class Alphagram
    {
        private final char[] key;

        private Alphagram(String string)
        {
            this.key = string.toCharArray();
            Arrays.sort(this.key);
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }
            Alphagram alphagram = (Alphagram) o;
            return Arrays.equals(this.key, alphagram.key);
        }

        @Override
        public int hashCode()
        {
            return Arrays.hashCode(this.key);
        }

        @Override
        public String toString()
        {
            return new String(this.key);
        }
    }
}
```

### Method 57

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import com.google.common.collect.HashMultiset;
import com.google.common.collect.Multiset;
import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.RichIterable;
import org.eclipse.collections.api.bag.ParallelUnsortedBag;
import org.eclipse.collections.api.multimap.MutableMultimap;
import org.eclipse.collections.api.multimap.bag.UnsortedBagMultimap;
import org.eclipse.collections.api.multimap.list.MutableListMultimap;
import org.eclipse.collections.impl.bag.mutable.HashBag;
import org.eclipse.collections.impl.block.factory.Comparators;
import org.eclipse.collections.impl.block.factory.Procedures;
import org.eclipse.collections.impl.forkjoin.FJIterate;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.multimap.list.FastListMultimap;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AnagramBagTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    private static final int SIZE_THRESHOLD = 10;
    private final HashBag<String> ecWords = HashBag.newBag(FastList.newWithNValues(SIZE, () -> RandomStringUtils.randomAlphabetic(5).toUpperCase()));
    private final Multiset<String> guavaWords = HashMultiset.create(this.ecWords);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableListMultimap<Alphagram, String> groupBy = this.ecWords.groupBy(Alphagram::new, FastListMultimap.newMultimap());
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = ParallelIterate.groupBy(this.ecWords, Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        ParallelUnsortedBag<String> parallelUnsortedBag = this.ecWords.asParallel(this.executorService, BATCH_SIZE);
        UnsortedBagMultimap<Alphagram, String> groupBy = parallelUnsortedBag.groupBy(Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_forkjoin_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = FJIterate.groupBy(this.ecWords, Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        Map<Alphagram, List<String>> groupBy = this.guavaWords.stream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        Map<Alphagram, List<String>> groupBy = this.ecWords.stream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        Map<Alphagram, List<String>> groupBy = this.guavaWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        Map<Alphagram, List<String>> groupBy = this.ecWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    private static final class Alphagram
    {
        private final char[] key;

        private Alphagram(String string)
        {
            this.key = string.toCharArray();
            Arrays.sort(this.key);
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }
            Alphagram alphagram = (Alphagram) o;
            return Arrays.equals(this.key, alphagram.key);
        }

        @Override
        public int hashCode()
        {
            return Arrays.hashCode(this.key);
        }

        @Override
        public String toString()
        {
            return new String(this.key);
        }
    }
}
```

### Method 58

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import com.google.common.collect.HashMultiset;
import com.google.common.collect.Multiset;
import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.RichIterable;
import org.eclipse.collections.api.bag.ParallelUnsortedBag;
import org.eclipse.collections.api.multimap.MutableMultimap;
import org.eclipse.collections.api.multimap.bag.UnsortedBagMultimap;
import org.eclipse.collections.api.multimap.list.MutableListMultimap;
import org.eclipse.collections.impl.bag.mutable.HashBag;
import org.eclipse.collections.impl.block.factory.Comparators;
import org.eclipse.collections.impl.block.factory.Procedures;
import org.eclipse.collections.impl.forkjoin.FJIterate;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.multimap.list.FastListMultimap;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AnagramBagTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    private static final int SIZE_THRESHOLD = 10;
    private final HashBag<String> ecWords = HashBag.newBag(FastList.newWithNValues(SIZE, () -> RandomStringUtils.randomAlphabetic(5).toUpperCase()));
    private final Multiset<String> guavaWords = HashMultiset.create(this.ecWords);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableListMultimap<Alphagram, String> groupBy = this.ecWords.groupBy(Alphagram::new, FastListMultimap.newMultimap());
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = ParallelIterate.groupBy(this.ecWords, Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        ParallelUnsortedBag<String> parallelUnsortedBag = this.ecWords.asParallel(this.executorService, BATCH_SIZE);
        UnsortedBagMultimap<Alphagram, String> groupBy = parallelUnsortedBag.groupBy(Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_forkjoin_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = FJIterate.groupBy(this.ecWords, Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        Map<Alphagram, List<String>> groupBy = this.guavaWords.stream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        Map<Alphagram, List<String>> groupBy = this.ecWords.stream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        Map<Alphagram, List<String>> groupBy = this.guavaWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        Map<Alphagram, List<String>> groupBy = this.ecWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    private static final class Alphagram
    {
        private final char[] key;

        private Alphagram(String string)
        {
            this.key = string.toCharArray();
            Arrays.sort(this.key);
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }
            Alphagram alphagram = (Alphagram) o;
            return Arrays.equals(this.key, alphagram.key);
        }

        @Override
        public int hashCode()
        {
            return Arrays.hashCode(this.key);
        }

        @Override
        public String toString()
        {
            return new String(this.key);
        }
    }
}
```

### Method 59

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import com.google.common.collect.HashMultiset;
import com.google.common.collect.Multiset;
import org.apache.commons.lang3.RandomStringUtils;
import org.eclipse.collections.api.RichIterable;
import org.eclipse.collections.api.bag.ParallelUnsortedBag;
import org.eclipse.collections.api.multimap.MutableMultimap;
import org.eclipse.collections.api.multimap.bag.UnsortedBagMultimap;
import org.eclipse.collections.api.multimap.list.MutableListMultimap;
import org.eclipse.collections.impl.bag.mutable.HashBag;
import org.eclipse.collections.impl.block.factory.Comparators;
import org.eclipse.collections.impl.block.factory.Procedures;
import org.eclipse.collections.impl.forkjoin.FJIterate;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.multimap.list.FastListMultimap;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class AnagramBagTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    private static final int SIZE_THRESHOLD = 10;
    private final HashBag<String> ecWords = HashBag.newBag(FastList.newWithNValues(SIZE, () -> RandomStringUtils.randomAlphabetic(5).toUpperCase()));
    private final Multiset<String> guavaWords = HashMultiset.create(this.ecWords);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public void serial_eager_ec()
    {
        MutableListMultimap<Alphagram, String> groupBy = this.ecWords.groupBy(Alphagram::new, FastListMultimap.newMultimap());
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = ParallelIterate.groupBy(this.ecWords, Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        ParallelUnsortedBag<String> parallelUnsortedBag = this.ecWords.asParallel(this.executorService, BATCH_SIZE);
        UnsortedBagMultimap<Alphagram, String> groupBy = parallelUnsortedBag.groupBy(Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void parallel_eager_forkjoin_ec()
    {
        MutableMultimap<Alphagram, String> groupBy = FJIterate.groupBy(this.ecWords, Alphagram::new);
        groupBy.multiValuesView()
                .select(iterable -> iterable.size() >= SIZE_THRESHOLD)
                .toSortedList(Comparators.byIntFunction(RichIterable::size))
                .asReversed()
                .collect(iterable -> iterable.size() + ": " + iterable)
                .forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        Map<Alphagram, List<String>> groupBy = this.guavaWords.stream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        Map<Alphagram, List<String>> groupBy = this.ecWords.stream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        Map<Alphagram, List<String>> groupBy = this.guavaWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        Map<Alphagram, List<String>> groupBy = this.ecWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
        groupBy.entrySet()
                .parallelStream()
                .map(Map.Entry::getValue)
                .filter(list -> list.size() >= SIZE_THRESHOLD)
                .sorted(Comparator.<List<String>>comparingInt(List::size).reversed())
                .map(list -> list.size() + ": " + list)
                .forEach(e -> Assert.assertFalse(e.isEmpty()));
    }

    private static final class Alphagram
    {
        private final char[] key;

        private Alphagram(String string)
        {
            this.key = string.toCharArray();
            Arrays.sort(this.key);
        }

        @Override
        public boolean equals(Object o)
        {
            if (this == o)
            {
                return true;
            }
            if (o == null || this.getClass() != o.getClass())
            {
                return false;
            }
            Alphagram alphagram = (Alphagram) o;
            return Arrays.equals(this.key, alphagram.key);
        }

        @Override
        public int hashCode()
        {
            return Arrays.hashCode(this.key);
        }

        @Override
        public String toString()
        {
            return new String(this.key);
        }
    }
}
```

### Method 60

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Collections;
import java.util.IntSummaryStatistics;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.primitive.IntList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class SummarizeIntTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;
    private static final Stream<Integer> INTEGERS = new Random().ints(0, 10_000).boxed();

    private final List<Integer> integersJDK = INTEGERS.limit(SIZE).collect(Collectors.toList());
    private final MutableList<Integer> integersEC = FastList.newListWith(this.integersJDK.toArray(new Integer[SIZE]));
    private final IntList intList = this.integersEC.collectInt(Integer::intValue);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        Collections.shuffle(this.integersJDK);
        Collections.shuffle(this.integersEC);
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public IntSummaryStatistics serial_lazy_mapToIntSum_jdk()
    {
        return this.integersJDK.stream().mapToInt(Integer::intValue).summaryStatistics();
    }

    @Benchmark
    public IntSummaryStatistics serial_lazy_mapToIntSum_streams_ec()
    {
        return this.integersEC.stream().mapToInt(Integer::intValue).summaryStatistics();
    }

    @Benchmark
    public IntSummaryStatistics parallel_lazy_mapToIntSum_jdk()
    {
        return this.integersJDK.parallelStream().mapToInt(Integer::intValue).summaryStatistics();
    }

    @Benchmark
    public IntSummaryStatistics parallel_lazy_mapToIntSum_streams_ec()
    {
        return this.integersEC.parallelStream().mapToInt(Integer::intValue).summaryStatistics();
    }

    @Benchmark
    public IntSummaryStatistics serial_eager_summarizeInt_ec()
    {
        return this.integersEC.summarizeInt(Integer::intValue);
    }

    @Benchmark
    public IntSummaryStatistics serial_eager_collectIntSummaryStatistics_ec()
    {
        return this.integersEC.collectInt(Integer::intValue).summaryStatistics();
    }

    @Benchmark
    public IntSummaryStatistics serial_lazy_collectIntSummaryStatistics_ec()
    {
        return this.integersEC.asLazy().collectInt(Integer::intValue).summaryStatistics();
    }

    @Benchmark
    public IntSummaryStatistics serial_lazy_summarizeInt_ec()
    {
        return this.integersEC.asLazy().summarizeInt(Integer::intValue);
    }

    @Benchmark
    public IntSummaryStatistics serial_eager_summaryStatistics_intList()
    {
        return this.intList.summaryStatistics();
    }
}
```

### Method 61

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Collections;
import java.util.IntSummaryStatistics;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.primitive.IntList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class SummarizeIntTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;
    private static final Stream<Integer> INTEGERS = new Random().ints(0, 10_000).boxed();

    private final List<Integer> integersJDK = INTEGERS.limit(SIZE).collect(Collectors.toList());
    private final MutableList<Integer> integersEC = FastList.newListWith(this.integersJDK.toArray(new Integer[SIZE]));
    private final IntList intList = this.integersEC.collectInt(Integer::intValue);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        Collections.shuffle(this.integersJDK);
        Collections.shuffle(this.integersEC);
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public IntSummaryStatistics serial_lazy_mapToIntSum_jdk()
    {
        return this.integersJDK.stream().mapToInt(Integer::intValue).summaryStatistics();
    }

    @Benchmark
    public IntSummaryStatistics serial_lazy_mapToIntSum_streams_ec()
    {
        return this.integersEC.stream().mapToInt(Integer::intValue).summaryStatistics();
    }

    @Benchmark
    public IntSummaryStatistics parallel_lazy_mapToIntSum_jdk()
    {
        return this.integersJDK.parallelStream().mapToInt(Integer::intValue).summaryStatistics();
    }

    @Benchmark
    public IntSummaryStatistics parallel_lazy_mapToIntSum_streams_ec()
    {
        return this.integersEC.parallelStream().mapToInt(Integer::intValue).summaryStatistics();
    }

    @Benchmark
    public IntSummaryStatistics serial_eager_summarizeInt_ec()
    {
        return this.integersEC.summarizeInt(Integer::intValue);
    }

    @Benchmark
    public IntSummaryStatistics serial_eager_collectIntSummaryStatistics_ec()
    {
        return this.integersEC.collectInt(Integer::intValue).summaryStatistics();
    }

    @Benchmark
    public IntSummaryStatistics serial_lazy_collectIntSummaryStatistics_ec()
    {
        return this.integersEC.asLazy().collectInt(Integer::intValue).summaryStatistics();
    }

    @Benchmark
    public IntSummaryStatistics serial_lazy_summarizeInt_ec()
    {
        return this.integersEC.asLazy().summarizeInt(Integer::intValue);
    }

    @Benchmark
    public IntSummaryStatistics serial_eager_summaryStatistics_intList()
    {
        return this.intList.summaryStatistics();
    }
}
```

### Method 62

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.primitive.IntList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class CollectorJoiningTest
{
    private static final int SIZE = 25;
    private static final int BATCH_SIZE = 5;
    private static final Stream<Integer> INTEGERS = new Random().ints(0, 10_000).boxed();

    private final List<Integer> integersJDK = INTEGERS.limit(SIZE).collect(Collectors.toList());
    private final MutableList<Integer> integersEC = FastList.newListWith(this.integersJDK.toArray(new Integer[SIZE]));
    private final IntList intList = this.integersEC.collectInt(Integer::intValue);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        Collections.shuffle(this.integersJDK);
        Collections.shuffle(this.integersEC);
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public String serial_lazy_mapToStringJoining_jdk()
    {
        return this.integersJDK.stream().map(Object::toString).collect(Collectors.joining(","));
    }

    @Benchmark
    public String serial_lazy_mapToStringJoining_ec()
    {
        return this.integersEC.stream().map(Object::toString).collect(Collectors.joining(","));
    }

    @Benchmark
    public String parallel_lazy_mapToStringJoining_jdk()
    {
        return this.integersJDK.parallelStream().map(Object::toString).collect(Collectors.joining(","));
    }

    @Benchmark
    public String parallel_lazy_mapToStringJoining_ec()
    {
        return this.integersEC.parallelStream().map(Object::toString).collect(Collectors.joining(","));
    }

    @Benchmark
    public String serial_eager_collectToStringJoining_ec()
    {
        return this.integersEC.collect(Object::toString).reduceInPlace(Collectors.joining(","));
    }

    @Benchmark
    public String serial_lazy_collectToStringJoining_ec()
    {
        return this.integersEC.asLazy().collect(Object::toString).reduceInPlace(Collectors.joining(","));
    }

    @Benchmark
    public String serial_eager_makeString_ec()
    {
        return this.integersEC.makeString(",");
    }

    @Benchmark
    public String parallel_lazy_makeString_ec()
    {
        return this.integersEC.asParallel(this.executorService, BATCH_SIZE).makeString(",");
    }

    @Benchmark
    public String serial_eager_primitiveMakeString_ec()
    {
        return this.intList.makeString(",");
    }
}
```

### Method 63

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.primitive.IntList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class CollectorJoiningTest
{
    private static final int SIZE = 25;
    private static final int BATCH_SIZE = 5;
    private static final Stream<Integer> INTEGERS = new Random().ints(0, 10_000).boxed();

    private final List<Integer> integersJDK = INTEGERS.limit(SIZE).collect(Collectors.toList());
    private final MutableList<Integer> integersEC = FastList.newListWith(this.integersJDK.toArray(new Integer[SIZE]));
    private final IntList intList = this.integersEC.collectInt(Integer::intValue);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        Collections.shuffle(this.integersJDK);
        Collections.shuffle(this.integersEC);
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public String serial_lazy_mapToStringJoining_jdk()
    {
        return this.integersJDK.stream().map(Object::toString).collect(Collectors.joining(","));
    }

    @Benchmark
    public String serial_lazy_mapToStringJoining_ec()
    {
        return this.integersEC.stream().map(Object::toString).collect(Collectors.joining(","));
    }

    @Benchmark
    public String parallel_lazy_mapToStringJoining_jdk()
    {
        return this.integersJDK.parallelStream().map(Object::toString).collect(Collectors.joining(","));
    }

    @Benchmark
    public String parallel_lazy_mapToStringJoining_ec()
    {
        return this.integersEC.parallelStream().map(Object::toString).collect(Collectors.joining(","));
    }

    @Benchmark
    public String serial_eager_collectToStringJoining_ec()
    {
        return this.integersEC.collect(Object::toString).reduceInPlace(Collectors.joining(","));
    }

    @Benchmark
    public String serial_lazy_collectToStringJoining_ec()
    {
        return this.integersEC.asLazy().collect(Object::toString).reduceInPlace(Collectors.joining(","));
    }

    @Benchmark
    public String serial_eager_makeString_ec()
    {
        return this.integersEC.makeString(",");
    }

    @Benchmark
    public String parallel_lazy_makeString_ec()
    {
        return this.integersEC.asParallel(this.executorService, BATCH_SIZE).makeString(",");
    }

    @Benchmark
    public String serial_eager_primitiveMakeString_ec()
    {
        return this.intList.makeString(",");
    }
}
```

### Method 64

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.primitive.IntList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class SumOfIntTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;
    private static final Stream<Integer> INTEGERS = new Random().ints(0, 10_000).boxed();

    private final List<Integer> integersJDK = INTEGERS.limit(SIZE).collect(Collectors.toList());
    private final MutableList<Integer> integersEC = FastList.newListWith(this.integersJDK.toArray(new Integer[SIZE]));
    private final IntList intList = this.integersEC.collectInt(Integer::intValue);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        Collections.shuffle(this.integersJDK);
        Collections.shuffle(this.integersEC);
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public int serial_lazy_mapToIntSum_jdk()
    {
        return this.integersJDK.stream().mapToInt(Integer::intValue).sum();
    }

    @Benchmark
    public int serial_lazy_mapToIntSum_streams_ec()
    {
        return this.integersEC.stream().mapToInt(Integer::intValue).sum();
    }

    @Benchmark
    public long serial_lazy_mapToLongSum_jdk()
    {
        return this.integersJDK.stream().mapToLong(Integer::longValue).sum();
    }

    @Benchmark
    public long serial_lazy_mapToLongSum_streams_ec()
    {
        return this.integersEC.stream().mapToLong(Integer::longValue).sum();
    }

    @Benchmark
    public int parallel_lazy_mapToIntSum_jdk()
    {
        return this.integersJDK.parallelStream().mapToInt(Integer::intValue).sum();
    }

    @Benchmark
    public int parallel_lazy_mapToIntSum_streams_ec()
    {
        return this.integersEC.parallelStream().mapToInt(Integer::intValue).sum();
    }

    @Benchmark
    public long parallel_lazy_mapToLongSum_jdk()
    {
        return this.integersJDK.parallelStream().mapToLong(Integer::longValue).sum();
    }

    @Benchmark
    public long parallel_lazy_mapToLongSum_streams_ec()
    {
        return this.integersEC.parallelStream().mapToLong(Integer::longValue).sum();
    }

    @Benchmark
    public long serial_eager_directSumOfInt_ec()
    {
        return this.integersEC.sumOfInt(Integer::intValue);
    }

    @Benchmark
    public long serial_eager_collectIntSum_ec()
    {
        return this.integersEC.collectInt(Integer::intValue).sum();
    }

    @Benchmark
    public long serial_lazy_collectIntSum_ec()
    {
        return this.integersEC.asLazy().collectInt(Integer::intValue).sum();
    }

    @Benchmark
    public long parallel_lazy_sumOfInt_ec()
    {
        return this.integersEC.asParallel(this.executorService, BATCH_SIZE).sumOfInt(Integer::intValue);
    }

    @Benchmark
    public long serial_lazy_sumOfInt_ec()
    {
        return this.integersEC.asLazy().sumOfInt(Integer::intValue);
    }

    @Benchmark
    public long serial_eager_sum_intList()
    {
        return this.intList.sum();
    }
}
```

### Method 65

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.primitive.IntList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class SumOfIntTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;
    private static final Stream<Integer> INTEGERS = new Random().ints(0, 10_000).boxed();

    private final List<Integer> integersJDK = INTEGERS.limit(SIZE).collect(Collectors.toList());
    private final MutableList<Integer> integersEC = FastList.newListWith(this.integersJDK.toArray(new Integer[SIZE]));
    private final IntList intList = this.integersEC.collectInt(Integer::intValue);

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
        Collections.shuffle(this.integersJDK);
        Collections.shuffle(this.integersEC);
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public int serial_lazy_mapToIntSum_jdk()
    {
        return this.integersJDK.stream().mapToInt(Integer::intValue).sum();
    }

    @Benchmark
    public int serial_lazy_mapToIntSum_streams_ec()
    {
        return this.integersEC.stream().mapToInt(Integer::intValue).sum();
    }

    @Benchmark
    public long serial_lazy_mapToLongSum_jdk()
    {
        return this.integersJDK.stream().mapToLong(Integer::longValue).sum();
    }

    @Benchmark
    public long serial_lazy_mapToLongSum_streams_ec()
    {
        return this.integersEC.stream().mapToLong(Integer::longValue).sum();
    }

    @Benchmark
    public int parallel_lazy_mapToIntSum_jdk()
    {
        return this.integersJDK.parallelStream().mapToInt(Integer::intValue).sum();
    }

    @Benchmark
    public int parallel_lazy_mapToIntSum_streams_ec()
    {
        return this.integersEC.parallelStream().mapToInt(Integer::intValue).sum();
    }

    @Benchmark
    public long parallel_lazy_mapToLongSum_jdk()
    {
        return this.integersJDK.parallelStream().mapToLong(Integer::longValue).sum();
    }

    @Benchmark
    public long parallel_lazy_mapToLongSum_streams_ec()
    {
        return this.integersEC.parallelStream().mapToLong(Integer::longValue).sum();
    }

    @Benchmark
    public long serial_eager_directSumOfInt_ec()
    {
        return this.integersEC.sumOfInt(Integer::intValue);
    }

    @Benchmark
    public long serial_eager_collectIntSum_ec()
    {
        return this.integersEC.collectInt(Integer::intValue).sum();
    }

    @Benchmark
    public long serial_lazy_collectIntSum_ec()
    {
        return this.integersEC.asLazy().collectInt(Integer::intValue).sum();
    }

    @Benchmark
    public long parallel_lazy_sumOfInt_ec()
    {
        return this.integersEC.asParallel(this.executorService, BATCH_SIZE).sumOfInt(Integer::intValue);
    }

    @Benchmark
    public long serial_lazy_sumOfInt_ec()
    {
        return this.integersEC.asLazy().sumOfInt(Integer::intValue);
    }

    @Benchmark
    public long serial_eager_sum_intList()
    {
        return this.intList.sum();
    }
}
```

### Method 66

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Comparator;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.impl.jmh.domain.Position;
import org.eclipse.collections.impl.jmh.domain.Positions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MaxByDoubleTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;

    // Comparator which autoboxes doubles: slow
    private static final Comparator<Position> MARKET_VALUE_COMPARATOR_METHODREF =
            Comparator.comparing(Position::getMarketValue);

    private static final Comparator<Position> MARKET_VALUE_COMPARATOR_LAMBDA =
            (Position p1, Position p2) -> Double.compare(p1.getMarketValue(), p2.getMarketValue());

    private final Positions positions = new Positions(SIZE).shuffle();

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public Position maxByMarketValue_serial_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().max(MARKET_VALUE_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position maxByMarketValue_serial_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().max(MARKET_VALUE_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position maxByMarketValue_serial_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.maxBy(MARKET_VALUE_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position maxByMarketValue_serial_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.maxBy(MARKET_VALUE_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position maxByMarketValue_parallel_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().max(
                MARKET_VALUE_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position maxByMarketValue_parallel_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().max(
                MARKET_VALUE_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position maxByMarketValue_parallel_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.maxBy(MARKET_VALUE_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position maxByMarketValue_parallel_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.maxBy(MARKET_VALUE_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position maxByMarketValue_serial_eager_ec()
    {
        return this.positions.getEcPositions().maxBy(Position::getMarketValue);
    }

    @Benchmark
    public Position maxByMarketValue_serial_lazy_ec()
    {
        return this.positions.getEcPositions().asLazy().maxBy(Position::getMarketValue);
    }

    @Benchmark
    public Position maxByMarketValue_parallel_lazy_ec()
    {
        return this.positions.getEcPositions().asParallel(this.executorService, BATCH_SIZE).maxBy(Position::getMarketValue);
    }
}
```

### Method 67

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Comparator;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.impl.jmh.domain.Position;
import org.eclipse.collections.impl.jmh.domain.Positions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MaxByDoubleTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;

    // Comparator which autoboxes doubles: slow
    private static final Comparator<Position> MARKET_VALUE_COMPARATOR_METHODREF =
            Comparator.comparing(Position::getMarketValue);

    private static final Comparator<Position> MARKET_VALUE_COMPARATOR_LAMBDA =
            (Position p1, Position p2) -> Double.compare(p1.getMarketValue(), p2.getMarketValue());

    private final Positions positions = new Positions(SIZE).shuffle();

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public Position maxByMarketValue_serial_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().max(MARKET_VALUE_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position maxByMarketValue_serial_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().max(MARKET_VALUE_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position maxByMarketValue_serial_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.maxBy(MARKET_VALUE_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position maxByMarketValue_serial_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.maxBy(MARKET_VALUE_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position maxByMarketValue_parallel_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().max(
                MARKET_VALUE_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position maxByMarketValue_parallel_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().max(
                MARKET_VALUE_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position maxByMarketValue_parallel_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.maxBy(MARKET_VALUE_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position maxByMarketValue_parallel_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.maxBy(MARKET_VALUE_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position maxByMarketValue_serial_eager_ec()
    {
        return this.positions.getEcPositions().maxBy(Position::getMarketValue);
    }

    @Benchmark
    public Position maxByMarketValue_serial_lazy_ec()
    {
        return this.positions.getEcPositions().asLazy().maxBy(Position::getMarketValue);
    }

    @Benchmark
    public Position maxByMarketValue_parallel_lazy_ec()
    {
        return this.positions.getEcPositions().asParallel(this.executorService, BATCH_SIZE).maxBy(Position::getMarketValue);
    }
}
```

### Method 68

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Comparator;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.impl.jmh.domain.Position;
import org.eclipse.collections.impl.jmh.domain.Positions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MaxByIntTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;

    // Comparator which autoboxes ints -> slow
    private static final Comparator<Position> QUANTITY_COMPARATOR_METHODREF =
            Comparator.comparing(Position::getQuantity);

    private static final Comparator<Position> QUANTITY_COMPARATOR_LAMBDA =
            (Position p1, Position p2) -> Integer.compare(p1.getQuantity(), p2.getQuantity());

    private final Positions positions = new Positions(SIZE).shuffle();

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public Position maxByQuantity_serial_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().max(QUANTITY_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position maxByQuantity_serial_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().max(QUANTITY_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position maxByQuantity_serial_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.maxBy(QUANTITY_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position maxByQuantity_serial_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.maxBy(QUANTITY_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position maxByQuantity_parallel_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().max(
                QUANTITY_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position maxByQuantity_parallel_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().max(
                QUANTITY_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position maxByQuantity_parallel_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.maxBy(QUANTITY_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position maxByQuantity_parallel_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.maxBy(QUANTITY_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position maxByQuantity_serial_eager_ec()
    {
        return this.positions.getEcPositions().maxBy(Position::getQuantity);
    }

    @Benchmark
    public Position maxByQuantity_serial_lazy_ec()
    {
        return this.positions.getEcPositions().asLazy().maxBy(Position::getQuantity);
    }

    @Benchmark
    public Position maxByQuantity_parallel_lazy_ec()
    {
        return this.positions.getEcPositions().asParallel(this.executorService, BATCH_SIZE).maxBy(
                Position::getQuantity);
    }
}
```

### Method 69

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Comparator;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.impl.jmh.domain.Position;
import org.eclipse.collections.impl.jmh.domain.Positions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MaxByIntTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;

    // Comparator which autoboxes ints -> slow
    private static final Comparator<Position> QUANTITY_COMPARATOR_METHODREF =
            Comparator.comparing(Position::getQuantity);

    private static final Comparator<Position> QUANTITY_COMPARATOR_LAMBDA =
            (Position p1, Position p2) -> Integer.compare(p1.getQuantity(), p2.getQuantity());

    private final Positions positions = new Positions(SIZE).shuffle();

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public Position maxByQuantity_serial_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().max(QUANTITY_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position maxByQuantity_serial_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().max(QUANTITY_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position maxByQuantity_serial_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.maxBy(QUANTITY_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position maxByQuantity_serial_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.maxBy(QUANTITY_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position maxByQuantity_parallel_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().max(
                QUANTITY_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position maxByQuantity_parallel_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().max(
                QUANTITY_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position maxByQuantity_parallel_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.maxBy(QUANTITY_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position maxByQuantity_parallel_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.maxBy(QUANTITY_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position maxByQuantity_serial_eager_ec()
    {
        return this.positions.getEcPositions().maxBy(Position::getQuantity);
    }

    @Benchmark
    public Position maxByQuantity_serial_lazy_ec()
    {
        return this.positions.getEcPositions().asLazy().maxBy(Position::getQuantity);
    }

    @Benchmark
    public Position maxByQuantity_parallel_lazy_ec()
    {
        return this.positions.getEcPositions().asParallel(this.executorService, BATCH_SIZE).maxBy(
                Position::getQuantity);
    }
}
```

### Method 70

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Comparator;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.impl.jmh.domain.Position;
import org.eclipse.collections.impl.jmh.domain.Positions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MinByDoubleTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;

    // Comparator which autoboxes doubles: slow
    private static final Comparator<Position> MARKET_VALUE_COMPARATOR_METHODREF =
            Comparator.comparing(Position::getMarketValue);

    private static final Comparator<Position> MARKET_VALUE_COMPARATOR_LAMBDA =
            (Position p1, Position p2) -> Double.compare(p1.getMarketValue(), p2.getMarketValue());

    private final Positions positions = new Positions(SIZE).shuffle();

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public Position minByMarketValue_serial_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().min(MARKET_VALUE_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position minByMarketValue_serial_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().min(MARKET_VALUE_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position minByMarketValue_serial_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.minBy(MARKET_VALUE_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position minByMarketValue_serial_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.minBy(MARKET_VALUE_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position minByMarketValue_parallel_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().min(
                MARKET_VALUE_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position minByMarketValue_parallel_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().min(
                MARKET_VALUE_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position minByMarketValue_parallel_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.minBy(MARKET_VALUE_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position minByMarketValue_parallel_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.minBy(MARKET_VALUE_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position minByMarketValue_serial_eager_ec()
    {
        return this.positions.getEcPositions().minBy(Position::getMarketValue);
    }

    @Benchmark
    public Position minByMarketValue_serial_lazy_ec()
    {
        return this.positions.getEcPositions().asLazy().minBy(Position::getMarketValue);
    }

    @Benchmark
    public Position minByMarketValue_parallel_lazy_ec()
    {
        return this.positions.getEcPositions().asParallel(this.executorService, BATCH_SIZE).minBy(
                Position::getMarketValue);
    }
}
```

### Method 71

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Comparator;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.impl.jmh.domain.Position;
import org.eclipse.collections.impl.jmh.domain.Positions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MinByDoubleTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;

    // Comparator which autoboxes doubles: slow
    private static final Comparator<Position> MARKET_VALUE_COMPARATOR_METHODREF =
            Comparator.comparing(Position::getMarketValue);

    private static final Comparator<Position> MARKET_VALUE_COMPARATOR_LAMBDA =
            (Position p1, Position p2) -> Double.compare(p1.getMarketValue(), p2.getMarketValue());

    private final Positions positions = new Positions(SIZE).shuffle();

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public Position minByMarketValue_serial_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().min(MARKET_VALUE_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position minByMarketValue_serial_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().min(MARKET_VALUE_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position minByMarketValue_serial_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.minBy(MARKET_VALUE_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position minByMarketValue_serial_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.minBy(MARKET_VALUE_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position minByMarketValue_parallel_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().min(
                MARKET_VALUE_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position minByMarketValue_parallel_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().min(
                MARKET_VALUE_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position minByMarketValue_parallel_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.minBy(MARKET_VALUE_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position minByMarketValue_parallel_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.minBy(MARKET_VALUE_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position minByMarketValue_serial_eager_ec()
    {
        return this.positions.getEcPositions().minBy(Position::getMarketValue);
    }

    @Benchmark
    public Position minByMarketValue_serial_lazy_ec()
    {
        return this.positions.getEcPositions().asLazy().minBy(Position::getMarketValue);
    }

    @Benchmark
    public Position minByMarketValue_parallel_lazy_ec()
    {
        return this.positions.getEcPositions().asParallel(this.executorService, BATCH_SIZE).minBy(
                Position::getMarketValue);
    }
}
```

### Method 72

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Comparator;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.impl.jmh.domain.Position;
import org.eclipse.collections.impl.jmh.domain.Positions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MinByIntTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;

    // Comparator which autoboxes ints -> slow
    private static final Comparator<Position> QUANTITY_COMPARATOR_METHODREF =
            Comparator.comparing(Position::getQuantity);

    private static final Comparator<Position> QUANTITY_COMPARATOR_LAMBDA =
            (Position p1, Position p2) -> Integer.compare(p1.getQuantity(), p2.getQuantity());

    private final Positions positions = new Positions(SIZE).shuffle();

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public Position minByQuantity_serial_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().min(QUANTITY_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position minByQuantity_serial_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().min(QUANTITY_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position minByQuantity_serial_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.minBy(QUANTITY_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position minByQuantity_serial_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.minBy(QUANTITY_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position minByQuantity_parallel_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().min(
                QUANTITY_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position minByQuantity_parallel_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().min(
                QUANTITY_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position minByQuantity_parallel_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.minBy(QUANTITY_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position minByQuantity_parallel_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.minBy(QUANTITY_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position minByQuantity_serial_eager_ec()
    {
        return this.positions.getEcPositions().minBy(Position::getQuantity);
    }

    @Benchmark
    public Position minByQuantity_serial_lazy_ec()
    {
        return this.positions.getEcPositions().asLazy().minBy(Position::getQuantity);
    }

    @Benchmark
    public Position minByQuantity_parallel_lazy_ec()
    {
        return this.positions.getEcPositions().asParallel(this.executorService, BATCH_SIZE).minBy(
                Position::getQuantity);
    }
}
```

### Method 73

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Comparator;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import org.eclipse.collections.impl.jmh.domain.Position;
import org.eclipse.collections.impl.jmh.domain.Positions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class MinByIntTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;

    // Comparator which autoboxes ints -> slow
    private static final Comparator<Position> QUANTITY_COMPARATOR_METHODREF =
            Comparator.comparing(Position::getQuantity);

    private static final Comparator<Position> QUANTITY_COMPARATOR_LAMBDA =
            (Position p1, Position p2) -> Integer.compare(p1.getQuantity(), p2.getQuantity());

    private final Positions positions = new Positions(SIZE).shuffle();

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public Position minByQuantity_serial_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().min(QUANTITY_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position minByQuantity_serial_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().min(QUANTITY_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position minByQuantity_serial_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.minBy(QUANTITY_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position minByQuantity_serial_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().stream().collect(
                Collectors.minBy(QUANTITY_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position minByQuantity_parallel_lazy_direct_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().min(
                QUANTITY_COMPARATOR_METHODREF).get();
    }

    @Benchmark
    public Position minByQuantity_parallel_lazy_direct_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().min(
                QUANTITY_COMPARATOR_LAMBDA).get();
    }

    @Benchmark
    public Position minByQuantity_parallel_lazy_collect_methodref_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.minBy(QUANTITY_COMPARATOR_METHODREF)).get();
    }

    @Benchmark
    public Position minByQuantity_parallel_lazy_collect_lambda_jdk()
    {
        return this.positions.getJdkPositions().parallelStream().collect(
                Collectors.minBy(QUANTITY_COMPARATOR_LAMBDA)).get();
    }

    @Benchmark
    public Position minByQuantity_serial_eager_ec()
    {
        return this.positions.getEcPositions().minBy(Position::getQuantity);
    }

    @Benchmark
    public Position minByQuantity_serial_lazy_ec()
    {
        return this.positions.getEcPositions().asLazy().minBy(Position::getQuantity);
    }

    @Benchmark
    public Position minByQuantity_parallel_lazy_ec()
    {
        return this.positions.getEcPositions().asParallel(this.executorService, BATCH_SIZE).minBy(
                Position::getQuantity);
    }
}
```

### Method 74

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.IntIntMap;
import com.koloboke.collect.map.hash.HashIntIntMaps;
import org.eclipse.collections.api.block.function.primitive.IntToObjectFunction;
import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.primitive.MutableIntList;
import org.eclipse.collections.api.map.primitive.MutableIntIntMap;
import org.eclipse.collections.api.set.primitive.MutableIntSet;
import org.eclipse.collections.impl.SpreadFunctions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.list.mutable.primitive.IntArrayList;
import org.eclipse.collections.impl.map.mutable.primitive.IntIntHashMap;
import org.eclipse.collections.impl.set.mutable.primitive.IntHashSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class IntIntMapSmallStressTest
{
    private static final int LOOP_COUNT = 100;
    private static final int KEY_COUNT = 500;
    private static final int MAP_SIZE = 1_000;

    @Param({"true", "false"})
    public boolean fullyRandom;
    private IntIntMap intIntKoloboke;
    private MutableIntIntMap intIntEc;
    private Map<Integer, Integer> integerIntegerJdk;
    private int[] ecIntKeysForMap;
    private int[] kolobokeIntKeysForMap;
    private Integer[] jdkIntKeysForMap;

    private int jdkIndex(int key)
    {
        return this.mask(key ^ (key >>> 16));
    }

    private int kolobokeIndex(int key)
    {
        int h = key * 0x9e3779b9;
        return this.mask(h ^ h >> 16);
    }

    private int ecIndex(int element)
    {
        return this.mask(element);
    }

    private int ecIndexTwo(int element)
    {
        return this.mask(SpreadFunctions.intSpreadTwo(element));
    }

    private int mask(int spread)
    {
        return spread & ((1 << 11) - 1);
    }

    @Setup
    public void setUp()
    {
        this.intIntKoloboke = HashIntIntMaps.newMutableMap(MAP_SIZE);
        this.intIntEc = new IntIntHashMap(MAP_SIZE);
        this.integerIntegerJdk = new HashMap<>(MAP_SIZE);

        Random random = new Random(0x123456789ABCDL);

        int[] randomNumbersForMap = this.getRandomKeys(random).toArray();

        int number = 23;
        int lower = Integer.MIN_VALUE;
        int upper = Integer.MAX_VALUE;
        this.kolobokeIntKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getKolobokeArray(number, lower, upper, random);
        this.ecIntKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getECArray(number, lower, upper, random);
        this.jdkIntKeysForMap = this.fullyRandom
                ? IntIntMapSmallStressTest.boxIntArray(randomNumbersForMap)
                : this.getJDKArray(lower, upper, random);

        for (int i = 0; i < KEY_COUNT; i++)
        {
            this.intIntKoloboke.put(this.kolobokeIntKeysForMap[i], 5);
            this.intIntEc.put(this.ecIntKeysForMap[i], 5);
            this.integerIntegerJdk.put(this.jdkIntKeysForMap[i], 5);
        }

        this.shuffle(this.ecIntKeysForMap, random);
        this.shuffle(this.kolobokeIntKeysForMap, random);
        this.shuffle(this.jdkIntKeysForMap, random);
    }

    protected int[] getECArray(int number, int lower, int upper, Random random)
    {
        int[] ecCollisions = this.getECSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(ecCollisions, random);
        return ecCollisions;
    }

    protected MutableIntList getECSequenceCollisions(int number, int lower, int upper)
    {
        MutableIntList ecCollidingNumbers = new IntArrayList();
        for (int i = lower; i < upper && ecCollidingNumbers.size() < KEY_COUNT; i++)
        {
            if (this.ecIndex(i) - this.ecIndex(number) >= 0
                    && this.ecIndex(i) - this.ecIndex(number) < 10
                    && (this.ecIndexTwo(i) - this.ecIndexTwo(number) >= 0)
                    && (this.ecIndexTwo(i) - this.ecIndexTwo(number) < 10))
            {
                ecCollidingNumbers.add(i);
            }
        }
        return ecCollidingNumbers;
    }

    protected Integer[] getJDKArray(int lower, int upper, Random random)
    {
        MutableList<Integer> collisions = this.getJDKSequenceCollisions(lower, upper);
        Integer[] jdkCollision = collisions.toArray(new Integer[collisions.size()]);
        this.shuffle(jdkCollision, random);
        return jdkCollision;
    }

    protected MutableList<Integer> getJDKSequenceCollisions(int lower, int upper)
    {
        MutableList<Integer> jdkCollidingNumbers = FastList.newList();
        int slots = 1; // slots = KEY_COUNT / (1 << 32) / (1 << MAP_SIZE) + 1;
        MutableIntSet indices = new IntHashSet();
        for (int i = lower; i < upper && jdkCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.jdkIndex(i);
            if (indices.size() < slots)
            {
                indices.add(index);
                jdkCollidingNumbers.add(i);
            }
            else if (indices.contains(index))
            {
                jdkCollidingNumbers.add(i);
            }
        }
        return jdkCollidingNumbers;
    }

    protected int[] getKolobokeArray(int number, int lower, int upper, Random random)
    {
        int[] kolobokeCollisions = this.getKolobokeSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(kolobokeCollisions, random);
        return kolobokeCollisions;
    }

    protected MutableIntList getKolobokeSequenceCollisions(int number, int lower, int upper)
    {
        MutableIntList kolobokeCollidingNumbers = new IntArrayList();
        for (int i = lower; i < upper && kolobokeCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.kolobokeIndex(i);
            if (index >= number && index <= number + 100)
            {
                kolobokeCollidingNumbers.add(i);
            }
        }
        return kolobokeCollidingNumbers;
    }

    protected MutableIntSet getRandomKeys(Random random)
    {
        MutableIntSet set = new IntHashSet(KEY_COUNT);
        while (set.size() < KEY_COUNT)
        {
            set.add(random.nextInt());
        }

        return set;
    }

    @Benchmark
    public void jdkGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.integerIntegerJdk.get(this.jdkIntKeysForMap[i]) == null)
                {
                    throw new AssertionError(this.jdkIntKeysForMap[i] + " not in map");
                }
            }
            if (this.integerIntegerJdk.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.integerIntegerJdk.size());
            }
        }
    }

    @Benchmark
    public void kolobokeGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.intIntKoloboke.get(this.kolobokeIntKeysForMap[i]) == this.intIntKoloboke.defaultValue())
                {
                    throw new AssertionError(this.kolobokeIntKeysForMap[i] + " not in map");
                }
            }
            if (this.intIntKoloboke.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.intIntKoloboke.size());
            }
        }
    }

    @Benchmark
    public void ecGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.intIntEc.get(this.ecIntKeysForMap[i]) == 0)
                {
                    throw new AssertionError(this.ecIntKeysForMap[i] + " not in map");
                }
            }
            if (this.intIntEc.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.intIntEc.size());
            }
        }
    }

    @Benchmark
    public void jdkPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.jdkIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokePut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.kolobokeIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableIntIntMap newMap = new IntIntHashMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.ecIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableIntIntMap newMap = new IntIntHashMap(this.intIntEc);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.ecIntKeysForMap[i]);
            }
            if (newMap.notEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void jdkRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.jdkIntKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokeRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.kolobokeIntKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    public void shuffle(int[] intArray, Random rnd)
    {
        for (int i = intArray.length; i > 1; i--)
        {
            IntIntMapSmallStressTest.swap(intArray, i - 1, rnd.nextInt(i));
        }
    }

    public void shuffle(Integer[] integerArray, Random rnd)
    {
        for (int i = integerArray.length; i > 1; i--)
        {
            IntIntMapSmallStressTest.swap(integerArray, i - 1, rnd.nextInt(i));
        }
    }

    private static void swap(int[] arr, int i, int j)
    {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private static void swap(Integer[] arr, int i, int j)
    {
        Integer tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private static Integer[] boxIntArray(int[] arr)
    {
        MutableList<Integer> list = new IntArrayList(arr).collect((IntToObjectFunction<Integer>) Integer::valueOf);
        return list.toArray(new Integer[arr.length]);
    }
}
```

### Method 75

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.IntIntMap;
import com.koloboke.collect.map.hash.HashIntIntMaps;
import org.eclipse.collections.api.block.function.primitive.IntToObjectFunction;
import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.primitive.MutableIntList;
import org.eclipse.collections.api.map.primitive.MutableIntIntMap;
import org.eclipse.collections.api.set.primitive.MutableIntSet;
import org.eclipse.collections.impl.SpreadFunctions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.list.mutable.primitive.IntArrayList;
import org.eclipse.collections.impl.map.mutable.primitive.IntIntHashMap;
import org.eclipse.collections.impl.set.mutable.primitive.IntHashSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class IntIntMapSmallStressTest
{
    private static final int LOOP_COUNT = 100;
    private static final int KEY_COUNT = 500;
    private static final int MAP_SIZE = 1_000;

    @Param({"true", "false"})
    public boolean fullyRandom;
    private IntIntMap intIntKoloboke;
    private MutableIntIntMap intIntEc;
    private Map<Integer, Integer> integerIntegerJdk;
    private int[] ecIntKeysForMap;
    private int[] kolobokeIntKeysForMap;
    private Integer[] jdkIntKeysForMap;

    private int jdkIndex(int key)
    {
        return this.mask(key ^ (key >>> 16));
    }

    private int kolobokeIndex(int key)
    {
        int h = key * 0x9e3779b9;
        return this.mask(h ^ h >> 16);
    }

    private int ecIndex(int element)
    {
        return this.mask(element);
    }

    private int ecIndexTwo(int element)
    {
        return this.mask(SpreadFunctions.intSpreadTwo(element));
    }

    private int mask(int spread)
    {
        return spread & ((1 << 11) - 1);
    }

    @Setup
    public void setUp()
    {
        this.intIntKoloboke = HashIntIntMaps.newMutableMap(MAP_SIZE);
        this.intIntEc = new IntIntHashMap(MAP_SIZE);
        this.integerIntegerJdk = new HashMap<>(MAP_SIZE);

        Random random = new Random(0x123456789ABCDL);

        int[] randomNumbersForMap = this.getRandomKeys(random).toArray();

        int number = 23;
        int lower = Integer.MIN_VALUE;
        int upper = Integer.MAX_VALUE;
        this.kolobokeIntKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getKolobokeArray(number, lower, upper, random);
        this.ecIntKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getECArray(number, lower, upper, random);
        this.jdkIntKeysForMap = this.fullyRandom
                ? IntIntMapSmallStressTest.boxIntArray(randomNumbersForMap)
                : this.getJDKArray(lower, upper, random);

        for (int i = 0; i < KEY_COUNT; i++)
        {
            this.intIntKoloboke.put(this.kolobokeIntKeysForMap[i], 5);
            this.intIntEc.put(this.ecIntKeysForMap[i], 5);
            this.integerIntegerJdk.put(this.jdkIntKeysForMap[i], 5);
        }

        this.shuffle(this.ecIntKeysForMap, random);
        this.shuffle(this.kolobokeIntKeysForMap, random);
        this.shuffle(this.jdkIntKeysForMap, random);
    }

    protected int[] getECArray(int number, int lower, int upper, Random random)
    {
        int[] ecCollisions = this.getECSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(ecCollisions, random);
        return ecCollisions;
    }

    protected MutableIntList getECSequenceCollisions(int number, int lower, int upper)
    {
        MutableIntList ecCollidingNumbers = new IntArrayList();
        for (int i = lower; i < upper && ecCollidingNumbers.size() < KEY_COUNT; i++)
        {
            if (this.ecIndex(i) - this.ecIndex(number) >= 0
                    && this.ecIndex(i) - this.ecIndex(number) < 10
                    && (this.ecIndexTwo(i) - this.ecIndexTwo(number) >= 0)
                    && (this.ecIndexTwo(i) - this.ecIndexTwo(number) < 10))
            {
                ecCollidingNumbers.add(i);
            }
        }
        return ecCollidingNumbers;
    }

    protected Integer[] getJDKArray(int lower, int upper, Random random)
    {
        MutableList<Integer> collisions = this.getJDKSequenceCollisions(lower, upper);
        Integer[] jdkCollision = collisions.toArray(new Integer[collisions.size()]);
        this.shuffle(jdkCollision, random);
        return jdkCollision;
    }

    protected MutableList<Integer> getJDKSequenceCollisions(int lower, int upper)
    {
        MutableList<Integer> jdkCollidingNumbers = FastList.newList();
        int slots = 1; // slots = KEY_COUNT / (1 << 32) / (1 << MAP_SIZE) + 1;
        MutableIntSet indices = new IntHashSet();
        for (int i = lower; i < upper && jdkCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.jdkIndex(i);
            if (indices.size() < slots)
            {
                indices.add(index);
                jdkCollidingNumbers.add(i);
            }
            else if (indices.contains(index))
            {
                jdkCollidingNumbers.add(i);
            }
        }
        return jdkCollidingNumbers;
    }

    protected int[] getKolobokeArray(int number, int lower, int upper, Random random)
    {
        int[] kolobokeCollisions = this.getKolobokeSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(kolobokeCollisions, random);
        return kolobokeCollisions;
    }

    protected MutableIntList getKolobokeSequenceCollisions(int number, int lower, int upper)
    {
        MutableIntList kolobokeCollidingNumbers = new IntArrayList();
        for (int i = lower; i < upper && kolobokeCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.kolobokeIndex(i);
            if (index >= number && index <= number + 100)
            {
                kolobokeCollidingNumbers.add(i);
            }
        }
        return kolobokeCollidingNumbers;
    }

    protected MutableIntSet getRandomKeys(Random random)
    {
        MutableIntSet set = new IntHashSet(KEY_COUNT);
        while (set.size() < KEY_COUNT)
        {
            set.add(random.nextInt());
        }

        return set;
    }

    @Benchmark
    public void jdkGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.integerIntegerJdk.get(this.jdkIntKeysForMap[i]) == null)
                {
                    throw new AssertionError(this.jdkIntKeysForMap[i] + " not in map");
                }
            }
            if (this.integerIntegerJdk.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.integerIntegerJdk.size());
            }
        }
    }

    @Benchmark
    public void kolobokeGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.intIntKoloboke.get(this.kolobokeIntKeysForMap[i]) == this.intIntKoloboke.defaultValue())
                {
                    throw new AssertionError(this.kolobokeIntKeysForMap[i] + " not in map");
                }
            }
            if (this.intIntKoloboke.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.intIntKoloboke.size());
            }
        }
    }

    @Benchmark
    public void ecGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.intIntEc.get(this.ecIntKeysForMap[i]) == 0)
                {
                    throw new AssertionError(this.ecIntKeysForMap[i] + " not in map");
                }
            }
            if (this.intIntEc.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.intIntEc.size());
            }
        }
    }

    @Benchmark
    public void jdkPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.jdkIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokePut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.kolobokeIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableIntIntMap newMap = new IntIntHashMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.ecIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableIntIntMap newMap = new IntIntHashMap(this.intIntEc);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.ecIntKeysForMap[i]);
            }
            if (newMap.notEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void jdkRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.jdkIntKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokeRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.kolobokeIntKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    public void shuffle(int[] intArray, Random rnd)
    {
        for (int i = intArray.length; i > 1; i--)
        {
            IntIntMapSmallStressTest.swap(intArray, i - 1, rnd.nextInt(i));
        }
    }

    public void shuffle(Integer[] integerArray, Random rnd)
    {
        for (int i = integerArray.length; i > 1; i--)
        {
            IntIntMapSmallStressTest.swap(integerArray, i - 1, rnd.nextInt(i));
        }
    }

    private static void swap(int[] arr, int i, int j)
    {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private static void swap(Integer[] arr, int i, int j)
    {
        Integer tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private static Integer[] boxIntArray(int[] arr)
    {
        MutableList<Integer> list = new IntArrayList(arr).collect((IntToObjectFunction<Integer>) Integer::valueOf);
        return list.toArray(new Integer[arr.length]);
    }
}
```

### Method 76

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.IntIntMap;
import com.koloboke.collect.map.hash.HashIntIntMaps;
import org.eclipse.collections.api.block.function.primitive.IntToObjectFunction;
import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.primitive.MutableIntList;
import org.eclipse.collections.api.map.primitive.MutableIntIntMap;
import org.eclipse.collections.api.set.primitive.MutableIntSet;
import org.eclipse.collections.impl.SpreadFunctions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.list.mutable.primitive.IntArrayList;
import org.eclipse.collections.impl.map.mutable.primitive.IntIntHashMap;
import org.eclipse.collections.impl.set.mutable.primitive.IntHashSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class IntIntMapSmallStressTest
{
    private static final int LOOP_COUNT = 100;
    private static final int KEY_COUNT = 500;
    private static final int MAP_SIZE = 1_000;

    @Param({"true", "false"})
    public boolean fullyRandom;
    private IntIntMap intIntKoloboke;
    private MutableIntIntMap intIntEc;
    private Map<Integer, Integer> integerIntegerJdk;
    private int[] ecIntKeysForMap;
    private int[] kolobokeIntKeysForMap;
    private Integer[] jdkIntKeysForMap;

    private int jdkIndex(int key)
    {
        return this.mask(key ^ (key >>> 16));
    }

    private int kolobokeIndex(int key)
    {
        int h = key * 0x9e3779b9;
        return this.mask(h ^ h >> 16);
    }

    private int ecIndex(int element)
    {
        return this.mask(element);
    }

    private int ecIndexTwo(int element)
    {
        return this.mask(SpreadFunctions.intSpreadTwo(element));
    }

    private int mask(int spread)
    {
        return spread & ((1 << 11) - 1);
    }

    @Setup
    public void setUp()
    {
        this.intIntKoloboke = HashIntIntMaps.newMutableMap(MAP_SIZE);
        this.intIntEc = new IntIntHashMap(MAP_SIZE);
        this.integerIntegerJdk = new HashMap<>(MAP_SIZE);

        Random random = new Random(0x123456789ABCDL);

        int[] randomNumbersForMap = this.getRandomKeys(random).toArray();

        int number = 23;
        int lower = Integer.MIN_VALUE;
        int upper = Integer.MAX_VALUE;
        this.kolobokeIntKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getKolobokeArray(number, lower, upper, random);
        this.ecIntKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getECArray(number, lower, upper, random);
        this.jdkIntKeysForMap = this.fullyRandom
                ? IntIntMapSmallStressTest.boxIntArray(randomNumbersForMap)
                : this.getJDKArray(lower, upper, random);

        for (int i = 0; i < KEY_COUNT; i++)
        {
            this.intIntKoloboke.put(this.kolobokeIntKeysForMap[i], 5);
            this.intIntEc.put(this.ecIntKeysForMap[i], 5);
            this.integerIntegerJdk.put(this.jdkIntKeysForMap[i], 5);
        }

        this.shuffle(this.ecIntKeysForMap, random);
        this.shuffle(this.kolobokeIntKeysForMap, random);
        this.shuffle(this.jdkIntKeysForMap, random);
    }

    protected int[] getECArray(int number, int lower, int upper, Random random)
    {
        int[] ecCollisions = this.getECSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(ecCollisions, random);
        return ecCollisions;
    }

    protected MutableIntList getECSequenceCollisions(int number, int lower, int upper)
    {
        MutableIntList ecCollidingNumbers = new IntArrayList();
        for (int i = lower; i < upper && ecCollidingNumbers.size() < KEY_COUNT; i++)
        {
            if (this.ecIndex(i) - this.ecIndex(number) >= 0
                    && this.ecIndex(i) - this.ecIndex(number) < 10
                    && (this.ecIndexTwo(i) - this.ecIndexTwo(number) >= 0)
                    && (this.ecIndexTwo(i) - this.ecIndexTwo(number) < 10))
            {
                ecCollidingNumbers.add(i);
            }
        }
        return ecCollidingNumbers;
    }

    protected Integer[] getJDKArray(int lower, int upper, Random random)
    {
        MutableList<Integer> collisions = this.getJDKSequenceCollisions(lower, upper);
        Integer[] jdkCollision = collisions.toArray(new Integer[collisions.size()]);
        this.shuffle(jdkCollision, random);
        return jdkCollision;
    }

    protected MutableList<Integer> getJDKSequenceCollisions(int lower, int upper)
    {
        MutableList<Integer> jdkCollidingNumbers = FastList.newList();
        int slots = 1; // slots = KEY_COUNT / (1 << 32) / (1 << MAP_SIZE) + 1;
        MutableIntSet indices = new IntHashSet();
        for (int i = lower; i < upper && jdkCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.jdkIndex(i);
            if (indices.size() < slots)
            {
                indices.add(index);
                jdkCollidingNumbers.add(i);
            }
            else if (indices.contains(index))
            {
                jdkCollidingNumbers.add(i);
            }
        }
        return jdkCollidingNumbers;
    }

    protected int[] getKolobokeArray(int number, int lower, int upper, Random random)
    {
        int[] kolobokeCollisions = this.getKolobokeSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(kolobokeCollisions, random);
        return kolobokeCollisions;
    }

    protected MutableIntList getKolobokeSequenceCollisions(int number, int lower, int upper)
    {
        MutableIntList kolobokeCollidingNumbers = new IntArrayList();
        for (int i = lower; i < upper && kolobokeCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.kolobokeIndex(i);
            if (index >= number && index <= number + 100)
            {
                kolobokeCollidingNumbers.add(i);
            }
        }
        return kolobokeCollidingNumbers;
    }

    protected MutableIntSet getRandomKeys(Random random)
    {
        MutableIntSet set = new IntHashSet(KEY_COUNT);
        while (set.size() < KEY_COUNT)
        {
            set.add(random.nextInt());
        }

        return set;
    }

    @Benchmark
    public void jdkGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.integerIntegerJdk.get(this.jdkIntKeysForMap[i]) == null)
                {
                    throw new AssertionError(this.jdkIntKeysForMap[i] + " not in map");
                }
            }
            if (this.integerIntegerJdk.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.integerIntegerJdk.size());
            }
        }
    }

    @Benchmark
    public void kolobokeGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.intIntKoloboke.get(this.kolobokeIntKeysForMap[i]) == this.intIntKoloboke.defaultValue())
                {
                    throw new AssertionError(this.kolobokeIntKeysForMap[i] + " not in map");
                }
            }
            if (this.intIntKoloboke.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.intIntKoloboke.size());
            }
        }
    }

    @Benchmark
    public void ecGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.intIntEc.get(this.ecIntKeysForMap[i]) == 0)
                {
                    throw new AssertionError(this.ecIntKeysForMap[i] + " not in map");
                }
            }
            if (this.intIntEc.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.intIntEc.size());
            }
        }
    }

    @Benchmark
    public void jdkPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.jdkIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokePut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.kolobokeIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableIntIntMap newMap = new IntIntHashMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.ecIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableIntIntMap newMap = new IntIntHashMap(this.intIntEc);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.ecIntKeysForMap[i]);
            }
            if (newMap.notEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void jdkRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.jdkIntKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokeRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.kolobokeIntKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    public void shuffle(int[] intArray, Random rnd)
    {
        for (int i = intArray.length; i > 1; i--)
        {
            IntIntMapSmallStressTest.swap(intArray, i - 1, rnd.nextInt(i));
        }
    }

    public void shuffle(Integer[] integerArray, Random rnd)
    {
        for (int i = integerArray.length; i > 1; i--)
        {
            IntIntMapSmallStressTest.swap(integerArray, i - 1, rnd.nextInt(i));
        }
    }

    private static void swap(int[] arr, int i, int j)
    {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private static void swap(Integer[] arr, int i, int j)
    {
        Integer tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private static Integer[] boxIntArray(int[] arr)
    {
        MutableList<Integer> list = new IntArrayList(arr).collect((IntToObjectFunction<Integer>) Integer::valueOf);
        return list.toArray(new Integer[arr.length]);
    }
}
```

### Method 77

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.IntIntMap;
import com.koloboke.collect.map.hash.HashIntIntMaps;
import org.eclipse.collections.api.block.function.primitive.IntToObjectFunction;
import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.primitive.MutableIntList;
import org.eclipse.collections.api.map.primitive.MutableIntIntMap;
import org.eclipse.collections.api.set.primitive.MutableIntSet;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.list.mutable.primitive.IntArrayList;
import org.eclipse.collections.impl.map.mutable.primitive.IntIntHashMap;
import org.eclipse.collections.impl.set.mutable.primitive.IntHashSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class IntIntMapLargeStressTest
{
    private static final int LOOP_COUNT = 1;
    private static final int KEY_COUNT = 400_000;
    private static final int MAP_SIZE = 1_000_000;

    @Param({"true", "false"})
    public boolean fullyRandom;
    private IntIntMap intIntKoloboke;
    private MutableIntIntMap intIntEc;
    private Map<Integer, Integer> integerIntegerJdk;
    private int[] ecIntKeysForMap;
    private int[] kolobokeIntKeysForMap;
    private Integer[] jdkIntKeysForMap;

    private int jdkIndex(int key)
    {
        return this.mask(key ^ (key >>> 16));
    }

    private int kolobokeIndex(int key)
    {
        int h = key * 0x9e3779b9;
        return this.mask(h ^ h >> 16);
    }

    private int ecIndex(int element)
    {
        return this.mask(element);
    }

    private int mask(int spread)
    {
        return spread & ((1 << 20) - 1);
    }

    @Setup
    public void setUp()
    {
        this.intIntKoloboke = HashIntIntMaps.newMutableMap(MAP_SIZE);
        this.intIntEc = new IntIntHashMap(MAP_SIZE);
        this.integerIntegerJdk = new HashMap<>(MAP_SIZE);

        Random random = new Random(0x123456789ABCDL);

        int[] randomNumbersForMap = this.getRandomKeys(random).toArray();

        int number = 23;
        int lower = Integer.MIN_VALUE;
        int upper = Integer.MAX_VALUE;
        this.kolobokeIntKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getKolobokeArray(number, lower, upper, random);
        this.ecIntKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getECArray(number, lower, upper, random);
        this.jdkIntKeysForMap = this.fullyRandom
                ? IntIntMapLargeStressTest.boxIntArray(randomNumbersForMap)
                : this.getJDKArray(lower, upper, random);

        for (int i = 0; i < KEY_COUNT; i++)
        {
            this.intIntKoloboke.put(this.kolobokeIntKeysForMap[i], 5);
            this.intIntEc.put(this.ecIntKeysForMap[i], 5);
            this.integerIntegerJdk.put(this.jdkIntKeysForMap[i], 5);
        }

        this.shuffle(this.ecIntKeysForMap, random);
        this.shuffle(this.kolobokeIntKeysForMap, random);
        this.shuffle(this.jdkIntKeysForMap, random);
    }

    protected int[] getECArray(int number, int lower, int upper, Random random)
    {
        int[] ecCollisions = this.getECSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(ecCollisions, random);
        return ecCollisions;
    }

    protected MutableIntList getECSequenceCollisions(int number, int lower, int upper)
    {
        MutableIntList ecCollidingNumbers = new IntArrayList();
        for (int i = lower; i < upper && ecCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.ecIndex(i);
            if (index >= number && index <= number + 100)
            {
                ecCollidingNumbers.add(i);
            }
        }
        return ecCollidingNumbers;
    }

    protected Integer[] getJDKArray(int lower, int upper, Random random)
    {
        MutableList<Integer> collisions = this.getJDKSequenceCollisions(lower, upper);
        Integer[] jdkCollision = collisions.toArray(new Integer[collisions.size()]);
        this.shuffle(jdkCollision, random);
        return jdkCollision;
    }

    protected MutableList<Integer> getJDKSequenceCollisions(int lower, int upper)
    {
        MutableList<Integer> jdkCollidingNumbers = FastList.newList();
        int slots = KEY_COUNT / (1 << 12) + 1;
        MutableIntSet indices = new IntHashSet();
        for (int i = lower; i < upper && jdkCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.jdkIndex(i);
            if (indices.size() < slots)
            {
                indices.add(index);
                jdkCollidingNumbers.add(i);
            }
            else if (indices.contains(index))
            {
                jdkCollidingNumbers.add(i);
            }
        }
        return jdkCollidingNumbers;
    }

    protected int[] getKolobokeArray(int number, int lower, int upper, Random random)
    {
        int[] kolobokeCollisions = this.getKolobokeSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(kolobokeCollisions, random);
        return kolobokeCollisions;
    }

    protected MutableIntList getKolobokeSequenceCollisions(int number, int lower, int upper)
    {
        MutableIntList kolobokeCollidingNumbers = new IntArrayList();
        for (int i = lower; i < upper && kolobokeCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.kolobokeIndex(i);
            if (index >= number && index <= number + 100)
            {
                kolobokeCollidingNumbers.add(i);
            }
        }
        return kolobokeCollidingNumbers;
    }

    protected MutableIntSet getRandomKeys(Random random)
    {
        MutableIntSet set = new IntHashSet(KEY_COUNT);
        while (set.size() < KEY_COUNT)
        {
            set.add(random.nextInt());
        }

        return set;
    }

    @Benchmark
    public void jdkGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.integerIntegerJdk.get(this.jdkIntKeysForMap[i]) == null)
                {
                    throw new AssertionError(this.jdkIntKeysForMap[i] + " not in map");
                }
            }
            if (this.integerIntegerJdk.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.integerIntegerJdk.size());
            }
        }
    }

    @Benchmark
    public void kolobokeGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.intIntKoloboke.get(this.kolobokeIntKeysForMap[i]) == this.intIntKoloboke.defaultValue())
                {
                    throw new AssertionError(this.kolobokeIntKeysForMap[i] + " not in map");
                }
            }
            if (this.intIntKoloboke.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.intIntKoloboke.size());
            }
        }
    }

    @Benchmark
    public void ecGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.intIntEc.get(this.ecIntKeysForMap[i]) == 0)
                {
                    throw new AssertionError(this.ecIntKeysForMap[i] + " not in map");
                }
            }
            if (this.intIntEc.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.intIntEc.size());
            }
        }
    }

    @Benchmark
    public void jdkPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.jdkIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokePut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.kolobokeIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableIntIntMap newMap = new IntIntHashMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.ecIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableIntIntMap newMap = new IntIntHashMap(this.intIntEc);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.ecIntKeysForMap[i]);
            }
            if (newMap.notEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void jdkRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.jdkIntKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokeRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.kolobokeIntKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    public void shuffle(int[] intArray, Random rnd)
    {
        for (int i = intArray.length; i > 1; i--)
        {
            IntIntMapLargeStressTest.swap(intArray, i - 1, rnd.nextInt(i));
        }
    }

    public void shuffle(Integer[] integerArray, Random rnd)
    {
        for (int i = integerArray.length; i > 1; i--)
        {
            IntIntMapLargeStressTest.swap(integerArray, i - 1, rnd.nextInt(i));
        }
    }

    private static void swap(int[] arr, int i, int j)
    {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private static void swap(Integer[] arr, int i, int j)
    {
        Integer tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private static Integer[] boxIntArray(int[] arr)
    {
        MutableList<Integer> list = new IntArrayList(arr).collect((IntToObjectFunction<Integer>) Integer::valueOf);
        return list.toArray(new Integer[arr.length]);
    }
}
```

### Method 78

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.IntIntMap;
import com.koloboke.collect.map.hash.HashIntIntMaps;
import org.eclipse.collections.api.block.function.primitive.IntToObjectFunction;
import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.primitive.MutableIntList;
import org.eclipse.collections.api.map.primitive.MutableIntIntMap;
import org.eclipse.collections.api.set.primitive.MutableIntSet;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.list.mutable.primitive.IntArrayList;
import org.eclipse.collections.impl.map.mutable.primitive.IntIntHashMap;
import org.eclipse.collections.impl.set.mutable.primitive.IntHashSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class IntIntMapLargeStressTest
{
    private static final int LOOP_COUNT = 1;
    private static final int KEY_COUNT = 400_000;
    private static final int MAP_SIZE = 1_000_000;

    @Param({"true", "false"})
    public boolean fullyRandom;
    private IntIntMap intIntKoloboke;
    private MutableIntIntMap intIntEc;
    private Map<Integer, Integer> integerIntegerJdk;
    private int[] ecIntKeysForMap;
    private int[] kolobokeIntKeysForMap;
    private Integer[] jdkIntKeysForMap;

    private int jdkIndex(int key)
    {
        return this.mask(key ^ (key >>> 16));
    }

    private int kolobokeIndex(int key)
    {
        int h = key * 0x9e3779b9;
        return this.mask(h ^ h >> 16);
    }

    private int ecIndex(int element)
    {
        return this.mask(element);
    }

    private int mask(int spread)
    {
        return spread & ((1 << 20) - 1);
    }

    @Setup
    public void setUp()
    {
        this.intIntKoloboke = HashIntIntMaps.newMutableMap(MAP_SIZE);
        this.intIntEc = new IntIntHashMap(MAP_SIZE);
        this.integerIntegerJdk = new HashMap<>(MAP_SIZE);

        Random random = new Random(0x123456789ABCDL);

        int[] randomNumbersForMap = this.getRandomKeys(random).toArray();

        int number = 23;
        int lower = Integer.MIN_VALUE;
        int upper = Integer.MAX_VALUE;
        this.kolobokeIntKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getKolobokeArray(number, lower, upper, random);
        this.ecIntKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getECArray(number, lower, upper, random);
        this.jdkIntKeysForMap = this.fullyRandom
                ? IntIntMapLargeStressTest.boxIntArray(randomNumbersForMap)
                : this.getJDKArray(lower, upper, random);

        for (int i = 0; i < KEY_COUNT; i++)
        {
            this.intIntKoloboke.put(this.kolobokeIntKeysForMap[i], 5);
            this.intIntEc.put(this.ecIntKeysForMap[i], 5);
            this.integerIntegerJdk.put(this.jdkIntKeysForMap[i], 5);
        }

        this.shuffle(this.ecIntKeysForMap, random);
        this.shuffle(this.kolobokeIntKeysForMap, random);
        this.shuffle(this.jdkIntKeysForMap, random);
    }

    protected int[] getECArray(int number, int lower, int upper, Random random)
    {
        int[] ecCollisions = this.getECSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(ecCollisions, random);
        return ecCollisions;
    }

    protected MutableIntList getECSequenceCollisions(int number, int lower, int upper)
    {
        MutableIntList ecCollidingNumbers = new IntArrayList();
        for (int i = lower; i < upper && ecCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.ecIndex(i);
            if (index >= number && index <= number + 100)
            {
                ecCollidingNumbers.add(i);
            }
        }
        return ecCollidingNumbers;
    }

    protected Integer[] getJDKArray(int lower, int upper, Random random)
    {
        MutableList<Integer> collisions = this.getJDKSequenceCollisions(lower, upper);
        Integer[] jdkCollision = collisions.toArray(new Integer[collisions.size()]);
        this.shuffle(jdkCollision, random);
        return jdkCollision;
    }

    protected MutableList<Integer> getJDKSequenceCollisions(int lower, int upper)
    {
        MutableList<Integer> jdkCollidingNumbers = FastList.newList();
        int slots = KEY_COUNT / (1 << 12) + 1;
        MutableIntSet indices = new IntHashSet();
        for (int i = lower; i < upper && jdkCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.jdkIndex(i);
            if (indices.size() < slots)
            {
                indices.add(index);
                jdkCollidingNumbers.add(i);
            }
            else if (indices.contains(index))
            {
                jdkCollidingNumbers.add(i);
            }
        }
        return jdkCollidingNumbers;
    }

    protected int[] getKolobokeArray(int number, int lower, int upper, Random random)
    {
        int[] kolobokeCollisions = this.getKolobokeSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(kolobokeCollisions, random);
        return kolobokeCollisions;
    }

    protected MutableIntList getKolobokeSequenceCollisions(int number, int lower, int upper)
    {
        MutableIntList kolobokeCollidingNumbers = new IntArrayList();
        for (int i = lower; i < upper && kolobokeCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.kolobokeIndex(i);
            if (index >= number && index <= number + 100)
            {
                kolobokeCollidingNumbers.add(i);
            }
        }
        return kolobokeCollidingNumbers;
    }

    protected MutableIntSet getRandomKeys(Random random)
    {
        MutableIntSet set = new IntHashSet(KEY_COUNT);
        while (set.size() < KEY_COUNT)
        {
            set.add(random.nextInt());
        }

        return set;
    }

    @Benchmark
    public void jdkGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.integerIntegerJdk.get(this.jdkIntKeysForMap[i]) == null)
                {
                    throw new AssertionError(this.jdkIntKeysForMap[i] + " not in map");
                }
            }
            if (this.integerIntegerJdk.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.integerIntegerJdk.size());
            }
        }
    }

    @Benchmark
    public void kolobokeGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.intIntKoloboke.get(this.kolobokeIntKeysForMap[i]) == this.intIntKoloboke.defaultValue())
                {
                    throw new AssertionError(this.kolobokeIntKeysForMap[i] + " not in map");
                }
            }
            if (this.intIntKoloboke.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.intIntKoloboke.size());
            }
        }
    }

    @Benchmark
    public void ecGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.intIntEc.get(this.ecIntKeysForMap[i]) == 0)
                {
                    throw new AssertionError(this.ecIntKeysForMap[i] + " not in map");
                }
            }
            if (this.intIntEc.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.intIntEc.size());
            }
        }
    }

    @Benchmark
    public void jdkPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.jdkIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokePut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.kolobokeIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableIntIntMap newMap = new IntIntHashMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.ecIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableIntIntMap newMap = new IntIntHashMap(this.intIntEc);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.ecIntKeysForMap[i]);
            }
            if (newMap.notEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void jdkRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.jdkIntKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokeRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.kolobokeIntKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    public void shuffle(int[] intArray, Random rnd)
    {
        for (int i = intArray.length; i > 1; i--)
        {
            IntIntMapLargeStressTest.swap(intArray, i - 1, rnd.nextInt(i));
        }
    }

    public void shuffle(Integer[] integerArray, Random rnd)
    {
        for (int i = integerArray.length; i > 1; i--)
        {
            IntIntMapLargeStressTest.swap(integerArray, i - 1, rnd.nextInt(i));
        }
    }

    private static void swap(int[] arr, int i, int j)
    {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private static void swap(Integer[] arr, int i, int j)
    {
        Integer tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private static Integer[] boxIntArray(int[] arr)
    {
        MutableList<Integer> list = new IntArrayList(arr).collect((IntToObjectFunction<Integer>) Integer::valueOf);
        return list.toArray(new Integer[arr.length]);
    }
}
```

### Method 79

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.IntIntMap;
import com.koloboke.collect.map.hash.HashIntIntMaps;
import org.eclipse.collections.api.block.function.primitive.IntToObjectFunction;
import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.api.list.primitive.MutableIntList;
import org.eclipse.collections.api.map.primitive.MutableIntIntMap;
import org.eclipse.collections.api.set.primitive.MutableIntSet;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.eclipse.collections.impl.list.mutable.primitive.IntArrayList;
import org.eclipse.collections.impl.map.mutable.primitive.IntIntHashMap;
import org.eclipse.collections.impl.set.mutable.primitive.IntHashSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class IntIntMapLargeStressTest
{
    private static final int LOOP_COUNT = 1;
    private static final int KEY_COUNT = 400_000;
    private static final int MAP_SIZE = 1_000_000;

    @Param({"true", "false"})
    public boolean fullyRandom;
    private IntIntMap intIntKoloboke;
    private MutableIntIntMap intIntEc;
    private Map<Integer, Integer> integerIntegerJdk;
    private int[] ecIntKeysForMap;
    private int[] kolobokeIntKeysForMap;
    private Integer[] jdkIntKeysForMap;

    private int jdkIndex(int key)
    {
        return this.mask(key ^ (key >>> 16));
    }

    private int kolobokeIndex(int key)
    {
        int h = key * 0x9e3779b9;
        return this.mask(h ^ h >> 16);
    }

    private int ecIndex(int element)
    {
        return this.mask(element);
    }

    private int mask(int spread)
    {
        return spread & ((1 << 20) - 1);
    }

    @Setup
    public void setUp()
    {
        this.intIntKoloboke = HashIntIntMaps.newMutableMap(MAP_SIZE);
        this.intIntEc = new IntIntHashMap(MAP_SIZE);
        this.integerIntegerJdk = new HashMap<>(MAP_SIZE);

        Random random = new Random(0x123456789ABCDL);

        int[] randomNumbersForMap = this.getRandomKeys(random).toArray();

        int number = 23;
        int lower = Integer.MIN_VALUE;
        int upper = Integer.MAX_VALUE;
        this.kolobokeIntKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getKolobokeArray(number, lower, upper, random);
        this.ecIntKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getECArray(number, lower, upper, random);
        this.jdkIntKeysForMap = this.fullyRandom
                ? IntIntMapLargeStressTest.boxIntArray(randomNumbersForMap)
                : this.getJDKArray(lower, upper, random);

        for (int i = 0; i < KEY_COUNT; i++)
        {
            this.intIntKoloboke.put(this.kolobokeIntKeysForMap[i], 5);
            this.intIntEc.put(this.ecIntKeysForMap[i], 5);
            this.integerIntegerJdk.put(this.jdkIntKeysForMap[i], 5);
        }

        this.shuffle(this.ecIntKeysForMap, random);
        this.shuffle(this.kolobokeIntKeysForMap, random);
        this.shuffle(this.jdkIntKeysForMap, random);
    }

    protected int[] getECArray(int number, int lower, int upper, Random random)
    {
        int[] ecCollisions = this.getECSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(ecCollisions, random);
        return ecCollisions;
    }

    protected MutableIntList getECSequenceCollisions(int number, int lower, int upper)
    {
        MutableIntList ecCollidingNumbers = new IntArrayList();
        for (int i = lower; i < upper && ecCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.ecIndex(i);
            if (index >= number && index <= number + 100)
            {
                ecCollidingNumbers.add(i);
            }
        }
        return ecCollidingNumbers;
    }

    protected Integer[] getJDKArray(int lower, int upper, Random random)
    {
        MutableList<Integer> collisions = this.getJDKSequenceCollisions(lower, upper);
        Integer[] jdkCollision = collisions.toArray(new Integer[collisions.size()]);
        this.shuffle(jdkCollision, random);
        return jdkCollision;
    }

    protected MutableList<Integer> getJDKSequenceCollisions(int lower, int upper)
    {
        MutableList<Integer> jdkCollidingNumbers = FastList.newList();
        int slots = KEY_COUNT / (1 << 12) + 1;
        MutableIntSet indices = new IntHashSet();
        for (int i = lower; i < upper && jdkCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.jdkIndex(i);
            if (indices.size() < slots)
            {
                indices.add(index);
                jdkCollidingNumbers.add(i);
            }
            else if (indices.contains(index))
            {
                jdkCollidingNumbers.add(i);
            }
        }
        return jdkCollidingNumbers;
    }

    protected int[] getKolobokeArray(int number, int lower, int upper, Random random)
    {
        int[] kolobokeCollisions = this.getKolobokeSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(kolobokeCollisions, random);
        return kolobokeCollisions;
    }

    protected MutableIntList getKolobokeSequenceCollisions(int number, int lower, int upper)
    {
        MutableIntList kolobokeCollidingNumbers = new IntArrayList();
        for (int i = lower; i < upper && kolobokeCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.kolobokeIndex(i);
            if (index >= number && index <= number + 100)
            {
                kolobokeCollidingNumbers.add(i);
            }
        }
        return kolobokeCollidingNumbers;
    }

    protected MutableIntSet getRandomKeys(Random random)
    {
        MutableIntSet set = new IntHashSet(KEY_COUNT);
        while (set.size() < KEY_COUNT)
        {
            set.add(random.nextInt());
        }

        return set;
    }

    @Benchmark
    public void jdkGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.integerIntegerJdk.get(this.jdkIntKeysForMap[i]) == null)
                {
                    throw new AssertionError(this.jdkIntKeysForMap[i] + " not in map");
                }
            }
            if (this.integerIntegerJdk.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.integerIntegerJdk.size());
            }
        }
    }

    @Benchmark
    public void kolobokeGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.intIntKoloboke.get(this.kolobokeIntKeysForMap[i]) == this.intIntKoloboke.defaultValue())
                {
                    throw new AssertionError(this.kolobokeIntKeysForMap[i] + " not in map");
                }
            }
            if (this.intIntKoloboke.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.intIntKoloboke.size());
            }
        }
    }

    @Benchmark
    public void ecGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.intIntEc.get(this.ecIntKeysForMap[i]) == 0)
                {
                    throw new AssertionError(this.ecIntKeysForMap[i] + " not in map");
                }
            }
            if (this.intIntEc.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.intIntEc.size());
            }
        }
    }

    @Benchmark
    public void jdkPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.jdkIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokePut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.kolobokeIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableIntIntMap newMap = new IntIntHashMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.ecIntKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableIntIntMap newMap = new IntIntHashMap(this.intIntEc);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.ecIntKeysForMap[i]);
            }
            if (newMap.notEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void jdkRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.jdkIntKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokeRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.kolobokeIntKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    public void shuffle(int[] intArray, Random rnd)
    {
        for (int i = intArray.length; i > 1; i--)
        {
            IntIntMapLargeStressTest.swap(intArray, i - 1, rnd.nextInt(i));
        }
    }

    public void shuffle(Integer[] integerArray, Random rnd)
    {
        for (int i = integerArray.length; i > 1; i--)
        {
            IntIntMapLargeStressTest.swap(integerArray, i - 1, rnd.nextInt(i));
        }
    }

    private static void swap(int[] arr, int i, int j)
    {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private static void swap(Integer[] arr, int i, int j)
    {
        Integer tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private static Integer[] boxIntArray(int[] arr)
    {
        MutableList<Integer> list = new IntArrayList(arr).collect((IntToObjectFunction<Integer>) Integer::valueOf);
        return list.toArray(new Integer[arr.length]);
    }
}
```

### Method 80

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableListMultimap;
import com.google.common.collect.Multimaps;
import org.eclipse.collections.api.RichIterable;
import org.eclipse.collections.api.multimap.Multimap;
import org.eclipse.collections.api.multimap.set.UnsortedSetMultimap;
import org.eclipse.collections.api.set.MutableSet;
import org.eclipse.collections.api.set.UnsortedSetIterable;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.multimap.set.UnifiedSetMultimap;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.eclipse.collections.impl.test.Verify;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Ignore;
import org.junit.Test;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class GroupBySetTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final Set<Integer> integersJDK = new HashSet<>(Interval.zeroTo(SIZE - 1));
    private final UnifiedSet<Integer> integersEC = new UnifiedSet<>(Interval.zeroTo(SIZE - 1));

    private ExecutorService executorService;

    @Before
    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @After
    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public Map<Boolean, Set<Integer>> groupBy_2_keys_serial_lazy_jdk()
    {
        Map<Boolean, Set<Integer>> multimap = this.integersJDK.stream()
                .collect(Collectors.groupingBy(each -> each % 2 == 0, Collectors.toSet()));
        Verify.assertSize(2, multimap);
        return multimap;
    }

    @Benchmark
    public Map<Boolean, Set<Integer>> groupBy_2_keys_serial_lazy_streams_ec()
    {
        Map<Boolean, Set<Integer>> multimap = this.integersEC.stream()
                .collect(Collectors.groupingBy(each -> each % 2 == 0, Collectors.toSet()));
        Verify.assertSize(2, multimap);
        return multimap;
    }

    @Test
    public void test_groupBy_2_keys_serial_lazy_jdk()
    {
        Map<Boolean, Set<Integer>> multimap = this.groupBy_2_keys_serial_lazy_jdk();
        Set<Integer> odds = multimap.get(false);
        Set<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), evens);
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), odds);
    }

    @Test
    public void test_groupBy_2_keys_serial_lazy_streams_ec()
    {
        Map<Boolean, Set<Integer>> multimap = this.groupBy_2_keys_serial_lazy_streams_ec();
        Set<Integer> odds = multimap.get(false);
        Set<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), evens);
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), odds);
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_100_keys_serial_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.integersJDK.stream().collect(Collectors.groupingBy(each -> each % 100, Collectors.toSet()));
        Verify.assertSize(100, multimap);
        return multimap;
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_100_keys_serial_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.integersEC.stream().collect(Collectors.groupingBy(each -> each % 100, Collectors.toSet()));
        Verify.assertSize(100, multimap);
        return multimap;
    }

    @Test
    public void test_groupBy_100_keys_serial_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_100_keys_serial_lazy_jdk();
        for (int i = 0; i < 100; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), integers);
        }
    }

    @Test
    public void test_groupBy_100_keys_serial_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_100_keys_serial_lazy_streams_ec();
        for (int i = 0; i < 100; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), integers);
        }
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_10000_keys_serial_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.integersJDK.stream().collect(Collectors.groupingBy(each -> each % 10_000, Collectors.toSet()));
        Verify.assertSize(10_000, multimap);
        return multimap;
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_10000_keys_serial_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.integersEC.stream().collect(Collectors.groupingBy(each -> each % 10_000, Collectors.toSet()));
        Verify.assertSize(10_000, multimap);
        return multimap;
    }

    @Test
    public void test_groupBy_10000_keys_serial_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_10000_keys_serial_lazy_jdk();
        for (int i = 0; i < 10_000; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), integers);
        }
    }

    @Test
    public void test_groupBy_10000_keys_serial_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_10000_keys_serial_lazy_streams_ec();
        for (int i = 0; i < 10_000; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), integers);
        }
    }

    @Benchmark
    public Map<Boolean, Set<Integer>> groupBy_2_keys_parallel_lazy_jdk()
    {
        Map<Boolean, Set<Integer>> multimap = this.integersJDK.parallelStream().collect(Collectors.groupingBy(each -> each % 2 == 0, Collectors.toSet()));
        Verify.assertSize(2, multimap);
        return multimap;
    }

    @Benchmark
    public Map<Boolean, Set<Integer>> groupBy_2_keys_parallel_lazy_streams_ec()
    {
        Map<Boolean, Set<Integer>> multimap = this.integersEC.parallelStream().collect(Collectors.groupingBy(each -> each % 2 == 0, Collectors.toSet()));
        Verify.assertSize(2, multimap);
        return multimap;
    }

    @Test
    public void test_groupBy_2_keys_parallel_lazy_jdk()
    {
        Map<Boolean, Set<Integer>> multimap = this.groupBy_2_keys_parallel_lazy_jdk();
        Set<Integer> odds = multimap.get(false);
        Set<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), evens);
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), odds);
    }

    @Test
    public void test_groupBy_2_keys_parallel_lazy_streams_ec()
    {
        Map<Boolean, Set<Integer>> multimap = this.groupBy_2_keys_parallel_lazy_streams_ec();
        Set<Integer> odds = multimap.get(false);
        Set<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), evens);
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), odds);
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_100_keys_parallel_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.integersJDK.parallelStream().collect(Collectors.groupingBy(each -> each % 100, Collectors.toSet()));
        Verify.assertSize(100, multimap);
        return multimap;
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_100_keys_parallel_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.integersEC.parallelStream().collect(Collectors.groupingBy(each -> each % 100, Collectors.toSet()));
        Verify.assertSize(100, multimap);
        return multimap;
    }

    @Test
    public void test_groupBy_100_keys_parallel_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_100_keys_parallel_lazy_jdk();
        for (int i = 0; i < 100; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), integers);
        }
    }

    @Test
    public void test_groupBy_100_keys_parallel_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_100_keys_parallel_lazy_streams_ec();
        for (int i = 0; i < 100; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), integers);
        }
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_10000_keys_parallel_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.integersJDK.parallelStream().collect(Collectors.groupingBy(each -> each % 10_000, Collectors.toSet()));
        Verify.assertSize(10_000, multimap);
        return multimap;
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_10000_keys_parallel_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.integersEC.parallelStream().collect(Collectors.groupingBy(each -> each % 10_000, Collectors.toSet()));
        Verify.assertSize(10_000, multimap);
        return multimap;
    }

    @Test
    public void test_groupBy_10000_keys_parallel_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_10000_keys_parallel_lazy_jdk();
        for (int i = 0; i < 10_000; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), integers);
        }
    }

    @Test
    public void test_groupBy_10000_keys_parallel_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_10000_keys_parallel_lazy_streams_ec();
        for (int i = 0; i < 10_000; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), integers);
        }
    }

    @Benchmark
    public ImmutableListMultimap<Boolean, Integer> groupBy_unordered_lists_2_keys_serial_eager_guava()
    {
        ImmutableListMultimap<Boolean, Integer> multimap = Multimaps.index(this.integersJDK, each -> each % 2 == 0);
        Verify.assertSize(2, multimap.asMap());
        return multimap;
    }

    @Ignore("Why is Guava reordering values?")
    @Test
    public void test_groupBy_unordered_lists_2_keys_serial_eager_guava()
    {
        ImmutableListMultimap<Boolean, Integer> multimap = this.groupBy_unordered_lists_2_keys_serial_eager_guava();
        ImmutableList<Integer> odds = multimap.get(false);
        ImmutableList<Integer> evens = multimap.get(true);
        Verify.assertListsEqual(Interval.fromToBy(0, 999_999, 2), evens);
        Verify.assertListsEqual(Interval.fromToBy(1, 999_999, 2), odds);
    }

    @Benchmark
    public ImmutableListMultimap<Integer, Integer> groupBy_unordered_lists_100_keys_serial_eager_guava()
    {
        ImmutableListMultimap<Integer, Integer> multimap = Multimaps.index(this.integersJDK, each -> each % 100);
        Verify.assertSize(100, multimap.asMap());
        return multimap;
    }

    @Test
    public void test_groupBy_unordered_lists_100_keys_serial_eager_guava()
    {
        ImmutableListMultimap<Integer, Integer> multimap = this.groupBy_unordered_lists_100_keys_serial_eager_guava();
        for (int i = 0; i < 100; i++)
        {
            ImmutableList<Integer> integers = multimap.get(i);
            Verify.assertSize(10_000, integers);
            Assert.assertEquals(Interval.fromToBy(i, 999_999, 100), integers);
        }
    }

    @Benchmark
    public ImmutableListMultimap<Integer, Integer> groupBy_unordered_lists_10000_keys_serial_eager_guava()
    {
        ImmutableListMultimap<Integer, Integer> multimap = Multimaps.index(this.integersJDK, each -> each % 10000);
        Verify.assertSize(10_000, multimap.asMap());
        return multimap;
    }

    @Test
    public void test_groupBy_unordered_lists_10000_keys_serial_eager_guava()
    {
        ImmutableListMultimap<Integer, Integer> multimap = this.groupBy_unordered_lists_10000_keys_serial_eager_guava();
        for (int i = 0; i < 10_000; i++)
        {
            ImmutableList<Integer> integers = multimap.get(i);
            Verify.assertSize(100, integers);
            Assert.assertEquals(Interval.fromToBy(i, 999_999, 10_000), integers);
        }
    }

    @Benchmark
    public UnifiedSetMultimap<Boolean, Integer> groupBy_2_keys_serial_eager_ec()
    {
        UnifiedSetMultimap<Boolean, Integer> multimap = this.integersEC.groupBy(each -> each % 2 == 0);
        Assert.assertEquals(2, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_2_keys_serial_eager_ec()
    {
        UnifiedSetMultimap<Boolean, Integer> multimap = this.groupBy_2_keys_serial_eager_ec();
        Set<Integer> odds = multimap.get(false);
        Set<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), evens);
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), odds);
    }

    @Benchmark
    public UnifiedSetMultimap<Integer, Integer> groupBy_100_keys_serial_eager_ec()
    {
        UnifiedSetMultimap<Integer, Integer> multimap = this.integersEC.groupBy(each -> each % 100);
        Assert.assertEquals(100, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_100_keys_serial_eager_ec()
    {
        UnifiedSetMultimap<Integer, Integer> multimap = this.groupBy_100_keys_serial_eager_ec();
        for (int i = 0; i < 100; i++)
        {
            MutableSet<Integer> integers = multimap.get(i);
            Verify.assertSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), integers);
        }
    }

    @Benchmark
    public UnifiedSetMultimap<Integer, Integer> groupBy_10000_keys_serial_eager_ec()
    {
        UnifiedSetMultimap<Integer, Integer> multimap = this.integersEC.groupBy(each -> each % 10_000);
        Assert.assertEquals(10_000, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_10000_keys_serial_eager_ec()
    {
        UnifiedSetMultimap<Integer, Integer> multimap = this.groupBy_10000_keys_serial_eager_ec();
        for (int i = 0; i < 10_000; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), integers);
        }
    }

    @Benchmark
    public Multimap<Boolean, Integer> groupBy_unordered_lists_2_keys_serial_lazy_ec()
    {
        Multimap<Boolean, Integer> multimap = this.integersEC.asLazy().groupBy(each -> each % 2 == 0);
        Assert.assertEquals(2, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_unordered_lists_2_keys_serial_lazy_ec()
    {
        Multimap<Boolean, Integer> multimap = this.groupBy_unordered_lists_2_keys_serial_lazy_ec();
        RichIterable<Integer> odds = multimap.get(false);
        RichIterable<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), evens.toSet());
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), odds.toSet());
    }

    @Benchmark
    public Multimap<Integer, Integer> groupBy_unordered_lists_100_keys_serial_lazy_ec()
    {
        Multimap<Integer, Integer> multimap = this.integersEC.asLazy().groupBy(each -> each % 100);
        Assert.assertEquals(100, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_unordered_lists_100_keys_serial_lazy_ec()
    {
        Multimap<Integer, Integer> multimap = this.groupBy_unordered_lists_100_keys_serial_lazy_ec();
        for (int i = 0; i < 100; i++)
        {
            RichIterable<Integer> integers = multimap.get(i);
            Verify.assertIterableSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), integers.toSet());
        }
    }

    @Benchmark
    public Multimap<Integer, Integer> groupBy_unordered_lists_10000_keys_serial_lazy_ec()
    {
        Multimap<Integer, Integer> multimap = this.integersEC.asLazy().groupBy(each -> each % 10_000);
        Assert.assertEquals(10_000, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_unordered_lists_10000_keys_serial_lazy_ec()
    {
        Multimap<Integer, Integer> multimap = this.groupBy_unordered_lists_10000_keys_serial_lazy_ec();
        for (int i = 0; i < 10_000; i++)
        {
            RichIterable<Integer> integers = multimap.get(i);
            Verify.assertIterableSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), integers.toSet());
        }
    }

    @Benchmark
    public UnsortedSetMultimap<Boolean, Integer> groupBy_2_keys_parallel_lazy_ec()
    {
        UnsortedSetMultimap<Boolean, Integer> multimap = this.integersEC.asParallel(this.executorService, BATCH_SIZE).groupBy(each -> each % 2 == 0);
        Assert.assertEquals(2, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_2_keys_parallel_lazy_ec()
    {
        UnsortedSetMultimap<Boolean, Integer> multimap = this.groupBy_2_keys_parallel_lazy_ec();
        UnsortedSetIterable<Integer> odds = multimap.get(false);
        UnsortedSetIterable<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), (Set<?>) evens);
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), (Set<?>) odds);
    }

    @Benchmark
    public UnsortedSetMultimap<Integer, Integer> groupBy_100_keys_parallel_lazy_ec()
    {
        UnsortedSetMultimap<Integer, Integer> multimap = this.integersEC.asParallel(this.executorService, BATCH_SIZE).groupBy(each -> each % 100);
        Assert.assertEquals(100, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_100_keys_parallel_lazy_ec()
    {
        UnsortedSetMultimap<Integer, Integer> multimap = this.groupBy_100_keys_parallel_lazy_ec();
        for (int i = 0; i < 100; i++)
        {
            UnsortedSetIterable<Integer> integers = multimap.get(i);
            Verify.assertIterableSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), (Set<?>) integers);
        }
    }

    @Benchmark
    public UnsortedSetMultimap<Integer, Integer> groupBy_10000_keys_parallel_lazy_ec()
    {
        UnsortedSetMultimap<Integer, Integer> multimap = this.integersEC.asParallel(this.executorService, BATCH_SIZE).groupBy(each -> each % 10_000);
        Assert.assertEquals(10_000, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_10000_keys_parallel_lazy_ec()
    {
        UnsortedSetMultimap<Integer, Integer> multimap = this.groupBy_10000_keys_parallel_lazy_ec();
        for (int i = 0; i < 10_000; i++)
        {
            UnsortedSetIterable<Integer> integers = multimap.get(i);
            Verify.assertIterableSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), (Set<?>) integers);
        }
    }

    @Benchmark
    public void groupBy_2_keys_serial_eager_scala()
    {
        GroupBySetScalaTest.groupBy_2_keys_serial_eager_scala();
    }

    @Test
    public void test_groupBy_2_keys_serial_eager_scala()
    {
        GroupBySetScalaTest.test_groupBy_2_keys_serial_eager_scala();
    }

    @Benchmark
    public void groupBy_100_keys_serial_eager_scala()
    {
        GroupBySetScalaTest.groupBy_100_keys_serial_eager_scala();
    }

    @Test
    public void test_groupBy_100_keys_serial_eager_scala()
    {
        GroupBySetScalaTest.test_groupBy_100_keys_serial_eager_scala();
    }

    @Benchmark
    public void groupBy_10000_keys_serial_eager_scala()
    {
        GroupBySetScalaTest.groupBy_10000_keys_serial_eager_scala();
    }

    @Test
    public void test_groupBy_10000_keys_serial_eager_scala()
    {
        GroupBySetScalaTest.test_groupBy_10000_keys_serial_eager_scala();
    }

    @Benchmark
    public void groupBy_2_keys_serial_lazy_scala()
    {
        GroupBySetScalaTest.groupBy_unordered_lists_2_keys_serial_lazy_scala();
    }

    @Test
    public void test_groupBy_unordered_lists_2_keys_serial_lazy_scala()
    {
        GroupBySetScalaTest.test_groupBy_unordered_lists_2_keys_serial_lazy_scala();
    }

    @Benchmark
    public void groupBy_100_keys_serial_lazy_scala()
    {
        GroupBySetScalaTest.groupBy_unordered_lists_100_keys_serial_lazy_scala();
    }

    @Test
    public void test_groupBy_unordered_lists_100_keys_serial_lazy_scala()
    {
        GroupBySetScalaTest.test_groupBy_unordered_lists_100_keys_serial_lazy_scala();
    }

    @Benchmark
    public void groupBy_10000_keys_serial_lazy_scala()
    {
        GroupBySetScalaTest.groupBy_unordered_lists_10000_keys_serial_lazy_scala();
    }

    @Test
    public void test_groupBy_unordered_lists_10000_keys_serial_lazy_scala()
    {
        GroupBySetScalaTest.test_groupBy_unordered_lists_10000_keys_serial_lazy_scala();
    }

    @Benchmark
    public void groupBy_2_keys_parallel_lazy_scala()
    {
        GroupBySetScalaTest.groupBy_2_keys_parallel_lazy_scala();
    }

    @Test
    public void test_groupBy_2_keys_parallel_lazy_scala()
    {
        GroupBySetScalaTest.test_groupBy_2_keys_parallel_lazy_scala();
    }

    @Benchmark
    public void groupBy_100_keys_parallel_lazy_scala()
    {
        GroupBySetScalaTest.groupBy_100_keys_parallel_lazy_scala();
    }

    @Test
    public void test_groupBy_100_keys_parallel_lazy_scala()
    {
        GroupBySetScalaTest.test_groupBy_100_keys_parallel_lazy_scala();
    }

    @Benchmark
    public void groupBy_10000_keys_parallel_lazy_scala()
    {
        GroupBySetScalaTest.groupBy_10000_keys_parallel_lazy_scala();
    }

    @Test
    public void test_groupBy_10000_keys_parallel_lazy_scala()
    {
        GroupBySetScalaTest.test_groupBy_10000_keys_parallel_lazy_scala();
    }
}
```

### Method 81

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableListMultimap;
import com.google.common.collect.Multimaps;
import org.eclipse.collections.api.RichIterable;
import org.eclipse.collections.api.multimap.Multimap;
import org.eclipse.collections.api.multimap.set.UnsortedSetMultimap;
import org.eclipse.collections.api.set.MutableSet;
import org.eclipse.collections.api.set.UnsortedSetIterable;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.multimap.set.UnifiedSetMultimap;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.eclipse.collections.impl.test.Verify;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Ignore;
import org.junit.Test;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class GroupBySetTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;
    private final Set<Integer> integersJDK = new HashSet<>(Interval.zeroTo(SIZE - 1));
    private final UnifiedSet<Integer> integersEC = new UnifiedSet<>(Interval.zeroTo(SIZE - 1));

    private ExecutorService executorService;

    @Before
    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @After
    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public Map<Boolean, Set<Integer>> groupBy_2_keys_serial_lazy_jdk()
    {
        Map<Boolean, Set<Integer>> multimap = this.integersJDK.stream()
                .collect(Collectors.groupingBy(each -> each % 2 == 0, Collectors.toSet()));
        Verify.assertSize(2, multimap);
        return multimap;
    }

    @Benchmark
    public Map<Boolean, Set<Integer>> groupBy_2_keys_serial_lazy_streams_ec()
    {
        Map<Boolean, Set<Integer>> multimap = this.integersEC.stream()
                .collect(Collectors.groupingBy(each -> each % 2 == 0, Collectors.toSet()));
        Verify.assertSize(2, multimap);
        return multimap;
    }

    @Test
    public void test_groupBy_2_keys_serial_lazy_jdk()
    {
        Map<Boolean, Set<Integer>> multimap = this.groupBy_2_keys_serial_lazy_jdk();
        Set<Integer> odds = multimap.get(false);
        Set<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), evens);
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), odds);
    }

    @Test
    public void test_groupBy_2_keys_serial_lazy_streams_ec()
    {
        Map<Boolean, Set<Integer>> multimap = this.groupBy_2_keys_serial_lazy_streams_ec();
        Set<Integer> odds = multimap.get(false);
        Set<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), evens);
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), odds);
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_100_keys_serial_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.integersJDK.stream().collect(Collectors.groupingBy(each -> each % 100, Collectors.toSet()));
        Verify.assertSize(100, multimap);
        return multimap;
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_100_keys_serial_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.integersEC.stream().collect(Collectors.groupingBy(each -> each % 100, Collectors.toSet()));
        Verify.assertSize(100, multimap);
        return multimap;
    }

    @Test
    public void test_groupBy_100_keys_serial_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_100_keys_serial_lazy_jdk();
        for (int i = 0; i < 100; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), integers);
        }
    }

    @Test
    public void test_groupBy_100_keys_serial_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_100_keys_serial_lazy_streams_ec();
        for (int i = 0; i < 100; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), integers);
        }
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_10000_keys_serial_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.integersJDK.stream().collect(Collectors.groupingBy(each -> each % 10_000, Collectors.toSet()));
        Verify.assertSize(10_000, multimap);
        return multimap;
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_10000_keys_serial_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.integersEC.stream().collect(Collectors.groupingBy(each -> each % 10_000, Collectors.toSet()));
        Verify.assertSize(10_000, multimap);
        return multimap;
    }

    @Test
    public void test_groupBy_10000_keys_serial_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_10000_keys_serial_lazy_jdk();
        for (int i = 0; i < 10_000; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), integers);
        }
    }

    @Test
    public void test_groupBy_10000_keys_serial_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_10000_keys_serial_lazy_streams_ec();
        for (int i = 0; i < 10_000; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), integers);
        }
    }

    @Benchmark
    public Map<Boolean, Set<Integer>> groupBy_2_keys_parallel_lazy_jdk()
    {
        Map<Boolean, Set<Integer>> multimap = this.integersJDK.parallelStream().collect(Collectors.groupingBy(each -> each % 2 == 0, Collectors.toSet()));
        Verify.assertSize(2, multimap);
        return multimap;
    }

    @Benchmark
    public Map<Boolean, Set<Integer>> groupBy_2_keys_parallel_lazy_streams_ec()
    {
        Map<Boolean, Set<Integer>> multimap = this.integersEC.parallelStream().collect(Collectors.groupingBy(each -> each % 2 == 0, Collectors.toSet()));
        Verify.assertSize(2, multimap);
        return multimap;
    }

    @Test
    public void test_groupBy_2_keys_parallel_lazy_jdk()
    {
        Map<Boolean, Set<Integer>> multimap = this.groupBy_2_keys_parallel_lazy_jdk();
        Set<Integer> odds = multimap.get(false);
        Set<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), evens);
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), odds);
    }

    @Test
    public void test_groupBy_2_keys_parallel_lazy_streams_ec()
    {
        Map<Boolean, Set<Integer>> multimap = this.groupBy_2_keys_parallel_lazy_streams_ec();
        Set<Integer> odds = multimap.get(false);
        Set<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), evens);
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), odds);
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_100_keys_parallel_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.integersJDK.parallelStream().collect(Collectors.groupingBy(each -> each % 100, Collectors.toSet()));
        Verify.assertSize(100, multimap);
        return multimap;
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_100_keys_parallel_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.integersEC.parallelStream().collect(Collectors.groupingBy(each -> each % 100, Collectors.toSet()));
        Verify.assertSize(100, multimap);
        return multimap;
    }

    @Test
    public void test_groupBy_100_keys_parallel_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_100_keys_parallel_lazy_jdk();
        for (int i = 0; i < 100; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), integers);
        }
    }

    @Test
    public void test_groupBy_100_keys_parallel_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_100_keys_parallel_lazy_streams_ec();
        for (int i = 0; i < 100; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), integers);
        }
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_10000_keys_parallel_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.integersJDK.parallelStream().collect(Collectors.groupingBy(each -> each % 10_000, Collectors.toSet()));
        Verify.assertSize(10_000, multimap);
        return multimap;
    }

    @Benchmark
    public Map<Integer, Set<Integer>> groupBy_10000_keys_parallel_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.integersEC.parallelStream().collect(Collectors.groupingBy(each -> each % 10_000, Collectors.toSet()));
        Verify.assertSize(10_000, multimap);
        return multimap;
    }

    @Test
    public void test_groupBy_10000_keys_parallel_lazy_jdk()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_10000_keys_parallel_lazy_jdk();
        for (int i = 0; i < 10_000; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), integers);
        }
    }

    @Test
    public void test_groupBy_10000_keys_parallel_lazy_streams_ec()
    {
        Map<Integer, Set<Integer>> multimap = this.groupBy_10000_keys_parallel_lazy_streams_ec();
        for (int i = 0; i < 10_000; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), integers);
        }
    }

    @Benchmark
    public ImmutableListMultimap<Boolean, Integer> groupBy_unordered_lists_2_keys_serial_eager_guava()
    {
        ImmutableListMultimap<Boolean, Integer> multimap = Multimaps.index(this.integersJDK, each -> each % 2 == 0);
        Verify.assertSize(2, multimap.asMap());
        return multimap;
    }

    @Ignore("Why is Guava reordering values?")
    @Test
    public void test_groupBy_unordered_lists_2_keys_serial_eager_guava()
    {
        ImmutableListMultimap<Boolean, Integer> multimap = this.groupBy_unordered_lists_2_keys_serial_eager_guava();
        ImmutableList<Integer> odds = multimap.get(false);
        ImmutableList<Integer> evens = multimap.get(true);
        Verify.assertListsEqual(Interval.fromToBy(0, 999_999, 2), evens);
        Verify.assertListsEqual(Interval.fromToBy(1, 999_999, 2), odds);
    }

    @Benchmark
    public ImmutableListMultimap<Integer, Integer> groupBy_unordered_lists_100_keys_serial_eager_guava()
    {
        ImmutableListMultimap<Integer, Integer> multimap = Multimaps.index(this.integersJDK, each -> each % 100);
        Verify.assertSize(100, multimap.asMap());
        return multimap;
    }

    @Test
    public void test_groupBy_unordered_lists_100_keys_serial_eager_guava()
    {
        ImmutableListMultimap<Integer, Integer> multimap = this.groupBy_unordered_lists_100_keys_serial_eager_guava();
        for (int i = 0; i < 100; i++)
        {
            ImmutableList<Integer> integers = multimap.get(i);
            Verify.assertSize(10_000, integers);
            Assert.assertEquals(Interval.fromToBy(i, 999_999, 100), integers);
        }
    }

    @Benchmark
    public ImmutableListMultimap<Integer, Integer> groupBy_unordered_lists_10000_keys_serial_eager_guava()
    {
        ImmutableListMultimap<Integer, Integer> multimap = Multimaps.index(this.integersJDK, each -> each % 10000);
        Verify.assertSize(10_000, multimap.asMap());
        return multimap;
    }

    @Test
    public void test_groupBy_unordered_lists_10000_keys_serial_eager_guava()
    {
        ImmutableListMultimap<Integer, Integer> multimap = this.groupBy_unordered_lists_10000_keys_serial_eager_guava();
        for (int i = 0; i < 10_000; i++)
        {
            ImmutableList<Integer> integers = multimap.get(i);
            Verify.assertSize(100, integers);
            Assert.assertEquals(Interval.fromToBy(i, 999_999, 10_000), integers);
        }
    }

    @Benchmark
    public UnifiedSetMultimap<Boolean, Integer> groupBy_2_keys_serial_eager_ec()
    {
        UnifiedSetMultimap<Boolean, Integer> multimap = this.integersEC.groupBy(each -> each % 2 == 0);
        Assert.assertEquals(2, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_2_keys_serial_eager_ec()
    {
        UnifiedSetMultimap<Boolean, Integer> multimap = this.groupBy_2_keys_serial_eager_ec();
        Set<Integer> odds = multimap.get(false);
        Set<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), evens);
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), odds);
    }

    @Benchmark
    public UnifiedSetMultimap<Integer, Integer> groupBy_100_keys_serial_eager_ec()
    {
        UnifiedSetMultimap<Integer, Integer> multimap = this.integersEC.groupBy(each -> each % 100);
        Assert.assertEquals(100, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_100_keys_serial_eager_ec()
    {
        UnifiedSetMultimap<Integer, Integer> multimap = this.groupBy_100_keys_serial_eager_ec();
        for (int i = 0; i < 100; i++)
        {
            MutableSet<Integer> integers = multimap.get(i);
            Verify.assertSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), integers);
        }
    }

    @Benchmark
    public UnifiedSetMultimap<Integer, Integer> groupBy_10000_keys_serial_eager_ec()
    {
        UnifiedSetMultimap<Integer, Integer> multimap = this.integersEC.groupBy(each -> each % 10_000);
        Assert.assertEquals(10_000, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_10000_keys_serial_eager_ec()
    {
        UnifiedSetMultimap<Integer, Integer> multimap = this.groupBy_10000_keys_serial_eager_ec();
        for (int i = 0; i < 10_000; i++)
        {
            Set<Integer> integers = multimap.get(i);
            Verify.assertSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), integers);
        }
    }

    @Benchmark
    public Multimap<Boolean, Integer> groupBy_unordered_lists_2_keys_serial_lazy_ec()
    {
        Multimap<Boolean, Integer> multimap = this.integersEC.asLazy().groupBy(each -> each % 2 == 0);
        Assert.assertEquals(2, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_unordered_lists_2_keys_serial_lazy_ec()
    {
        Multimap<Boolean, Integer> multimap = this.groupBy_unordered_lists_2_keys_serial_lazy_ec();
        RichIterable<Integer> odds = multimap.get(false);
        RichIterable<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), evens.toSet());
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), odds.toSet());
    }

    @Benchmark
    public Multimap<Integer, Integer> groupBy_unordered_lists_100_keys_serial_lazy_ec()
    {
        Multimap<Integer, Integer> multimap = this.integersEC.asLazy().groupBy(each -> each % 100);
        Assert.assertEquals(100, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_unordered_lists_100_keys_serial_lazy_ec()
    {
        Multimap<Integer, Integer> multimap = this.groupBy_unordered_lists_100_keys_serial_lazy_ec();
        for (int i = 0; i < 100; i++)
        {
            RichIterable<Integer> integers = multimap.get(i);
            Verify.assertIterableSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), integers.toSet());
        }
    }

    @Benchmark
    public Multimap<Integer, Integer> groupBy_unordered_lists_10000_keys_serial_lazy_ec()
    {
        Multimap<Integer, Integer> multimap = this.integersEC.asLazy().groupBy(each -> each % 10_000);
        Assert.assertEquals(10_000, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_unordered_lists_10000_keys_serial_lazy_ec()
    {
        Multimap<Integer, Integer> multimap = this.groupBy_unordered_lists_10000_keys_serial_lazy_ec();
        for (int i = 0; i < 10_000; i++)
        {
            RichIterable<Integer> integers = multimap.get(i);
            Verify.assertIterableSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), integers.toSet());
        }
    }

    @Benchmark
    public UnsortedSetMultimap<Boolean, Integer> groupBy_2_keys_parallel_lazy_ec()
    {
        UnsortedSetMultimap<Boolean, Integer> multimap = this.integersEC.asParallel(this.executorService, BATCH_SIZE).groupBy(each -> each % 2 == 0);
        Assert.assertEquals(2, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_2_keys_parallel_lazy_ec()
    {
        UnsortedSetMultimap<Boolean, Integer> multimap = this.groupBy_2_keys_parallel_lazy_ec();
        UnsortedSetIterable<Integer> odds = multimap.get(false);
        UnsortedSetIterable<Integer> evens = multimap.get(true);
        Verify.assertSetsEqual(Interval.fromToBy(0, 999_999, 2).toSet(), (Set<?>) evens);
        Verify.assertSetsEqual(Interval.fromToBy(1, 999_999, 2).toSet(), (Set<?>) odds);
    }

    @Benchmark
    public UnsortedSetMultimap<Integer, Integer> groupBy_100_keys_parallel_lazy_ec()
    {
        UnsortedSetMultimap<Integer, Integer> multimap = this.integersEC.asParallel(this.executorService, BATCH_SIZE).groupBy(each -> each % 100);
        Assert.assertEquals(100, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_100_keys_parallel_lazy_ec()
    {
        UnsortedSetMultimap<Integer, Integer> multimap = this.groupBy_100_keys_parallel_lazy_ec();
        for (int i = 0; i < 100; i++)
        {
            UnsortedSetIterable<Integer> integers = multimap.get(i);
            Verify.assertIterableSize(10_000, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 100).toSet(), (Set<?>) integers);
        }
    }

    @Benchmark
    public UnsortedSetMultimap<Integer, Integer> groupBy_10000_keys_parallel_lazy_ec()
    {
        UnsortedSetMultimap<Integer, Integer> multimap = this.integersEC.asParallel(this.executorService, BATCH_SIZE).groupBy(each -> each % 10_000);
        Assert.assertEquals(10_000, multimap.sizeDistinct());
        return multimap;
    }

    @Test
    public void test_groupBy_10000_keys_parallel_lazy_ec()
    {
        UnsortedSetMultimap<Integer, Integer> multimap = this.groupBy_10000_keys_parallel_lazy_ec();
        for (int i = 0; i < 10_000; i++)
        {
            UnsortedSetIterable<Integer> integers = multimap.get(i);
            Verify.assertIterableSize(100, integers);
            Verify.assertSetsEqual(Interval.fromToBy(i, 999_999, 10_000).toSet(), (Set<?>) integers);
        }
    }

    @Benchmark
    public void groupBy_2_keys_serial_eager_scala()
    {
        GroupBySetScalaTest.groupBy_2_keys_serial_eager_scala();
    }

    @Test
    public void test_groupBy_2_keys_serial_eager_scala()
    {
        GroupBySetScalaTest.test_groupBy_2_keys_serial_eager_scala();
    }

    @Benchmark
    public void groupBy_100_keys_serial_eager_scala()
    {
        GroupBySetScalaTest.groupBy_100_keys_serial_eager_scala();
    }

    @Test
    public void test_groupBy_100_keys_serial_eager_scala()
    {
        GroupBySetScalaTest.test_groupBy_100_keys_serial_eager_scala();
    }

    @Benchmark
    public void groupBy_10000_keys_serial_eager_scala()
    {
        GroupBySetScalaTest.groupBy_10000_keys_serial_eager_scala();
    }

    @Test
    public void test_groupBy_10000_keys_serial_eager_scala()
    {
        GroupBySetScalaTest.test_groupBy_10000_keys_serial_eager_scala();
    }

    @Benchmark
    public void groupBy_2_keys_serial_lazy_scala()
    {
        GroupBySetScalaTest.groupBy_unordered_lists_2_keys_serial_lazy_scala();
    }

    @Test
    public void test_groupBy_unordered_lists_2_keys_serial_lazy_scala()
    {
        GroupBySetScalaTest.test_groupBy_unordered_lists_2_keys_serial_lazy_scala();
    }

    @Benchmark
    public void groupBy_100_keys_serial_lazy_scala()
    {
        GroupBySetScalaTest.groupBy_unordered_lists_100_keys_serial_lazy_scala();
    }

    @Test
    public void test_groupBy_unordered_lists_100_keys_serial_lazy_scala()
    {
        GroupBySetScalaTest.test_groupBy_unordered_lists_100_keys_serial_lazy_scala();
    }

    @Benchmark
    public void groupBy_10000_keys_serial_lazy_scala()
    {
        GroupBySetScalaTest.groupBy_unordered_lists_10000_keys_serial_lazy_scala();
    }

    @Test
    public void test_groupBy_unordered_lists_10000_keys_serial_lazy_scala()
    {
        GroupBySetScalaTest.test_groupBy_unordered_lists_10000_keys_serial_lazy_scala();
    }

    @Benchmark
    public void groupBy_2_keys_parallel_lazy_scala()
    {
        GroupBySetScalaTest.groupBy_2_keys_parallel_lazy_scala();
    }

    @Test
    public void test_groupBy_2_keys_parallel_lazy_scala()
    {
        GroupBySetScalaTest.test_groupBy_2_keys_parallel_lazy_scala();
    }

    @Benchmark
    public void groupBy_100_keys_parallel_lazy_scala()
    {
        GroupBySetScalaTest.groupBy_100_keys_parallel_lazy_scala();
    }

    @Test
    public void test_groupBy_100_keys_parallel_lazy_scala()
    {
        GroupBySetScalaTest.test_groupBy_100_keys_parallel_lazy_scala();
    }

    @Benchmark
    public void groupBy_10000_keys_parallel_lazy_scala()
    {
        GroupBySetScalaTest.groupBy_10000_keys_parallel_lazy_scala();
    }

    @Test
    public void test_groupBy_10000_keys_parallel_lazy_scala()
    {
        GroupBySetScalaTest.test_groupBy_10000_keys_parallel_lazy_scala();
    }
}
```

### Method 82

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.impl.block.factory.Procedures;
import org.eclipse.collections.impl.block.procedure.CountProcedure;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class CountSetTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    @Param({"0", "1", "2", "3"})
    public int megamorphicWarmupLevel;

    private final Set<Integer> integersJDK = new HashSet<>(Interval.oneTo(SIZE));
    private final UnifiedSet<Integer> integersEC = new UnifiedSet<>(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Setup(Level.Trial)
    public void setUp_megamorphic()
    {
        if (this.megamorphicWarmupLevel > 0)
        {
            // serial, lazy, JDK
            {
                long evens = this.integersJDK.stream().filter(each -> each % 2 == 0).count();
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersJDK.stream().filter(each -> each % 2 == 1).count();
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersJDK.stream().filter(each -> (each & 1) == 0).count();
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // parallel, lazy, JDK
            {
                long evens = this.integersJDK.parallelStream().filter(each -> each % 2 == 0).count();
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersJDK.parallelStream().filter(each -> each % 2 == 1).count();
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersJDK.parallelStream().filter(each -> (each & 1) == 0).count();
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // serial, lazy, EC
            {
                long evens = this.integersEC.asLazy().count(each -> each % 2 == 0);
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersEC.asLazy().count(each -> each % 2 == 1);
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersEC.asLazy().count(each -> (each & 1) == 0);
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // parallel, lazy, EC
            {
                long evens = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> each % 2 == 0);
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> each % 2 == 1);
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> (each & 1) == 0);
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // serial, eager, EC
            {
                long evens = this.integersEC.count(each -> each % 2 == 0);
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersEC.count(each -> each % 2 == 1);
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersEC.count(each -> (each & 1) == 0);
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // parallel, eager, EC
            long evens = ParallelIterate.count(this.integersEC, each -> each % 2 == 0);
            Assert.assertEquals(SIZE / 2, evens);
            long odds = ParallelIterate.count(this.integersEC, each -> each % 2 == 1);
            Assert.assertEquals(SIZE / 2, odds);
            long evens2 = ParallelIterate.count(this.integersEC, each -> (each & 1) == 0);
            Assert.assertEquals(SIZE / 2, evens2);
        }

        if (this.megamorphicWarmupLevel > 1)
        {
            // stream().mapToLong().reduce()
            Assert.assertEquals(
                    500001500000L,
                    this.integersJDK.stream().mapToLong(each -> each + 1).reduce(0, (accum, each) -> accum + each));

            Assert.assertEquals(
                    500002500000L,
                    this.integersJDK.stream().mapToLong(each -> each + 2).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));

            Assert.assertEquals(
                    500003500000L,
                    this.integersJDK.stream().mapToLong(each -> each + 3).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));

            // parallelStream().mapToLong().reduce()
            Assert.assertEquals(
                    500001500000L,
                    this.integersJDK.parallelStream().mapToLong(each -> each + 1).reduce(0, (accum, each) -> accum + each));

            Assert.assertEquals(
                    500002500000L,
                    this.integersJDK.parallelStream().mapToLong(each -> each + 2).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));

            Assert.assertEquals(
                    500003500000L,
                    this.integersJDK.parallelStream().mapToLong(each -> each + 3).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));
        }

        if (this.megamorphicWarmupLevel > 2)
        {
            this.integersEC.asLazy().forEach(Procedures.cast(Assert::assertNotNull));
            this.integersEC.asLazy().forEach(Procedures.cast(each -> Assert.assertEquals(each, each)));
            this.integersEC.asLazy().forEach(new CountProcedure<>());

            this.integersEC.asParallel(this.executorService, BATCH_SIZE).forEach(Assert::assertNotNull);
            this.integersEC.asParallel(this.executorService, BATCH_SIZE).forEach(each -> Assert.assertEquals(each, each));
            this.integersEC.asParallel(this.executorService, BATCH_SIZE).forEach(new CountProcedure<>());

            this.integersJDK.stream().forEach(Assert::assertNotNull);
            this.integersJDK.stream().forEach(each -> Assert.assertEquals(each, each));

            this.integersJDK.parallelStream().forEach(Assert::assertNotNull);
            this.integersJDK.parallelStream().forEach(each -> Assert.assertEquals(each, each));
        }

        CountSetScalaTest.megamorphic(this.megamorphicWarmupLevel);
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        long evens = this.integersJDK.stream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        long evens = this.integersEC.stream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        long evens = this.integersJDK.parallelStream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        long evens = this.integersEC.parallelStream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_eager_ec()
    {
        int evens = this.integersEC.count(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_lazy_ec()
    {
        int evens = this.integersEC.asLazy().count(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        int evens = ParallelIterate.count(this.integersEC, each -> each % 2 == 0, BATCH_SIZE, this.executorService);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        int evens = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_eager_scala()
    {
        CountSetScalaTest.serial_eager_scala();
    }

    @Benchmark
    public void serial_lazy_scala()
    {
        CountSetScalaTest.serial_lazy_scala();
    }

    @Benchmark
    public void parallel_lazy_scala()
    {
        CountSetScalaTest.parallel_lazy_scala();
    }
}
```

### Method 83

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.impl.block.factory.Procedures;
import org.eclipse.collections.impl.block.procedure.CountProcedure;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.parallel.ParallelIterate;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.junit.Assert;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class CountSetTest
{
    private static final int SIZE = 1_000_000;
    private static final int BATCH_SIZE = 10_000;

    @Param({"0", "1", "2", "3"})
    public int megamorphicWarmupLevel;

    private final Set<Integer> integersJDK = new HashSet<>(Interval.oneTo(SIZE));
    private final UnifiedSet<Integer> integersEC = new UnifiedSet<>(Interval.oneTo(SIZE));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Setup(Level.Trial)
    public void setUp_megamorphic()
    {
        if (this.megamorphicWarmupLevel > 0)
        {
            // serial, lazy, JDK
            {
                long evens = this.integersJDK.stream().filter(each -> each % 2 == 0).count();
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersJDK.stream().filter(each -> each % 2 == 1).count();
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersJDK.stream().filter(each -> (each & 1) == 0).count();
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // parallel, lazy, JDK
            {
                long evens = this.integersJDK.parallelStream().filter(each -> each % 2 == 0).count();
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersJDK.parallelStream().filter(each -> each % 2 == 1).count();
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersJDK.parallelStream().filter(each -> (each & 1) == 0).count();
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // serial, lazy, EC
            {
                long evens = this.integersEC.asLazy().count(each -> each % 2 == 0);
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersEC.asLazy().count(each -> each % 2 == 1);
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersEC.asLazy().count(each -> (each & 1) == 0);
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // parallel, lazy, EC
            {
                long evens = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> each % 2 == 0);
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> each % 2 == 1);
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> (each & 1) == 0);
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // serial, eager, EC
            {
                long evens = this.integersEC.count(each -> each % 2 == 0);
                Assert.assertEquals(SIZE / 2, evens);
                long odds = this.integersEC.count(each -> each % 2 == 1);
                Assert.assertEquals(SIZE / 2, odds);
                long evens2 = this.integersEC.count(each -> (each & 1) == 0);
                Assert.assertEquals(SIZE / 2, evens2);
            }

            // parallel, eager, EC
            long evens = ParallelIterate.count(this.integersEC, each -> each % 2 == 0);
            Assert.assertEquals(SIZE / 2, evens);
            long odds = ParallelIterate.count(this.integersEC, each -> each % 2 == 1);
            Assert.assertEquals(SIZE / 2, odds);
            long evens2 = ParallelIterate.count(this.integersEC, each -> (each & 1) == 0);
            Assert.assertEquals(SIZE / 2, evens2);
        }

        if (this.megamorphicWarmupLevel > 1)
        {
            // stream().mapToLong().reduce()
            Assert.assertEquals(
                    500001500000L,
                    this.integersJDK.stream().mapToLong(each -> each + 1).reduce(0, (accum, each) -> accum + each));

            Assert.assertEquals(
                    500002500000L,
                    this.integersJDK.stream().mapToLong(each -> each + 2).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));

            Assert.assertEquals(
                    500003500000L,
                    this.integersJDK.stream().mapToLong(each -> each + 3).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));

            // parallelStream().mapToLong().reduce()
            Assert.assertEquals(
                    500001500000L,
                    this.integersJDK.parallelStream().mapToLong(each -> each + 1).reduce(0, (accum, each) -> accum + each));

            Assert.assertEquals(
                    500002500000L,
                    this.integersJDK.parallelStream().mapToLong(each -> each + 2).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));

            Assert.assertEquals(
                    500003500000L,
                    this.integersJDK.parallelStream().mapToLong(each -> each + 3).reduce(0, (accum, each) -> {
                        Assert.assertTrue(each >= 0);
                        return accum + each;
                    }));
        }

        if (this.megamorphicWarmupLevel > 2)
        {
            this.integersEC.asLazy().forEach(Procedures.cast(Assert::assertNotNull));
            this.integersEC.asLazy().forEach(Procedures.cast(each -> Assert.assertEquals(each, each)));
            this.integersEC.asLazy().forEach(new CountProcedure<>());

            this.integersEC.asParallel(this.executorService, BATCH_SIZE).forEach(Assert::assertNotNull);
            this.integersEC.asParallel(this.executorService, BATCH_SIZE).forEach(each -> Assert.assertEquals(each, each));
            this.integersEC.asParallel(this.executorService, BATCH_SIZE).forEach(new CountProcedure<>());

            this.integersJDK.stream().forEach(Assert::assertNotNull);
            this.integersJDK.stream().forEach(each -> Assert.assertEquals(each, each));

            this.integersJDK.parallelStream().forEach(Assert::assertNotNull);
            this.integersJDK.parallelStream().forEach(each -> Assert.assertEquals(each, each));
        }

        CountSetScalaTest.megamorphic(this.megamorphicWarmupLevel);
    }

    @Benchmark
    public void serial_lazy_jdk()
    {
        long evens = this.integersJDK.stream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_lazy_streams_ec()
    {
        long evens = this.integersEC.stream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_lazy_jdk()
    {
        long evens = this.integersJDK.parallelStream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_lazy_streams_ec()
    {
        long evens = this.integersEC.parallelStream().filter(each -> each % 2 == 0).count();
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_eager_ec()
    {
        int evens = this.integersEC.count(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_lazy_ec()
    {
        int evens = this.integersEC.asLazy().count(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_eager_ec()
    {
        int evens = ParallelIterate.count(this.integersEC, each -> each % 2 == 0, BATCH_SIZE, this.executorService);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void parallel_lazy_ec()
    {
        int evens = this.integersEC.asParallel(this.executorService, BATCH_SIZE).count(each -> each % 2 == 0);
        Assert.assertEquals(SIZE / 2, evens);
    }

    @Benchmark
    public void serial_eager_scala()
    {
        CountSetScalaTest.serial_eager_scala();
    }

    @Benchmark
    public void serial_lazy_scala()
    {
        CountSetScalaTest.serial_lazy_scala();
    }

    @Benchmark
    public void parallel_lazy_scala()
    {
        CountSetScalaTest.parallel_lazy_scala();
    }
}
```

### Method 84

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.TimeUnit;

import org.eclipse.collections.api.set.MutableSet;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.eclipse.collections.impl.set.mutable.UnifiedSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class SetAddAllTest
{
    private static final int SIZE = 1000;
    private final Set<Integer> integersJDK = new HashSet<>(Interval.oneTo(SIZE));
    private final MutableSet<Integer> integersEC = Interval.oneTo(SIZE).toSet();

    @Benchmark
    public void jdk()
    {
        Set<Integer> result = new HashSet<>();
        for (int i = 0; i < 1000; i++)
        {
            result.addAll(this.integersJDK);
        }
    }

    @Benchmark
    public void ec()
    {
        MutableSet<Integer> result = UnifiedSet.newSet();
        for (int i = 0; i < 1000; i++)
        {
            result.addAll(this.integersEC);
        }
    }
}
```

### Method 85

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class SumOfDoubleTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;
    private static final Stream<Double> DOUBLES = new Random().doubles(1.0d, 100.0d).boxed();

    private final List<Double> doublesJDK = DOUBLES.limit(SIZE).collect(Collectors.toList());
    private final MutableList<Double> doublesEC = FastList.newListWith(this.doublesJDK.toArray(new Double[SIZE]));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public double serial_lazy_collectDoubleSum_jdk()
    {
        return this.doublesJDK.stream().mapToDouble(each -> each).sum();
    }

    @Benchmark
    public double serial_lazy_collectDoubleSum_streams_ec()
    {
        return this.doublesEC.stream().mapToDouble(each -> each).sum();
    }

    @Benchmark
    public double parallel_lazy_collectDoubleSum_jdk()
    {
        return this.doublesJDK.parallelStream().mapToDouble(each -> each).sum();
    }

    @Benchmark
    public double parallel_lazy_collectDoubleSum_streams_ec()
    {
        return this.doublesEC.parallelStream().mapToDouble(each -> each).sum();
    }

    @Benchmark
    public double serial_eager_directSumOfDouble_ec()
    {
        return this.doublesEC.sumOfDouble(each -> each);
    }

    @Benchmark
    public double serial_eager_collectDoubleSum_ec()
    {
        return this.doublesEC.collectDouble(each -> each).sum();
    }

    @Benchmark
    public double serial_lazy_collectDoubleSum_ec()
    {
        return this.doublesEC.asLazy().collectDouble(each -> each).sum();
    }

    @Benchmark
    public double parallel_lazy_directSumOfDouble_ec()
    {
        return this.doublesEC.asParallel(this.executorService, BATCH_SIZE).sumOfDouble(Double::doubleValue);
    }

    @Benchmark
    public double serial_lazy_directSumOfDouble_ec()
    {
        return this.doublesEC.asLazy().sumOfDouble(each -> each);
    }
}
```

### Method 86

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.eclipse.collections.api.list.MutableList;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.FastList;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.TearDown;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class SumOfDoubleTest
{
    private static final int SIZE = 3_000_000;
    private static final int BATCH_SIZE = 10_000;
    private static final Stream<Double> DOUBLES = new Random().doubles(1.0d, 100.0d).boxed();

    private final List<Double> doublesJDK = DOUBLES.limit(SIZE).collect(Collectors.toList());
    private final MutableList<Double> doublesEC = FastList.newListWith(this.doublesJDK.toArray(new Double[SIZE]));

    private ExecutorService executorService;

    @Setup
    public void setUp()
    {
        this.executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @TearDown
    public void tearDown() throws InterruptedException
    {
        this.executorService.shutdownNow();
        this.executorService.awaitTermination(1L, TimeUnit.SECONDS);
    }

    @Benchmark
    public double serial_lazy_collectDoubleSum_jdk()
    {
        return this.doublesJDK.stream().mapToDouble(each -> each).sum();
    }

    @Benchmark
    public double serial_lazy_collectDoubleSum_streams_ec()
    {
        return this.doublesEC.stream().mapToDouble(each -> each).sum();
    }

    @Benchmark
    public double parallel_lazy_collectDoubleSum_jdk()
    {
        return this.doublesJDK.parallelStream().mapToDouble(each -> each).sum();
    }

    @Benchmark
    public double parallel_lazy_collectDoubleSum_streams_ec()
    {
        return this.doublesEC.parallelStream().mapToDouble(each -> each).sum();
    }

    @Benchmark
    public double serial_eager_directSumOfDouble_ec()
    {
        return this.doublesEC.sumOfDouble(each -> each);
    }

    @Benchmark
    public double serial_eager_collectDoubleSum_ec()
    {
        return this.doublesEC.collectDouble(each -> each).sum();
    }

    @Benchmark
    public double serial_lazy_collectDoubleSum_ec()
    {
        return this.doublesEC.asLazy().collectDouble(each -> each).sum();
    }

    @Benchmark
    public double parallel_lazy_directSumOfDouble_ec()
    {
        return this.doublesEC.asParallel(this.executorService, BATCH_SIZE).sumOfDouble(Double::doubleValue);
    }

    @Benchmark
    public double serial_lazy_directSumOfDouble_ec()
    {
        return this.doublesEC.asLazy().sumOfDouble(each -> each);
    }
}
```

### Method 87

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.LongLongMap;
import com.koloboke.collect.map.hash.HashLongLongMaps;
import org.eclipse.collections.api.list.primitive.MutableLongList;
import org.eclipse.collections.api.map.primitive.MutableLongLongMap;
import org.eclipse.collections.api.set.primitive.MutableLongSet;
import org.eclipse.collections.impl.SpreadFunctions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.primitive.LongArrayList;
import org.eclipse.collections.impl.map.mutable.primitive.LongLongHashMap;
import org.eclipse.collections.impl.set.mutable.primitive.LongHashSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class LongLongMapSmallStressTest
{
    private static final int LOOP_COUNT = 100;
    private static final int KEY_COUNT = 500;
    private static final int MAP_SIZE = 1_000;

    @Param({"true", "false"})
    public boolean fullyRandom;
    private LongLongMap longLongKoloboke;
    private MutableLongLongMap longLongEc;
    private long[] ecLongKeysForMap;
    private long[] kolobokeLongKeysForMap;

    private int kolobokeIndex(int key)
    {
        long h = key * 0x9e3779b97f4a7c15L;
        h ^= h >> 32;
        return this.mask((int) (h ^ (h >> 16)));
    }

    private int ecIndex(int element)
    {
        return this.mask(element);
    }

    private int ecIndexTwo(int element)
    {
        return this.mask((int) SpreadFunctions.longSpreadTwo(element));
    }

    private int mask(int spread)
    {
        return spread & ((1 << 11) - 1);
    }

    @Setup
    public void setUp()
    {
        this.longLongKoloboke = HashLongLongMaps.newMutableMap(MAP_SIZE);
        this.longLongEc = new LongLongHashMap(MAP_SIZE);

        Random random = new Random(0x123456789ABCDL);

        int number = 23;
        int lower = Integer.MIN_VALUE;
        int upper = Integer.MAX_VALUE;

        long[] randomNumbersForMap = this.getRandomKeys(random).toArray();

        this.ecLongKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getECArray(number, lower, upper, random);
        this.kolobokeLongKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getKolobokeArray(number, lower, upper, random);

        for (int i = 0; i < KEY_COUNT; i++)
        {
            this.longLongKoloboke.put(this.kolobokeLongKeysForMap[i], 5);
            this.longLongEc.put(this.ecLongKeysForMap[i], 5);
        }

        this.shuffle(this.ecLongKeysForMap, random);
        this.shuffle(this.kolobokeLongKeysForMap, random);
    }

    private MutableLongSet getRandomKeys(Random random)
    {
        MutableLongSet set = new LongHashSet(KEY_COUNT);
        while (set.size() < KEY_COUNT)
        {
            set.add(random.nextLong());
        }
        return set;
    }

    protected long[] getECArray(int number, int lower, int upper, Random random)
    {
        long[] ecCollisions = this.getECSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(ecCollisions, random);
        return ecCollisions;
    }

    private MutableLongList getECSequenceCollisions(int number, int lower, int upper)
    {
        MutableLongList ecCollidingNumbers = new LongArrayList();
        for (int i = lower; i < upper && ecCollidingNumbers.size() < KEY_COUNT; i++)
        {
            if (this.ecIndex(i) - this.ecIndex(number) >= 0 && this.ecIndex(i) - this.ecIndex(number) < 10
                    && (this.ecIndexTwo(i) - this.ecIndexTwo(number) >= 0) && (this.ecIndexTwo(i) - this.ecIndexTwo(number) < 10))
            {
                ecCollidingNumbers.add(i);
            }
        }
        return ecCollidingNumbers;
    }

    protected long[] getKolobokeArray(int number, int lower, int upper, Random random)
    {
        long[] kolobokeCollisions = this.getKolobokeSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(kolobokeCollisions, random);
        return kolobokeCollisions;
    }

    private MutableLongList getKolobokeSequenceCollisions(int number, int lower, int upper)
    {
        MutableLongList kolobokeCollidingNumbers = new LongArrayList();
        for (int i = lower; i < upper && kolobokeCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.kolobokeIndex(i);
            if (index >= number && index <= number + 100)
            {
                kolobokeCollidingNumbers.add(i);
            }
        }
        return kolobokeCollidingNumbers;
    }

    @Benchmark
    public void kolobokeGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.longLongKoloboke.get(this.kolobokeLongKeysForMap[i]) == this.longLongKoloboke.defaultValue())
                {
                    throw new AssertionError(this.kolobokeLongKeysForMap[i] + " not in map");
                }
            }
            if (this.longLongKoloboke.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.longLongKoloboke.size());
            }
        }
    }

    @Benchmark
    public void ecGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.longLongEc.get(this.ecLongKeysForMap[i]) == 0)
                {
                    throw new AssertionError(this.ecLongKeysForMap[i] + " not in map");
                }
            }
            if (this.longLongEc.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.longLongEc.size());
            }
        }
    }

    @Benchmark
    public void kolobokePut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.kolobokeLongKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableLongLongMap newMap = new LongLongHashMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.ecLongKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableLongLongMap newMap = new LongLongHashMap(this.longLongEc);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.ecLongKeysForMap[i]);
            }
            if (newMap.notEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokeRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.kolobokeLongKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    public void shuffle(long[] array, Random rnd)
    {
        for (int i = array.length; i > 1; i--)
        {
            LongLongMapSmallStressTest.swap(array, i - 1, rnd.nextInt(i));
        }
    }

    private static void swap(long[] arr, int i, int j)
    {
        long tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
```

### Method 88

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.LongLongMap;
import com.koloboke.collect.map.hash.HashLongLongMaps;
import org.eclipse.collections.api.list.primitive.MutableLongList;
import org.eclipse.collections.api.map.primitive.MutableLongLongMap;
import org.eclipse.collections.api.set.primitive.MutableLongSet;
import org.eclipse.collections.impl.SpreadFunctions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.primitive.LongArrayList;
import org.eclipse.collections.impl.map.mutable.primitive.LongLongHashMap;
import org.eclipse.collections.impl.set.mutable.primitive.LongHashSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class LongLongMapSmallStressTest
{
    private static final int LOOP_COUNT = 100;
    private static final int KEY_COUNT = 500;
    private static final int MAP_SIZE = 1_000;

    @Param({"true", "false"})
    public boolean fullyRandom;
    private LongLongMap longLongKoloboke;
    private MutableLongLongMap longLongEc;
    private long[] ecLongKeysForMap;
    private long[] kolobokeLongKeysForMap;

    private int kolobokeIndex(int key)
    {
        long h = key * 0x9e3779b97f4a7c15L;
        h ^= h >> 32;
        return this.mask((int) (h ^ (h >> 16)));
    }

    private int ecIndex(int element)
    {
        return this.mask(element);
    }

    private int ecIndexTwo(int element)
    {
        return this.mask((int) SpreadFunctions.longSpreadTwo(element));
    }

    private int mask(int spread)
    {
        return spread & ((1 << 11) - 1);
    }

    @Setup
    public void setUp()
    {
        this.longLongKoloboke = HashLongLongMaps.newMutableMap(MAP_SIZE);
        this.longLongEc = new LongLongHashMap(MAP_SIZE);

        Random random = new Random(0x123456789ABCDL);

        int number = 23;
        int lower = Integer.MIN_VALUE;
        int upper = Integer.MAX_VALUE;

        long[] randomNumbersForMap = this.getRandomKeys(random).toArray();

        this.ecLongKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getECArray(number, lower, upper, random);
        this.kolobokeLongKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getKolobokeArray(number, lower, upper, random);

        for (int i = 0; i < KEY_COUNT; i++)
        {
            this.longLongKoloboke.put(this.kolobokeLongKeysForMap[i], 5);
            this.longLongEc.put(this.ecLongKeysForMap[i], 5);
        }

        this.shuffle(this.ecLongKeysForMap, random);
        this.shuffle(this.kolobokeLongKeysForMap, random);
    }

    private MutableLongSet getRandomKeys(Random random)
    {
        MutableLongSet set = new LongHashSet(KEY_COUNT);
        while (set.size() < KEY_COUNT)
        {
            set.add(random.nextLong());
        }
        return set;
    }

    protected long[] getECArray(int number, int lower, int upper, Random random)
    {
        long[] ecCollisions = this.getECSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(ecCollisions, random);
        return ecCollisions;
    }

    private MutableLongList getECSequenceCollisions(int number, int lower, int upper)
    {
        MutableLongList ecCollidingNumbers = new LongArrayList();
        for (int i = lower; i < upper && ecCollidingNumbers.size() < KEY_COUNT; i++)
        {
            if (this.ecIndex(i) - this.ecIndex(number) >= 0 && this.ecIndex(i) - this.ecIndex(number) < 10
                    && (this.ecIndexTwo(i) - this.ecIndexTwo(number) >= 0) && (this.ecIndexTwo(i) - this.ecIndexTwo(number) < 10))
            {
                ecCollidingNumbers.add(i);
            }
        }
        return ecCollidingNumbers;
    }

    protected long[] getKolobokeArray(int number, int lower, int upper, Random random)
    {
        long[] kolobokeCollisions = this.getKolobokeSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(kolobokeCollisions, random);
        return kolobokeCollisions;
    }

    private MutableLongList getKolobokeSequenceCollisions(int number, int lower, int upper)
    {
        MutableLongList kolobokeCollidingNumbers = new LongArrayList();
        for (int i = lower; i < upper && kolobokeCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.kolobokeIndex(i);
            if (index >= number && index <= number + 100)
            {
                kolobokeCollidingNumbers.add(i);
            }
        }
        return kolobokeCollidingNumbers;
    }

    @Benchmark
    public void kolobokeGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.longLongKoloboke.get(this.kolobokeLongKeysForMap[i]) == this.longLongKoloboke.defaultValue())
                {
                    throw new AssertionError(this.kolobokeLongKeysForMap[i] + " not in map");
                }
            }
            if (this.longLongKoloboke.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.longLongKoloboke.size());
            }
        }
    }

    @Benchmark
    public void ecGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.longLongEc.get(this.ecLongKeysForMap[i]) == 0)
                {
                    throw new AssertionError(this.ecLongKeysForMap[i] + " not in map");
                }
            }
            if (this.longLongEc.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.longLongEc.size());
            }
        }
    }

    @Benchmark
    public void kolobokePut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.kolobokeLongKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableLongLongMap newMap = new LongLongHashMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.ecLongKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableLongLongMap newMap = new LongLongHashMap(this.longLongEc);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.ecLongKeysForMap[i]);
            }
            if (newMap.notEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokeRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.kolobokeLongKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    public void shuffle(long[] array, Random rnd)
    {
        for (int i = array.length; i > 1; i--)
        {
            LongLongMapSmallStressTest.swap(array, i - 1, rnd.nextInt(i));
        }
    }

    private static void swap(long[] arr, int i, int j)
    {
        long tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
```

### Method 89

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.LongLongMap;
import com.koloboke.collect.map.hash.HashLongLongMaps;
import org.eclipse.collections.api.list.primitive.MutableLongList;
import org.eclipse.collections.api.map.primitive.MutableLongLongMap;
import org.eclipse.collections.api.set.primitive.MutableLongSet;
import org.eclipse.collections.impl.SpreadFunctions;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.primitive.LongArrayList;
import org.eclipse.collections.impl.map.mutable.primitive.LongLongHashMap;
import org.eclipse.collections.impl.set.mutable.primitive.LongHashSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class LongLongMapSmallStressTest
{
    private static final int LOOP_COUNT = 100;
    private static final int KEY_COUNT = 500;
    private static final int MAP_SIZE = 1_000;

    @Param({"true", "false"})
    public boolean fullyRandom;
    private LongLongMap longLongKoloboke;
    private MutableLongLongMap longLongEc;
    private long[] ecLongKeysForMap;
    private long[] kolobokeLongKeysForMap;

    private int kolobokeIndex(int key)
    {
        long h = key * 0x9e3779b97f4a7c15L;
        h ^= h >> 32;
        return this.mask((int) (h ^ (h >> 16)));
    }

    private int ecIndex(int element)
    {
        return this.mask(element);
    }

    private int ecIndexTwo(int element)
    {
        return this.mask((int) SpreadFunctions.longSpreadTwo(element));
    }

    private int mask(int spread)
    {
        return spread & ((1 << 11) - 1);
    }

    @Setup
    public void setUp()
    {
        this.longLongKoloboke = HashLongLongMaps.newMutableMap(MAP_SIZE);
        this.longLongEc = new LongLongHashMap(MAP_SIZE);

        Random random = new Random(0x123456789ABCDL);

        int number = 23;
        int lower = Integer.MIN_VALUE;
        int upper = Integer.MAX_VALUE;

        long[] randomNumbersForMap = this.getRandomKeys(random).toArray();

        this.ecLongKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getECArray(number, lower, upper, random);
        this.kolobokeLongKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getKolobokeArray(number, lower, upper, random);

        for (int i = 0; i < KEY_COUNT; i++)
        {
            this.longLongKoloboke.put(this.kolobokeLongKeysForMap[i], 5);
            this.longLongEc.put(this.ecLongKeysForMap[i], 5);
        }

        this.shuffle(this.ecLongKeysForMap, random);
        this.shuffle(this.kolobokeLongKeysForMap, random);
    }

    private MutableLongSet getRandomKeys(Random random)
    {
        MutableLongSet set = new LongHashSet(KEY_COUNT);
        while (set.size() < KEY_COUNT)
        {
            set.add(random.nextLong());
        }
        return set;
    }

    protected long[] getECArray(int number, int lower, int upper, Random random)
    {
        long[] ecCollisions = this.getECSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(ecCollisions, random);
        return ecCollisions;
    }

    private MutableLongList getECSequenceCollisions(int number, int lower, int upper)
    {
        MutableLongList ecCollidingNumbers = new LongArrayList();
        for (int i = lower; i < upper && ecCollidingNumbers.size() < KEY_COUNT; i++)
        {
            if (this.ecIndex(i) - this.ecIndex(number) >= 0 && this.ecIndex(i) - this.ecIndex(number) < 10
                    && (this.ecIndexTwo(i) - this.ecIndexTwo(number) >= 0) && (this.ecIndexTwo(i) - this.ecIndexTwo(number) < 10))
            {
                ecCollidingNumbers.add(i);
            }
        }
        return ecCollidingNumbers;
    }

    protected long[] getKolobokeArray(int number, int lower, int upper, Random random)
    {
        long[] kolobokeCollisions = this.getKolobokeSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(kolobokeCollisions, random);
        return kolobokeCollisions;
    }

    private MutableLongList getKolobokeSequenceCollisions(int number, int lower, int upper)
    {
        MutableLongList kolobokeCollidingNumbers = new LongArrayList();
        for (int i = lower; i < upper && kolobokeCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.kolobokeIndex(i);
            if (index >= number && index <= number + 100)
            {
                kolobokeCollidingNumbers.add(i);
            }
        }
        return kolobokeCollidingNumbers;
    }

    @Benchmark
    public void kolobokeGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.longLongKoloboke.get(this.kolobokeLongKeysForMap[i]) == this.longLongKoloboke.defaultValue())
                {
                    throw new AssertionError(this.kolobokeLongKeysForMap[i] + " not in map");
                }
            }
            if (this.longLongKoloboke.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.longLongKoloboke.size());
            }
        }
    }

    @Benchmark
    public void ecGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.longLongEc.get(this.ecLongKeysForMap[i]) == 0)
                {
                    throw new AssertionError(this.ecLongKeysForMap[i] + " not in map");
                }
            }
            if (this.longLongEc.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.longLongEc.size());
            }
        }
    }

    @Benchmark
    public void kolobokePut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.kolobokeLongKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableLongLongMap newMap = new LongLongHashMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.ecLongKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableLongLongMap newMap = new LongLongHashMap(this.longLongEc);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.ecLongKeysForMap[i]);
            }
            if (newMap.notEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokeRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.kolobokeLongKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    public void shuffle(long[] array, Random rnd)
    {
        for (int i = array.length; i > 1; i--)
        {
            LongLongMapSmallStressTest.swap(array, i - 1, rnd.nextInt(i));
        }
    }

    private static void swap(long[] arr, int i, int j)
    {
        long tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
```

### Method 90

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.LongLongMap;
import com.koloboke.collect.map.hash.HashLongLongMaps;
import org.eclipse.collections.api.list.primitive.MutableLongList;
import org.eclipse.collections.api.map.primitive.MutableLongLongMap;
import org.eclipse.collections.api.set.primitive.MutableLongSet;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.primitive.LongArrayList;
import org.eclipse.collections.impl.map.mutable.primitive.LongLongHashMap;
import org.eclipse.collections.impl.set.mutable.primitive.LongHashSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class LongLongMapLargeStressTest
{
    private static final int LOOP_COUNT = 1;
    private static final int KEY_COUNT = 400_000;
    private static final int MAP_SIZE = 1_000_000;

    @Param({"true", "false"})
    public boolean fullyRandom;
    private LongLongMap longLongKoloboke;
    private MutableLongLongMap longLongEc;
    private long[] ecLongKeysForMap;
    private long[] kolobokeLongKeysForMap;

    private int kolobokeIndex(int key)
    {
        long h = key * 0x9e3779b97f4a7c15L;
        h ^= h >> 32;
        return this.mask((int) (h ^ (h >> 16)));
    }

    private int ecIndex(int element)
    {
        return this.mask(element);
    }

    private int mask(int spread)
    {
        return spread & ((1 << 20) - 1);
    }

    @Setup
    public void setUp()
    {
        this.longLongKoloboke = HashLongLongMaps.newMutableMap(MAP_SIZE);
        this.longLongEc = new LongLongHashMap(MAP_SIZE);

        Random random = new Random(0x123456789ABCDL);

        int number = 23;
        int lower = Integer.MIN_VALUE;
        int upper = Integer.MAX_VALUE;

        long[] randomNumbersForMap = this.getRandomKeys(random).toArray();

        this.ecLongKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getECArray(number, lower, upper, random);
        this.kolobokeLongKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getKolobokeArray(number, lower, upper, random);

        for (int i = 0; i < KEY_COUNT; i++)
        {
            this.longLongKoloboke.put(this.kolobokeLongKeysForMap[i], 5);
            this.longLongEc.put(this.ecLongKeysForMap[i], 5);
        }

        this.shuffle(this.ecLongKeysForMap, random);
        this.shuffle(this.kolobokeLongKeysForMap, random);
    }

    private MutableLongSet getRandomKeys(Random random)
    {
        MutableLongSet set = new LongHashSet(KEY_COUNT);
        while (set.size() < KEY_COUNT)
        {
            set.add(random.nextLong());
        }
        return set;
    }

    protected long[] getECArray(int number, int lower, int upper, Random random)
    {
        long[] ecCollisions = this.getECSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(ecCollisions, random);
        return ecCollisions;
    }

    private MutableLongList getECSequenceCollisions(int number, int lower, int upper)
    {
        MutableLongList ecCollidingNumbers = new LongArrayList();
        for (int i = lower; i < upper && ecCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.ecIndex(i);
            if (index >= number && index <= number + 100)
            {
                ecCollidingNumbers.add(i);
            }
        }
        return ecCollidingNumbers;
    }

    protected long[] getKolobokeArray(int number, int lower, int upper, Random random)
    {
        long[] kolobokeCollisions = this.getKolobokeSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(kolobokeCollisions, random);
        return kolobokeCollisions;
    }

    private MutableLongList getKolobokeSequenceCollisions(int number, int lower, int upper)
    {
        MutableLongList kolobokeCollidingNumbers = new LongArrayList();
        for (int i = lower; i < upper && kolobokeCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.kolobokeIndex(i);
            if (index >= number && index <= number + 100)
            {
                kolobokeCollidingNumbers.add(i);
            }
        }
        return kolobokeCollidingNumbers;
    }

    @Benchmark
    public void kolobokeGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.longLongKoloboke.get(this.kolobokeLongKeysForMap[i]) == this.longLongKoloboke.defaultValue())
                {
                    throw new AssertionError(this.kolobokeLongKeysForMap[i] + " not in map");
                }
            }
            if (this.longLongKoloboke.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.longLongKoloboke.size());
            }
        }
    }

    @Benchmark
    public void ecGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.longLongEc.get(this.ecLongKeysForMap[i]) == 0)
                {
                    throw new AssertionError(this.ecLongKeysForMap[i] + " not in map");
                }
            }
            if (this.longLongEc.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.longLongEc.size());
            }
        }
    }

    @Benchmark
    public void kolobokePut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.kolobokeLongKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableLongLongMap newMap = new LongLongHashMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.ecLongKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableLongLongMap newMap = new LongLongHashMap(this.longLongEc);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.ecLongKeysForMap[i]);
            }
            if (newMap.notEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokeRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.kolobokeLongKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    public void shuffle(long[] array, Random rnd)
    {
        for (int i = array.length; i > 1; i--)
        {
            LongLongMapLargeStressTest.swap(array, i - 1, rnd.nextInt(i));
        }
    }

    private static void swap(long[] arr, int i, int j)
    {
        long tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
```

### Method 91

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.LongLongMap;
import com.koloboke.collect.map.hash.HashLongLongMaps;
import org.eclipse.collections.api.list.primitive.MutableLongList;
import org.eclipse.collections.api.map.primitive.MutableLongLongMap;
import org.eclipse.collections.api.set.primitive.MutableLongSet;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.primitive.LongArrayList;
import org.eclipse.collections.impl.map.mutable.primitive.LongLongHashMap;
import org.eclipse.collections.impl.set.mutable.primitive.LongHashSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class LongLongMapLargeStressTest
{
    private static final int LOOP_COUNT = 1;
    private static final int KEY_COUNT = 400_000;
    private static final int MAP_SIZE = 1_000_000;

    @Param({"true", "false"})
    public boolean fullyRandom;
    private LongLongMap longLongKoloboke;
    private MutableLongLongMap longLongEc;
    private long[] ecLongKeysForMap;
    private long[] kolobokeLongKeysForMap;

    private int kolobokeIndex(int key)
    {
        long h = key * 0x9e3779b97f4a7c15L;
        h ^= h >> 32;
        return this.mask((int) (h ^ (h >> 16)));
    }

    private int ecIndex(int element)
    {
        return this.mask(element);
    }

    private int mask(int spread)
    {
        return spread & ((1 << 20) - 1);
    }

    @Setup
    public void setUp()
    {
        this.longLongKoloboke = HashLongLongMaps.newMutableMap(MAP_SIZE);
        this.longLongEc = new LongLongHashMap(MAP_SIZE);

        Random random = new Random(0x123456789ABCDL);

        int number = 23;
        int lower = Integer.MIN_VALUE;
        int upper = Integer.MAX_VALUE;

        long[] randomNumbersForMap = this.getRandomKeys(random).toArray();

        this.ecLongKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getECArray(number, lower, upper, random);
        this.kolobokeLongKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getKolobokeArray(number, lower, upper, random);

        for (int i = 0; i < KEY_COUNT; i++)
        {
            this.longLongKoloboke.put(this.kolobokeLongKeysForMap[i], 5);
            this.longLongEc.put(this.ecLongKeysForMap[i], 5);
        }

        this.shuffle(this.ecLongKeysForMap, random);
        this.shuffle(this.kolobokeLongKeysForMap, random);
    }

    private MutableLongSet getRandomKeys(Random random)
    {
        MutableLongSet set = new LongHashSet(KEY_COUNT);
        while (set.size() < KEY_COUNT)
        {
            set.add(random.nextLong());
        }
        return set;
    }

    protected long[] getECArray(int number, int lower, int upper, Random random)
    {
        long[] ecCollisions = this.getECSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(ecCollisions, random);
        return ecCollisions;
    }

    private MutableLongList getECSequenceCollisions(int number, int lower, int upper)
    {
        MutableLongList ecCollidingNumbers = new LongArrayList();
        for (int i = lower; i < upper && ecCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.ecIndex(i);
            if (index >= number && index <= number + 100)
            {
                ecCollidingNumbers.add(i);
            }
        }
        return ecCollidingNumbers;
    }

    protected long[] getKolobokeArray(int number, int lower, int upper, Random random)
    {
        long[] kolobokeCollisions = this.getKolobokeSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(kolobokeCollisions, random);
        return kolobokeCollisions;
    }

    private MutableLongList getKolobokeSequenceCollisions(int number, int lower, int upper)
    {
        MutableLongList kolobokeCollidingNumbers = new LongArrayList();
        for (int i = lower; i < upper && kolobokeCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.kolobokeIndex(i);
            if (index >= number && index <= number + 100)
            {
                kolobokeCollidingNumbers.add(i);
            }
        }
        return kolobokeCollidingNumbers;
    }

    @Benchmark
    public void kolobokeGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.longLongKoloboke.get(this.kolobokeLongKeysForMap[i]) == this.longLongKoloboke.defaultValue())
                {
                    throw new AssertionError(this.kolobokeLongKeysForMap[i] + " not in map");
                }
            }
            if (this.longLongKoloboke.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.longLongKoloboke.size());
            }
        }
    }

    @Benchmark
    public void ecGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.longLongEc.get(this.ecLongKeysForMap[i]) == 0)
                {
                    throw new AssertionError(this.ecLongKeysForMap[i] + " not in map");
                }
            }
            if (this.longLongEc.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.longLongEc.size());
            }
        }
    }

    @Benchmark
    public void kolobokePut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.kolobokeLongKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableLongLongMap newMap = new LongLongHashMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.ecLongKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableLongLongMap newMap = new LongLongHashMap(this.longLongEc);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.ecLongKeysForMap[i]);
            }
            if (newMap.notEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokeRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.kolobokeLongKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    public void shuffle(long[] array, Random rnd)
    {
        for (int i = array.length; i > 1; i--)
        {
            LongLongMapLargeStressTest.swap(array, i - 1, rnd.nextInt(i));
        }
    }

    private static void swap(long[] arr, int i, int j)
    {
        long tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
```

### Method 92

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.Random;
import java.util.concurrent.TimeUnit;

import com.koloboke.collect.map.LongLongMap;
import com.koloboke.collect.map.hash.HashLongLongMaps;
import org.eclipse.collections.api.list.primitive.MutableLongList;
import org.eclipse.collections.api.map.primitive.MutableLongLongMap;
import org.eclipse.collections.api.set.primitive.MutableLongSet;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.mutable.primitive.LongArrayList;
import org.eclipse.collections.impl.map.mutable.primitive.LongLongHashMap;
import org.eclipse.collections.impl.set.mutable.primitive.LongHashSet;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class LongLongMapLargeStressTest
{
    private static final int LOOP_COUNT = 1;
    private static final int KEY_COUNT = 400_000;
    private static final int MAP_SIZE = 1_000_000;

    @Param({"true", "false"})
    public boolean fullyRandom;
    private LongLongMap longLongKoloboke;
    private MutableLongLongMap longLongEc;
    private long[] ecLongKeysForMap;
    private long[] kolobokeLongKeysForMap;

    private int kolobokeIndex(int key)
    {
        long h = key * 0x9e3779b97f4a7c15L;
        h ^= h >> 32;
        return this.mask((int) (h ^ (h >> 16)));
    }

    private int ecIndex(int element)
    {
        return this.mask(element);
    }

    private int mask(int spread)
    {
        return spread & ((1 << 20) - 1);
    }

    @Setup
    public void setUp()
    {
        this.longLongKoloboke = HashLongLongMaps.newMutableMap(MAP_SIZE);
        this.longLongEc = new LongLongHashMap(MAP_SIZE);

        Random random = new Random(0x123456789ABCDL);

        int number = 23;
        int lower = Integer.MIN_VALUE;
        int upper = Integer.MAX_VALUE;

        long[] randomNumbersForMap = this.getRandomKeys(random).toArray();

        this.ecLongKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getECArray(number, lower, upper, random);
        this.kolobokeLongKeysForMap = this.fullyRandom
                ? randomNumbersForMap
                : this.getKolobokeArray(number, lower, upper, random);

        for (int i = 0; i < KEY_COUNT; i++)
        {
            this.longLongKoloboke.put(this.kolobokeLongKeysForMap[i], 5);
            this.longLongEc.put(this.ecLongKeysForMap[i], 5);
        }

        this.shuffle(this.ecLongKeysForMap, random);
        this.shuffle(this.kolobokeLongKeysForMap, random);
    }

    private MutableLongSet getRandomKeys(Random random)
    {
        MutableLongSet set = new LongHashSet(KEY_COUNT);
        while (set.size() < KEY_COUNT)
        {
            set.add(random.nextLong());
        }
        return set;
    }

    protected long[] getECArray(int number, int lower, int upper, Random random)
    {
        long[] ecCollisions = this.getECSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(ecCollisions, random);
        return ecCollisions;
    }

    private MutableLongList getECSequenceCollisions(int number, int lower, int upper)
    {
        MutableLongList ecCollidingNumbers = new LongArrayList();
        for (int i = lower; i < upper && ecCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.ecIndex(i);
            if (index >= number && index <= number + 100)
            {
                ecCollidingNumbers.add(i);
            }
        }
        return ecCollidingNumbers;
    }

    protected long[] getKolobokeArray(int number, int lower, int upper, Random random)
    {
        long[] kolobokeCollisions = this.getKolobokeSequenceCollisions(number, lower, upper).toArray();
        this.shuffle(kolobokeCollisions, random);
        return kolobokeCollisions;
    }

    private MutableLongList getKolobokeSequenceCollisions(int number, int lower, int upper)
    {
        MutableLongList kolobokeCollidingNumbers = new LongArrayList();
        for (int i = lower; i < upper && kolobokeCollidingNumbers.size() < KEY_COUNT; i++)
        {
            int index = this.kolobokeIndex(i);
            if (index >= number && index <= number + 100)
            {
                kolobokeCollidingNumbers.add(i);
            }
        }
        return kolobokeCollidingNumbers;
    }

    @Benchmark
    public void kolobokeGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.longLongKoloboke.get(this.kolobokeLongKeysForMap[i]) == this.longLongKoloboke.defaultValue())
                {
                    throw new AssertionError(this.kolobokeLongKeysForMap[i] + " not in map");
                }
            }
            if (this.longLongKoloboke.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.longLongKoloboke.size());
            }
        }
    }

    @Benchmark
    public void ecGet()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            for (int i = 0; i < KEY_COUNT; i++)
            {
                if (this.longLongEc.get(this.ecLongKeysForMap[i]) == 0)
                {
                    throw new AssertionError(this.ecLongKeysForMap[i] + " not in map");
                }
            }
            if (this.longLongEc.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + this.longLongEc.size());
            }
        }
    }

    @Benchmark
    public void kolobokePut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.kolobokeLongKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecPut()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableLongLongMap newMap = new LongLongHashMap(MAP_SIZE);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.put(this.ecLongKeysForMap[i], 4);
            }
            if (newMap.size() != KEY_COUNT)
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void ecRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            MutableLongLongMap newMap = new LongLongHashMap(this.longLongEc);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.ecLongKeysForMap[i]);
            }
            if (newMap.notEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    @Benchmark
    public void kolobokeRemove()
    {
        for (int j = 0; j < LOOP_COUNT; j++)
        {
            LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
            for (int i = 0; i < KEY_COUNT; i++)
            {
                newMap.remove(this.kolobokeLongKeysForMap[i]);
            }
            if (!newMap.isEmpty())
            {
                throw new AssertionError("size is " + newMap.size());
            }
        }
    }

    public void shuffle(long[] array, Random rnd)
    {
        for (int i = array.length; i > 1; i--)
        {
            LongLongMapLargeStressTest.swap(array, i - 1, rnd.nextInt(i));
        }
    }

    private static void swap(long[] arr, int i, int j)
    {
        long tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
```

### Method 93

```java
/*
 * Copyright (c) 2024 Goldman Sachs and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v. 1.0 which accompany this distribution.
 * The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 */

package org.eclipse.collections.impl.jmh;

import java.util.concurrent.TimeUnit;

import com.google.common.collect.HashMultiset;
import com.google.common.collect.Multiset;
import org.eclipse.collections.api.bag.MutableBag;
import org.eclipse.collections.impl.bag.mutable.HashBag;
import org.eclipse.collections.impl.jmh.runner.AbstractJMHTestRunner;
import org.eclipse.collections.impl.list.Interval;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Warmup;

@State(Scope.Thread)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Fork(2)
@Warmup(iterations = 10, time = 2)
@Measurement(iterations = 10, time = 2)
public class BagAddAllTest
{
    private static final int SIZE = 1000;
    private final Multiset<Integer> integersGuava = HashMultiset.create(Interval.oneTo(SIZE));
    private final MutableBag<Integer> integersEC = Interval.oneTo(SIZE).toBag();

    @Benchmark
    public void guava()
    {
        Multiset<Integer> result = HashMultiset.create();
        for (int i = 0; i < 1000; i++)
        {
            result.addAll(this.integersGuava);
        }
    }

    @Benchmark
    public void ec()
    {
        MutableBag<Integer> result = HashBag.newBag();
        for (int i = 0; i < 1000; i++)
        {
            result.addAll(this.integersEC);
        }
    }
}
```

## JMH UNSINKED VARIABLE - Unsinked variable inside benchmark method

### Method 1

```java
@Benchmark
public void ec() {
    MutableBag<Integer> result = HashBag.newBag();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersEC);
    }
}
```

### Method 2

```java
@Benchmark
public void ec() {
    MutableList<Integer> result = FastList.newList();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersEC);
    }
    if (result.size() != 1_000_000) {
        throw new AssertionError();
    }
}
```

### Method 3

```java
@Benchmark
public void ec() {
    MutableSet<Integer> result = UnifiedSet.newSet();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersEC);
    }
}
```

### Method 4

```java
@Benchmark
public void ecPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.ecIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 5

```java
@Benchmark
public void ecPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.ecIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 6

```java
@Benchmark
public void ecPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableLongLongMap newMap = new LongLongHashMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.ecLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 7

```java
@Benchmark
public void ecPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableLongLongMap newMap = new LongLongHashMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.ecLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 8

```java
@Benchmark
public void ecRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(this.intIntEc);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.ecIntKeysForMap[i]);
        }
        if (newMap.notEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 9

```java
@Benchmark
public void ecRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(this.intIntEc);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.ecIntKeysForMap[i]);
        }
        if (newMap.notEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 10

```java
@Benchmark
public void ecRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableLongLongMap newMap = new LongLongHashMap(this.longLongEc);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.ecLongKeysForMap[i]);
        }
        if (newMap.notEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 11

```java
@Benchmark
public void ecRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableLongLongMap newMap = new LongLongHashMap(this.longLongEc);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.ecLongKeysForMap[i]);
        }
        if (newMap.notEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 12

```java
@Benchmark
public void guava() {
    Multiset<Integer> result = HashMultiset.create();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersGuava);
    }
}
```

### Method 13

```java
@Benchmark
public void jdk() {
    List<Integer> result = new ArrayList<>();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersJDK);
    }
    if (result.size() != 1_000_000) {
        throw new AssertionError();
    }
}
```

### Method 14

```java
@Benchmark
public void jdk() {
    Set<Integer> result = new HashSet<>();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersJDK);
    }
}
```

### Method 15

```java
@Benchmark
public void jdkPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.jdkIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 16

```java
@Benchmark
public void jdkPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.jdkIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 17

```java
@Benchmark
public void jdkRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.jdkIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 18

```java
@Benchmark
public void jdkRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.jdkIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 19

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 20

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 21

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 22

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 23

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 24

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 25

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeLongKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 26

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeLongKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 27

```java
@Benchmark
public void parallel_eager_ec() {
    Collection<Integer> evens = ParallelIterate.select(this.integersEC, each -> each % 2 == 0);
    Assert.assertEquals(SIZE / 2, evens.size());
}
```

### Method 28

```java
@Benchmark
public void parallel_eager_ec() {
    Collection<String> evenStrings = ParallelIterate.collectIf(this.integersEC, e -> e % 2 == 0, Object::toString);
    Collection<String> oddStrings = ParallelIterate.collectIf(this.integersEC, e -> e % 2 == 1, Object::toString);
    Assert.assertEquals(SIZE / 2, evenStrings.size());
    Assert.assertEquals(SIZE / 2, oddStrings.size());
}
```

### Method 29

```java
@Benchmark
public void parallel_eager_ec() {
    MutableMultimap<Alphagram, String> groupBy = ParallelIterate.groupBy(this.ecWords, Alphagram::new);
    CompositeFastList<RichIterable<String>> select = ParallelIterate.select(groupBy.multiValuesView(), iterable -> iterable.size() >= SIZE_THRESHOLD, new CompositeFastList<>(), false);
    Collection<String> collect = ParallelIterate.collect(select.toSortedList(Comparators.byIntFunction(RichIterable::size)).asReversed(), iterable -> iterable.size() + ": " + iterable);
    ParallelIterate.forEach(collect, Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
}
```

### Method 30

```java
@Benchmark
public void parallel_eager_ec() {
    MutableMultimap<Alphagram, String> groupBy = ParallelIterate.groupBy(this.ecWords, Alphagram::new);
    groupBy.multiValuesView().select(iterable -> iterable.size() >= SIZE_THRESHOLD).toSortedList(Comparators.byIntFunction(RichIterable::size)).asReversed().collect(iterable -> iterable.size() + ": " + iterable).forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
}
```

### Method 31

```java
@Benchmark
public void parallel_eager_ec() {
    MutableMultimap<Alphagram, String> groupBy = ParallelIterate.groupBy(this.ecWords, Alphagram::new);
    groupBy.multiValuesView().select(iterable -> iterable.size() >= SIZE_THRESHOLD).toSortedList(Comparators.byIntFunction(RichIterable::size)).asReversed().collect(iterable -> iterable.size() + ": " + iterable).forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
}
```

### Method 32

```java
@Benchmark
public void parallel_eager_forkjoin_ec() {
    MutableMultimap<Alphagram, String> groupBy = FJIterate.groupBy(this.ecWords, Alphagram::new);
    CompositeFastList<RichIterable<String>> select = FJIterate.select(groupBy.multiValuesView(), iterable -> iterable.size() >= SIZE_THRESHOLD, new CompositeFastList<>(), false);
    Collection<String> collect = FJIterate.collect(select.toSortedList(Comparators.byIntFunction(RichIterable::size)).asReversed(), iterable -> iterable.size() + ": " + iterable);
    FJIterate.forEach(collect, Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
}
```

### Method 33

```java
@Benchmark
public void parallel_eager_forkjoin_ec() {
    MutableMultimap<Alphagram, String> groupBy = FJIterate.groupBy(this.ecWords, Alphagram::new);
    groupBy.multiValuesView().select(iterable -> iterable.size() >= SIZE_THRESHOLD).toSortedList(Comparators.byIntFunction(RichIterable::size)).asReversed().collect(iterable -> iterable.size() + ": " + iterable).forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
}
```

### Method 34

```java
@Benchmark
public void parallel_eager_forkjoin_ec() {
    MutableMultimap<Alphagram, String> groupBy = FJIterate.groupBy(this.ecWords, Alphagram::new);
    groupBy.multiValuesView().select(iterable -> iterable.size() >= SIZE_THRESHOLD).toSortedList(Comparators.byIntFunction(RichIterable::size)).asReversed().collect(iterable -> iterable.size() + ": " + iterable).forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
}
```

### Method 35

```java
@Benchmark
public void parallel_lazy_ec() {
    ParallelListIterable<Integer> parallelListIterable = this.integersEC.asParallel(this.service, BATCH_SIZE);
    MutableList<Integer> evens = parallelListIterable.select(each -> each % 2 == 0).toList();
    Assert.assertEquals(SIZE / 2, evens.size());
}
```

### Method 36

```java
@Benchmark
public void parallel_lazy_ec() {
    ParallelListIterable<Integer> parallelListIterable = this.integersEC.asParallel(this.service, BATCH_SIZE);
    MutableList<String> evenStrings = parallelListIterable.select(e -> e % 2 == 0).collect(Object::toString).toList();
    MutableList<String> oddStrings = parallelListIterable.select(e -> e % 2 == 1).collect(Object::toString).toList();
    Assert.assertEquals(SIZE / 2, evenStrings.size());
    Assert.assertEquals(SIZE / 2, oddStrings.size());
}
```

### Method 37

```java
@Benchmark
public void parallel_lazy_ec() {
    ParallelUnsortedBag<String> parallelUnsortedBag = this.ecWords.asParallel(this.executorService, BATCH_SIZE);
    UnsortedBagMultimap<Alphagram, String> groupBy = parallelUnsortedBag.groupBy(Alphagram::new);
    groupBy.multiValuesView().select(iterable -> iterable.size() >= SIZE_THRESHOLD).toSortedList(Comparators.byIntFunction(RichIterable::size)).asReversed().collect(iterable -> iterable.size() + ": " + iterable).forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
}
```

### Method 38

```java
@Benchmark
public void parallel_lazy_ec() {
    UnsortedSetMultimap<Alphagram, String> multimap = this.ecWords.asParallel(this.executorService, BATCH_SIZE).groupBy(Alphagram::new);
    FastList<Pair<Integer, String>> pairs = (FastList<Pair<Integer, String>>) FastList.newList(multimap.multiValuesView()).asParallel(this.executorService, BATCH_SIZE).select(iterable -> iterable.size() >= SIZE_THRESHOLD).collect(iterable -> Tuples.pair(iterable.size(), iterable.size() + ": " + iterable)).toSortedList((pair1, pair2) -> Integer.compare(pair2.getOne(), pair1.getOne()));
    pairs.asParallel(this.executorService, BATCH_SIZE).collect(Pair::getTwo).forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
}
```

### Method 39

```java
@Benchmark
public void parallel_lazy_jdk() {
    List<Integer> evens = this.integersJDK.parallelStream().filter(each -> each % 2 == 0).collect(Collectors.toList());
    Assert.assertEquals(SIZE / 2, evens.size());
}
```

### Method 40

```java
@Benchmark
public void parallel_lazy_jdk() {
    List<String> evenStrings = this.integersJDK.parallelStream().filter(e -> e % 2 == 0).map(Object::toString).collect(Collectors.toList());
    List<String> oddStrings = this.integersJDK.parallelStream().filter(e -> e % 2 == 1).map(Object::toString).collect(Collectors.toList());
    Assert.assertEquals(SIZE / 2, evenStrings.size());
    Assert.assertEquals(SIZE / 2, oddStrings.size());
}
```

### Method 41

```java
@Benchmark
public void parallel_lazy_jdk() {
    Map<Alphagram, List<String>> groupBy = this.guavaWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
    groupBy.entrySet().parallelStream().map(Map.Entry::getValue).filter(list -> list.size() >= SIZE_THRESHOLD).sorted(Comparator.<List<String>>comparingInt(List::size).reversed()).map(list -> list.size() + ": " + list).forEach(e -> Assert.assertFalse(e.isEmpty()));
}
```

### Method 42

```java
@Benchmark
public void parallel_lazy_jdk() {
    Map<Alphagram, List<String>> groupBy = this.jdkWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
    groupBy.entrySet().parallelStream().map(Map.Entry::getValue).filter(list -> list.size() >= SIZE_THRESHOLD).sorted(Comparator.<List<String>>comparingInt(List::size).reversed()).map(list -> list.size() + ": " + list).forEach(e -> Assert.assertFalse(e.isEmpty()));
}
```

### Method 43

```java
@Benchmark
public void parallel_lazy_jdk() {
    Map<Alphagram, Set<String>> groupBy = this.jdkWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
    groupBy.entrySet().parallelStream().map(Map.Entry::getValue).filter(list -> list.size() >= SIZE_THRESHOLD).sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed()).parallel().map(list -> list.size() + ": " + list).forEach(e -> Assert.assertFalse(e.isEmpty()));
}
```

### Method 44

```java
@Benchmark
public void parallel_lazy_streams_ec() {
    List<Integer> evens = this.integersEC.parallelStream().filter(each -> each % 2 == 0).collect(Collectors.toList());
    Assert.assertEquals(SIZE / 2, evens.size());
}
```

### Method 45

```java
@Benchmark
public void parallel_lazy_streams_ec() {
    List<String> evenStrings = this.integersEC.parallelStream().filter(e -> e % 2 == 0).map(Object::toString).collect(Collectors.toList());
    List<String> oddStrings = this.integersEC.parallelStream().filter(e -> e % 2 == 1).map(Object::toString).collect(Collectors.toList());
    Assert.assertEquals(SIZE / 2, evenStrings.size());
    Assert.assertEquals(SIZE / 2, oddStrings.size());
}
```

### Method 46

```java
@Benchmark
public void parallel_lazy_streams_ec() {
    Map<Alphagram, List<String>> groupBy = this.ecWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
    groupBy.entrySet().parallelStream().map(Map.Entry::getValue).filter(list -> list.size() >= SIZE_THRESHOLD).sorted(Comparator.<List<String>>comparingInt(List::size).reversed()).map(list -> list.size() + ": " + list).forEach(e -> Assert.assertFalse(e.isEmpty()));
}
```

### Method 47

```java
@Benchmark
public void parallel_lazy_streams_ec() {
    Map<Alphagram, List<String>> groupBy = this.ecWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new));
    groupBy.entrySet().parallelStream().map(Map.Entry::getValue).filter(list -> list.size() >= SIZE_THRESHOLD).sorted(Comparator.<List<String>>comparingInt(List::size).reversed()).map(list -> list.size() + ": " + list).forEach(e -> Assert.assertFalse(e.isEmpty()));
}
```

### Method 48

```java
@Benchmark
public void parallel_lazy_streams_ec() {
    Map<Alphagram, Set<String>> groupBy = this.ecWords.parallelStream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
    groupBy.entrySet().parallelStream().map(Map.Entry::getValue).filter(list -> list.size() >= SIZE_THRESHOLD).sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed()).parallel().map(list -> list.size() + ": " + list).forEach(e -> Assert.assertFalse(e.isEmpty()));
}
```

### Method 49

```java
@Benchmark
public void serial_eager_ec() {
    MutableList<Integer> evens = this.integersEC.reject(each -> each % 2 == 1);
    MutableList<Integer> odds = this.integersEC.reject(each -> each % 2 == 0);
    Assert.assertEquals(SIZE / 2, evens.size());
    Assert.assertEquals(SIZE / 2, odds.size());
}
```

### Method 50

```java
@Benchmark
public void serial_eager_ec() {
    MutableList<Integer> evens = this.integersEC.select(each -> each % 2 == 0);
    Assert.assertEquals(SIZE / 2, evens.size());
}
```

### Method 51

```java
@Benchmark
public void serial_eager_ec() {
    MutableList<String> evenStrings = this.integersEC.collectIf(e -> e % 2 == 0, Object::toString);
    MutableList<String> oddStrings = this.integersEC.collectIf(e -> e % 2 == 1, Object::toString);
    Assert.assertEquals(SIZE / 2, evenStrings.size());
    Assert.assertEquals(SIZE / 2, oddStrings.size());
}
```

### Method 52

```java
@Benchmark
public void serial_eager_ec() {
    MutableListMultimap<Alphagram, String> groupBy = this.ecWords.groupBy(Alphagram::new);
    groupBy.multiValuesView().select(iterable -> iterable.size() >= SIZE_THRESHOLD).toSortedList(Comparators.byIntFunction(RichIterable::size)).asReversed().collect(iterable -> iterable.size() + ": " + iterable).forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
}
```

### Method 53

```java
@Benchmark
public void serial_eager_ec() {
    MutableListMultimap<Alphagram, String> groupBy = this.ecWords.groupBy(Alphagram::new, FastListMultimap.newMultimap());
    groupBy.multiValuesView().select(iterable -> iterable.size() >= SIZE_THRESHOLD).toSortedList(Comparators.byIntFunction(RichIterable::size)).asReversed().collect(iterable -> iterable.size() + ": " + iterable).forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
}
```

### Method 54

```java
@Benchmark
public void serial_eager_ec() {
    MutableSetMultimap<Alphagram, String> groupBy = this.ecWords.groupBy(Alphagram::new);
    groupBy.multiValuesView().select(iterable -> iterable.size() >= SIZE_THRESHOLD).toSortedList(Comparators.byIntFunction(RichIterable::size)).asReversed().collect(iterable -> iterable.size() + ": " + iterable).forEach(Procedures.cast(e -> Assert.assertFalse(e.isEmpty())));
}
```

### Method 55

```java
@Benchmark
public void serial_eager_ec_select_predicates_not() {
    MutableList<Integer> evens = this.integersEC.select(Predicates.not(each -> each % 2 == 1));
    MutableList<Integer> odds = this.integersEC.select(Predicates.not(each -> each % 2 == 0));
    Assert.assertEquals(SIZE / 2, evens.size());
    Assert.assertEquals(SIZE / 2, odds.size());
}
```

### Method 56

```java
@Benchmark
public void serial_lazy_ec() {
    MutableList<Integer> evens = this.integersEC.asLazy().reject(each -> each % 2 == 1).toList();
    MutableList<Integer> odds = this.integersEC.asLazy().reject(each -> each % 2 == 0).toList();
    Assert.assertEquals(SIZE / 2, evens.size());
    Assert.assertEquals(SIZE / 2, odds.size());
}
```

### Method 57

```java
@Benchmark
public void serial_lazy_ec() {
    MutableList<Integer> evens = this.integersEC.asLazy().select(each -> each % 2 == 0).toList();
    Assert.assertEquals(SIZE / 2, evens.size());
}
```

### Method 58

```java
@Benchmark
public void serial_lazy_ec() {
    MutableList<String> evenStrings = this.integersEC.asLazy().select(e -> e % 2 == 0).collect(Object::toString).toList();
    MutableList<String> oddStrings = this.integersEC.asLazy().select(e -> e % 2 == 1).collect(Object::toString).toList();
    Assert.assertEquals(SIZE / 2, evenStrings.size());
    Assert.assertEquals(SIZE / 2, oddStrings.size());
}
```

### Method 59

```java
@Benchmark
public void serial_lazy_jdk() {
    List<Integer> evens = this.integersJDK.stream().filter(each -> each % 2 == 0).collect(Collectors.toList());
    Assert.assertEquals(SIZE / 2, evens.size());
}
```

### Method 60

```java
@Benchmark
public void serial_lazy_jdk() {
    List<String> evenStrings = this.integersJDK.stream().filter(e -> e % 2 == 0).map(Object::toString).collect(Collectors.toList());
    List<String> oddStrings = this.integersJDK.stream().filter(e -> e % 2 == 1).map(Object::toString).collect(Collectors.toList());
    Assert.assertEquals(SIZE / 2, evenStrings.size());
    Assert.assertEquals(SIZE / 2, oddStrings.size());
}
```

### Method 61

```java
@Benchmark
public void serial_lazy_jdk() {
    Map<Alphagram, List<String>> groupBy = this.guavaWords.stream().collect(Collectors.groupingBy(Alphagram::new));
    groupBy.entrySet().stream().map(Map.Entry::getValue).filter(list -> list.size() >= SIZE_THRESHOLD).sorted(Comparator.<List<String>>comparingInt(List::size).reversed()).map(list -> list.size() + ": " + list).forEach(e -> Assert.assertFalse(e.isEmpty()));
}
```

### Method 62

```java
@Benchmark
public void serial_lazy_jdk() {
    Map<Alphagram, List<String>> groupBy = this.jdkWords.stream().collect(Collectors.groupingBy(Alphagram::new));
    groupBy.entrySet().stream().map(Map.Entry::getValue).filter(list -> list.size() >= SIZE_THRESHOLD).sorted(Comparator.<List<String>>comparingInt(List::size).reversed()).map(list -> list.size() + ": " + list).forEach(e -> Assert.assertFalse(e.isEmpty()));
}
```

### Method 63

```java
@Benchmark
public void serial_lazy_jdk() {
    Map<Alphagram, Set<String>> groupBy = this.jdkWords.stream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
    groupBy.entrySet().stream().map(Map.Entry::getValue).filter(list -> list.size() >= SIZE_THRESHOLD).sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed()).map(list -> list.size() + ": " + list).forEach(e -> Assert.assertFalse(e.isEmpty()));
}
```

### Method 64

```java
@Benchmark
public void serial_lazy_jdk_lambda_negate() {
    Predicate<Integer> predicate1 = each -> each % 2 == 1;
    List<Integer> evens = this.integersJDK.stream().filter(predicate1.negate()).collect(Collectors.toList());
    Predicate<Integer> predicate2 = each -> each % 2 == 0;
    List<Integer> odds = this.integersJDK.stream().filter(predicate2.negate()).collect(Collectors.toList());
    Assert.assertEquals(SIZE / 2, evens.size());
    Assert.assertEquals(SIZE / 2, odds.size());
}
```

### Method 65

```java
@Benchmark
public void serial_lazy_jdk_lambda_not() {
    List<Integer> evens = this.integersJDK.stream().filter(each -> each % 2 != 1).collect(Collectors.toList());
    List<Integer> odds = this.integersJDK.stream().filter(each -> each % 2 != 0).collect(Collectors.toList());
    Assert.assertEquals(SIZE / 2, evens.size());
    Assert.assertEquals(SIZE / 2, odds.size());
}
```

### Method 66

```java
@Benchmark
public void serial_lazy_streams_ec() {
    List<Integer> evens = this.integersEC.stream().filter(each -> each % 2 == 0).collect(Collectors.toList());
    Assert.assertEquals(SIZE / 2, evens.size());
}
```

### Method 67

```java
@Benchmark
public void serial_lazy_streams_ec() {
    List<String> evenStrings = this.integersEC.stream().filter(e -> e % 2 == 0).map(Object::toString).collect(Collectors.toList());
    List<String> oddStrings = this.integersEC.stream().filter(e -> e % 2 == 1).map(Object::toString).collect(Collectors.toList());
    Assert.assertEquals(SIZE / 2, evenStrings.size());
    Assert.assertEquals(SIZE / 2, oddStrings.size());
}
```

### Method 68

```java
@Benchmark
public void serial_lazy_streams_ec() {
    Map<Alphagram, List<String>> groupBy = this.ecWords.stream().collect(Collectors.groupingBy(Alphagram::new));
    groupBy.entrySet().stream().map(Map.Entry::getValue).filter(list -> list.size() >= SIZE_THRESHOLD).sorted(Comparator.<List<String>>comparingInt(List::size).reversed()).map(list -> list.size() + ": " + list).forEach(e -> Assert.assertFalse(e.isEmpty()));
}
```

### Method 69

```java
@Benchmark
public void serial_lazy_streams_ec() {
    Map<Alphagram, List<String>> groupBy = this.ecWords.stream().collect(Collectors.groupingBy(Alphagram::new));
    groupBy.entrySet().stream().map(Map.Entry::getValue).filter(list -> list.size() >= SIZE_THRESHOLD).sorted(Comparator.<List<String>>comparingInt(List::size).reversed()).map(list -> list.size() + ": " + list).forEach(e -> Assert.assertFalse(e.isEmpty()));
}
```

### Method 70

```java
@Benchmark
public void serial_lazy_streams_ec() {
    Map<Alphagram, Set<String>> groupBy = this.ecWords.stream().collect(Collectors.groupingBy(Alphagram::new, Collectors.toSet()));
    groupBy.entrySet().stream().map(Map.Entry::getValue).filter(list -> list.size() >= SIZE_THRESHOLD).sorted(Comparator.<Set<String>>comparingInt(Set::size).reversed()).map(list -> list.size() + ": " + list).forEach(e -> Assert.assertFalse(e.isEmpty()));
}
```

### Method 71

```java
@Benchmark
public void serial_lazy_streams_ec_lambda_negate() {
    Predicate<Integer> predicate1 = each -> each % 2 == 1;
    List<Integer> evens = this.integersEC.stream().filter(predicate1.negate()).collect(Collectors.toList());
    Predicate<Integer> predicate2 = each -> each % 2 == 0;
    List<Integer> odds = this.integersEC.stream().filter(predicate2.negate()).collect(Collectors.toList());
    Assert.assertEquals(SIZE / 2, evens.size());
    Assert.assertEquals(SIZE / 2, odds.size());
}
```

### Method 72

```java
@Benchmark
public void serial_lazy_streams_ec_lambda_not() {
    List<Integer> evens = this.integersEC.stream().filter(each -> each % 2 != 1).collect(Collectors.toList());
    List<Integer> odds = this.integersEC.stream().filter(each -> each % 2 != 0).collect(Collectors.toList());
    Assert.assertEquals(SIZE / 2, evens.size());
    Assert.assertEquals(SIZE / 2, odds.size());
}
```

### Method 73

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public MutableList<Integer> serial_eager_ec() {
    FastList<Integer> select1 = this.integersEC.select(each -> each % 10_000 != 0);
    FastList<String> collect1 = select1.collect(String::valueOf);
    FastList<Integer> collect2 = collect1.collect(Integer::valueOf);
    FastList<Integer> list = collect2.select(each -> (each + 1) % 10_000 != 0);
    Verify.assertSize(999_800, list);
    return list;
}
```

### Method 74

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public MutableSet<Integer> serial_eager_ec() {
    FastList<Integer> select1 = this.integersEC.select(each -> each % 10_000 != 0);
    FastList<String> collect1 = select1.collect(String::valueOf);
    FastList<Integer> collect2 = collect1.collect(Integer::valueOf);
    UnifiedSet<Integer> set = collect2.select(each -> (each + 1) % 10_000 != 0, UnifiedSet.newSet());
    Verify.assertSize(999_800, set);
    return set;
}
```

### Method 75

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void copyTest(Blackhole blackHole) {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        MutableLongIntMap newMap = new LongIntHashMap(this.longIntMap);
        blackHole.consume(newMap.get(0));
    }
}
```

### Method 76

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void presizedPut() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        MutableLongIntMap newMap = new LongIntHashMap(this.mapSizeDividedBy16000);
        for (int i = 0; i < this.mapSizeDividedBy16000 * 64; i++) {
            newMap.put(this.randomLongsForMap[i], this.randomIntegersForMap[i]);
        }
    }
}
```

### Method 77

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void presizedPut() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy64 / 64; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(this.mapSizeDividedBy64);
        for (int i = 0; i < this.mapSizeDividedBy64 * 64; i++) {
            newMap.put(this.randomIntsForKeys[i], this.randomIntsForValues[i]);
        }
    }
}
```

### Method 78

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void put() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        MutableLongIntMap newMap = new LongIntHashMap();
        for (int i = 0; i < this.mapSizeDividedBy16000 * 64; i++) {
            newMap.put(this.randomLongsForMap[i], this.randomIntegersForMap[i]);
        }
    }
}
```

### Method 79

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void put() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy64 / 64; j++) {
        MutableIntIntMap newMap = new IntIntHashMap();
        for (int i = 0; i < this.mapSizeDividedBy64 * 64; i++) {
            newMap.put(this.randomIntsForKeys[i], this.randomIntsForValues[i]);
        }
    }
}
```

### Method 80

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void remove() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        MutableLongIntMap newMap = new LongIntHashMap(this.longIntMap);
        for (int i = 0; i < this.mapSizeDividedBy16000 * 64; i++) {
            newMap.remove(this.randomLongsForMap[i]);
        }
    }
}
```

### Method 81

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void remove() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy64 / 64; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(this.intIntMap);
        for (int i = 0; i < this.mapSizeDividedBy64 * 64; i++) {
            newMap.remove(this.randomIntsForKeys[i]);
        }
    }
}
```

## JMH IGNORED METHOD RETURN - Method return not used or consumed by a Blackhole.

### Method 1

```java
@Benchmark
public Map<String, String> jdk() {
    int localSize = this.size;
    float localLoadFactor = this.loadFactor;
    String[] localElements = this.elements;
    /**
     * @see HashMap#DEFAULT_INITIAL_CAPACITY
     */
    int defaultInitialCapacity = 16;
    Map<String, String> jdk = this.isPresized ? new HashMap<>(localSize, localLoadFactor) : new HashMap<>(defaultInitialCapacity, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        jdk.put(localElements[i], "dummy");
    }
    return jdk;
}
```

### Method 2

```java
@Benchmark
public Map<String, String> scalaAnyRef() {
    int localSize = this.size;
    String[] localElements = this.elements;
    Map<String, String> scalaAnyRefMap = this.isPresized ? new AnyRefMap<>(localSize) : new AnyRefMap<>();
    for (int i = 0; i < localSize; i++) {
        scalaAnyRefMap.put(localElements[i], "dummy");
    }
    return scalaAnyRefMap;
}
```

### Method 3

```java
@Benchmark
public MutableMap<String, String> ec() {
    int localSize = this.size;
    float localLoadFactor = this.loadFactor;
    String[] localElements = this.elements;
    /**
     * @see UnifiedMap#DEFAULT_INITIAL_CAPACITY
     */
    int defaultInitialCapacity = 8;
    MutableMap<String, String> ec = this.isPresized ? UnifiedMap.newMap(localSize, localLoadFactor) : UnifiedMap.newMap(defaultInitialCapacity, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        ec.put(localElements[i], "dummy");
    }
    return ec;
}
```

### Method 4

```java
@Benchmark
public MutableMap<String, String> mutableEcPut() {
    int localSize = this.size;
    /**
     * @see UnifiedMap#DEFAULT_LOAD_FACTOR
     */
    float localLoadFactor = 0.75f;
    String[] localElements = this.elements;
    MutableMap<String, String> map = UnifiedMap.newMap(localSize, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        map.put(localElements[i], "dummy");
    }
    return map;
}
```

### Method 5

```java
@Benchmark
public ObjObjMap<String, String> koloboke() {
    int localSize = this.size;
    String[] localElements = this.elements;
    ObjObjMap<String, String> koloboke = this.isPresized ? HashObjObjMaps.newMutableMap(localSize) : HashObjObjMaps.newMutableMap();
    for (int i = 0; i < localSize; i++) {
        koloboke.put(localElements[i], "dummy");
    }
    return koloboke;
}
```

### Method 6

```java
@Benchmark
public ObjectObjectMap<String, String> hppc() {
    int localSize = this.size;
    float localLoadFactor = this.loadFactor;
    String[] localElements = this.elements;
    int defaultInitialCapacity = Containers.DEFAULT_EXPECTED_ELEMENTS;
    ObjectObjectMap<String, String> hppc = this.isPresized ? new ObjectObjectHashMap<>(localSize, localLoadFactor) : new ObjectObjectHashMap<>(defaultInitialCapacity, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        hppc.put(localElements[i], "dummy");
    }
    return hppc;
}
```

### Method 7

```java
@Benchmark
public TMap<String, String> trove() {
    int localSize = this.size;
    float localLoadFactor = this.loadFactor;
    String[] localElements = this.elements;
    int defaultInitialCapacity = Constants.DEFAULT_CAPACITY;
    TMap<String, String> trove = this.isPresized ? new THashMap<>(localSize, localLoadFactor) : new THashMap<>(defaultInitialCapacity, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        trove.put(localElements[i], "dummy");
    }
    return trove;
}
```

### Method 8

```java
@Benchmark
public scala.collection.mutable.HashMap<String, String> mutableScalaPut() {
    int localSize = this.size;
    String[] localElements = this.elements;
    scala.collection.mutable.HashMap<String, String> map = new PresizableHashMap<>(localSize);
    for (int i = 0; i < localSize; i++) {
        map.put(localElements[i], "dummy");
    }
    return map;
}
```

### Method 9

```java
@Benchmark
public scala.collection.mutable.HashMap<String, String> scala() {
    int localSize = this.size;
    if (Float.compare(this.loadFactor, 0.75f) != 0) {
        throw new IllegalArgumentException();
    }
    String[] localElements = this.elements;
    /**
     * @see HashTable#initialSize()
     */
    int defaultInitialSize = 16;
    scala.collection.mutable.HashMap<String, String> scala = this.isPresized ? new PresizableHashMap<>(localSize) : new PresizableHashMap<>(defaultInitialSize);
    for (int i = 0; i < localSize; i++) {
        scala.put(localElements[i], "dummy");
    }
    return scala;
}
```

### Method 10

```java
@Benchmark
public void ec() {
    MutableBag<Integer> result = HashBag.newBag();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersEC);
    }
}
```

### Method 11

```java
@Benchmark
public void ec() {
    MutableList<Integer> result = FastList.newList();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersEC);
    }
    if (result.size() != 1_000_000) {
        throw new AssertionError();
    }
}
```

### Method 12

```java
@Benchmark
public void ec() {
    MutableSet<Integer> result = UnifiedSet.newSet();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersEC);
    }
}
```

### Method 13

```java
@Benchmark
public void guava() {
    Multiset<Integer> result = HashMultiset.create();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersGuava);
    }
}
```

### Method 14

```java
@Benchmark
public void jdk() {
    List<Integer> result = new ArrayList<>();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersJDK);
    }
    if (result.size() != 1_000_000) {
        throw new AssertionError();
    }
}
```

### Method 15

```java
@Benchmark
public void jdk() {
    Set<Integer> result = new HashSet<>();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersJDK);
    }
}
```

### Method 16

```java
@Benchmark
public void jdkPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.jdkIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 17

```java
@Benchmark
public void jdkPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.jdkIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 18

```java
@Benchmark
public void jdkRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.jdkIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 19

```java
@Benchmark
public void jdkRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.jdkIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 20

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 21

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 22

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 23

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 24

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 25

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 26

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeLongKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 27

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeLongKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 28

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public MutableList<Integer> serial_eager_ec_hand_coded() {
    FastList<Integer> list = new FastList<>();
    int size = this.integersEC.size();
    for (int i = 0; i < size; i++) {
        Integer integer = this.integersEC.get(i);
        if (integer % 10_000 != 0 && (Integer.valueOf(String.valueOf(integer)) + 1) % 10_000 != 0) {
            list.add(integer);
        }
    }
    Verify.assertSize(999_800, list);
    return list;
}
```

## JMH LOOP INSIDE BENCHMARK - Usage of loops in the JMH benchmark function.

### Method 1

```java
@Benchmark
public Map<String, String> jdk() {
    int localSize = this.size;
    float localLoadFactor = this.loadFactor;
    String[] localElements = this.elements;
    /**
     * @see HashMap#DEFAULT_INITIAL_CAPACITY
     */
    int defaultInitialCapacity = 16;
    Map<String, String> jdk = this.isPresized ? new HashMap<>(localSize, localLoadFactor) : new HashMap<>(defaultInitialCapacity, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        jdk.put(localElements[i], "dummy");
    }
    return jdk;
}
```

### Method 2

```java
@Benchmark
public Map<String, String> jdk() {
    int localSize = this.size;
    float localLoadFactor = this.loadFactor;
    String[] localElements = this.elements;
    /**
     * @see HashMap#DEFAULT_INITIAL_CAPACITY
     */
    int defaultInitialCapacity = 16;
    Map<String, String> jdk = this.isPresized ? new HashMap<>(localSize, localLoadFactor) : new HashMap<>(defaultInitialCapacity, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        jdk.put(localElements[i], "dummy");
    }
    return jdk;
}
```

### Method 3

```java
@Benchmark
public Map<String, String> scalaAnyRef() {
    int localSize = this.size;
    String[] localElements = this.elements;
    Map<String, String> scalaAnyRefMap = this.isPresized ? new AnyRefMap<>(localSize) : new AnyRefMap<>();
    for (int i = 0; i < localSize; i++) {
        scalaAnyRefMap.put(localElements[i], "dummy");
    }
    return scalaAnyRefMap;
}
```

### Method 4

```java
@Benchmark
public Map<String, String> scalaAnyRef() {
    int localSize = this.size;
    String[] localElements = this.elements;
    Map<String, String> scalaAnyRefMap = this.isPresized ? new AnyRefMap<>(localSize) : new AnyRefMap<>();
    for (int i = 0; i < localSize; i++) {
        scalaAnyRefMap.put(localElements[i], "dummy");
    }
    return scalaAnyRefMap;
}
```

### Method 5

```java
@Benchmark
public MutableMap<String, String> ec() {
    int localSize = this.size;
    float localLoadFactor = this.loadFactor;
    String[] localElements = this.elements;
    /**
     * @see UnifiedMap#DEFAULT_INITIAL_CAPACITY
     */
    int defaultInitialCapacity = 8;
    MutableMap<String, String> ec = this.isPresized ? UnifiedMap.newMap(localSize, localLoadFactor) : UnifiedMap.newMap(defaultInitialCapacity, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        ec.put(localElements[i], "dummy");
    }
    return ec;
}
```

### Method 6

```java
@Benchmark
public MutableMap<String, String> ec() {
    int localSize = this.size;
    float localLoadFactor = this.loadFactor;
    String[] localElements = this.elements;
    /**
     * @see UnifiedMap#DEFAULT_INITIAL_CAPACITY
     */
    int defaultInitialCapacity = 8;
    MutableMap<String, String> ec = this.isPresized ? UnifiedMap.newMap(localSize, localLoadFactor) : UnifiedMap.newMap(defaultInitialCapacity, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        ec.put(localElements[i], "dummy");
    }
    return ec;
}
```

### Method 7

```java
@Benchmark
public MutableMap<String, String> mutableEcPut() {
    int localSize = this.size;
    /**
     * @see UnifiedMap#DEFAULT_LOAD_FACTOR
     */
    float localLoadFactor = 0.75f;
    String[] localElements = this.elements;
    MutableMap<String, String> map = UnifiedMap.newMap(localSize, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        map.put(localElements[i], "dummy");
    }
    return map;
}
```

### Method 8

```java
@Benchmark
public ObjObjMap<String, String> koloboke() {
    int localSize = this.size;
    String[] localElements = this.elements;
    ObjObjMap<String, String> koloboke = this.isPresized ? HashObjObjMaps.newMutableMap(localSize) : HashObjObjMaps.newMutableMap();
    for (int i = 0; i < localSize; i++) {
        koloboke.put(localElements[i], "dummy");
    }
    return koloboke;
}
```

### Method 9

```java
@Benchmark
public ObjObjMap<String, String> koloboke() {
    int localSize = this.size;
    String[] localElements = this.elements;
    ObjObjMap<String, String> koloboke = this.isPresized ? HashObjObjMaps.newMutableMap(localSize) : HashObjObjMaps.newMutableMap();
    for (int i = 0; i < localSize; i++) {
        koloboke.put(localElements[i], "dummy");
    }
    return koloboke;
}
```

### Method 10

```java
@Benchmark
public ObjectObjectMap<String, String> hppc() {
    int localSize = this.size;
    float localLoadFactor = this.loadFactor;
    String[] localElements = this.elements;
    int defaultInitialCapacity = Containers.DEFAULT_EXPECTED_ELEMENTS;
    ObjectObjectMap<String, String> hppc = this.isPresized ? new ObjectObjectHashMap<>(localSize, localLoadFactor) : new ObjectObjectHashMap<>(defaultInitialCapacity, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        hppc.put(localElements[i], "dummy");
    }
    return hppc;
}
```

### Method 11

```java
@Benchmark
public ObjectObjectMap<String, String> hppc() {
    int localSize = this.size;
    float localLoadFactor = this.loadFactor;
    String[] localElements = this.elements;
    int defaultInitialCapacity = Containers.DEFAULT_EXPECTED_ELEMENTS;
    ObjectObjectMap<String, String> hppc = this.isPresized ? new ObjectObjectHashMap<>(localSize, localLoadFactor) : new ObjectObjectHashMap<>(defaultInitialCapacity, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        hppc.put(localElements[i], "dummy");
    }
    return hppc;
}
```

### Method 12

```java
@Benchmark
public TMap<String, String> trove() {
    int localSize = this.size;
    float localLoadFactor = this.loadFactor;
    String[] localElements = this.elements;
    int defaultInitialCapacity = Constants.DEFAULT_CAPACITY;
    TMap<String, String> trove = this.isPresized ? new THashMap<>(localSize, localLoadFactor) : new THashMap<>(defaultInitialCapacity, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        trove.put(localElements[i], "dummy");
    }
    return trove;
}
```

### Method 13

```java
@Benchmark
public TMap<String, String> trove() {
    int localSize = this.size;
    float localLoadFactor = this.loadFactor;
    String[] localElements = this.elements;
    int defaultInitialCapacity = Constants.DEFAULT_CAPACITY;
    TMap<String, String> trove = this.isPresized ? new THashMap<>(localSize, localLoadFactor) : new THashMap<>(defaultInitialCapacity, localLoadFactor);
    for (int i = 0; i < localSize; i++) {
        trove.put(localElements[i], "dummy");
    }
    return trove;
}
```

### Method 14

```java
@Benchmark
public scala.collection.immutable.Map<String, String> immutableScalaPut() {
    int localSize = this.size;
    String[] localElements = this.elements;
    scala.collection.immutable.Map<String, String> map = HashMap$.MODULE$.empty();
    for (int i = 0; i < localSize; i++) {
        map = map.updated(localElements[i], "dummy");
    }
    return map;
}
```

### Method 15

```java
@Benchmark
public scala.collection.mutable.HashMap<String, String> mutableScalaPut() {
    int localSize = this.size;
    String[] localElements = this.elements;
    scala.collection.mutable.HashMap<String, String> map = new PresizableHashMap<>(localSize);
    for (int i = 0; i < localSize; i++) {
        map.put(localElements[i], "dummy");
    }
    return map;
}
```

### Method 16

```java
@Benchmark
public scala.collection.mutable.HashMap<String, String> scala() {
    int localSize = this.size;
    if (Float.compare(this.loadFactor, 0.75f) != 0) {
        throw new IllegalArgumentException();
    }
    String[] localElements = this.elements;
    /**
     * @see HashTable#initialSize()
     */
    int defaultInitialSize = 16;
    scala.collection.mutable.HashMap<String, String> scala = this.isPresized ? new PresizableHashMap<>(localSize) : new PresizableHashMap<>(defaultInitialSize);
    for (int i = 0; i < localSize; i++) {
        scala.put(localElements[i], "dummy");
    }
    return scala;
}
```

### Method 17

```java
@Benchmark
public scala.collection.mutable.HashMap<String, String> scala() {
    int localSize = this.size;
    if (Float.compare(this.loadFactor, 0.75f) != 0) {
        throw new IllegalArgumentException();
    }
    String[] localElements = this.elements;
    /**
     * @see HashTable#initialSize()
     */
    int defaultInitialSize = 16;
    scala.collection.mutable.HashMap<String, String> scala = this.isPresized ? new PresizableHashMap<>(localSize) : new PresizableHashMap<>(defaultInitialSize);
    for (int i = 0; i < localSize; i++) {
        scala.put(localElements[i], "dummy");
    }
    return scala;
}
```

### Method 18

```java
@Benchmark
public void contains_immutable_ec() {
    int size = SIZE;
    ImmutableSortedSet<Integer> localEcImmutable = this.ecImmutable;
    for (int i = 0; i < size; i += 2) {
        if (!localEcImmutable.contains(i)) {
            throw new AssertionError(i);
        }
    }
    for (int i = 1; i < size; i += 2) {
        if (localEcImmutable.contains(i)) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 19

```java
@Benchmark
public void contains_immutable_ec() {
    int size = SIZE;
    ImmutableSortedSet<Integer> localEcImmutable = this.ecImmutable;
    for (int i = 0; i < size; i += 2) {
        if (!localEcImmutable.contains(i)) {
            throw new AssertionError(i);
        }
    }
    for (int i = 1; i < size; i += 2) {
        if (localEcImmutable.contains(i)) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 20

```java
@Benchmark
public void contains_mutable_ec() {
    int size = SIZE;
    MutableSortedSet<Integer> localEcMutable = this.ecMutable;
    for (int i = 0; i < size; i += 2) {
        if (!localEcMutable.contains(i)) {
            throw new AssertionError(i);
        }
    }
    for (int i = 1; i < size; i += 2) {
        if (localEcMutable.contains(i)) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 21

```java
@Benchmark
public void contains_mutable_ec() {
    int size = SIZE;
    MutableSortedSet<Integer> localEcMutable = this.ecMutable;
    for (int i = 0; i < size; i += 2) {
        if (!localEcMutable.contains(i)) {
            throw new AssertionError(i);
        }
    }
    for (int i = 1; i < size; i += 2) {
        if (localEcMutable.contains(i)) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 22

```java
@Benchmark
public void ec() {
    MutableBag<Integer> result = HashBag.newBag();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersEC);
    }
}
```

### Method 23

```java
@Benchmark
public void ec() {
    MutableList<Integer> result = FastList.newList();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersEC);
    }
    if (result.size() != 1_000_000) {
        throw new AssertionError();
    }
}
```

### Method 24

```java
@Benchmark
public void ec() {
    MutableSet<Integer> result = UnifiedSet.newSet();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersEC);
    }
}
```

### Method 25

```java
@Benchmark
public void ecGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.intIntEc.get(this.ecIntKeysForMap[i]) == 0) {
                throw new AssertionError(this.ecIntKeysForMap[i] + " not in map");
            }
        }
        if (this.intIntEc.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.intIntEc.size());
        }
    }
}
```

### Method 26

```java
@Benchmark
public void ecGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.intIntEc.get(this.ecIntKeysForMap[i]) == 0) {
                throw new AssertionError(this.ecIntKeysForMap[i] + " not in map");
            }
        }
        if (this.intIntEc.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.intIntEc.size());
        }
    }
}
```

### Method 27

```java
@Benchmark
public void ecGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.intIntEc.get(this.ecIntKeysForMap[i]) == 0) {
                throw new AssertionError(this.ecIntKeysForMap[i] + " not in map");
            }
        }
        if (this.intIntEc.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.intIntEc.size());
        }
    }
}
```

### Method 28

```java
@Benchmark
public void ecGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.intIntEc.get(this.ecIntKeysForMap[i]) == 0) {
                throw new AssertionError(this.ecIntKeysForMap[i] + " not in map");
            }
        }
        if (this.intIntEc.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.intIntEc.size());
        }
    }
}
```

### Method 29

```java
@Benchmark
public void ecGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.longLongEc.get(this.ecLongKeysForMap[i]) == 0) {
                throw new AssertionError(this.ecLongKeysForMap[i] + " not in map");
            }
        }
        if (this.longLongEc.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.longLongEc.size());
        }
    }
}
```

### Method 30

```java
@Benchmark
public void ecGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.longLongEc.get(this.ecLongKeysForMap[i]) == 0) {
                throw new AssertionError(this.ecLongKeysForMap[i] + " not in map");
            }
        }
        if (this.longLongEc.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.longLongEc.size());
        }
    }
}
```

### Method 31

```java
@Benchmark
public void ecGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.longLongEc.get(this.ecLongKeysForMap[i]) == 0) {
                throw new AssertionError(this.ecLongKeysForMap[i] + " not in map");
            }
        }
        if (this.longLongEc.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.longLongEc.size());
        }
    }
}
```

### Method 32

```java
@Benchmark
public void ecGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.longLongEc.get(this.ecLongKeysForMap[i]) == 0) {
                throw new AssertionError(this.ecLongKeysForMap[i] + " not in map");
            }
        }
        if (this.longLongEc.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.longLongEc.size());
        }
    }
}
```

### Method 33

```java
@Benchmark
public void ecPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.ecIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 34

```java
@Benchmark
public void ecPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.ecIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 35

```java
@Benchmark
public void ecPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.ecIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 36

```java
@Benchmark
public void ecPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.ecIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 37

```java
@Benchmark
public void ecPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableLongLongMap newMap = new LongLongHashMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.ecLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 38

```java
@Benchmark
public void ecPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableLongLongMap newMap = new LongLongHashMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.ecLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 39

```java
@Benchmark
public void ecPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableLongLongMap newMap = new LongLongHashMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.ecLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 40

```java
@Benchmark
public void ecPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableLongLongMap newMap = new LongLongHashMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.ecLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 41

```java
@Benchmark
public void ecRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(this.intIntEc);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.ecIntKeysForMap[i]);
        }
        if (newMap.notEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 42

```java
@Benchmark
public void ecRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(this.intIntEc);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.ecIntKeysForMap[i]);
        }
        if (newMap.notEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 43

```java
@Benchmark
public void ecRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(this.intIntEc);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.ecIntKeysForMap[i]);
        }
        if (newMap.notEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 44

```java
@Benchmark
public void ecRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(this.intIntEc);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.ecIntKeysForMap[i]);
        }
        if (newMap.notEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 45

```java
@Benchmark
public void ecRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableLongLongMap newMap = new LongLongHashMap(this.longLongEc);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.ecLongKeysForMap[i]);
        }
        if (newMap.notEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 46

```java
@Benchmark
public void ecRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableLongLongMap newMap = new LongLongHashMap(this.longLongEc);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.ecLongKeysForMap[i]);
        }
        if (newMap.notEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 47

```java
@Benchmark
public void ecRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableLongLongMap newMap = new LongLongHashMap(this.longLongEc);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.ecLongKeysForMap[i]);
        }
        if (newMap.notEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 48

```java
@Benchmark
public void ecRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        MutableLongLongMap newMap = new LongLongHashMap(this.longLongEc);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.ecLongKeysForMap[i]);
        }
        if (newMap.notEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 49

```java
@Benchmark
public void get() {
    int localSize = this.size;
    String[] localElements = this.elements;
    ImmutableMap<String, String> localEcMap = this.ecMap;
    for (int i = 0; i < localSize; i++) {
        if (localEcMap.get(localElements[i]) == null) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 50

```java
@Benchmark
public void get() {
    int localSize = this.size;
    String[] localElements = this.elements;
    Map<String, String> localJdkMap = this.jdkMap;
    for (int i = 0; i < localSize; i++) {
        if (localJdkMap.get(localElements[i]) == null) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 51

```java
@Benchmark
public void get() {
    int localSize = this.size;
    String[] localElements = this.elements;
    Map<String, String> localScalaAnyRefMap = this.scalaAnyRefMap;
    for (int i = 0; i < localSize; i++) {
        if (!localScalaAnyRefMap.get(localElements[i]).isDefined()) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 52

```java
@Benchmark
public void get() {
    int localSize = this.size;
    String[] localElements = this.elements;
    Map<String, String> localScalaMap = this.scalaMap;
    for (int i = 0; i < localSize; i++) {
        if (!localScalaMap.get(localElements[i]).isDefined()) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 53

```java
@Benchmark
public void get() {
    int localSize = this.size;
    String[] localElements = this.elements;
    Map<String, String> localScalaMap = this.scalaMap;
    for (int i = 0; i < localSize; i++) {
        if (!localScalaMap.get(localElements[i]).isDefined()) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 54

```java
@Benchmark
public void get() {
    int localSize = this.size;
    String[] localElements = this.elements;
    MutableMap<String, String> localEcMap = this.ecMap;
    for (int i = 0; i < localSize; i++) {
        if (localEcMap.get(localElements[i]) == null) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 55

```java
@Benchmark
public void get() {
    int localSize = this.size;
    String[] localElements = this.elements;
    ObjObjMap<String, String> localKolobokeMap = this.kolobokeMap;
    for (int i = 0; i < localSize; i++) {
        if (localKolobokeMap.get(localElements[i]) == null) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 56

```java
@Benchmark
public void get() {
    int localSize = this.size;
    String[] localElements = this.elements;
    ObjectObjectMap<String, String> localHppcMap = this.hppcMap;
    for (int i = 0; i < localSize; i++) {
        if (localHppcMap.get(localElements[i]) == null) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 57

```java
@Benchmark
public void get() {
    int localSize = this.size;
    String[] localElements = this.elements;
    TMap<String, String> localTroveMap = this.troveMap;
    for (int i = 0; i < localSize; i++) {
        if (localTroveMap.get(localElements[i]) == null) {
            throw new AssertionError(i);
        }
    }
}
```

### Method 58

```java
@Benchmark
public void guava() {
    Multiset<Integer> result = HashMultiset.create();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersGuava);
    }
}
```

### Method 59

```java
@Benchmark
public void jdk() {
    List<Integer> result = new ArrayList<>();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersJDK);
    }
    if (result.size() != 1_000_000) {
        throw new AssertionError();
    }
}
```

### Method 60

```java
@Benchmark
public void jdk() {
    Set<Integer> result = new HashSet<>();
    for (int i = 0; i < 1000; i++) {
        result.addAll(this.integersJDK);
    }
}
```

### Method 61

```java
@Benchmark
public void jdkGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.integerIntegerJdk.get(this.jdkIntKeysForMap[i]) == null) {
                throw new AssertionError(this.jdkIntKeysForMap[i] + " not in map");
            }
        }
        if (this.integerIntegerJdk.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.integerIntegerJdk.size());
        }
    }
}
```

### Method 62

```java
@Benchmark
public void jdkGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.integerIntegerJdk.get(this.jdkIntKeysForMap[i]) == null) {
                throw new AssertionError(this.jdkIntKeysForMap[i] + " not in map");
            }
        }
        if (this.integerIntegerJdk.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.integerIntegerJdk.size());
        }
    }
}
```

### Method 63

```java
@Benchmark
public void jdkGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.integerIntegerJdk.get(this.jdkIntKeysForMap[i]) == null) {
                throw new AssertionError(this.jdkIntKeysForMap[i] + " not in map");
            }
        }
        if (this.integerIntegerJdk.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.integerIntegerJdk.size());
        }
    }
}
```

### Method 64

```java
@Benchmark
public void jdkGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.integerIntegerJdk.get(this.jdkIntKeysForMap[i]) == null) {
                throw new AssertionError(this.jdkIntKeysForMap[i] + " not in map");
            }
        }
        if (this.integerIntegerJdk.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.integerIntegerJdk.size());
        }
    }
}
```

### Method 65

```java
@Benchmark
public void jdkPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.jdkIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 66

```java
@Benchmark
public void jdkPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.jdkIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 67

```java
@Benchmark
public void jdkPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.jdkIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 68

```java
@Benchmark
public void jdkPut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.jdkIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 69

```java
@Benchmark
public void jdkRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.jdkIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 70

```java
@Benchmark
public void jdkRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.jdkIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 71

```java
@Benchmark
public void jdkRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.jdkIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 72

```java
@Benchmark
public void jdkRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        Map<Integer, Integer> newMap = new HashMap<>(this.integerIntegerJdk);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.jdkIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 73

```java
@Benchmark
public void kolobokeGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.intIntKoloboke.get(this.kolobokeIntKeysForMap[i]) == this.intIntKoloboke.defaultValue()) {
                throw new AssertionError(this.kolobokeIntKeysForMap[i] + " not in map");
            }
        }
        if (this.intIntKoloboke.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.intIntKoloboke.size());
        }
    }
}
```

### Method 74

```java
@Benchmark
public void kolobokeGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.intIntKoloboke.get(this.kolobokeIntKeysForMap[i]) == this.intIntKoloboke.defaultValue()) {
                throw new AssertionError(this.kolobokeIntKeysForMap[i] + " not in map");
            }
        }
        if (this.intIntKoloboke.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.intIntKoloboke.size());
        }
    }
}
```

### Method 75

```java
@Benchmark
public void kolobokeGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.intIntKoloboke.get(this.kolobokeIntKeysForMap[i]) == this.intIntKoloboke.defaultValue()) {
                throw new AssertionError(this.kolobokeIntKeysForMap[i] + " not in map");
            }
        }
        if (this.intIntKoloboke.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.intIntKoloboke.size());
        }
    }
}
```

### Method 76

```java
@Benchmark
public void kolobokeGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.intIntKoloboke.get(this.kolobokeIntKeysForMap[i]) == this.intIntKoloboke.defaultValue()) {
                throw new AssertionError(this.kolobokeIntKeysForMap[i] + " not in map");
            }
        }
        if (this.intIntKoloboke.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.intIntKoloboke.size());
        }
    }
}
```

### Method 77

```java
@Benchmark
public void kolobokeGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.longLongKoloboke.get(this.kolobokeLongKeysForMap[i]) == this.longLongKoloboke.defaultValue()) {
                throw new AssertionError(this.kolobokeLongKeysForMap[i] + " not in map");
            }
        }
        if (this.longLongKoloboke.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.longLongKoloboke.size());
        }
    }
}
```

### Method 78

```java
@Benchmark
public void kolobokeGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.longLongKoloboke.get(this.kolobokeLongKeysForMap[i]) == this.longLongKoloboke.defaultValue()) {
                throw new AssertionError(this.kolobokeLongKeysForMap[i] + " not in map");
            }
        }
        if (this.longLongKoloboke.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.longLongKoloboke.size());
        }
    }
}
```

### Method 79

```java
@Benchmark
public void kolobokeGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.longLongKoloboke.get(this.kolobokeLongKeysForMap[i]) == this.longLongKoloboke.defaultValue()) {
                throw new AssertionError(this.kolobokeLongKeysForMap[i] + " not in map");
            }
        }
        if (this.longLongKoloboke.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.longLongKoloboke.size());
        }
    }
}
```

### Method 80

```java
@Benchmark
public void kolobokeGet() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        for (int i = 0; i < KEY_COUNT; i++) {
            if (this.longLongKoloboke.get(this.kolobokeLongKeysForMap[i]) == this.longLongKoloboke.defaultValue()) {
                throw new AssertionError(this.kolobokeLongKeysForMap[i] + " not in map");
            }
        }
        if (this.longLongKoloboke.size() != KEY_COUNT) {
            throw new AssertionError("size is " + this.longLongKoloboke.size());
        }
    }
}
```

### Method 81

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 82

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 83

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 84

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeIntKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 85

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 86

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 87

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 88

```java
@Benchmark
public void kolobokePut() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(MAP_SIZE);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.put(this.kolobokeLongKeysForMap[i], 4);
        }
        if (newMap.size() != KEY_COUNT) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 89

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 90

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 91

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 92

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        IntIntMap newMap = HashIntIntMaps.newMutableMap(this.intIntKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeIntKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 93

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeLongKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 94

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeLongKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 95

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeLongKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 96

```java
@Benchmark
public void kolobokeRemove() {
    for (int j = 0; j < LOOP_COUNT; j++) {
        LongLongMap newMap = HashLongLongMaps.newMutableMap(this.longLongKoloboke);
        for (int i = 0; i < KEY_COUNT; i++) {
            newMap.remove(this.kolobokeLongKeysForMap[i]);
        }
        if (!newMap.isEmpty()) {
            throw new AssertionError("size is " + newMap.size());
        }
    }
}
```

### Method 97

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public MutableList<Integer> serial_eager_ec_hand_coded() {
    FastList<Integer> list = new FastList<>();
    int size = this.integersEC.size();
    for (int i = 0; i < size; i++) {
        Integer integer = this.integersEC.get(i);
        if (integer % 10_000 != 0 && (Integer.valueOf(String.valueOf(integer)) + 1) % 10_000 != 0) {
            list.add(integer);
        }
    }
    Verify.assertSize(999_800, list);
    return list;
}
```

### Method 98

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void copyTest(Blackhole blackHole) {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        MutableLongIntMap newMap = new LongIntHashMap(this.longIntMap);
        blackHole.consume(newMap.get(0));
    }
}
```

### Method 99

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void get(Blackhole blackHole) {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        for (int i = 0; i < this.mapSizeDividedBy16000 * 64; i++) {
            blackHole.consume(this.longIntMap.get(this.randomLongsForMap[i]));
        }
    }
}
```

### Method 100

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void get(Blackhole blackHole) {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        for (int i = 0; i < this.mapSizeDividedBy16000 * 64; i++) {
            blackHole.consume(this.longIntMap.get(this.randomLongsForMap[i]));
        }
    }
}
```

### Method 101

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void get(Blackhole blackHole) {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy64 / 64; j++) {
        for (int i = 0; i < this.mapSizeDividedBy64 * 64; i++) {
            blackHole.consume(this.intIntMap.get(this.randomIntsForKeys[i]));
        }
    }
}
```

### Method 102

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void get(Blackhole blackHole) {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy64 / 64; j++) {
        for (int i = 0; i < this.mapSizeDividedBy64 * 64; i++) {
            blackHole.consume(this.intIntMap.get(this.randomIntsForKeys[i]));
        }
    }
}
```

### Method 103

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void presizedPut() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        MutableLongIntMap newMap = new LongIntHashMap(this.mapSizeDividedBy16000);
        for (int i = 0; i < this.mapSizeDividedBy16000 * 64; i++) {
            newMap.put(this.randomLongsForMap[i], this.randomIntegersForMap[i]);
        }
    }
}
```

### Method 104

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void presizedPut() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        MutableLongIntMap newMap = new LongIntHashMap(this.mapSizeDividedBy16000);
        for (int i = 0; i < this.mapSizeDividedBy16000 * 64; i++) {
            newMap.put(this.randomLongsForMap[i], this.randomIntegersForMap[i]);
        }
    }
}
```

### Method 105

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void presizedPut() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy64 / 64; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(this.mapSizeDividedBy64);
        for (int i = 0; i < this.mapSizeDividedBy64 * 64; i++) {
            newMap.put(this.randomIntsForKeys[i], this.randomIntsForValues[i]);
        }
    }
}
```

### Method 106

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void presizedPut() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy64 / 64; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(this.mapSizeDividedBy64);
        for (int i = 0; i < this.mapSizeDividedBy64 * 64; i++) {
            newMap.put(this.randomIntsForKeys[i], this.randomIntsForValues[i]);
        }
    }
}
```

### Method 107

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void put() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        MutableLongIntMap newMap = new LongIntHashMap();
        for (int i = 0; i < this.mapSizeDividedBy16000 * 64; i++) {
            newMap.put(this.randomLongsForMap[i], this.randomIntegersForMap[i]);
        }
    }
}
```

### Method 108

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void put() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        MutableLongIntMap newMap = new LongIntHashMap();
        for (int i = 0; i < this.mapSizeDividedBy16000 * 64; i++) {
            newMap.put(this.randomLongsForMap[i], this.randomIntegersForMap[i]);
        }
    }
}
```

### Method 109

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void put() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy64 / 64; j++) {
        MutableIntIntMap newMap = new IntIntHashMap();
        for (int i = 0; i < this.mapSizeDividedBy64 * 64; i++) {
            newMap.put(this.randomIntsForKeys[i], this.randomIntsForValues[i]);
        }
    }
}
```

### Method 110

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void put() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy64 / 64; j++) {
        MutableIntIntMap newMap = new IntIntHashMap();
        for (int i = 0; i < this.mapSizeDividedBy64 * 64; i++) {
            newMap.put(this.randomIntsForKeys[i], this.randomIntsForValues[i]);
        }
    }
}
```

### Method 111

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void remove() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        MutableLongIntMap newMap = new LongIntHashMap(this.longIntMap);
        for (int i = 0; i < this.mapSizeDividedBy16000 * 64; i++) {
            newMap.remove(this.randomLongsForMap[i]);
        }
    }
}
```

### Method 112

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void remove() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy16000 / 64; j++) {
        MutableLongIntMap newMap = new LongIntHashMap(this.longIntMap);
        for (int i = 0; i < this.mapSizeDividedBy16000 * 64; i++) {
            newMap.remove(this.randomLongsForMap[i]);
        }
    }
}
```

### Method 113

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void remove() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy64 / 64; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(this.intIntMap);
        for (int i = 0; i < this.mapSizeDividedBy64 * 64; i++) {
            newMap.remove(this.randomIntsForKeys[i]);
        }
    }
}
```

### Method 114

```java
@Warmup(iterations = 20)
@Measurement(iterations = 10)
@Benchmark
public void remove() {
    for (int j = 0; j < 10_000_000 / this.mapSizeDividedBy64 / 64; j++) {
        MutableIntIntMap newMap = new IntIntHashMap(this.intIntMap);
        for (int i = 0; i < this.mapSizeDividedBy64 * 64; i++) {
            newMap.remove(this.randomIntsForKeys[i]);
        }
    }
}
```

## JMH IGNORED STATIC METHOD RETURN - Static method return not used or consumed by a Blackhole.

### Method 1

```java
@Benchmark
public IntList filterJDKIntStreamParallelToEC() {
    return IntStream.of(this.ints).parallel().filter(i -> i % 2 == 0).collect(IntLists.mutable::empty, MutableIntList::add, MutableIntList::addAll);
}
```

### Method 2

```java
@Benchmark
public IntList mapJDKIntStreamParallelToEC() {
    return IntStream.of(this.ints).parallel().map(i -> i * 2).collect(IntLists.mutable::empty, MutableIntList::add, MutableIntList::addAll);
}
```

### Method 3

```java
@Benchmark
public long arrayList_arrayListIterate_forEach() {
    LongAdder adder = new LongAdder();
    ArrayListIterate.forEach(this.arrayList, adder::add);
    return adder.longValue();
}
```

### Method 4

```java
@Benchmark
public long arrayList_iterate_forEach() {
    LongAdder adder = new LongAdder();
    Iterate.forEach(this.arrayList, adder::add);
    return adder.longValue();
}
```

### Method 5

```java
@Benchmark
public long cowal_iterate_forEach() {
    LongAdder adder = new LongAdder();
    Iterate.forEach(this.cowaList, adder::add);
    return adder.longValue();
}
```

### Method 6

```java
@Benchmark
public long cowal_listIterate_forEach() {
    LongAdder adder = new LongAdder();
    ListIterate.forEach(this.cowaList, adder::add);
    return adder.longValue();
}
```

### Method 7

```java
@Benchmark
public long synchArrayList_iterate_forEach() {
    LongAdder adder = new LongAdder();
    Iterate.forEach(this.synchArrayList, adder::add);
    return adder.longValue();
}
```

### Method 8

```java
@Benchmark
public long synchArrayList_listIterate_forEach() {
    LongAdder adder = new LongAdder();
    ListIterate.forEach(this.synchArrayList, adder::add);
    return adder.longValue();
}
```

