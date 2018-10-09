# This source code is part of the Biotite package and is distributed
# under the 3-Clause BSD License. Please see 'LICENSE.rst' for further
# information.

from typing import (
    Optional,
    Dict,
    Tuple,
    Union,
    Iterable,
    Iterator,
    List,
    TextIO
)
from ....file import TextFile
from ...seqtypes import NucleotideSequence, ProteinSequence
from ...annotation import Annotation, AnnotatedSequence

class GenBankFile:
    def __init__(self) -> None: ...
    def read(self, file: Union[str, TextIO]) -> None: ...
    def write(self, file: Union[str, TextIO]) -> None: ...
    def get_locus(self) -> Dict[str, str]: ...
    def get_definition(self) -> str: ...
    def get_accession(self) -> str: ...
    def get_version(self) -> str: ...
    def get_gi(self) -> str: ...
    def get_db_link(self) -> Dict[str, str]: ...
    def get_source(self) -> str: ...
    def get_references(
        self
    ) -> List[Dict[str, Union[Tuple[int, int], str]]]: ...
    def get_comment(self) -> str: ...
    def get_annotation(
        self, include_only: Optional[List[str]] = None
    ) -> Annotation: ...
    def get_sequence(self) -> NucleotideSequence: ...
    def get_annotated_sequence(
        self, include_only: Optional[List[str]] = None
    ) -> AnnotatedSequence: ...


class GenPeptFile(GenBankFile):
    def get_db_source(self) -> str: ...
    def get_locus(self) -> Dict[str, str]: ...
    def get_sequence(self) -> ProteinSequence: ...


class MultiFile(TextFile, Iterable[GenBankFile]):
    def __init__(self, file_type: str) -> None: ...
    def __iter__(self) -> Iterator[GenBankFile]: ...