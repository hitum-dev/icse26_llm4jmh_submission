## JMH STATE FINAL STATIC PRIMITIVE - JMH State primitive static field declared final.

### Method 1

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2.collector;

import io.micrometer.core.instrument.MeterRegistry;
import io.micrometer.prometheus.PrometheusConfig;
import io.micrometer.prometheus.PrometheusMeterRegistry;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import zipkin2.server.internal.MicrometerCollectorMetrics;

@Measurement(iterations = 80, time = 1)
@Warmup(iterations = 20, time = 1)
@Fork(3)
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(1)
public class MetricsBenchmarks {
  static final int LONG_SPAN = 5000;
  static final int MEDIUM_SPAN = 1000;
  static final int SHORT_SPAN = 500;
  private MeterRegistry registry = new PrometheusMeterRegistry(PrometheusConfig.DEFAULT);
  private InMemoryCollectorMetrics inMemoryCollectorMetrics = new InMemoryCollectorMetrics();
  private MicrometerCollectorMetrics micrometerCollectorMetrics = new MicrometerCollectorMetrics(registry);

  @Benchmark
  public int incrementBytes_longSpans_inMemory() {
    return incrementBytes(inMemoryCollectorMetrics, LONG_SPAN);
  }

  @Benchmark
  public int incrementBytes_longSpans_Actuate() {
    return incrementBytes(micrometerCollectorMetrics, LONG_SPAN);
  }

  @Benchmark
  public int incrementBytes_mediumSpans_inMemory() {
    return incrementBytes(inMemoryCollectorMetrics, MEDIUM_SPAN);
  }

  @Benchmark
  public int incrementBytes_mediumSpans_Actuate() {
    return incrementBytes(micrometerCollectorMetrics, MEDIUM_SPAN);
  }

  @Benchmark
  public int incrementBytes_shortSpans_inMemory() {
    return incrementBytes(inMemoryCollectorMetrics, SHORT_SPAN);
  }

  @Benchmark
  public int incrementBytes_shortSpans_Actuate() {
    return incrementBytes(micrometerCollectorMetrics, SHORT_SPAN);
  }

  private int incrementBytes(CollectorMetrics collectorMetrics, int bytes) {
    collectorMetrics.incrementBytes(bytes);
    return bytes;
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .include(".*" + MetricsBenchmarks.class.getSimpleName() + ".*")
      .threads(40)
      .build();

    new Runner(opt).run();
  }
}
```

### Method 2

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2.collector;

import io.micrometer.core.instrument.MeterRegistry;
import io.micrometer.prometheus.PrometheusConfig;
import io.micrometer.prometheus.PrometheusMeterRegistry;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import zipkin2.server.internal.MicrometerCollectorMetrics;

@Measurement(iterations = 80, time = 1)
@Warmup(iterations = 20, time = 1)
@Fork(3)
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(1)
public class MetricsBenchmarks {
  static final int LONG_SPAN = 5000;
  static final int MEDIUM_SPAN = 1000;
  static final int SHORT_SPAN = 500;
  private MeterRegistry registry = new PrometheusMeterRegistry(PrometheusConfig.DEFAULT);
  private InMemoryCollectorMetrics inMemoryCollectorMetrics = new InMemoryCollectorMetrics();
  private MicrometerCollectorMetrics micrometerCollectorMetrics = new MicrometerCollectorMetrics(registry);

  @Benchmark
  public int incrementBytes_longSpans_inMemory() {
    return incrementBytes(inMemoryCollectorMetrics, LONG_SPAN);
  }

  @Benchmark
  public int incrementBytes_longSpans_Actuate() {
    return incrementBytes(micrometerCollectorMetrics, LONG_SPAN);
  }

  @Benchmark
  public int incrementBytes_mediumSpans_inMemory() {
    return incrementBytes(inMemoryCollectorMetrics, MEDIUM_SPAN);
  }

  @Benchmark
  public int incrementBytes_mediumSpans_Actuate() {
    return incrementBytes(micrometerCollectorMetrics, MEDIUM_SPAN);
  }

  @Benchmark
  public int incrementBytes_shortSpans_inMemory() {
    return incrementBytes(inMemoryCollectorMetrics, SHORT_SPAN);
  }

  @Benchmark
  public int incrementBytes_shortSpans_Actuate() {
    return incrementBytes(micrometerCollectorMetrics, SHORT_SPAN);
  }

  private int incrementBytes(CollectorMetrics collectorMetrics, int bytes) {
    collectorMetrics.incrementBytes(bytes);
    return bytes;
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .include(".*" + MetricsBenchmarks.class.getSimpleName() + ".*")
      .threads(40)
      .build();

    new Runner(opt).run();
  }
}
```

### Method 3

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2.collector;

import io.micrometer.core.instrument.MeterRegistry;
import io.micrometer.prometheus.PrometheusConfig;
import io.micrometer.prometheus.PrometheusMeterRegistry;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import zipkin2.server.internal.MicrometerCollectorMetrics;

@Measurement(iterations = 80, time = 1)
@Warmup(iterations = 20, time = 1)
@Fork(3)
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(1)
public class MetricsBenchmarks {
  static final int LONG_SPAN = 5000;
  static final int MEDIUM_SPAN = 1000;
  static final int SHORT_SPAN = 500;
  private MeterRegistry registry = new PrometheusMeterRegistry(PrometheusConfig.DEFAULT);
  private InMemoryCollectorMetrics inMemoryCollectorMetrics = new InMemoryCollectorMetrics();
  private MicrometerCollectorMetrics micrometerCollectorMetrics = new MicrometerCollectorMetrics(registry);

  @Benchmark
  public int incrementBytes_longSpans_inMemory() {
    return incrementBytes(inMemoryCollectorMetrics, LONG_SPAN);
  }

  @Benchmark
  public int incrementBytes_longSpans_Actuate() {
    return incrementBytes(micrometerCollectorMetrics, LONG_SPAN);
  }

  @Benchmark
  public int incrementBytes_mediumSpans_inMemory() {
    return incrementBytes(inMemoryCollectorMetrics, MEDIUM_SPAN);
  }

  @Benchmark
  public int incrementBytes_mediumSpans_Actuate() {
    return incrementBytes(micrometerCollectorMetrics, MEDIUM_SPAN);
  }

