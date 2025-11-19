## JMH IGNORED METHOD RETURN - Method return not used or consumed by a Blackhole.

### Method 1 (false alert)

```java
/**
 * Benchmark decoding a list of DependencyLink objects from a JSON array.
 */
@Benchmark
public Collection<DependencyLink> decodeList() {
    // Clear the collection to ensure the decoder populates it from scratch.
    decodeListResult.clear();
    decoder.decodeList(listLinkBytes, decodeListResult);
    // Return the collection to keep the work observable to the JMH harness.
    return decodeListResult;
}
```

### Method 2 (

```java
/**
 * Benchmark for {@link StrictTraceId#filterTraces(Iterable)}.
 */
@Benchmark
public List<List<Span>> benchFilterTracesByIds() {
    Mapper<List<List<Span>>, List<List<Span>>> mapper = StrictTraceId.filterTraces(filterTraceIds);
    List<List<Span>> copy = new ArrayList<>(traces.size());
    for (List<Span> trace : traces) {
        copy.add(new ArrayList<>(trace));
    }
    return mapper.map(copy);
}
```

### Method 3

```java
/**
 * Benchmark for {@link StrictTraceId#filterTraces(QueryRequest)}.
 */
@Benchmark
public List<List<Span>> benchFilterTracesIfClashOnLowerTraceId() {
    Mapper<List<List<Span>>, List<List<Span>>> mapper = StrictTraceId.filterTraces(dummyRequest);
    List<List<Span>> copy = new ArrayList<>(traces.size());
    for (List<Span> trace : traces) {
        copy.add(new ArrayList<>(trace));
    }
    return mapper.map(copy);
}
```

### Method 4

```java
/**
 * Benchmark the core serialization routine.
 */
@Benchmark
public void serializeBulkPayload() {
    ByteBuf payload = BulkCallBuilder.serialize(allocator, entry, shouldAddType);
    // Release the buffer to avoid memory leaks during the benchmark.
    payload.release();
}
```

### Method 5

```java
/**
 * Benchmark the cost of building a {@link Span} from a fully populated builder.
 */
@Benchmark
public Span buildSpan() {
    // Clone the builder to avoid mutating the shared instance.
    Span.Builder b = builder.clone();
    // Simulate a tiny change that would be typical in a real workload.
    b.timestamp(System.nanoTime());
    return b.build();
}
```

### Method 6

```java
/**
 * Benchmark the cost of storing a batch of spans.
 */
@Benchmark
public void benchmarkAccept() throws Exception {
    // Each iteration stores a fresh copy to avoid mutation side‑effects.
    List<Span> copy = new ArrayList<>(spansBatch);
    Call<Void> call = storage.accept(copy);
    call.execute();
}
```

### Method 7

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public void parseDependencyLink(Blackhole bh) throws IOException {
    try (JsonParser parser = FACTORY.createParser(dependencyLinkJson)) {
        // advance to START_OBJECT
        parser.nextToken();
        DependencyLink link = JsonSerializers.DEPENDENCY_LINK_PARSER.parse(parser);
        bh.consume(link);
    }
}
```

### Method 8

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public void parseSpan(Blackhole bh) throws IOException {
    try (JsonParser parser = FACTORY.createParser(spanJson)) {
        // advance to START_OBJECT
        parser.nextToken();
        Span span = JsonSerializers.SPAN_PARSER.parse(parser);
        bh.consume(span);
    }
}
```

### Method 9

```java
@Benchmark
public DependencyLinker benchmarkPutTrace() {
    DependencyLinker freshLinker = new DependencyLinker(Logger.getLogger(DependencyLinker.class.getName()));
    freshLinker.putTrace(spans);
    return freshLinker;
}
```

### Method 10

```java
@Benchmark
public void md5Hashing(Blackhole bh) {
    writerEnabled.writeDocument(span, sink);
    ByteBuf slice = buffer.slice(0, buffer.writerIndex());
    String hash = BulkIndexWriter.md5(slice);
    bh.consume(hash);
    buffer.clear();
}
```

### Method 11

```java
@Benchmark
public void md5Hashing(Blackhole bh) {
    writerEnabled.writeDocument(span, sink);
    ByteBuf slice = buffer.slice(0, buffer.writerIndex());
    String hash = BulkIndexWriter.md5(slice);
    bh.consume(hash);
    buffer.clear();
}
```

### Method 12

```java
@Benchmark
public void sizeBooleanField() {
    BOOLEAN_FIELD.sizeInBytes(boolValue);
}
```

### Method 13

```java
@Benchmark
public void sizeFixed64Field() {
    FIXED64_FIELD.sizeInBytes(longValue);
}
```

### Method 14

```java
@Benchmark
public void sizeHexField() {
    HEX_FIELD.sizeInBytes(hexString);
}
```

### Method 15

```java
@Benchmark
public void sizeUtf8Field() {
    UTF8_FIELD.sizeInBytes(utf8String);
}
```

### Method 16

```java
@Benchmark
public void sizeVarintInt() {
    VARINT_FIELD.sizeInBytes(intValue);
}
```

### Method 17

```java
@Benchmark
public void sizeVarintLong() {
    VARINT_FIELD.sizeInBytes(longValue);
}
```

### Method 18

```java
@Benchmark
public void writeFixed32Field() {
    // Fixed32Field does not expose a write method; benchmark its size calculation.
    FIXED32_FIELD.sizeInBytes(int32Value);
}
```

### Method 19

```java
@Benchmark
public void writeSpanWithSearch(Blackhole bh) {
    String id = writerEnabled.writeDocument(span, sink);
    bh.consume(id);
    buffer.clear();
}
```

### Method 20

```java
@Benchmark
public void writeSpanWithoutSearch(Blackhole bh) {
    String id = writerDisabled.writeDocument(span, sink);
    bh.consume(id);
    buffer.clear();
}
```

