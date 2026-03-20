# Configuration

`SendouClient` accepts a small set of runtime options:

- `token`: bearer token from https://sendou.ink/api
- `base_url`: API root (`https://sendou.ink/api` by default)
- `timeout_seconds`: per-request timeout (20.0 by default)

```python
from sendou_sdk import SendouClient

client = SendouClient(
    token="YOUR_TOKEN",
    base_url="https://sendou.ink/api",
)
```

You can also use `async with SendouClient(...)` to ensure the underlying HTTP client
is always closed.

## Timeouts

Default timeout is 20 seconds.

```python
from sendou_sdk import SendouClient

client = SendouClient(token="YOUR_TOKEN", timeout_seconds=10.0)
```

## Environment variables

The SDK does not read environment variables automatically, but common usage looks like:

```python
import os
from sendou_sdk import SendouClient

client = SendouClient(
    token=os.getenv("SENDOU_TOKEN"),
    base_url=os.getenv("SENDOU_BASE_URL", "https://sendou.ink/api"),
)
```