  @Benchmark
  public int incrementBytes_shortSpans_inMemory() {
    return incrementBytes(inMemoryCollectorMetrics, SHORT_SPAN);
  }

  @Benchmark
  public int incrementBytes_shortSpans_Actuate() {
    return incrementBytes(micrometerCollectorMetrics, SHORT_SPAN);
  }

  private int incrementBytes(CollectorMetrics collectorMetrics, int bytes) {
    collectorMetrics.incrementBytes(bytes);
    return bytes;
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .include(".*" + MetricsBenchmarks.class.getSimpleName() + ".*")
      .threads(40)
      .build();

    new Runner(opt).run();
  }
}
```

### Method 4

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2.internal;

import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

@Measurement(iterations = 5, time = 1)
@Warmup(iterations = 10, time = 1)
@Fork(3)
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(1)
public class WriteBufferBenchmarks {
  static final Charset UTF_8 = Charset.forName("UTF-8");
  // Order id = d07c4daa-0fa9-4c03-90b1-e06c4edae250 doesn't exist
  static final String CHINESE_UTF8 = "订单d07c4daa-0fa9-4c03-90b1-e06c4edae250不存在";
  static final int CHINESE_UTF8_SIZE = UTF_8.encode(CHINESE_UTF8).remaining();
  /* length-prefixing a 1 KiB span */
  static final int TEST_INT = 1024;
  /* epoch micros timestamp */
  static final long TEST_LONG = 1472470996199000L;
  byte[] bytes = new byte[8];
  WriteBuffer buffer = WriteBuffer.wrap(bytes);

  @Benchmark public int utf8SizeInBytes_chinese() {
    return WriteBuffer.utf8SizeInBytes(CHINESE_UTF8);
  }

  @Benchmark public byte[] writeUtf8_chinese() {
    byte[] bytesUtf8 = new byte[CHINESE_UTF8_SIZE];
    WriteBuffer.wrap(bytesUtf8, 0).writeUtf8(CHINESE_UTF8);
    return bytesUtf8;
  }

  @Benchmark public ByteBuffer writeUtf8_chinese_jdk() {
    return UTF_8.encode(CHINESE_UTF8);
  }

  @Benchmark public int varIntSizeInBytes_32() {
    return WriteBuffer.varintSizeInBytes(TEST_INT);
  }

  @Benchmark public int varIntSizeInBytes_64() {
    return WriteBuffer.varintSizeInBytes(TEST_LONG);
  }

  @Benchmark public int writeVarint_32() {
    buffer.writeVarint(TEST_INT);
    return buffer.pos();
  }

  @Benchmark public int writeVarint_64() {
    buffer.writeVarint(TEST_LONG);
    return buffer.pos();
  }

  @Benchmark public int writeLongLe() {
    buffer.writeLongLe(TEST_LONG);
    return buffer.pos();
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .include(".*" + WriteBufferBenchmarks.class.getSimpleName() + ".*")
      .build();

    new Runner(opt).run();
  }
}
```

### Method 5

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2.internal;

import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

@Measurement(iterations = 5, time = 1)
@Warmup(iterations = 10, time = 1)
@Fork(3)
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(1)
public class WriteBufferBenchmarks {
  static final Charset UTF_8 = Charset.forName("UTF-8");
  // Order id = d07c4daa-0fa9-4c03-90b1-e06c4edae250 doesn't exist
  static final String CHINESE_UTF8 = "订单d07c4daa-0fa9-4c03-90b1-e06c4edae250不存在";
  static final int CHINESE_UTF8_SIZE = UTF_8.encode(CHINESE_UTF8).remaining();
  /* length-prefixing a 1 KiB span */
  static final int TEST_INT = 1024;
  /* epoch micros timestamp */
  static final long TEST_LONG = 1472470996199000L;
  byte[] bytes = new byte[8];
  WriteBuffer buffer = WriteBuffer.wrap(bytes);

  @Benchmark public int utf8SizeInBytes_chinese() {
    return WriteBuffer.utf8SizeInBytes(CHINESE_UTF8);
  }

  @Benchmark public byte[] writeUtf8_chinese() {
    byte[] bytesUtf8 = new byte[CHINESE_UTF8_SIZE];
    WriteBuffer.wrap(bytesUtf8, 0).writeUtf8(CHINESE_UTF8);
    return bytesUtf8;
  }

  @Benchmark public ByteBuffer writeUtf8_chinese_jdk() {
    return UTF_8.encode(CHINESE_UTF8);
  }

  @Benchmark public int varIntSizeInBytes_32() {
    return WriteBuffer.varintSizeInBytes(TEST_INT);
  }

  @Benchmark public int varIntSizeInBytes_64() {
    return WriteBuffer.varintSizeInBytes(TEST_LONG);
  }

  @Benchmark public int writeVarint_32() {
    buffer.writeVarint(TEST_INT);
    return buffer.pos();
  }

  @Benchmark public int writeVarint_64() {
    buffer.writeVarint(TEST_LONG);
    return buffer.pos();
  }

  @Benchmark public int writeLongLe() {
    buffer.writeLongLe(TEST_LONG);
    return buffer.pos();
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .include(".*" + WriteBufferBenchmarks.class.getSimpleName() + ".*")
      .build();

    new Runner(opt).run();
  }
}
```

### Method 6

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2.internal;

import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

@Measurement(iterations = 5, time = 1)
@Warmup(iterations = 10, time = 1)
@Fork(3)
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(1)
public class WriteBufferBenchmarks {
  static final Charset UTF_8 = Charset.forName("UTF-8");
  // Order id = d07c4daa-0fa9-4c03-90b1-e06c4edae250 doesn't exist
  static final String CHINESE_UTF8 = "订单d07c4daa-0fa9-4c03-90b1-e06c4edae250不存在";
  static final int CHINESE_UTF8_SIZE = UTF_8.encode(CHINESE_UTF8).remaining();
  /* length-prefixing a 1 KiB span */
  static final int TEST_INT = 1024;
  /* epoch micros timestamp */
  static final long TEST_LONG = 1472470996199000L;
  byte[] bytes = new byte[8];
  WriteBuffer buffer = WriteBuffer.wrap(bytes);

  @Benchmark public int utf8SizeInBytes_chinese() {
    return WriteBuffer.utf8SizeInBytes(CHINESE_UTF8);
  }

  @Benchmark public byte[] writeUtf8_chinese() {
    byte[] bytesUtf8 = new byte[CHINESE_UTF8_SIZE];
    WriteBuffer.wrap(bytesUtf8, 0).writeUtf8(CHINESE_UTF8);
    return bytesUtf8;
  }

  @Benchmark public ByteBuffer writeUtf8_chinese_jdk() {
    return UTF_8.encode(CHINESE_UTF8);
  }

  @Benchmark public int varIntSizeInBytes_32() {
    return WriteBuffer.varintSizeInBytes(TEST_INT);
  }

  @Benchmark public int varIntSizeInBytes_64() {
    return WriteBuffer.varintSizeInBytes(TEST_LONG);
  }

  @Benchmark public int writeVarint_32() {
    buffer.writeVarint(TEST_INT);
    return buffer.pos();
  }

  @Benchmark public int writeVarint_64() {
    buffer.writeVarint(TEST_LONG);
    return buffer.pos();
  }

  @Benchmark public int writeLongLe() {
    buffer.writeLongLe(TEST_LONG);
    return buffer.pos();
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .include(".*" + WriteBufferBenchmarks.class.getSimpleName() + ".*")
      .build();

    new Runner(opt).run();
  }
}
```