## JMH UNSINKED VARIABLE - Unsinked variable inside benchmark method

### Method 1

```java
/**
 * Benchmark fetching all known service names.
 */
@Benchmark
public List<String> benchmarkGetServiceNames() throws Exception {
    Call<List<String>> call = storage.getServiceNames();
    return call.execute();
}
```

### Method 2

```java
/**
 * Benchmark for {@link StrictTraceId#filterSpans(String)}.
 */
@Benchmark
public List<Span> benchFilterSpans() {
    Mapper<List<Span>, List<Span>> mapper = StrictTraceId.filterSpans(targetTraceId);
    List<Span> copy = new ArrayList<>(spans);
    return mapper.map(copy);
}
```

### Method 3

```java
/**
 * Benchmark for {@link StrictTraceId#filterTraces(Iterable)}.
 */
@Benchmark
public List<List<Span>> benchFilterTracesByIds() {
    Mapper<List<List<Span>>, List<List<Span>>> mapper = StrictTraceId.filterTraces(filterTraceIds);
    List<List<Span>> copy = new ArrayList<>(traces.size());
    for (List<Span> trace : traces) {
        copy.add(new ArrayList<>(trace));
    }
    return mapper.map(copy);
}
```

### Method 4

```java
/**
 * Benchmark for {@link StrictTraceId#filterTraces(QueryRequest)}.
 */
@Benchmark
public List<List<Span>> benchFilterTracesIfClashOnLowerTraceId() {
    Mapper<List<List<Span>>, List<List<Span>>> mapper = StrictTraceId.filterTraces(dummyRequest);
    List<List<Span>> copy = new ArrayList<>(traces.size());
    for (List<Span> trace : traces) {
        copy.add(new ArrayList<>(trace));
    }
    return mapper.map(copy);
}
```

### Method 5

```java
/**
 * Benchmark retrieving a trace by its ID.
 */
@Benchmark
public List<Span> benchmarkGetTrace() throws Exception {
    Call<List<Span>> call = storage.getTrace(sampleTraceId);
    return call.execute();
}
```

### Method 6

```java
/**
 * Benchmark the core serialization routine.
 */
@Benchmark
public void serializeBulkPayload() {
    ByteBuf payload = BulkCallBuilder.serialize(allocator, entry, shouldAddType);
    // Release the buffer to avoid memory leaks during the benchmark.
    payload.release();
}
```

### Method 7

```java
/**
 * Benchmark the cost of building a {@link Span} from a fully populated builder.
 */
@Benchmark
public Span buildSpan() {
    // Clone the builder to avoid mutating the shared instance.
    Span.Builder b = builder.clone();
    // Simulate a tiny change that would be typical in a real workload.
    b.timestamp(System.nanoTime());
    return b.build();
}
```

### Method 8

```java
/**
 * Benchmark the cost of storing a batch of spans.
 */
@Benchmark
public void benchmarkAccept() throws Exception {
    // Each iteration stores a fresh copy to avoid mutation side‑effects.
    List<Span> copy = new ArrayList<>(spansBatch);
    Call<Void> call = storage.accept(copy);
    call.execute();
}
```

### Method 9

```java
/**
 * Benchmark the {@code invalidate} method.
 *
 * <p>Invalidates a randomly chosen key. This helps understand the cost of removal
 * under concurrent load.
 */
@Benchmark
public void invalidate(Blackhole bh) {
    int idx = ThreadLocalRandom.current().nextInt(distinctKeys);
    Integer key = keys[idx];
    limiter.invalidate(key);
    bh.consume(key);
}
```

### Method 10

```java
/**
 * Benchmark the {@code shouldInvoke} method.
 *
 * <p>Each invocation picks a key in a pseudo‑random fashion to simulate realistic
 * contention while avoiding hot‑spot bias.
 */
@Benchmark
public void shouldInvoke(Blackhole bh) {
    // Use a cheap round‑robin index combined with ThreadLocalRandom for better distribution.
    int idx = Math.abs(roundRobin.getAndIncrement() + ThreadLocalRandom.current().nextInt(distinctKeys)) % distinctKeys;
    Integer key = keys[idx];
    boolean allowed = limiter.shouldInvoke(key);
    bh.consume(allowed);
}
```

### Method 11

```java
/**
 * Helper benchmark to measure the cost of converting the input to UTF‑8 bytes.
 * This is used by {@link JsonEscaper#jsonEscapedSizeInBytes} when non‑ASCII characters are present.
 */
@Benchmark
public void utf8SizeInBytes(BenchmarkState state, Blackhole bh) {
    // WriteBuffer.utf8SizeInBytes is not public; we approximate using standard UTF‑8 encoding.
    byte[] bytes = state.input.toString().getBytes(StandardCharsets.UTF_8);
    bh.consume(bytes.length);
}
```

### Method 12

```java
@Benchmark
public SpanNode buildTree() {
    SpanNode.Builder builder = SpanNode.newBuilder(BENCHMARK_LOGGER);
    return builder.build(spans);
}
```

## JMH STATE FINAL STATIC PRIMITIVE - JMH State primitive static field declared final.

### Method 1

