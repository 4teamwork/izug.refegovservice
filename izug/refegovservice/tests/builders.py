from ftw.builder.archetypes import ArchetypesBuilder
from ftw.builder import builder_registry


class EgovLeistungBuilder(ArchetypesBuilder):

    portal_type = 'EgovLeistung'

builder_registry.register('egov leistung', EgovLeistungBuilder)


class RefEgovServiceBuilder(ArchetypesBuilder):

    portal_type = 'RefEgovService'

builder_registry.register('ref egov service', RefEgovServiceBuilder)
