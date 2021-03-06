from typing import Any, Optional

from pymongo import common as common
from pymongo import helpers as helpers
from pymongo import message as message
from pymongo.bulk import BulkOperationBuilder as BulkOperationBuilder
from pymongo.change_stream import CollectionChangeStream as CollectionChangeStream
from pymongo.collation import validate_collation_or_none as validate_collation_or_none
from pymongo.command_cursor import CommandCursor as CommandCursor
from pymongo.command_cursor import RawBatchCommandCursor as RawBatchCommandCursor
from pymongo.common import ORDERED_TYPES as ORDERED_TYPES
from pymongo.cursor import Cursor as Cursor
from pymongo.cursor import RawBatchCursor as RawBatchCursor
from pymongo.errors import BulkWriteError as BulkWriteError
from pymongo.errors import ConfigurationError as ConfigurationError
from pymongo.errors import InvalidName as InvalidName
from pymongo.errors import InvalidOperation as InvalidOperation
from pymongo.errors import OperationFailure as OperationFailure
from pymongo.operations import IndexModel as IndexModel
from pymongo.read_preferences import ReadPreference as ReadPreference
from pymongo.results import BulkWriteResult as BulkWriteResult
from pymongo.results import DeleteResult as DeleteResult
from pymongo.results import InsertManyResult as InsertManyResult
from pymongo.results import InsertOneResult as InsertOneResult
from pymongo.results import UpdateResult as UpdateResult
from pymongo.write_concern import WriteConcern as WriteConcern


class ReturnDocument:
    BEFORE: bool = ...
    AFTER: bool = ...