```java
package zipkin2.codec;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.TimeUnit;
import zipkin2.DependencyLink;
import zipkin.server.*;
import zipkin2.codec.*;
import zipkin2.collector.*;
import zipkin2.elasticsearch.*;
import zipkin2.elasticsearch.internal.*;
import zipkin2.elasticsearch.internal.client.*;
import zipkin2.internal.*;
import zipkin2.server.internal.*;
import zipkin2.server.internal.activemq.*;
import zipkin2.server.internal.banner.*;
import zipkin2.server.internal.brave.*;
import zipkin2.server.internal.cassandra3.*;
import zipkin2.server.internal.elasticsearch.*;
import zipkin2.server.internal.health.*;
import zipkin2.server.internal.kafka.*;
import zipkin2.server.internal.mysql.*;
import zipkin2.server.internal.prometheus.*;
import zipkin2.server.internal.rabbitmq.*;
import zipkin2.server.internal.scribe.*;
import zipkin2.server.internal.throttle.*;
import zipkin2.server.internal.ui.*;
import zipkin2.storage.*;
import zipkin2.storage.cassandra.*;
import zipkin2.storage.cassandra.internal.*;
import zipkin2.storage.cassandra.internal.call.*;
import zipkin2.v1.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link DependencyLinkBytesDecoder.JSON_V1}.
 *
 * <p>These benchmarks measure the throughput of JSON decoding for a single {@link DependencyLink}
 * and for a list of {@link DependencyLink}s. The data set is generated once per thread to avoid
 * allocation overhead during the measurement phase.
 *
 * <p>Typical usage:
 *
 * <pre>
 *   mvn clean install -DskipTests
 *   java -jar target/benchmarks.jar -prof gc
 * </pre>
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 3, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Thread)
public class DependencyLinkBytesDecoderBenchmark {

    /**
     * Number of links in the list payload used for the list benchmark.
     */
    private static final int LIST_SIZE = 1000;

    /**
     * JSON representation of a single DependencyLink.
     */
    private byte[] singleLinkBytes;

    /**
     * JSON representation of a list of DependencyLink objects.
     */
    private byte[] listLinkBytes;

    /**
     * Decoder under test.
     */
    private final DependencyLinkBytesDecoder decoder = DependencyLinkBytesDecoder.JSON_V1;

    /**
     * Reusable collection for the list decode benchmark to avoid allocation inside the measured code.
     */
    private Collection<DependencyLink> decodeListResult;

    /**
     * Prepare JSON payloads before each benchmark thread starts.
     */
    @Setup(Level.Trial)
    public void setUp() {
        // Build a deterministic DependencyLink instance.
        DependencyLink link = DependencyLink.newBuilder().parent("serviceA").child("serviceB").callCount(12345L).errorCount(67L).build();
        // Serialize the single link using the same codec to guarantee a realistic payload.
        // The codec does not provide a serializer, so we construct the JSON manually.
        String singleJson = String.format("{\"parent\":\"%s\",\"child\":\"%s\",\"callCount\":%d,\"errorCount\":%d}", link.parent(), link.child(), link.callCount(), link.errorCount());
        this.singleLinkBytes = singleJson.getBytes(java.nio.charset.StandardCharsets.UTF_8);
        // Build a JSON array containing LIST_SIZE copies of the same link.
        StringBuilder sb = new StringBuilder();
        sb.append('[');
        for (int i = 0; i < LIST_SIZE; i++) {
            if (i > 0)
                sb.append(',');
            sb.append(singleJson);
        }
        sb.append(']');
        this.listLinkBytes = sb.toString().getBytes(java.nio.charset.StandardCharsets.UTF_8);
        // Allocate the collection once; the decoder will clear and reuse it.
        this.decodeListResult = new ArrayList<>(LIST_SIZE);
    }

    /**
     * Benchmark decoding a single DependencyLink from JSON bytes.
     */
    @Benchmark
    public DependencyLink decodeOne() {
        // The decoder returns a new object each call; returning it prevents dead‑code elimination.
        return decoder.decodeOne(singleLinkBytes);
    }

    /**
     * Benchmark decoding a list of DependencyLink objects from a JSON array.
     */
    @Benchmark
    public Collection<DependencyLink> decodeList() {
        // Clear the collection to ensure the decoder populates it from scratch.
        decodeListResult.clear();
        decoder.decodeList(listLinkBytes, decodeListResult);
        // Return the collection to keep the work observable to the JMH harness.
        return decodeListResult;
    }
}
```

### Method 2

