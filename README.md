# FLEXT-Tap-Oracle-OIC

[![Singer SDK](https://img.shields.io/badge/singer--sdk-compliant-brightgreen.svg)](https://sdk.meltano.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**FLEXT-Tap-Oracle-OIC** extracts metadata and operational data from Oracle Integration Cloud (OIC). It provides complete observability and audit capabilities for enterprise integration landscapes.

Part of the [FLEXT](https://github.com/flext-sh/flext) ecosystem.

## 🚀 Key Features

- **Comprehensive Metadata**: Syncs Integrations (`integrations`), Connections (`connections`), Packages (`packages`), and Agents (`agents`).
- **Operational Visibility**: Streams for execution metrics (`metrics`), activity logs (`activity`), and error tracking (`tracking`).
- **Secure Access**: Built-in OAuth2 support for IDCS authentication with automatic token handling.
- **Incremental Sync**: Efficiently syncs only new activity and metric data to minimize API load.
- **Resilience**: Robust retry logic and backoff strategies for OIC API limits.

## 📦 Installation

To usage in your Meltano project, add the extractor to your `meltano.yml`:

```yaml
plugins:
  extractors:
    - name: tap-oracle-oic
      pip_url: flext-tap-oracle-oic
      config:
        base_url: ${OIC_BASE_URL}
        oauth_client_id: ${OIC_CLIENT_ID}
        oauth_client_secret: ${OIC_CLIENT_SECRET}
        oauth_token_url: ${OIC_TOKEN_URL}
        oauth_client_aud: ${OIC_AUDIENCE}
```

## 🛠️ Usage

### Configuration

Configure connectivity to your OIC instance:

```json
{
  "base_url": "https://instance.integration.ocp.oraclecloud.com",
  "oauth_client_id": "client_id",
  "oauth_client_secret": "client_secret",
  "oauth_token_url": "https://idcs.identity.oraclecloud.com/oauth2/v1/token",
  "oauth_client_aud": "urn:opc:resource:consumer::all"
}
```

### Discovery Mode

Generate a catalog of available OIC resources:

```bash
tap-oracle-oic --config config.json --discover > catalog.json
```

### Data Extraction

Run the tap to extract data:

```bash
tap-oracle-oic --config config.json --catalog catalog.json | target-jsonl
```

## 🏗️ Architecture

Built on the Singer SDK, ensuring standard compliance:

- **Streams**: Maps REST API resources to Singer streams.
- **Auth**: Centralized OAuth handling via `flext-oracle-oic-ext`.
- **State**: Tracks `updated_time` for incremental replication of logs.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/development.md) for details on adding new resource streams.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
