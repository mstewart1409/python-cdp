# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: IndexedDB (experimental)

from __future__ import annotations
import enum
import typing
from dataclasses import dataclass
from .util import event_class, T_JSON_DICT

from . import runtime


@dataclass
class DatabaseWithObjectStores:
    '''
    Database with an array of object stores.
    '''
    #: Database name.
    name: str

    #: Database version (type is not 'integer', as the standard
    #: requires the version number to be 'unsigned long long')
    version: float

    #: Object stores in this database.
    object_stores: typing.List[ObjectStore]

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['name'] = self.name
        json['version'] = self.version
        json['objectStores'] = [i.to_json() for i in self.object_stores]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> DatabaseWithObjectStores:
        return cls(
            name=str(json['name']),
            version=float(json['version']),
            object_stores=[ObjectStore.from_json(i) for i in json['objectStores']],
        )


@dataclass
class ObjectStore:
    '''
    Object store.
    '''
    #: Object store name.
    name: str

    #: Object store key path.
    key_path: KeyPath

    #: If true, object store has auto increment flag set.
    auto_increment: bool

    #: Indexes in this object store.
    indexes: typing.List[ObjectStoreIndex]

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['name'] = self.name
        json['keyPath'] = self.key_path.to_json()
        json['autoIncrement'] = self.auto_increment
        json['indexes'] = [i.to_json() for i in self.indexes]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ObjectStore:
        return cls(
            name=str(json['name']),
            key_path=KeyPath.from_json(json['keyPath']),
            auto_increment=bool(json['autoIncrement']),
            indexes=[ObjectStoreIndex.from_json(i) for i in json['indexes']],
        )


@dataclass
class ObjectStoreIndex:
    '''
    Object store index.
    '''
    #: Index name.
    name: str

    #: Index key path.
    key_path: KeyPath

    #: If true, index is unique.
    unique: bool

    #: If true, index allows multiple entries for a key.
    multi_entry: bool

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['name'] = self.name
        json['keyPath'] = self.key_path.to_json()
        json['unique'] = self.unique
        json['multiEntry'] = self.multi_entry
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ObjectStoreIndex:
        return cls(
            name=str(json['name']),
            key_path=KeyPath.from_json(json['keyPath']),
            unique=bool(json['unique']),
            multi_entry=bool(json['multiEntry']),
        )


@dataclass
class Key:
    '''
    Key.
    '''
    #: Key type.
    type_: str

    #: Number value.
    number: typing.Optional[float] = None

    #: String value.
    string: typing.Optional[str] = None

    #: Date value.
    date: typing.Optional[float] = None

    #: Array value.
    array: typing.Optional[typing.List[Key]] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['type'] = self.type_
        if self.number is not None:
            json['number'] = self.number
        if self.string is not None:
            json['string'] = self.string
        if self.date is not None:
            json['date'] = self.date
        if self.array is not None:
            json['array'] = [i.to_json() for i in self.array]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> Key:
        return cls(
            type_=str(json['type']),
            number=float(json['number']) if 'number' in json else None,
            string=str(json['string']) if 'string' in json else None,
            date=float(json['date']) if 'date' in json else None,
            array=[Key.from_json(i) for i in json['array']] if 'array' in json else None,
        )


@dataclass
class KeyRange:
    '''
    Key range.
    '''
    #: If true lower bound is open.
    lower_open: bool

    #: If true upper bound is open.
    upper_open: bool

    #: Lower bound.
    lower: typing.Optional[Key] = None

    #: Upper bound.
    upper: typing.Optional[Key] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['lowerOpen'] = self.lower_open
        json['upperOpen'] = self.upper_open
        if self.lower is not None:
            json['lower'] = self.lower.to_json()
        if self.upper is not None:
            json['upper'] = self.upper.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> KeyRange:
        return cls(
            lower_open=bool(json['lowerOpen']),
            upper_open=bool(json['upperOpen']),
            lower=Key.from_json(json['lower']) if 'lower' in json else None,
            upper=Key.from_json(json['upper']) if 'upper' in json else None,
        )


@dataclass
class DataEntry:
    '''
    Data entry.
    '''
    #: Key object.
    key: runtime.RemoteObject

    #: Primary key object.
    primary_key: runtime.RemoteObject

    #: Value object.
    value: runtime.RemoteObject

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['key'] = self.key.to_json()
        json['primaryKey'] = self.primary_key.to_json()
        json['value'] = self.value.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> DataEntry:
        return cls(
            key=runtime.RemoteObject.from_json(json['key']),
            primary_key=runtime.RemoteObject.from_json(json['primaryKey']),
            value=runtime.RemoteObject.from_json(json['value']),
        )


@dataclass
class KeyPath:
    '''
    Key path.
    '''
    #: Key path type.
    type_: str

    #: String value.
    string: typing.Optional[str] = None

    #: Array value.
    array: typing.Optional[typing.List[str]] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['type'] = self.type_
        if self.string is not None:
            json['string'] = self.string
        if self.array is not None:
            json['array'] = [i for i in self.array]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> KeyPath:
        return cls(
            type_=str(json['type']),
            string=str(json['string']) if 'string' in json else None,
            array=[str(i) for i in json['array']] if 'array' in json else None,
        )