```java
package zipkin2.elasticsearch.internal;

import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonParser;
import java.util.List;
import java.util.concurrent.TimeUnit;
import zipkin.server.*;
import zipkin2.codec.*;
import zipkin2.collector.*;
import zipkin2.elasticsearch.*;
import zipkin2.elasticsearch.internal.client.*;
import zipkin2.internal.*;
import zipkin2.server.internal.*;
import zipkin2.server.internal.activemq.*;
import zipkin2.server.internal.banner.*;
import zipkin2.server.internal.brave.*;
import zipkin2.server.internal.cassandra3.*;
import zipkin2.server.internal.elasticsearch.*;
import zipkin2.server.internal.health.*;
import zipkin2.server.internal.kafka.*;
import zipkin2.server.internal.mysql.*;
import zipkin2.server.internal.prometheus.*;
import zipkin2.server.internal.rabbitmq.*;
import zipkin2.server.internal.scribe.*;
import zipkin2.server.internal.throttle.*;
import zipkin2.server.internal.ui.*;
import zipkin2.storage.*;
import zipkin2.storage.cassandra.*;
import zipkin2.storage.cassandra.internal.*;
import zipkin2.storage.cassandra.internal.call.*;
import zipkin2.v1.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link JsonReaders}. The benchmarks focus on throughput, i.e. how many
 * operations can be performed per time unit. Each benchmark creates a fresh {@link JsonParser}
 * to avoid state leakage between iterations.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 2)
@Threads(1)
@State(Scope.Benchmark)
public class JsonReadersBenchmark {

    /**
     * Sample JSON used for all benchmarks.
     */
    private static final String SAMPLE_JSON = "{\n" + "  \"path1\": {\n" + "    \"field\": \"value1\",\n" + "    \"nested\": {\"target\": \"found\"}\n" + "  },\n" + "  \"path2\": {\n" + "    \"field\": \"value2\",\n" + "    \"array\": [\n" + "      {\"name\": \"alice\"},\n" + "      {\"name\": \"bob\"},\n" + "      {\"name\": \"carol\"}\n" + "    ]\n" + "  },\n" + "  \"collect\": [\n" + "    {\"name\": \"alice\"},\n" + "    {\"name\": \"bob\"},\n" + "    {\"name\": \"alice\"},\n" + "    {\"name\": \"dave\"}\n" + "  ]\n" + "}";

    private JsonFactory factory;

    @Setup(Level.Trial)
    public void setUp() {
        factory = new JsonFactory();
    }

    /**
     * Helper that creates a new parser positioned at the start of the JSON document.
     */
    private JsonParser newParser() throws Exception {
        JsonParser parser = factory.createParser(SAMPLE_JSON);
        // Move to the first token (START_OBJECT) so that JsonReaders methods can work directly.
        parser.nextToken();
        return parser;
    }

    @Benchmark
    public void benchmarkEnterPathSingle(Blackhole bh) throws Exception {
        try (JsonParser parser = newParser()) {
            JsonParser result = JsonReaders.enterPath(parser, "path1");
            bh.consume(result);
        }
    }

    @Benchmark
    public void benchmarkEnterPathDouble(Blackhole bh) throws Exception {
        try (JsonParser parser = newParser()) {
            JsonParser result = JsonReaders.enterPath(parser, "path1", "path2");
            bh.consume(result);
        }
    }

    @Benchmark
    public void benchmarkCollectValuesNamed(Blackhole bh) throws Exception {
        try (JsonParser parser = newParser()) {
            List<String> names = JsonReaders.collectValuesNamed(parser, "name");
            bh.consume(names);
        }
    }

    @Benchmark
    public void benchmarkCheckStartObjectTrue(Blackhole bh) throws Exception {
        try (JsonParser parser = newParser()) {
            boolean ok = JsonReaders.checkStartObject(parser, true);
            bh.consume(ok);
        }
    }

    @Benchmark
    public void benchmarkCheckStartObjectFalse(Blackhole bh) throws Exception {
        try (JsonParser parser = newParser()) {
            boolean ok = JsonReaders.checkStartObject(parser, false);
            bh.consume(ok);
        }
    }
}
```

### Method 3

```java
package zipkin2.elasticsearch;

import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonParser;
import java.util.concurrent.TimeUnit;
import java.util.function.Supplier;
import zipkin2.elasticsearch.ElasticsearchVersion.Parser;
import zipkin.server.*;
import zipkin2.codec.*;
import zipkin2.collector.*;
import zipkin2.elasticsearch.*;
import zipkin2.elasticsearch.internal.*;
import zipkin2.elasticsearch.internal.client.*;
import zipkin2.internal.*;
import zipkin2.server.internal.*;
import zipkin2.server.internal.activemq.*;
import zipkin2.server.internal.banner.*;
import zipkin2.server.internal.brave.*;
import zipkin2.server.internal.cassandra3.*;
import zipkin2.server.internal.elasticsearch.*;
import zipkin2.server.internal.health.*;
import zipkin2.server.internal.kafka.*;
import zipkin2.server.internal.mysql.*;
import zipkin2.server.internal.prometheus.*;
import zipkin2.server.internal.rabbitmq.*;
import zipkin2.server.internal.scribe.*;
import zipkin2.server.internal.throttle.*;
import zipkin2.server.internal.ui.*;
import zipkin2.storage.*;
import zipkin2.storage.cassandra.*;
import zipkin2.storage.cassandra.internal.*;
import zipkin2.storage.cassandra.internal.call.*;
import zipkin2.v1.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * Benchmark for {@link Parser#convert(JsonParser, Supplier)}.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Benchmark)
public class ElasticsearchVersionBenchmark {

    /**
     * Sample Elasticsearch node info JSON containing the version number.
     */
    private static final String SAMPLE_JSON = "{\"version\":{\"number\":\"7.10.2\"}}";

    private JsonFactory jsonFactory;

    private Supplier<String> contentSupplier;

    @Setup(Level.Trial)
    public void setUp() {
        jsonFactory = new JsonFactory();
        // Supplier returns the raw JSON string; used only when parsing fails.
        contentSupplier = () -> SAMPLE_JSON;
    }

    /**
     * Benchmarks the conversion of a JSON response into an {@link ElasticsearchVersion}.
     *
     * <p>The benchmark creates a fresh {@link JsonParser} for each invocation to emulate the real
     * usage pattern where a parser is obtained per HTTP response.
     */
    @Benchmark
    public ElasticsearchVersion parseVersion() throws Exception {
        try (JsonParser parser = jsonFactory.createParser(SAMPLE_JSON)) {
            return Parser.INSTANCE.convert(parser, contentSupplier);
        }
    }
}
```

### Method 4

