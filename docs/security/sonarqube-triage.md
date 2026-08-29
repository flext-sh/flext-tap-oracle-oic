# Triagem SonarCloud — flext-sh/flext-tap-oracle-oic

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead: `mro-2wjm.18`

## Resumo

**28 issues** — BLOCKER 0, CRITICAL 10, MAJOR 4, MINOR 14
Tipos: VULNERABILITY 4, BUG 0, CODE_SMELL 24 · **Debt total: 156min**

| regra | issues |
|---|---|
| `python:S116` | 11 |
| `python:S1192` | 8 |
| `python:S3776` | 2 |
| `githubactions:S8233` | 2 |
| `githubactions:S8264` | 1 |
| `text:S8565` | 1 |
| `python:S7504` | 1 |
| `python:S6353` | 1 |
| `python:S5685` | 1 |

## Como usar

Cada issue traz a **mensagem do SonarQube** (descreve o problema e o impacto), o **código real** (linha `>>>`), o tipo e o effort estimado.
**Decisão**: `corrigir` / `falso-positivo` (marcar na plataforma com justificativa) / `risco-aceito`. Ordem: BLOCKER → CRITICAL → VULNERABILITY → MAJOR. CODE_SMELL em volume pede correção de padrão.

## Issues

### 1 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_tap_oracle_oic/_models/streams.py:87` · **Effort**: 14min

> Define a constant instead of duplicating this literal "Creation timestamp" 7 times.

```python
       83                      ),
       84                      th.Meltano.SingerProperty(
       85                          "created",
       86                          th.Meltano.SingerDateTimeType(),
>>>    87                          description="Creation timestamp",
       88                      ),
       89                      th.Meltano.SingerProperty(
       90                          "lastUpdated",
       91                          th.Meltano.SingerDateTimeType(),
```

**Decisão**: pendente

### 2 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_tap_oracle_oic/_models/streams.py:92` · **Effort**: 14min

> Define a constant instead of duplicating this literal "Last update timestamp" 7 times.

```python
       88                      ),
       89                      th.Meltano.SingerProperty(
       90                          "lastUpdated",
       91                          th.Meltano.SingerDateTimeType(),
>>>    92                          description="Last update timestamp",
       93                      ),
       94                      th.Meltano.SingerProperty(
       95                          "createdBy",
       96                          th.Meltano.SingerStringType(),
```

**Decisão**: pendente

### 3 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_tap_oracle_oic/_models/streams.py:97` · **Effort**: 14min

> Define a constant instead of duplicating this literal "Created by user" 7 times.

```python
       93                      ),
       94                      th.Meltano.SingerProperty(
       95                          "createdBy",
       96                          th.Meltano.SingerStringType(),
>>>    97                          description="Created by user",
       98                      ),
       99                      th.Meltano.SingerProperty(
      100                          "lastUpdatedBy",
      101                          th.Meltano.SingerStringType(),
```

**Decisão**: pendente

### 4 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_tap_oracle_oic/_models/streams.py:102` · **Effort**: 12min

> Define a constant instead of duplicating this literal "Last updated by user" 6 times.

```python
       98                      ),
       99                      th.Meltano.SingerProperty(
      100                          "lastUpdatedBy",
      101                          th.Meltano.SingerStringType(),
>>>   102                          description="Last updated by user",
      103                      ),
      104                      th.Meltano.SingerProperty(
      105                          "connections",
      106                          th.Meltano.SingerArrayType(th.Meltano.SingerObjectType()),
```

**Decisão**: pendente

### 5 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_tap_oracle_oic/_models/streams.py:142` · **Effort**: 6min

> Define a constant instead of duplicating this literal "Project ID" 3 times.

```python
      138                      ),
      139                      th.Meltano.SingerProperty(
      140                          "projectId",
      141                          th.Meltano.SingerStringType(),
>>>   142                          description="Project ID",
      143                      ),
      144                      th.Meltano.SingerProperty(
      145                          "folderId",
      146                          th.Meltano.SingerStringType(),
```

