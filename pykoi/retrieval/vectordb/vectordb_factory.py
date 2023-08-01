""" A factory for creating vector databases."""
from typing import Union

from pykoi.retrieval.llm.constants import LlmName
from pykoi.retrieval.llm.embedding_factory import EmbeddingFactory
from pykoi.retrieval.vectordb.abs_vectordb import AbsVectorDb
from pykoi.retrieval.vectordb.chroma import ChromaDb
from pykoi.retrieval.vectordb.constants import VectorDbName


class VectorDbFactory:
    """
    A factory for creating vector databases.
    """

    @staticmethod
    def create(
        model_name: Union[str, LlmName], vector_db_name: Union[str, VectorDbName]
    ) -> AbsVectorDb:
        """
        Create a vector database.

        Args:
            model_name: The name of the model.
            vector_db_name: The name of the vector database.

        Returns:
            AbsVectorDb: The vector database.
        """
        try:
            vector_db_name = VectorDbName(vector_db_name)
            model_name = LlmName(model_name)
            model_embedding = EmbeddingFactory.create_embedding(model_name.value)
            if vector_db_name == VectorDbName.CHROMA:
                return ChromaDb(model_embedding)

        except Exception as ex:
            raise Exception("Unknown db: {}".format(vector_db_name)) from ex
