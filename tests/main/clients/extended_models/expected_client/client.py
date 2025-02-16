from .async_base_client import AsyncBaseClient
from .fragments_with_mixins import FragmentsWithMixins
from .get_query_a import GetQueryA
from .get_query_a_with_fragment import GetQueryAWithFragment
from .get_query_b import GetQueryB


def gql(q: str) -> str:
    return q


class Client(AsyncBaseClient):
    async def get_query_a(self) -> GetQueryA:
        query = gql(
            """
            query getQueryA {
              queryA {
                fieldA
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetQueryA.model_validate(data)

    async def get_query_b(self) -> GetQueryB:
        query = gql(
            """
            query getQueryB {
              queryB {
                fieldB
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetQueryB.model_validate(data)

    async def get_query_a_with_fragment(self) -> GetQueryAWithFragment:
        query = gql(
            """
            query getQueryAWithFragment {
              ...getQueryAFragment
            }

            fragment getQueryAFragment on Query {
              queryA {
                fieldA
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetQueryAWithFragment.model_validate(data)

    async def fragments_with_mixins(self) -> FragmentsWithMixins:
        query = gql(
            """
            query fragmentsWithMixins {
              queryA {
                ...fragmentA
              }
              queryB {
                ...fragmentB
              }
            }

            fragment fragmentA on TypeA @mixin(from: ".mixins_a", import: "MixinA") {
              fieldA
            }

            fragment fragmentB on TypeB @mixin(from: ".mixins_b", import: "MixinB") {
              fieldB
            }
            """
        )
        variables: dict[str, object] = {}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return FragmentsWithMixins.model_validate(data)