**Decisão**: pendente

### 6 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_tap_oracle_oic/_models/streams.py:246` · **Effort**: 8min

> Define a constant instead of duplicating this literal "Usage count" 4 times.

```python
      242                      ),
      243                      th.Meltano.SingerProperty(
      244                          "usageCount",
      245                          th.Meltano.SingerIntegerType(),
>>>   246                          description="Usage count",
      247                      ),
      248                      th.Meltano.SingerProperty(
      249                          "lockedBy",
      250                          th.Meltano.SingerStringType(),
```

**Decisão**: pendente

### 7 · 🟠 CRITICAL · CODE_SMELL · `python:S3776`
**Local**: `src/flext_tap_oracle_oic/models.py:222` · **Effort**: 6min

> Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed.

```python
      218                  """
      219                  _ = context
      220                  yield from ()
      221  
>>>   222              def get_url_params(
      223                  self, context: t.JsonMapping | None, next_page_token: int | None
      224              ) -> t.JsonMapping:
      225                  """Build URL parameters for Oracle OIC API requests.
      226  
```

**Decisão**: pendente

### 8 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_tap_oracle_oic/models.py:479` · **Effort**: 6min

> Define a constant instead of duplicating this literal "Received %s records" 3 times.

```python
      475              ) -> None:
      476                  """Track response metrics for monitoring and optimization."""
      477                  self.logger.debug("Response status: %s", response.status_code)
      478                  if not isinstance(data, Mapping):
>>>   479                      self.logger.debug("Received %s records", len(data))
      480                      return
      481                  envelope = self._as_oic_envelope(data)
      482                  if envelope is None:
      483                      return
```

**Decisão**: pendente

### 9 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_tap_oracle_oic/tap.py:130` · **Effort**: 8min

> Define a constant instead of duplicating this literal "OIC API request" 4 times.

```python
      126          try:
      127              response_result = self._api_client.get(url, headers=headers_result.value)
      128              if response_result.failure:
      129                  return r[FlextApiModels.Api.HttpResponse].fail_op(
>>>   130                      "OIC API request", response_result.error
      131                  )
      132              response = response_result.value
      133              if response.status_code >= c.TapOracleOic.HTTP_ERROR_STATUS_THRESHOLD:
      134                  return r[FlextApiModels.Api.HttpResponse].fail(
```

**Decisão**: pendente

### 10 · 🟠 CRITICAL · CODE_SMELL · `python:S3776`
**Local**: `src/flext_tap_oracle_oic/utilities.py:335` · **Effort**: 6min

> Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed.

```python
      331                  t.json_mapping_adapter().validate_python(settings)
      332              )
      333  
      334          @staticmethod
>>>   335          def validate_stream_config(settings: t.JsonMapping) -> p.Result[t.JsonMapping]:
      336              """Validate OIC tap stream configuration.
      337  
      338              Args:
      339              settings: Stream configuration
```

**Decisão**: pendente

### 11 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8264`
**Local**: `.github/workflows/docs.yml:18` · **Effort**: 5min

> Move this read permission from workflow level to job level.

```yaml
       14        - ".github/workflows/docs.yml"
       15    workflow_dispatch:
       16  
       17  permissions:
>>>    18    contents: read
       19    pages: write
       20    id-token: write
       21  
       22  concurrency:
```

**Decisão**: pendente

### 12 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:19` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       15    workflow_dispatch:
       16  
       17  permissions:
       18    contents: read
>>>    19    pages: write
       20    id-token: write
       21  
       22  concurrency:
       23    group: pages
```

**Decisão**: pendente

### 13 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:20` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       16  
       17  permissions:
       18    contents: read
       19    pages: write
>>>    20    id-token: write
       21  
       22  concurrency:
       23    group: pages
       24    cancel-in-progress: false