```java
package zipkin2.internal;

import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import zipkin2.DependencyLink;
import zipkin.server.*;
import zipkin2.codec.*;
import zipkin2.collector.*;
import zipkin2.elasticsearch.*;
import zipkin2.elasticsearch.internal.*;
import zipkin2.elasticsearch.internal.client.*;
import zipkin2.server.internal.*;
import zipkin2.server.internal.activemq.*;
import zipkin2.server.internal.banner.*;
import zipkin2.server.internal.brave.*;
import zipkin2.server.internal.cassandra3.*;
import zipkin2.server.internal.elasticsearch.*;
import zipkin2.server.internal.health.*;
import zipkin2.server.internal.kafka.*;
import zipkin2.server.internal.mysql.*;
import zipkin2.server.internal.prometheus.*;
import zipkin2.server.internal.rabbitmq.*;
import zipkin2.server.internal.scribe.*;
import zipkin2.server.internal.throttle.*;
import zipkin2.server.internal.ui.*;
import zipkin2.storage.*;
import zipkin2.storage.cassandra.*;
import zipkin2.storage.cassandra.internal.*;
import zipkin2.storage.cassandra.internal.call.*;
import zipkin2.v1.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link Dependencies} serialization and deserialization.
 *
 * The benchmarks measure throughput (operations per second) for:
 *   1. Serializing a {@link Dependencies} instance to Thrift binary format.
 *   2. Deserializing a Thrift binary payload back to a {@link Dependencies} instance.
 *
 * Best‑practice notes:
 *   • State is scoped to a single thread to avoid contention.
 *   • Data is prepared in {@link Setup(Level.Trial)} so that allocation of the test
 *     payload does not affect the measured operation.
 *   • {@link Blackhole} is used to consume results and prevent dead‑code elimination.
 *   • Warm‑up, measurement, and fork parameters follow common JMH recommendations.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(value = 3, jvmArgsAppend = { "-XX:+UnlockDiagnosticVMOptions", "-XX:+PrintCompilation" })
@State(Scope.Thread)
public class DependenciesBenchmark {

    /**
     * Number of {@link DependencyLink} objects in the test payload.
     */
    private static final int LINK_COUNT = 1_000;

    /**
     * The object under test.
     */
    private Dependencies dependencies;

    /**
     * Serialized representation of {@code dependencies}.
     */
    private ByteBuffer serialized;

    /**
     * Prepare a realistic {@link Dependencies} instance and its Thrift payload.
     */
    @Setup(Level.Trial)
    public void setUp() {
        List<DependencyLink> links = new ArrayList<>(LINK_COUNT);
        for (int i = 0; i < LINK_COUNT; i++) {
            DependencyLink link = DependencyLink.newBuilder().parent("service-" + (i % 10)).child("service-" + ((i + 1) % 10)).callCount(100 + i).errorCount(// occasional errors
            i % 5 == 0 ? 1 : 0).build();
            links.add(link);
        }
        dependencies = Dependencies.create(System.currentTimeMillis() - TimeUnit.HOURS.toMillis(1), System.currentTimeMillis(), links);
        // Pre‑serialize once; the buffer will be reused for the deserialization benchmark.
        serialized = dependencies.toThrift();
    }

    /**
     * Benchmark the serialization path: {@code Dependencies#toThrift()}.
     */
    @Benchmark
    public ByteBuffer serialize() {
        // Each call creates a fresh byte[] as per the implementation – this is the cost we want to measure.
        return dependencies.toThrift();
    }

    /**
     * Benchmark the deserialization path: {@code Dependencies#fromThrift(ByteBuffer)}.
     */
    @Benchmark
    public void deserialize(Blackhole bh) {
        // The method returns a new Dependencies instance; we feed it to Blackhole to avoid dead‑code elimination.
        Dependencies d = Dependencies.fromThrift(serialized);
        bh.consume(d);
    }

    /**
     * Benchmark the size calculation: {@code Dependencies#sizeInBytes()}.
     */
    @Benchmark
    public int sizeInBytes() {
        return dependencies.sizeInBytes();
    }
}
```

### Method 5

```java
package zipkin2.internal;

import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collection;
import java.util.concurrent.TimeUnit;
import zipkin2.Span;
import zipkin.server.*;
import zipkin2.codec.*;
import zipkin2.collector.*;
import zipkin2.elasticsearch.*;
import zipkin2.elasticsearch.internal.*;
import zipkin2.elasticsearch.internal.client.*;
import zipkin2.server.internal.*;
import zipkin2.server.internal.activemq.*;
import zipkin2.server.internal.banner.*;
import zipkin2.server.internal.brave.*;
import zipkin2.server.internal.cassandra3.*;
import zipkin2.server.internal.elasticsearch.*;
import zipkin2.server.internal.health.*;
import zipkin2.server.internal.kafka.*;
import zipkin2.server.internal.mysql.*;
import zipkin2.server.internal.prometheus.*;
import zipkin2.server.internal.rabbitmq.*;
import zipkin2.server.internal.scribe.*;
import zipkin2.server.internal.throttle.*;
import zipkin2.server.internal.ui.*;
import zipkin2.storage.*;
import zipkin2.storage.cassandra.*;
import zipkin2.storage.cassandra.internal.*;
import zipkin2.storage.cassandra.internal.call.*;
import zipkin2.v1.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link V1JsonSpanReader}. The benchmarks focus on the
 * throughput of parsing a typical Zipkin V1 JSON payload both for a single
 * span and for a list of spans.
 *
 * <p>Best‑practice notes:
 * <ul>
 *   <li>State is {@code Scope.Thread} to avoid contention.</li>
 *   <li>All mutable objects are created in {@link #setup()} and reused.</li>
 *   <li>Results are consumed via {@link Blackhole} to prevent dead‑code elimination.</li>
 *   <li>Warm‑up and measurement iterations are configured to give stable numbers.</li>
 * </ul>
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class V1JsonSpanReaderBenchmark {

    /**
     * JSON representation of a single typical Zipkin V1 span.
     */
    private static final String SINGLE_SPAN_JSON = "{" + "\"traceId\":\"463ac35c9f6413ad48485a3953bb6124\"," + "\"id\":\"a2fb4a1d1a96d312\"," + "\"name\":\"get\"," + "\"parentId\":\"0000000000000000\"," + "\"timestamp\":1472470996199000," + "\"duration\":207000," + "\"annotations\":[" + "  {\"timestamp\":1472470996199000,\"value\":\"cs\",\"endpoint\":{" + "    \"serviceName\":\"frontend\",\"ipv4\":\"127.0.0.1\",\"port\":9000}}" + "]," + "\"binaryAnnotations\":[" + "  {\"key\":\"http.path\",\"value\":\"/api\",\"endpoint\":{" + "    \"serviceName\":\"frontend\",\"ipv4\":\"127.0.0.1\",\"port\":9000}}" + "]," + "\"debug\":false" + "}";

    /**
     * Number of spans in the generated list payload.
     */
    private static final int LIST_SIZE = 1000;

    private String spanListJson;

    private byte[] singleSpanBytes;

    private byte[] listSpanBytes;

    private V1JsonSpanReader reader;

    private Collection<Span> outputCollection;

    @Setup(Level.Trial)
    public void setup() {
        // Build a JSON array containing LIST_SIZE copies of SINGLE_SPAN_JSON.
        StringBuilder sb = new StringBuilder();
        sb.append('[');
        for (int i = 0; i < LIST_SIZE; i++) {
            if (i > 0)
                sb.append(',');
            sb.append(SINGLE_SPAN_JSON);
        }
        sb.append(']');
        spanListJson = sb.toString();
        // Prepare byte arrays for fast buffer creation.
        singleSpanBytes = SINGLE_SPAN_JSON.getBytes(StandardCharsets.UTF_8);
        listSpanBytes = spanListJson.getBytes(StandardCharsets.UTF_8);
        // Initialise the reader and the output collection.
        reader = new V1JsonSpanReader();
        outputCollection = new ArrayList<>(LIST_SIZE);
    }

    @Benchmark
    public V1Span parseSingleSpan(Blackhole bh) throws Exception {
        // Create a fresh ReadBuffer for each iteration.
        ReadBuffer buffer = ReadBuffer.wrap(singleSpanBytes);
        V1Span result = reader.fromJson(new JsonCodec.JsonReader(buffer));
        bh.consume(result);
        return result;
    }

    @Benchmark
    public boolean parseSpanList(Blackhole bh) throws Exception {
        // Fresh buffer and cleared collection for each iteration.
        ReadBuffer buffer = ReadBuffer.wrap(listSpanBytes);
        outputCollection.clear();
        boolean ok = reader.readList(buffer, outputCollection);
        bh.consume(outputCollection);
        return ok;
    }
}
```

