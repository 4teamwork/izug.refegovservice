from ftw.builder.dexterity import DexterityBuilder
from ftw.builder import builder_registry


class EGovServiceBuilder(DexterityBuilder):

    portal_type = 'izug.EGovService'


builder_registry.register('egov service', EGovServiceBuilder)


class RefEgovServiceBuilder(DexterityBuilder):

    portal_type = 'RefEgovService'

builder_registry.register('ref egov service', RefEgovServiceBuilder)