```

**Decisão**: pendente

### 14 · 🟡 MAJOR · VULNERABILITY · `text:S8565`
**Local**: `pyproject.toml:-` · **Effort**: 5min

> Dependency versions are not predictable if the lock file (uv.lock, poetry.lock, pdm.lock or pylock.toml) is missing.

**Decisão**: pendente

### 15 · ⚪ MINOR · CODE_SMELL · `python:S7504`
**Local**: `conftest.py:20` · **Effort**: 5min

> Remove this unnecessary `list()` call on an already iterable object.

```python
       16      if (
       17          existing_package is None
       18          or Path(getattr(existing_package, "__file__", "")).resolve() != init_file
       19      ):
>>>    20          for module_name in list(sys.modules):
       21              if module_name == package_name or module_name.startswith(
       22                  f"{package_name}."
       23              ):
       24                  sys.modules.pop(module_name, None)
```

**Decisão**: pendente

### 16 · ⚪ MINOR · CODE_SMELL · `python:S6353`
**Local**: `src/flext_tap_oracle_oic/constants.py:40` · **Effort**: 5min

> Use concise character class syntax '\W' instead of '[^a-zA-Z0-9_]'.

```python
       36          SANITIZE_CAMEL_BOUNDARY_RE: ClassVar[t.RegexPattern] = re.compile(
       37              r"(?<!^)(?=[A-Z])"
       38          )
       39          SANITIZE_NON_IDENTIFIER_RE: ClassVar[t.RegexPattern] = re.compile(
>>>    40              r"[^a-zA-Z0-9_]"
       41          )
       42  
       43          DEFAULT_BATCH_SIZE: ClassVar[int] = 100
       44          MAX_RETRIES: ClassVar[int] = 3
```

**Decisão**: pendente

### 17 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_tap_oracle_oic/models.py:111` · **Effort**: 2min

> Rename this field "OicEnvelope" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
      107                  entity_name, label=name_label
      108              )
      109              FlextTapOracleOicModels.TapOracleOic.validate_optional_port(port)
      110  