### Method 6

```java
package zipkin2.internal;

import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collection;
import java.util.concurrent.TimeUnit;
import zipkin2.Span;
import zipkin.server.*;
import zipkin2.codec.*;
import zipkin2.collector.*;
import zipkin2.elasticsearch.*;
import zipkin2.elasticsearch.internal.*;
import zipkin2.elasticsearch.internal.client.*;
import zipkin2.server.internal.*;
import zipkin2.server.internal.activemq.*;
import zipkin2.server.internal.banner.*;
import zipkin2.server.internal.brave.*;
import zipkin2.server.internal.cassandra3.*;
import zipkin2.server.internal.elasticsearch.*;
import zipkin2.server.internal.health.*;
import zipkin2.server.internal.kafka.*;
import zipkin2.server.internal.mysql.*;
import zipkin2.server.internal.prometheus.*;
import zipkin2.server.internal.rabbitmq.*;
import zipkin2.server.internal.scribe.*;
import zipkin2.server.internal.throttle.*;
import zipkin2.server.internal.ui.*;
import zipkin2.storage.*;
import zipkin2.storage.cassandra.*;
import zipkin2.storage.cassandra.internal.*;
import zipkin2.storage.cassandra.internal.call.*;
import zipkin2.v1.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link V1JsonSpanReader}. The benchmarks focus on the
 * throughput of parsing a typical Zipkin V1 JSON payload both for a single
 * span and for a list of spans.
 *
 * <p>Best‑practice notes:
 * <ul>
 *   <li>State is {@code Scope.Thread} to avoid contention.</li>
 *   <li>All mutable objects are created in {@link #setup()} and reused.</li>
 *   <li>Results are consumed via {@link Blackhole} to prevent dead‑code elimination.</li>
 *   <li>Warm‑up and measurement iterations are configured to give stable numbers.</li>
 * </ul>
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class V1JsonSpanReaderBenchmark {

    /**
     * JSON representation of a single typical Zipkin V1 span.
     */
    private static final String SINGLE_SPAN_JSON = "{" + "\"traceId\":\"463ac35c9f6413ad48485a3953bb6124\"," + "\"id\":\"a2fb4a1d1a96d312\"," + "\"name\":\"get\"," + "\"parentId\":\"0000000000000000\"," + "\"timestamp\":1472470996199000," + "\"duration\":207000," + "\"annotations\":[" + "  {\"timestamp\":1472470996199000,\"value\":\"cs\",\"endpoint\":{" + "    \"serviceName\":\"frontend\",\"ipv4\":\"127.0.0.1\",\"port\":9000}}" + "]," + "\"binaryAnnotations\":[" + "  {\"key\":\"http.path\",\"value\":\"/api\",\"endpoint\":{" + "    \"serviceName\":\"frontend\",\"ipv4\":\"127.0.0.1\",\"port\":9000}}" + "]," + "\"debug\":false" + "}";

    /**
     * Number of spans in the generated list payload.
     */
    private static final int LIST_SIZE = 1000;

    private String spanListJson;

    private byte[] singleSpanBytes;

    private byte[] listSpanBytes;

    private V1JsonSpanReader reader;

    private Collection<Span> outputCollection;

    @Setup(Level.Trial)
    public void setup() {
        // Build a JSON array containing LIST_SIZE copies of SINGLE_SPAN_JSON.
        StringBuilder sb = new StringBuilder();
        sb.append('[');
        for (int i = 0; i < LIST_SIZE; i++) {
            if (i > 0)
                sb.append(',');
            sb.append(SINGLE_SPAN_JSON);
        }
        sb.append(']');
        spanListJson = sb.toString();
        // Prepare byte arrays for fast buffer creation.
        singleSpanBytes = SINGLE_SPAN_JSON.getBytes(StandardCharsets.UTF_8);
        listSpanBytes = spanListJson.getBytes(StandardCharsets.UTF_8);
        // Initialise the reader and the output collection.
        reader = new V1JsonSpanReader();
        outputCollection = new ArrayList<>(LIST_SIZE);
    }

    @Benchmark
    public V1Span parseSingleSpan(Blackhole bh) throws Exception {
        // Create a fresh ReadBuffer for each iteration.
        ReadBuffer buffer = ReadBuffer.wrap(singleSpanBytes);
        V1Span result = reader.fromJson(new JsonCodec.JsonReader(buffer));
        bh.consume(result);
        return result;
    }

    @Benchmark
    public boolean parseSpanList(Blackhole bh) throws Exception {
        // Fresh buffer and cleared collection for each iteration.
        ReadBuffer buffer = ReadBuffer.wrap(listSpanBytes);
        outputCollection.clear();
        boolean ok = reader.readList(buffer, outputCollection);
        bh.consume(outputCollection);
        return ok;
    }
}
```