### Method 7

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2.internal;

import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

@Measurement(iterations = 5, time = 1)
@Warmup(iterations = 10, time = 1)
@Fork(3)
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(1)
public class WriteBufferBenchmarks {
  static final Charset UTF_8 = Charset.forName("UTF-8");
  // Order id = d07c4daa-0fa9-4c03-90b1-e06c4edae250 doesn't exist
  static final String CHINESE_UTF8 = "订单d07c4daa-0fa9-4c03-90b1-e06c4edae250不存在";
  static final int CHINESE_UTF8_SIZE = UTF_8.encode(CHINESE_UTF8).remaining();
  /* length-prefixing a 1 KiB span */
  static final int TEST_INT = 1024;
  /* epoch micros timestamp */
  static final long TEST_LONG = 1472470996199000L;
  byte[] bytes = new byte[8];
  WriteBuffer buffer = WriteBuffer.wrap(bytes);

  @Benchmark public int utf8SizeInBytes_chinese() {
    return WriteBuffer.utf8SizeInBytes(CHINESE_UTF8);
  }

  @Benchmark public byte[] writeUtf8_chinese() {
    byte[] bytesUtf8 = new byte[CHINESE_UTF8_SIZE];
    WriteBuffer.wrap(bytesUtf8, 0).writeUtf8(CHINESE_UTF8);
    return bytesUtf8;
  }

  @Benchmark public ByteBuffer writeUtf8_chinese_jdk() {
    return UTF_8.encode(CHINESE_UTF8);
  }

  @Benchmark public int varIntSizeInBytes_32() {
    return WriteBuffer.varintSizeInBytes(TEST_INT);
  }

  @Benchmark public int varIntSizeInBytes_64() {
    return WriteBuffer.varintSizeInBytes(TEST_LONG);
  }

  @Benchmark public int writeVarint_32() {
    buffer.writeVarint(TEST_INT);
    return buffer.pos();
  }

  @Benchmark public int writeVarint_64() {
    buffer.writeVarint(TEST_LONG);
    return buffer.pos();
  }

  @Benchmark public int writeLongLe() {
    buffer.writeLongLe(TEST_LONG);
    return buffer.pos();
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .include(".*" + WriteBufferBenchmarks.class.getSimpleName() + ".*")
      .build();

    new Runner(opt).run();
  }
}
```

### Method 8

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2;

import com.esotericsoftware.kryo.Kryo;
import com.esotericsoftware.kryo.io.Input;
import com.esotericsoftware.kryo.io.Output;
import com.esotericsoftware.kryo.serializers.JavaSerializer;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

import static zipkin2.internal.HexCodec.lowerHexToUnsignedLong;

@Measurement(iterations = 5, time = 1)
@Warmup(iterations = 10, time = 1)
@Fork(3)
@BenchmarkMode(Mode.SampleTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(2)
public class SpanBenchmarks {
  static final Endpoint FRONTEND =
    Endpoint.newBuilder().serviceName("frontend").ip("127.0.0.1").build();
  static final Endpoint BACKEND =
    Endpoint.newBuilder().serviceName("backend").ip("192.168.99.101").port(9000).build();
  static final Span clientSpan = buildClientSpan(Span.newBuilder());

  final Span.Builder sharedBuilder;

  public SpanBenchmarks() {
    sharedBuilder = buildClientSpan().toBuilder();
  }

  static final String traceIdHex = "86154a4ba6e91385", spanIdHex = "4d1e00c0db9010db";
  static final long traceId = lowerHexToUnsignedLong(traceIdHex);
  static final long spanId = lowerHexToUnsignedLong(spanIdHex);

  @Benchmark
  public Span buildClientSpan() {
    return buildClientSpan(Span.newBuilder());
  }

  @Benchmark
  public Span buildClientSpan_longs() {
    return buildClientSpan_longs(Span.newBuilder());
  }

  static Span buildClientSpan(Span.Builder builder) {
    return builder
      .traceId(traceIdHex)
      .parentId(traceIdHex)
      .id(spanIdHex)
      .name("get")
      .kind(Span.Kind.CLIENT)
      .localEndpoint(FRONTEND)
      .remoteEndpoint(BACKEND)
      .timestamp(1472470996199000L)
      .duration(207000L)
      .addAnnotation(1472470996238000L, "ws")
      .addAnnotation(1472470996403000L, "wr")
      .putTag("http.path", "/api")
      .putTag("clnt/finagle.version", "6.45.0")
      .build();
  }

  static Span buildClientSpan_longs(Span.Builder builder) {
    return builder
      .traceId(0L, traceId)
      .parentId(traceId)
      .id(spanId)
      .name("get")
      .kind(Span.Kind.CLIENT)
      .localEndpoint(FRONTEND)
      .remoteEndpoint(BACKEND)
      .timestamp(1472470996199000L)
      .duration(207000L)
      .addAnnotation(1472470996238000L, "ws")
      .addAnnotation(1472470996403000L, "wr")
      .putTag("http.path", "/api")
      .putTag("clnt/finagle.version", "6.45.0")
      .build();
  }

  @Benchmark
  public Span buildClientSpan_clear() {
    return buildClientSpan(sharedBuilder.clear());
  }

  @Benchmark
  public Span buildClientSpan_clone() {
    return sharedBuilder.clone().build();
  }

  static final Kryo kryo = new Kryo();
  static final byte[] clientSpanSerialized;

  static {
    kryo.register(Span.class, new JavaSerializer());
    Output output = new Output(4096);
    kryo.writeObject(output, clientSpan);
    output.flush();
    clientSpanSerialized = output.getBuffer();
  }

  /** manually implemented with json so not as slow as normal java */
  @Benchmark
  public Span serialize_kryo() {
    return kryo.readObject(new Input(clientSpanSerialized), Span.class);
  }

  @Benchmark
  public byte[] deserialize_kryo() {
    Output output = new Output(clientSpanSerialized.length);
    kryo.writeObject(output, clientSpan);
    output.flush();
    return output.getBuffer();
  }

  @Benchmark
  public String padLeft_1Char() {
    return Span.padLeft("1", 16);
  }

  @Benchmark
  public String padLeft_15Chars() {
    return Span.padLeft("123456789012345", 16);
  }

  @Benchmark
  public String padLeft_17Chars() {
    return Span.padLeft("12345678901234567", 32);
  }

  @Benchmark
  public String padLeft_31Chars() {
    return Span.padLeft("1234567890123456789012345678901", 32);
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .include(".*" + SpanBenchmarks.class.getSimpleName() + ".*")
      .addProfiler("gc")
      .build();

    new Runner(opt).run();
  }
}
```

