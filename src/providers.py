import typing
from collections import namedtuple

ProviderInfo = namedtuple('ProviderInfo', ['sys_name', 'kontest_url'])

# TODO: fetch from sites api
providers = {
    'all':             '/api/v1/all',
    'codeforces':      '/api/v1/codeforces',
    'codeforces_gym':  '/api/v1/codeforces_gym',
    'topcoder':        '/api/v1/top_coder',
    'atcoder':         '/api/v1/at_coder',
    'codechef':        '/api/v1/code_chef',
    'cs_academy':      '/api/v1/cs_academy',
    'hackerrank':      '/api/v1/hacker_rank',
    'hackerearth':     '/api/v1/hacker_earth',
    'kickstart':       '/api/v1/kick_start',
    'leetcode':        '/api/v1/leet_code'
}


def normalize_provider_name(provider: str) -> str:
    return provider.lower()


def get_provider(provider: str) -> ProviderInfo:
    provider = normalize_provider_name(provider)

    if provider not in providers:
        raise ValueError(f"Unknown provider {provider}")

    return ProviderInfo(
        sys_name=provider,
        kontest_url=providers[provider]
    )


def list_providers() -> typing.List[str]:
    return list(providers.keys())


def has_provider(provider: str) -> bool:
    provider = normalize_provider_name(provider)
    return provider in providers