>>>   111          OicEnvelope = _OicEnvelope
      112  
      113          class OICBaseStream(FlextMeltanoModels.BaseModel):
      114              """Professional base stream class for Oracle Integration Cloud APIs.
      115  
```

**Decisão**: pendente

### 18 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_tap_oracle_oic/models.py:493` · **Effort**: 2min

> Rename this field "OicAuthenticationConfig" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
      489              def _validate_record(self, record: t.JsonMapping) -> bool:
      490                  """Validate record meets basic requirements for processing."""
      491                  return bool(record)
      492  
>>>   493          OicAuthenticationConfig = _OicAuthenticationConfig
      494  
      495          OicIntegrationEntity = _OicIntegrationEntity
      496  
      497          OicConnectionEntity = _OicConnectionEntity
```

**Decisão**: pendente

### 19 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_tap_oracle_oic/models.py:495` · **Effort**: 2min

> Rename this field "OicIntegrationEntity" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
      491                  return bool(record)
      492  
      493          OicAuthenticationConfig = _OicAuthenticationConfig
      494  
>>>   495          OicIntegrationEntity = _OicIntegrationEntity
      496  
      497          OicConnectionEntity = _OicConnectionEntity
      498  
      499          OicActivityRecord = _OicActivityRecord
```

**Decisão**: pendente

### 20 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_tap_oracle_oic/models.py:497` · **Effort**: 2min

> Rename this field "OicConnectionEntity" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
      493          OicAuthenticationConfig = _OicAuthenticationConfig
      494  
      495          OicIntegrationEntity = _OicIntegrationEntity
      496  
>>>   497          OicConnectionEntity = _OicConnectionEntity
      498  
      499          OicActivityRecord = _OicActivityRecord
      500  
      501          OicPackageEntity = _OicPackageEntity
```

**Decisão**: pendente

### 21 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_tap_oracle_oic/models.py:499` · **Effort**: 2min

> Rename this field "OicActivityRecord" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
      495          OicIntegrationEntity = _OicIntegrationEntity
      496  
      497          OicConnectionEntity = _OicConnectionEntity
      498  
>>>   499          OicActivityRecord = _OicActivityRecord
      500  
      501          OicPackageEntity = _OicPackageEntity
      502  
      503          OicMetricsRecord = _OicMetricsRecord
```

**Decisão**: pendente

### 22 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_tap_oracle_oic/models.py:501` · **Effort**: 2min

> Rename this field "OicPackageEntity" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
      497          OicConnectionEntity = _OicConnectionEntity
      498  
      499          OicActivityRecord = _OicActivityRecord
      500  
>>>   501          OicPackageEntity = _OicPackageEntity
      502  
      503          OicMetricsRecord = _OicMetricsRecord
      504  
      505          OicAgentEntity = _OicAgentEntity
```

**Decisão**: pendente

### 23 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_tap_oracle_oic/models.py:503` · **Effort**: 2min

> Rename this field "OicMetricsRecord" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
      499          OicActivityRecord = _OicActivityRecord
      500  
      501          OicPackageEntity = _OicPackageEntity
      502  
>>>   503          OicMetricsRecord = _OicMetricsRecord
      504  
      505          OicAgentEntity = _OicAgentEntity
      506  
      507          OicStreamConfiguration = _OicStreamConfiguration
```

**Decisão**: pendente

### 24 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_tap_oracle_oic/models.py:505` · **Effort**: 2min

> Rename this field "OicAgentEntity" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
      501          OicPackageEntity = _OicPackageEntity
      502  
      503          OicMetricsRecord = _OicMetricsRecord
      504  
>>>   505          OicAgentEntity = _OicAgentEntity
      506  
      507          OicStreamConfiguration = _OicStreamConfiguration
      508  
      509          OicApiResponse = _OicApiResponse
```

**Decisão**: pendente

### 25 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_tap_oracle_oic/models.py:507` · **Effort**: 2min

> Rename this field "OicStreamConfiguration" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
      503          OicMetricsRecord = _OicMetricsRecord
      504  
      505          OicAgentEntity = _OicAgentEntity
      506  
>>>   507          OicStreamConfiguration = _OicStreamConfiguration
      508  
      509          OicApiResponse = _OicApiResponse
      510  
      511          OicErrorContext = _OicErrorContext
```

**Decisão**: pendente

### 26 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_tap_oracle_oic/models.py:509` · **Effort**: 2min

> Rename this field "OicApiResponse" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
      505          OicAgentEntity = _OicAgentEntity
      506  
      507          OicStreamConfiguration = _OicStreamConfiguration
      508  
>>>   509          OicApiResponse = _OicApiResponse
      510  
      511          OicErrorContext = _OicErrorContext
      512  
      513          class OracleOic(m.OracleOic):
```

**Decisão**: pendente

### 27 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_tap_oracle_oic/models.py:511` · **Effort**: 2min

> Rename this field "OicErrorContext" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
      507          OicStreamConfiguration = _OicStreamConfiguration
      508  
      509          OicApiResponse = _OicApiResponse
      510  
>>>   511          OicErrorContext = _OicErrorContext
      512  
      513          class OracleOic(m.OracleOic):
      514              """Domain entity models for Oracle OIC resources.
      515  
```

**Decisão**: pendente

### 28 · ⚪ MINOR · CODE_SMELL · `python:S5685`
**Local**: `src/flext_tap_oracle_oic/tap.py:306` · **Effort**: 10min

> Move this assignment out of the argument list; ":=" operator is confusing in this context.

```python
      302                  schema=stream_schema,
      303                  key_properties=(),
      304                  replication_key=(
      305                      str(replication_key)
>>>   306                      if (replication_key := getattr(stream, "replication_key", None))
      307                      is not None
      308                      else None
      309                  ),
      310              )
```

**Decisão**: pendente