def clear_object_store(
        security_origin: str,
        database_name: str,
        object_store_name: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Clears all entries from an object store.

    :param security_origin: Security origin.
    :param database_name: Database name.
    :param object_store_name: Object store name.
    '''
    params: T_JSON_DICT = dict()
    params['securityOrigin'] = security_origin
    params['databaseName'] = database_name
    params['objectStoreName'] = object_store_name
    cmd_dict: T_JSON_DICT = {
        'method': 'IndexedDB.clearObjectStore',
        'params': params,
    }
    json = yield cmd_dict


def delete_database(
        security_origin: str,
        database_name: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Deletes a database.

    :param security_origin: Security origin.
    :param database_name: Database name.
    '''
    params: T_JSON_DICT = dict()
    params['securityOrigin'] = security_origin
    params['databaseName'] = database_name
    cmd_dict: T_JSON_DICT = {
        'method': 'IndexedDB.deleteDatabase',
        'params': params,
    }
    json = yield cmd_dict


def delete_object_store_entries(
        security_origin: str,
        database_name: str,
        object_store_name: str,
        key_range: KeyRange
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Delete a range of entries from an object store

    :param security_origin:
    :param database_name:
    :param object_store_name:
    :param key_range: Range of entry keys to delete
    '''
    params: T_JSON_DICT = dict()
    params['securityOrigin'] = security_origin
    params['databaseName'] = database_name
    params['objectStoreName'] = object_store_name
    params['keyRange'] = key_range.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'IndexedDB.deleteObjectStoreEntries',
        'params': params,
    }
    json = yield cmd_dict


def disable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Disables events from backend.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'IndexedDB.disable',
    }
    json = yield cmd_dict


def enable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Enables events from backend.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'IndexedDB.enable',
    }
    json = yield cmd_dict


def request_data(
        security_origin: str,
        database_name: str,
        object_store_name: str,
        index_name: str,
        skip_count: int,
        page_size: int,
        key_range: typing.Optional[KeyRange] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,typing.Tuple[typing.List[DataEntry], bool]]:
    '''
    Requests data from object store or index.

    :param security_origin: Security origin.
    :param database_name: Database name.
    :param object_store_name: Object store name.
    :param index_name: Index name, empty string for object store data requests.
    :param skip_count: Number of records to skip.
    :param page_size: Number of records to fetch.
    :param key_range: *(Optional)* Key range.
    :returns: A tuple with the following items:

        0. **objectStoreDataEntries** - Array of object store data entries.
        1. **hasMore** - If true, there are more entries to fetch in the given range.
    '''
    params: T_JSON_DICT = dict()
    params['securityOrigin'] = security_origin
    params['databaseName'] = database_name
    params['objectStoreName'] = object_store_name
    params['indexName'] = index_name
    params['skipCount'] = skip_count
    params['pageSize'] = page_size
    if key_range is not None:
        params['keyRange'] = key_range.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'IndexedDB.requestData',
        'params': params,
    }
    json = yield cmd_dict
    return (
        [DataEntry.from_json(i) for i in json['objectStoreDataEntries']],
        bool(json['hasMore'])
    )


def get_metadata(
        security_origin: str,
        database_name: str,
        object_store_name: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,typing.Tuple[float, float]]:
    '''
    Gets metadata of an object store

    :param security_origin: Security origin.
    :param database_name: Database name.
    :param object_store_name: Object store name.
    :returns: A tuple with the following items:

        0. **entriesCount** - the entries count
        1. **keyGeneratorValue** - the current value of key generator, to become the next inserted key into the object store. Valid if objectStore.autoIncrement is true.
    '''
    params: T_JSON_DICT = dict()
    params['securityOrigin'] = security_origin
    params['databaseName'] = database_name
    params['objectStoreName'] = object_store_name
    cmd_dict: T_JSON_DICT = {
        'method': 'IndexedDB.getMetadata',
        'params': params,
    }
    json = yield cmd_dict
    return (
        float(json['entriesCount']),
        float(json['keyGeneratorValue'])
    )


def request_database(
        security_origin: str,
        database_name: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,DatabaseWithObjectStores]:
    '''
    Requests database with given name in given frame.

    :param security_origin: Security origin.
    :param database_name: Database name.
    :returns: Database with an array of object stores.
    '''
    params: T_JSON_DICT = dict()
    params['securityOrigin'] = security_origin
    params['databaseName'] = database_name
    cmd_dict: T_JSON_DICT = {
        'method': 'IndexedDB.requestDatabase',
        'params': params,
    }
    json = yield cmd_dict
    return DatabaseWithObjectStores.from_json(json['databaseWithObjectStores'])


def request_database_names(
        security_origin: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,typing.List[str]]:
    '''
    Requests database names for given security origin.

    :param security_origin: Security origin.
    :returns: Database names for origin.
    '''
    params: T_JSON_DICT = dict()
    params['securityOrigin'] = security_origin
    cmd_dict: T_JSON_DICT = {
        'method': 'IndexedDB.requestDatabaseNames',
        'params': params,
    }
    json = yield cmd_dict
    return [str(i) for i in json['databaseNames']]