### Method 9

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2;

import com.esotericsoftware.kryo.Kryo;
import com.esotericsoftware.kryo.io.Input;
import com.esotericsoftware.kryo.io.Output;
import com.esotericsoftware.kryo.serializers.JavaSerializer;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

import static zipkin2.internal.HexCodec.lowerHexToUnsignedLong;

@Measurement(iterations = 5, time = 1)
@Warmup(iterations = 10, time = 1)
@Fork(3)
@BenchmarkMode(Mode.SampleTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(2)
public class SpanBenchmarks {
  static final Endpoint FRONTEND =
    Endpoint.newBuilder().serviceName("frontend").ip("127.0.0.1").build();
  static final Endpoint BACKEND =
    Endpoint.newBuilder().serviceName("backend").ip("192.168.99.101").port(9000).build();
  static final Span clientSpan = buildClientSpan(Span.newBuilder());

  final Span.Builder sharedBuilder;

  public SpanBenchmarks() {
    sharedBuilder = buildClientSpan().toBuilder();
  }

  static final String traceIdHex = "86154a4ba6e91385", spanIdHex = "4d1e00c0db9010db";
  static final long traceId = lowerHexToUnsignedLong(traceIdHex);
  static final long spanId = lowerHexToUnsignedLong(spanIdHex);

  @Benchmark
  public Span buildClientSpan() {
    return buildClientSpan(Span.newBuilder());
  }

  @Benchmark
  public Span buildClientSpan_longs() {
    return buildClientSpan_longs(Span.newBuilder());
  }

  static Span buildClientSpan(Span.Builder builder) {
    return builder
      .traceId(traceIdHex)
      .parentId(traceIdHex)
      .id(spanIdHex)
      .name("get")
      .kind(Span.Kind.CLIENT)
      .localEndpoint(FRONTEND)
      .remoteEndpoint(BACKEND)
      .timestamp(1472470996199000L)
      .duration(207000L)
      .addAnnotation(1472470996238000L, "ws")
      .addAnnotation(1472470996403000L, "wr")
      .putTag("http.path", "/api")
      .putTag("clnt/finagle.version", "6.45.0")
      .build();
  }

  static Span buildClientSpan_longs(Span.Builder builder) {
    return builder
      .traceId(0L, traceId)
      .parentId(traceId)
      .id(spanId)
      .name("get")
      .kind(Span.Kind.CLIENT)
      .localEndpoint(FRONTEND)
      .remoteEndpoint(BACKEND)
      .timestamp(1472470996199000L)
      .duration(207000L)
      .addAnnotation(1472470996238000L, "ws")
      .addAnnotation(1472470996403000L, "wr")
      .putTag("http.path", "/api")
      .putTag("clnt/finagle.version", "6.45.0")
      .build();
  }

  @Benchmark
  public Span buildClientSpan_clear() {
    return buildClientSpan(sharedBuilder.clear());
  }

  @Benchmark
  public Span buildClientSpan_clone() {
    return sharedBuilder.clone().build();
  }

  static final Kryo kryo = new Kryo();
  static final byte[] clientSpanSerialized;

  static {
    kryo.register(Span.class, new JavaSerializer());
    Output output = new Output(4096);
    kryo.writeObject(output, clientSpan);
    output.flush();
    clientSpanSerialized = output.getBuffer();
  }

  /** manually implemented with json so not as slow as normal java */
  @Benchmark
  public Span serialize_kryo() {
    return kryo.readObject(new Input(clientSpanSerialized), Span.class);
  }

  @Benchmark
  public byte[] deserialize_kryo() {
    Output output = new Output(clientSpanSerialized.length);
    kryo.writeObject(output, clientSpan);
    output.flush();
    return output.getBuffer();
  }

  @Benchmark
  public String padLeft_1Char() {
    return Span.padLeft("1", 16);
  }

  @Benchmark
  public String padLeft_15Chars() {
    return Span.padLeft("123456789012345", 16);
  }

  @Benchmark
  public String padLeft_17Chars() {
    return Span.padLeft("12345678901234567", 32);
  }

  @Benchmark
  public String padLeft_31Chars() {
    return Span.padLeft("1234567890123456789012345678901", 32);
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .include(".*" + SpanBenchmarks.class.getSimpleName() + ".*")
      .addProfiler("gc")
      .build();

    new Runner(opt).run();
  }
}
```

### Method 10

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2;

import com.esotericsoftware.kryo.Kryo;
import com.esotericsoftware.kryo.io.Input;
import com.esotericsoftware.kryo.io.Output;
import com.esotericsoftware.kryo.serializers.JavaSerializer;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

import static zipkin2.internal.HexCodec.lowerHexToUnsignedLong;

@Measurement(iterations = 5, time = 1)
@Warmup(iterations = 10, time = 1)
@Fork(3)
@BenchmarkMode(Mode.SampleTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(2)
public class SpanBenchmarks {
  static final Endpoint FRONTEND =
    Endpoint.newBuilder().serviceName("frontend").ip("127.0.0.1").build();
  static final Endpoint BACKEND =
    Endpoint.newBuilder().serviceName("backend").ip("192.168.99.101").port(9000).build();
  static final Span clientSpan = buildClientSpan(Span.newBuilder());

  final Span.Builder sharedBuilder;

  public SpanBenchmarks() {
    sharedBuilder = buildClientSpan().toBuilder();
  }

  static final String traceIdHex = "86154a4ba6e91385", spanIdHex = "4d1e00c0db9010db";
  static final long traceId = lowerHexToUnsignedLong(traceIdHex);
  static final long spanId = lowerHexToUnsignedLong(spanIdHex);

  @Benchmark
  public Span buildClientSpan() {
    return buildClientSpan(Span.newBuilder());
  }

  @Benchmark
  public Span buildClientSpan_longs() {
    return buildClientSpan_longs(Span.newBuilder());
  }

  static Span buildClientSpan(Span.Builder builder) {
    return builder
      .traceId(traceIdHex)
      .parentId(traceIdHex)
      .id(spanIdHex)
      .name("get")
      .kind(Span.Kind.CLIENT)
      .localEndpoint(FRONTEND)
      .remoteEndpoint(BACKEND)
      .timestamp(1472470996199000L)
      .duration(207000L)
      .addAnnotation(1472470996238000L, "ws")
      .addAnnotation(1472470996403000L, "wr")
      .putTag("http.path", "/api")
      .putTag("clnt/finagle.version", "6.45.0")
      .build();
  }

  static Span buildClientSpan_longs(Span.Builder builder) {
    return builder
      .traceId(0L, traceId)
      .parentId(traceId)
      .id(spanId)
      .name("get")
      .kind(Span.Kind.CLIENT)
      .localEndpoint(FRONTEND)
      .remoteEndpoint(BACKEND)
      .timestamp(1472470996199000L)
      .duration(207000L)
      .addAnnotation(1472470996238000L, "ws")
      .addAnnotation(1472470996403000L, "wr")
      .putTag("http.path", "/api")
      .putTag("clnt/finagle.version", "6.45.0")
      .build();
  }

  @Benchmark
  public Span buildClientSpan_clear() {
    return buildClientSpan(sharedBuilder.clear());
  }

  @Benchmark
  public Span buildClientSpan_clone() {
    return sharedBuilder.clone().build();
  }

  static final Kryo kryo = new Kryo();
  static final byte[] clientSpanSerialized;

  static {
    kryo.register(Span.class, new JavaSerializer());
    Output output = new Output(4096);
    kryo.writeObject(output, clientSpan);
    output.flush();
    clientSpanSerialized = output.getBuffer();
  }

  /** manually implemented with json so not as slow as normal java */
  @Benchmark
  public Span serialize_kryo() {
    return kryo.readObject(new Input(clientSpanSerialized), Span.class);
  }

  @Benchmark
  public byte[] deserialize_kryo() {
    Output output = new Output(clientSpanSerialized.length);
    kryo.writeObject(output, clientSpan);
    output.flush();
    return output.getBuffer();
  }

  @Benchmark
  public String padLeft_1Char() {
    return Span.padLeft("1", 16);
  }

  @Benchmark
  public String padLeft_15Chars() {
    return Span.padLeft("123456789012345", 16);
  }

  @Benchmark
  public String padLeft_17Chars() {
    return Span.padLeft("12345678901234567", 32);
  }

  @Benchmark
  public String padLeft_31Chars() {
    return Span.padLeft("1234567890123456789012345678901", 32);
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .include(".*" + SpanBenchmarks.class.getSimpleName() + ".*")
      .addProfiler("gc")
      .build();

    new Runner(opt).run();
  }
}
```

### Method 11

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2;

import com.esotericsoftware.kryo.Kryo;
import com.esotericsoftware.kryo.io.Input;
import com.esotericsoftware.kryo.io.Output;
import com.esotericsoftware.kryo.serializers.JavaSerializer;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

import static zipkin2.internal.HexCodec.lowerHexToUnsignedLong;

@Measurement(iterations = 5, time = 1)
@Warmup(iterations = 10, time = 1)
@Fork(3)
@BenchmarkMode(Mode.SampleTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(2)
public class SpanBenchmarks {
  static final Endpoint FRONTEND =
    Endpoint.newBuilder().serviceName("frontend").ip("127.0.0.1").build();
  static final Endpoint BACKEND =
    Endpoint.newBuilder().serviceName("backend").ip("192.168.99.101").port(9000).build();
  static final Span clientSpan = buildClientSpan(Span.newBuilder());

  final Span.Builder sharedBuilder;

  public SpanBenchmarks() {
    sharedBuilder = buildClientSpan().toBuilder();
  }

  static final String traceIdHex = "86154a4ba6e91385", spanIdHex = "4d1e00c0db9010db";
  static final long traceId = lowerHexToUnsignedLong(traceIdHex);
  static final long spanId = lowerHexToUnsignedLong(spanIdHex);

  @Benchmark
  public Span buildClientSpan() {
    return buildClientSpan(Span.newBuilder());
  }

  @Benchmark
  public Span buildClientSpan_longs() {
    return buildClientSpan_longs(Span.newBuilder());
  }

  static Span buildClientSpan(Span.Builder builder) {
    return builder
      .traceId(traceIdHex)
      .parentId(traceIdHex)
      .id(spanIdHex)
      .name("get")
      .kind(Span.Kind.CLIENT)
      .localEndpoint(FRONTEND)
      .remoteEndpoint(BACKEND)
      .timestamp(1472470996199000L)
      .duration(207000L)
      .addAnnotation(1472470996238000L, "ws")
      .addAnnotation(1472470996403000L, "wr")
      .putTag("http.path", "/api")
      .putTag("clnt/finagle.version", "6.45.0")
      .build();
  }

  static Span buildClientSpan_longs(Span.Builder builder) {
    return builder
      .traceId(0L, traceId)
      .parentId(traceId)
      .id(spanId)
      .name("get")
      .kind(Span.Kind.CLIENT)
      .localEndpoint(FRONTEND)
      .remoteEndpoint(BACKEND)
      .timestamp(1472470996199000L)
      .duration(207000L)
      .addAnnotation(1472470996238000L, "ws")
      .addAnnotation(1472470996403000L, "wr")
      .putTag("http.path", "/api")
      .putTag("clnt/finagle.version", "6.45.0")
      .build();
  }

  @Benchmark
  public Span buildClientSpan_clear() {
    return buildClientSpan(sharedBuilder.clear());
  }

  @Benchmark
  public Span buildClientSpan_clone() {
    return sharedBuilder.clone().build();
  }

  static final Kryo kryo = new Kryo();
  static final byte[] clientSpanSerialized;

  static {
    kryo.register(Span.class, new JavaSerializer());
    Output output = new Output(4096);
    kryo.writeObject(output, clientSpan);
    output.flush();
    clientSpanSerialized = output.getBuffer();
  }

  /** manually implemented with json so not as slow as normal java */
  @Benchmark
  public Span serialize_kryo() {
    return kryo.readObject(new Input(clientSpanSerialized), Span.class);
  }

  @Benchmark
  public byte[] deserialize_kryo() {
    Output output = new Output(clientSpanSerialized.length);
    kryo.writeObject(output, clientSpan);
    output.flush();
    return output.getBuffer();
  }

  @Benchmark
  public String padLeft_1Char() {
    return Span.padLeft("1", 16);
  }

  @Benchmark
  public String padLeft_15Chars() {
    return Span.padLeft("123456789012345", 16);
  }

  @Benchmark
  public String padLeft_17Chars() {
    return Span.padLeft("12345678901234567", 32);
  }

  @Benchmark
  public String padLeft_31Chars() {
    return Span.padLeft("1234567890123456789012345678901", 32);
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .include(".*" + SpanBenchmarks.class.getSimpleName() + ".*")
      .addProfiler("gc")
      .build();

    new Runner(opt).run();
  }
}
```

### Method 12

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2;

import java.net.Inet4Address;
import java.net.Inet6Address;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

@Measurement(iterations = 5, time = 1)
@Warmup(iterations = 10, time = 1)
@Fork(3)
@BenchmarkMode(Mode.SampleTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(2)
public class EndpointBenchmarks {
  static final String IPV4 = "43.0.192.2", IPV6 = "2001:db8::c001";
  static final InetAddress IPV4_ADDR, IPV6_ADDR;

  static {
    try {
      IPV4_ADDR = Inet4Address.getByName(IPV4);
      IPV6_ADDR = Inet6Address.getByName(IPV6);
    } catch (UnknownHostException e) {
      throw new AssertionError(e);
    }
  }

  Endpoint.Builder builder = Endpoint.newBuilder();

  @Benchmark public boolean parseIpv4_literal() {
    return builder.parseIp(IPV4);
  }

  @Benchmark public boolean parseIpv4_addr() {
    return builder.parseIp(IPV4_ADDR);
  }

  @Benchmark public boolean parseIpv4_bytes() {
    return builder.parseIp(IPV4_ADDR.getAddress());
  }

  @Benchmark public boolean parseIpv6_literal() {
    return builder.parseIp(IPV6);
  }

  @Benchmark public boolean parseIpv6_addr() {
    return builder.parseIp(IPV6_ADDR);
  }

  @Benchmark public boolean parseIpv6_bytes() {
    return builder.parseIp(IPV6_ADDR.getAddress());
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .addProfiler("gc")
      .include(".*" + EndpointBenchmarks.class.getSimpleName())
      .build();

    new Runner(opt).run();
  }
}
```

### Method 13

```java
/*
 * Copyright 2015-2019 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2;

import java.net.Inet4Address;
import java.net.Inet6Address;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

@Measurement(iterations = 5, time = 1)
@Warmup(iterations = 10, time = 1)
@Fork(3)
@BenchmarkMode(Mode.SampleTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(2)
public class EndpointBenchmarks {
  static final String IPV4 = "43.0.192.2", IPV6 = "2001:db8::c001";
  static final InetAddress IPV4_ADDR, IPV6_ADDR;

  static {
    try {
      IPV4_ADDR = Inet4Address.getByName(IPV4);
      IPV6_ADDR = Inet6Address.getByName(IPV6);
    } catch (UnknownHostException e) {
      throw new AssertionError(e);
    }
  }

  Endpoint.Builder builder = Endpoint.newBuilder();

  @Benchmark public boolean parseIpv4_literal() {
    return builder.parseIp(IPV4);
  }

  @Benchmark public boolean parseIpv4_addr() {
    return builder.parseIp(IPV4_ADDR);
  }

  @Benchmark public boolean parseIpv4_bytes() {
    return builder.parseIp(IPV4_ADDR.getAddress());
  }

  @Benchmark public boolean parseIpv6_literal() {
    return builder.parseIp(IPV6);
  }

  @Benchmark public boolean parseIpv6_addr() {
    return builder.parseIp(IPV6_ADDR);
  }

  @Benchmark public boolean parseIpv6_bytes() {
    return builder.parseIp(IPV6_ADDR.getAddress());
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .addProfiler("gc")
      .include(".*" + EndpointBenchmarks.class.getSimpleName())
      .build();

    new Runner(opt).run();
  }
}
```

## JMH IGNORED STATIC METHOD RETURN - Static method return not used or consumed by a Blackhole.

### Method 1

```java
@Benchmark
public HttpRequest buildAndWriteRequest_singleSpan() {
    BulkCallBuilder builder = new BulkCallBuilder(es, V6_0, "index-span");
    builder.index(spanIndex, "span", CLIENT_SPAN, BulkIndexWriter.SPAN);
    HttpCall.RequestSupplier supplier = builder.build().request;
    HttpRequestWriter request = HttpRequest.streaming(supplier.headers());
    supplier.writeBody(request::tryWrite);
    return request;
}
```

### Method 2

```java
@Benchmark
public HttpRequest buildAndWriteRequest_tenSpans() {
    BulkCallBuilder builder = new BulkCallBuilder(es, V6_0, "index-span");
    for (int i = 0; i < 10; i++) {
        builder.index(spanIndex, "span", CLIENT_SPAN, BulkIndexWriter.SPAN);
    }
    HttpCall.RequestSupplier supplier = builder.build().request;
    HttpRequestWriter request = HttpRequest.streaming(supplier.headers());
    supplier.writeBody(request::tryWrite);
    return request;
}
```

## JMH LOOP INSIDE BENCHMARK - Usage of loops in the JMH benchmark function.

### Method 1

```java
@Benchmark
public HttpRequest buildAndWriteRequest_tenSpans() {
    BulkCallBuilder builder = new BulkCallBuilder(es, V6_0, "index-span");
    for (int i = 0; i < 10; i++) {
        builder.index(spanIndex, "span", CLIENT_SPAN, BulkIndexWriter.SPAN);
    }
    HttpCall.RequestSupplier supplier = builder.build().request;
    HttpRequestWriter request = HttpRequest.streaming(supplier.headers());
    supplier.writeBody(request::tryWrite);
    return request;
}
```

### Method 2

```java
@Benchmark
public void execute_overCapacity() throws IOException {
    ThrottledCall overCapacity = (ThrottledCall) call.clone();
    ((FakeCall) overCapacity.delegate).overCapacity = true;
    try {
        overCapacity.execute();
    } catch (RejectedExecutionException e) {
        assert e == OVER_CAPACITY;
    }
}
```

## JMH STATE FINAL PRIMITIVE - JMH State primitive field declared final.

### Method 1

```java
/*
 * Copyright 2015-2020 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2.elasticsearch.internal;

import com.linecorp.armeria.common.HttpRequest;
import com.linecorp.armeria.common.HttpRequestWriter;
import io.netty.buffer.ByteBuf;
import io.netty.buffer.PooledByteBufAllocator;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import zipkin2.Span;
import zipkin2.codec.SpanBytesDecoder;
import zipkin2.elasticsearch.ElasticsearchStorage;
import zipkin2.elasticsearch.internal.BulkCallBuilder.IndexEntry;
import zipkin2.elasticsearch.internal.client.HttpCall;

import static java.nio.charset.StandardCharsets.UTF_8;
import static zipkin2.elasticsearch.ElasticsearchVersion.V6_0;
import static zipkin2.storage.cassandra.internal.Resources.resourceToString;

@Measurement(iterations = 5, time = 1)
@Warmup(iterations = 10, time = 1)
@Fork(3)
@BenchmarkMode(Mode.SampleTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(2)
public class BulkRequestBenchmarks {
  static final Span CLIENT_SPAN =
    SpanBytesDecoder.JSON_V2.decodeOne(resourceToString("/zipkin2-client.json").getBytes(UTF_8));

  final ElasticsearchStorage es = ElasticsearchStorage.newBuilder(() -> null).build();
  final long indexTimestamp = CLIENT_SPAN.timestampAsLong() / 1000L;
  final String spanIndex =
    es.indexNameFormatter().formatTypeAndTimestampForInsert("span", '-', indexTimestamp);
  final IndexEntry<Span> entry =
    BulkCallBuilder.newIndexEntry(spanIndex, "span", CLIENT_SPAN, BulkIndexWriter.SPAN);

  @Benchmark public ByteBuf writeRequest_singleSpan() {
    return BulkCallBuilder.serialize(PooledByteBufAllocator.DEFAULT, entry, true);
  }

  @Benchmark public HttpRequest buildAndWriteRequest_singleSpan() {
    BulkCallBuilder builder = new BulkCallBuilder(es, V6_0, "index-span");
    builder.index(spanIndex, "span", CLIENT_SPAN, BulkIndexWriter.SPAN);
    HttpCall.RequestSupplier supplier = builder.build().request;
    HttpRequestWriter request = HttpRequest.streaming(supplier.headers());
    supplier.writeBody(request::tryWrite);
    return request;
  }

  @Benchmark public HttpRequest buildAndWriteRequest_tenSpans() {
    BulkCallBuilder builder = new BulkCallBuilder(es, V6_0, "index-span");
    for (int i = 0; i < 10; i++) {
      builder.index(spanIndex, "span", CLIENT_SPAN, BulkIndexWriter.SPAN);
    }
    HttpCall.RequestSupplier supplier = builder.build().request;
    HttpRequestWriter request = HttpRequest.streaming(supplier.headers());
    supplier.writeBody(request::tryWrite);
    return request;
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .addProfiler("gc")
      .include(".*" + BulkRequestBenchmarks.class.getSimpleName() + ".*")
      .build();

    new Runner(opt).run();
  }
}
```

### Method 2

```java
/*
 * Copyright 2015-2020 The OpenZipkin Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
package zipkin2.elasticsearch.internal;

import com.linecorp.armeria.common.HttpRequest;
import com.linecorp.armeria.common.HttpRequestWriter;
import io.netty.buffer.ByteBuf;
import io.netty.buffer.PooledByteBufAllocator;
import java.util.concurrent.TimeUnit;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Fork;
import org.openjdk.jmh.annotations.Measurement;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.annotations.Threads;
import org.openjdk.jmh.annotations.Warmup;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import zipkin2.Span;
import zipkin2.codec.SpanBytesDecoder;
import zipkin2.elasticsearch.ElasticsearchStorage;
import zipkin2.elasticsearch.internal.BulkCallBuilder.IndexEntry;
import zipkin2.elasticsearch.internal.client.HttpCall;

import static java.nio.charset.StandardCharsets.UTF_8;
import static zipkin2.elasticsearch.ElasticsearchVersion.V6_0;
import static zipkin2.storage.cassandra.internal.Resources.resourceToString;

@Measurement(iterations = 5, time = 1)
@Warmup(iterations = 10, time = 1)
@Fork(3)
@BenchmarkMode(Mode.SampleTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
@Threads(2)
public class BulkRequestBenchmarks {
  static final Span CLIENT_SPAN =
    SpanBytesDecoder.JSON_V2.decodeOne(resourceToString("/zipkin2-client.json").getBytes(UTF_8));

  final ElasticsearchStorage es = ElasticsearchStorage.newBuilder(() -> null).build();
  final long indexTimestamp = CLIENT_SPAN.timestampAsLong() / 1000L;
  final String spanIndex =
    es.indexNameFormatter().formatTypeAndTimestampForInsert("span", '-', indexTimestamp);
  final IndexEntry<Span> entry =
    BulkCallBuilder.newIndexEntry(spanIndex, "span", CLIENT_SPAN, BulkIndexWriter.SPAN);

  @Benchmark public ByteBuf writeRequest_singleSpan() {
    return BulkCallBuilder.serialize(PooledByteBufAllocator.DEFAULT, entry, true);
  }

  @Benchmark public HttpRequest buildAndWriteRequest_singleSpan() {
    BulkCallBuilder builder = new BulkCallBuilder(es, V6_0, "index-span");
    builder.index(spanIndex, "span", CLIENT_SPAN, BulkIndexWriter.SPAN);
    HttpCall.RequestSupplier supplier = builder.build().request;
    HttpRequestWriter request = HttpRequest.streaming(supplier.headers());
    supplier.writeBody(request::tryWrite);
    return request;
  }

  @Benchmark public HttpRequest buildAndWriteRequest_tenSpans() {
    BulkCallBuilder builder = new BulkCallBuilder(es, V6_0, "index-span");
    for (int i = 0; i < 10; i++) {
      builder.index(spanIndex, "span", CLIENT_SPAN, BulkIndexWriter.SPAN);
    }
    HttpCall.RequestSupplier supplier = builder.build().request;
    HttpRequestWriter request = HttpRequest.streaming(supplier.headers());
    supplier.writeBody(request::tryWrite);
    return request;
  }

  // Convenience main entry-point
  public static void main(String[] args) throws RunnerException {
    Options opt = new OptionsBuilder()
      .addProfiler("gc")
      .include(".*" + BulkRequestBenchmarks.class.getSimpleName() + ".*")
      .build();

    new Runner(opt).run();
  }
}
```

## JMH UNSINKED VARIABLE - Unsinked variable inside benchmark method

### Method 1

```java
@Benchmark
public HttpRequest buildAndWriteRequest_singleSpan() {
    BulkCallBuilder builder = new BulkCallBuilder(es, V6_0, "index-span");
    builder.index(spanIndex, "span", CLIENT_SPAN, BulkIndexWriter.SPAN);
    HttpCall.RequestSupplier supplier = builder.build().request;
    HttpRequestWriter request = HttpRequest.streaming(supplier.headers());
    supplier.writeBody(request::tryWrite);
    return request;
}
```

### Method 2

```java
@Benchmark
public HttpRequest buildAndWriteRequest_tenSpans() {
    BulkCallBuilder builder = new BulkCallBuilder(es, V6_0, "index-span");
    for (int i = 0; i < 10; i++) {
        builder.index(spanIndex, "span", CLIENT_SPAN, BulkIndexWriter.SPAN);
    }
    HttpCall.RequestSupplier supplier = builder.build().request;
    HttpRequestWriter request = HttpRequest.streaming(supplier.headers());
    supplier.writeBody(request::tryWrite);
    return request;
}
```

### Method 3

```java
@Benchmark
public long readLong() {
    int pos = 0;
    return (longBuff[pos] & 0xffL) << 56 | (longBuff[pos + 1] & 0xffL) << 48 | (longBuff[pos + 2] & 0xffL) << 40 | (longBuff[pos + 3] & 0xffL) << 32 | (longBuff[pos + 4] & 0xffL) << 24 | (longBuff[pos + 5] & 0xffL) << 16 | (longBuff[pos + 6] & 0xffL) << 8 | (longBuff[pos + 7] & 0xffL);
}
```

### Method 4

```java
@Benchmark
public long readLong_8arity() {
    int pos = 0;
    byte[] longBuff = this.longBuff;
    return readLong(longBuff[pos] & 0xff, longBuff[pos + 1] & 0xff, longBuff[pos + 2] & 0xff, longBuff[pos + 3] & 0xff, longBuff[pos + 4] & 0xff, longBuff[pos + 5] & 0xff, longBuff[pos + 6] & 0xff, longBuff[pos + 7] & 0xff);
}
```

### Method 5

```java
@Benchmark
public long readLong_8arity_localArray() {
    int pos = 0;
    return readLong(longBuff[pos] & 0xff, longBuff[pos + 1] & 0xff, longBuff[pos + 2] & 0xff, longBuff[pos + 3] & 0xff, longBuff[pos + 4] & 0xff, longBuff[pos + 5] & 0xff, longBuff[pos + 6] & 0xff, longBuff[pos + 7] & 0xff);
}
```

### Method 6

```java
@Benchmark
public long readLong_localArray() {
    int pos = 0;
    byte[] longBuff = this.longBuff;
    return (longBuff[pos] & 0xffL) << 56 | (longBuff[pos + 1] & 0xffL) << 48 | (longBuff[pos + 2] & 0xffL) << 40 | (longBuff[pos + 3] & 0xffL) << 32 | (longBuff[pos + 4] & 0xffL) << 24 | (longBuff[pos + 5] & 0xffL) << 16 | (longBuff[pos + 6] & 0xffL) << 8 | (longBuff[pos + 7] & 0xffL);
}
```

### Method 7

```java
@Benchmark
public void execute_overCapacity() throws IOException {
    ThrottledCall overCapacity = (ThrottledCall) call.clone();
    ((FakeCall) overCapacity.delegate).overCapacity = true;
    try {
        overCapacity.execute();
    } catch (RejectedExecutionException e) {
        assert e == OVER_CAPACITY;
    }
}
```

### Method 8

```java
static long readLong(int p0, int p1, int p2, int p3, int p4, int p5, int p6, int p7) {
    return (p0 & 0xffL) << 56 | (p1 & 0xffL) << 48 | (p2 & 0xffL) << 40 | (p3 & 0xffL) << 32 | (p4 & 0xffL) << 24 | (p5 & 0xffL) << 16 | (p6 & 0xffL) << 8 | (p7 & 0xffL);
}
```

## JMH IGNORED METHOD RETURN - Method return not used or consumed by a Blackhole.

### Method 1

```java
@Benchmark
public void execute_overCapacity() throws IOException {
    ThrottledCall overCapacity = (ThrottledCall) call.clone();
    ((FakeCall) overCapacity.delegate).overCapacity = true;
    try {
        overCapacity.execute();
    } catch (RejectedExecutionException e) {
        assert e == OVER_CAPACITY;
    }
}
```

### Method 2

```java
@Benchmark
public void execute_throttled() throws IOException {
    // capacity is 1, so this will overdo it.
    call.limiter.acquire(null);
    call.clone().execute();
}
```

### Method 3

```java
@Benchmark
public void execute_throttled() throws IOException {
    // capacity is 1, so this will overdo it.
    call.limiter.acquire(null);
    call.clone().execute();
}
```