class Collection(common.BaseObject):
    def __init__(
        self,
        database: Any,
        name: Any,
        create: bool = ...,
        codec_options: Optional[Any] = ...,
        read_preference: Optional[Any] = ...,
        write_concern: Optional[Any] = ...,
        read_concern: Optional[Any] = ...,
        session: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...
    def __getattr__(self, name: Any): ...
    def __getitem__(self, name: Any): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    @property
    def full_name(self): ...
    @property
    def name(self): ...
    @property
    def database(self): ...
    def with_options(
        self,
        codec_options: Optional[Any] = ...,
        read_preference: Optional[Any] = ...,
        write_concern: Optional[Any] = ...,
        read_concern: Optional[Any] = ...,
    ): ...
    def initialize_unordered_bulk_op(self, bypass_document_validation: bool = ...): ...
    def initialize_ordered_bulk_op(self, bypass_document_validation: bool = ...): ...
    async def bulk_write(
        self,
        requests: Any,
        ordered: bool = ...,
        bypass_document_validation: bool = ...,
        session: Optional[Any] = ...,
    ): ...
    async def insert_one(
        self,
        document: Any,
        bypass_document_validation: bool = ...,
        session: Optional[Any] = ...,
    ): ...
    async def insert_many(
        self,
        documents: Any,
        ordered: bool = ...,
        bypass_document_validation: bool = ...,
        session: Optional[Any] = ...,
    ): ...
    async def replace_one(
        self,
        filter: Any,
        replacement: Any,
        upsert: bool = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[Any] = ...,
        hint: Optional[Any] = ...,
        session: Optional[Any] = ...,
    ): ...
    async def update_one(
        self,
        filter: Any,
        update: Any,
        upsert: bool = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[Any] = ...,
        array_filters: Optional[Any] = ...,
        hint: Optional[Any] = ...,
        session: Optional[Any] = ...,
    ): ...
    async def update_many(
        self,
        filter: Any,
        update: Any,
        upsert: bool = ...,
        array_filters: Optional[Any] = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[Any] = ...,
        hint: Optional[Any] = ...,
        session: Optional[Any] = ...,
    ): ...
    async def drop(self, session: Optional[Any] = ...) -> None: ...
    async def delete_one(
        self,
        filter: Any,
        collation: Optional[Any] = ...,
        hint: Optional[Any] = ...,
        session: Optional[Any] = ...,
    ): ...
    async def delete_many(
        self,
        filter: Any,
        collation: Optional[Any] = ...,
        hint: Optional[Any] = ...,
        session: Optional[Any] = ...,
    ): ...
    async def find_one(
        self, filter: Optional[Any] = ..., *args: Any, **kwargs: Any
    ): ...
    async def find(self, *args: Any, **kwargs: Any): ...
    async def find_raw_batches(self, *args: Any, **kwargs: Any): ...
    async def parallel_scan(
        self, num_cursors: Any, session: Optional[Any] = ..., **kwargs: Any
    ): ...
    async def estimated_document_count(self, **kwargs: Any): ...
    async def count_documents(
        self, filter: Any, session: Optional[Any] = ..., **kwargs: Any
    ): ...
    async def count(
        self, filter: Optional[Any] = ..., session: Optional[Any] = ..., **kwargs: Any
    ): ...
    async def create_indexes(
        self, indexes: Any, session: Optional[Any] = ..., **kwargs: Any
    ): ...
    async def create_index(
        self, keys: Any, session: Optional[Any] = ..., **kwargs: Any
    ): ...
    async def ensure_index(
        self, key_or_list: Any, cache_for: int = ..., **kwargs: Any
    ): ...
    async def drop_indexes(
        self, session: Optional[Any] = ..., **kwargs: Any
    ) -> None: ...
    async def drop_index(
        self, index_or_name: Any, session: Optional[Any] = ..., **kwargs: Any
    ) -> None: ...
    async def reindex(self, session: Optional[Any] = ..., **kwargs: Any): ...
    async def list_indexes(self, session: Optional[Any] = ...): ...
    async def index_information(self, session: Optional[Any] = ...): ...
    async def options(self, session: Optional[Any] = ...): ...
    async def aggregate(
        self, pipeline: Any, session: Optional[Any] = ..., **kwargs: Any
    ): ...
    async def aggregate_raw_batches(self, pipeline: Any, **kwargs: Any): ...
    async def watch(
        self,
        pipeline: Optional[Any] = ...,
        full_document: Optional[Any] = ...,
        resume_after: Optional[Any] = ...,
        max_await_time_ms: Optional[Any] = ...,
        batch_size: Optional[Any] = ...,
        collation: Optional[Any] = ...,
        start_at_operation_time: Optional[Any] = ...,
        session: Optional[Any] = ...,
        start_after: Optional[Any] = ...,
    ): ...
    async def group(
        self,
        key: Any,
        condition: Any,
        initial: Any,
        reduce: Any,
        finalize: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    async def rename(
        self, new_name: Any, session: Optional[Any] = ..., **kwargs: Any
    ): ...
    async def distinct(
        self,
        key: Any,
        filter: Optional[Any] = ...,
        session: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    async def map_reduce(
        self,
        map: Any,
        reduce: Any,
        out: Any,
        full_response: bool = ...,
        session: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    async def inline_map_reduce(
        self,
        map: Any,
        reduce: Any,
        full_response: bool = ...,
        session: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    async def find_one_and_delete(
        self,
        filter: Any,
        projection: Optional[Any] = ...,
        sort: Optional[Any] = ...,
        hint: Optional[Any] = ...,
        session: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    async def find_one_and_replace(
        self,
        filter: Any,
        replacement: Any,
        projection: Optional[Any] = ...,
        sort: Optional[Any] = ...,
        upsert: bool = ...,
        return_document: Any = ...,
        hint: Optional[Any] = ...,
        session: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    async def find_one_and_update(
        self,
        filter: Any,
        update: Any,
        projection: Optional[Any] = ...,
        sort: Optional[Any] = ...,
        upsert: bool = ...,
        return_document: Any = ...,
        array_filters: Optional[Any] = ...,
        hint: Optional[Any] = ...,
        session: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    async def save(
        self,
        to_save: Any,
        manipulate: bool = ...,
        check_keys: bool = ...,
        **kwargs: Any
    ): ...
    async def insert(
        self,
        doc_or_docs: Any,
        manipulate: bool = ...,
        check_keys: bool = ...,
        continue_on_error: bool = ...,
        **kwargs: Any
    ): ...
    async def update(
        self,
        spec: Any,
        document: Any,
        upsert: bool = ...,
        manipulate: bool = ...,
        multi: bool = ...,
        check_keys: bool = ...,
        **kwargs: Any
    ): ...
    async def remove(
        self, spec_or_id: Optional[Any] = ..., multi: bool = ..., **kwargs: Any
    ): ...
    async def find_and_modify(
        self,
        query: Any = ...,
        update: Optional[Any] = ...,
        upsert: bool = ...,
        sort: Optional[Any] = ...,
        full_response: bool = ...,
        manipulate: bool = ...,
        **kwargs: Any
    ): ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> None: ...
    next: Any = ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