### Method 7

```java
package zipkin2.internal;

import java.util.concurrent.TimeUnit;
import zipkin.server.*;
import zipkin2.codec.*;
import zipkin2.collector.*;
import zipkin2.elasticsearch.*;
import zipkin2.elasticsearch.internal.*;
import zipkin2.elasticsearch.internal.client.*;
import zipkin2.internal.*;
import zipkin2.server.internal.*;
import zipkin2.server.internal.activemq.*;
import zipkin2.server.internal.banner.*;
import zipkin2.server.internal.brave.*;
import zipkin2.server.internal.cassandra3.*;
import zipkin2.server.internal.elasticsearch.*;
import zipkin2.server.internal.health.*;
import zipkin2.server.internal.kafka.*;
import zipkin2.server.internal.mysql.*;
import zipkin2.server.internal.prometheus.*;
import zipkin2.server.internal.rabbitmq.*;
import zipkin2.server.internal.scribe.*;
import zipkin2.server.internal.throttle.*;
import zipkin2.server.internal.ui.*;
import zipkin2.storage.*;
import zipkin2.storage.cassandra.*;
import zipkin2.storage.cassandra.internal.*;
import zipkin2.storage.cassandra.internal.call.*;
import zipkin2.v1.*;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.infra.*;

/**
 * JMH benchmarks for {@link WriteBuffer}. Measures throughput of the most
 * frequently used write operations and size calculation helpers.
 */
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
@State(Scope.Thread)
public class WriteBufferBenchmark {

    // Buffer large enough for all benchmarked writes
    private static final int BUFFER_SIZE = 1024;

    private WriteBuffer buffer;

    private byte[] backing;

    // Test data
    private String asciiString;

    private String utf8String;

    private long longValue;

    private int intValue;

    @Setup(Level.Trial)
    public void setUpTrial() {
        backing = new byte[BUFFER_SIZE];
        asciiString = "The quick brown fox jumps over the lazy dog 1234567890";
        // Include multi-byte UTF‑8 characters and surrogate pairs
        utf8String = "こんにちは世界 🌍🚀";
        // Long.MAX_VALUE
        longValue = 9_223_372_036_854_775_807L;
        // large positive int
        intValue = 0x7F_FF_FF_FF;
    }

    @Setup(Level.Invocation)
    public void setUpInvocation() {
        // Reset buffer position before each invocation
        buffer = WriteBuffer.wrap(backing, 0);
    }

    // -------------------------------------------------------------------------
    // Write operations
    // -------------------------------------------------------------------------
    @Benchmark
    public WriteBuffer writeAsciiLong() {
        buffer.writeAscii(longValue);
        return buffer;
    }

    @Benchmark
    public WriteBuffer writeAsciiString() {
        buffer.writeAscii(asciiString);
        return buffer;
    }

    @Benchmark
    public WriteBuffer writeUtf8String() {
        buffer.writeUtf8(utf8String);
        return buffer;
    }

    @Benchmark
    public WriteBuffer writeVarintInt() {
        buffer.writeVarint(intValue);
        return buffer;
    }

    @Benchmark
    public WriteBuffer writeVarintLong() {
        buffer.writeVarint(longValue);
        return buffer;
    }

    @Benchmark
    public WriteBuffer writeLongHex() {
        buffer.writeLongHex(longValue);
        return buffer;
    }

    // -------------------------------------------------------------------------
    // Size calculation helpers (pure functions, no buffer mutation)
    // -------------------------------------------------------------------------
    @Benchmark
    public int asciiSizeInBytes() {
        return WriteBuffer.asciiSizeInBytes(longValue);
    }

    @Benchmark
    public int utf8SizeInBytes() {
        return WriteBuffer.utf8SizeInBytes(utf8String);
    }

    @Benchmark
    public int varintSizeInBytesInt() {
        return WriteBuffer.varintSizeInBytes(intValue);
    }

    @Benchmark
    public int varintSizeInBytesLong() {
        return WriteBuffer.varintSizeInBytes(longValue);
    }
}
```

## JMH LOOP INSIDE BENCHMARK - Usage of loops in the JMH benchmark function.

### Method 1

```java
/**
 * Benchmark for {@link StrictTraceId#filterTraces(Iterable)}.
 */
@Benchmark
public List<List<Span>> benchFilterTracesByIds() {
    Mapper<List<List<Span>>, List<List<Span>>> mapper = StrictTraceId.filterTraces(filterTraceIds);
    List<List<Span>> copy = new ArrayList<>(traces.size());
    for (List<Span> trace : traces) {
        copy.add(new ArrayList<>(trace));
    }
    return mapper.map(copy);
}
```

### Method 2

