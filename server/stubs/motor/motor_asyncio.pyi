from typing import Any, Optional


class AsyncIOMotorClient: ...
class AsyncIOMotorDatabase: ...

class AsyncIOMotorGridFSBucket:
    def __init__(self, db): ...
    async def open_download_stream_by_name(self, name): ...
    async def delete(self, id_): ...
    def open_upload_stream(self, name): ...

class AsyncIOMotorCollection:
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