```java
/**
 * Benchmark for {@link StrictTraceId#filterTraces(QueryRequest)}.
 */
@Benchmark
public List<List<Span>> benchFilterTracesIfClashOnLowerTraceId() {
    Mapper<List<List<Span>>, List<List<Span>>> mapper = StrictTraceId.filterTraces(dummyRequest);
    List<List<Span>> copy = new ArrayList<>(traces.size());
    for (List<Span> trace : traces) {
        copy.add(new ArrayList<>(trace));
    }
    return mapper.map(copy);
}
```

### Method 3

```java
/**
 * Benchmark the serialization of a list of Spans.
 */
@Benchmark
public byte[] benchmarkWriteList() {
    byte[][] results = new byte[spanList.size()][];
    for (int i = 0; i < spanList.size(); i++) {
        results[i] = codec.write(spanList.get(i));
    }
    return results[0];
}
```

### Method 4

```java
/**
 * Benchmarks the conversion of a JSON response into an {@link ElasticsearchVersion}.
 *
 * <p>The benchmark creates a fresh {@link JsonParser} for each invocation to emulate the real
 * usage pattern where a parser is obtained per HTTP response.
 */
@Benchmark
public ElasticsearchVersion parseVersion() throws Exception {
    try (JsonParser parser = jsonFactory.createParser(SAMPLE_JSON)) {
        return Parser.INSTANCE.convert(parser, contentSupplier);
    }
}
```

### Method 5

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public void parseDependencyLink(Blackhole bh) throws IOException {
    try (JsonParser parser = FACTORY.createParser(dependencyLinkJson)) {
        // advance to START_OBJECT
        parser.nextToken();
        DependencyLink link = JsonSerializers.DEPENDENCY_LINK_PARSER.parse(parser);
        bh.consume(link);
    }
}
```

### Method 6

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public void parseDependencyLink(Blackhole bh) throws IOException {
    try (JsonParser parser = FACTORY.createParser(dependencyLinkJson)) {
        // advance to START_OBJECT
        parser.nextToken();
        DependencyLink link = JsonSerializers.DEPENDENCY_LINK_PARSER.parse(parser);
        bh.consume(link);
    }
}
```

### Method 7

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public void parseSpan(Blackhole bh) throws IOException {
    try (JsonParser parser = FACTORY.createParser(spanJson)) {
        // advance to START_OBJECT
        parser.nextToken();
        Span span = JsonSerializers.SPAN_PARSER.parse(parser);
        bh.consume(span);
    }
}
```

### Method 8

```java
@Benchmark
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 10, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(2)
public void parseSpan(Blackhole bh) throws IOException {
    try (JsonParser parser = FACTORY.createParser(spanJson)) {
        // advance to START_OBJECT
        parser.nextToken();
        Span span = JsonSerializers.SPAN_PARSER.parse(parser);
        bh.consume(span);
    }
}
```

### Method 9

```java
@Benchmark
public void benchmarkCheckStartObjectFalse(Blackhole bh) throws Exception {
    try (JsonParser parser = newParser()) {
        boolean ok = JsonReaders.checkStartObject(parser, false);
        bh.consume(ok);
    }
}
```

### Method 10

```java
@Benchmark
public void benchmarkCheckStartObjectFalse(Blackhole bh) throws Exception {
    try (JsonParser parser = newParser()) {
        boolean ok = JsonReaders.checkStartObject(parser, false);
        bh.consume(ok);
    }
}
```

### Method 11

```java
@Benchmark
public void benchmarkCheckStartObjectTrue(Blackhole bh) throws Exception {
    try (JsonParser parser = newParser()) {
        boolean ok = JsonReaders.checkStartObject(parser, true);
        bh.consume(ok);
    }
}
```

### Method 12

```java
@Benchmark
public void benchmarkCheckStartObjectTrue(Blackhole bh) throws Exception {
    try (JsonParser parser = newParser()) {
        boolean ok = JsonReaders.checkStartObject(parser, true);
        bh.consume(ok);
    }
}
```

### Method 13

```java
@Benchmark
public void benchmarkCollectValuesNamed(Blackhole bh) throws Exception {
    try (JsonParser parser = newParser()) {
        List<String> names = JsonReaders.collectValuesNamed(parser, "name");
        bh.consume(names);
    }
}
```

### Method 14

```java
@Benchmark
public void benchmarkCollectValuesNamed(Blackhole bh) throws Exception {
    try (JsonParser parser = newParser()) {
        List<String> names = JsonReaders.collectValuesNamed(parser, "name");
        bh.consume(names);
    }
}
```

### Method 15

```java
@Benchmark
public void benchmarkEnterPathDouble(Blackhole bh) throws Exception {
    try (JsonParser parser = newParser()) {
        JsonParser result = JsonReaders.enterPath(parser, "path1", "path2");
        bh.consume(result);
    }
}
```

### Method 16

```java
@Benchmark
public void benchmarkEnterPathDouble(Blackhole bh) throws Exception {
    try (JsonParser parser = newParser()) {
        JsonParser result = JsonReaders.enterPath(parser, "path1", "path2");
        bh.consume(result);
    }
}
```

### Method 17

```java
@Benchmark
public void benchmarkEnterPathSingle(Blackhole bh) throws Exception {
    try (JsonParser parser = newParser()) {
        JsonParser result = JsonReaders.enterPath(parser, "path1");
        bh.consume(result);
    }
}
```

### Method 18

```java
@Benchmark
public void benchmarkEnterPathSingle(Blackhole bh) throws Exception {
    try (JsonParser parser = newParser()) {
        JsonParser result = JsonReaders.enterPath(parser, "path1");
        bh.consume(result);
    }
}
```

## JMH FIXTURE USING INVOCATION SCOPE - Fixture methods configured with Invocation scope. 

### Method 1

```java
@Setup(Level.Invocation)
public void setUpInvocation() {
    // Reset buffer position before each invocation
    buffer = WriteBuffer.wrap(backing, 0);
}
```

