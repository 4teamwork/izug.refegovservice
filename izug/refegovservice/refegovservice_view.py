from md5 import md5
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from suds import ServiceNotFound
from suds.client import Client
from suds.xsd.sxbasic import Import
from izug.refegovservice.interfaces import IRevEgovConfig
from urllib2 import URLError, HTTPError


class RefEgovServiceView(BrowserView):

    def __init__(self, context, request):
        """
        Gets the data from client
        """
        super(BrowserView, self).__init__(context, request)
        self.config = IRevEgovConfig(context)
        self.ref_ch_cache = self.config.get_ref_ch_cache()
        self.error = False

    def get_response(self):
        """
        Gets the response and saves the result and an md5-hash into
        annotations. If there is a problem getting the response, the response
        from annotations will be returned. If the md5-hash has changed,
        the annotations will be updated.
        """
        Import.bind('http://schemas.xmlsoap.org/soap/encoding/')
        pt = getToolByName(self.context, 'portal_properties')
        client_url = pt.wsrefegov_property_sheet.client_url
        client = None
        try:
            client = Client(client_url)
        except (URLError, HTTPError, ServiceNotFound):
            return self.ref_ch_cache['response']

        if client:
            try:
                response = client.service.GetServiceDetail(
                    eCHserviceID=self.context.getECHserviceID(),
                    eCHlanguageID="DE",
                    eCHmunicipalityID="01711",
                    eCHserviceVersionID=self.context.getECHserviceVersionID())

            except (URLError, HTTPError, ServiceNotFound):
                return self.ref_ch_cache['response']

            except Exception, e:
                if e.args == ('No services defined', ):
                    return self.ref_ch_cache['response']
                else:
                    self.error = True
                    return

            try:
                response.formularBlock.formular
            except AttributeError:
                self.error = True
                return

            response_dict = {}

            try:
                rtitle = response.infoBlock.serviceInfo.eCHservice.content
                response_dict['title'] = [
                    rtitle and rtitle.encode('utf8').decode('utf8') or
                    self.context.Title()]
                if 'generalInformationBlock' in response:
                    block = response['generalInformationBlock']
                    if 'generalInformation' in block:
                        response_dict[block._label] = [
                            block['generalInformation']]

                if 'prerequisiteBlock' in response:
                    block = response['prerequisiteBlock']
                    if 'prerequisite' in block:
                        response_dict[block._label] = [
                            cc.description for cc in block[
                                'prerequisite'] if cc.description]

                if 'procedureBlock' in response:
                    block = response['procedureBlock']
                    if 'procedure' in block:
                        response_dict[block._label] = [
                            cc.description for cc in block[
                                'procedure'] if cc.description]

                if 'formularBlock' in response:
                    block = response['formularBlock']
                    if 'formular' in block:
                        response_dict[block._label] = []
                        for row in block['formular']:
                            try:
                                content = "<a href='%s'>%s</a><div>%s"
                                "</div>" % (
                                    row._uri, row.formularName,
                                    row.description)
                                response_dict[block._label].append(content)
                            except AttributeError:
                                pass  # there is no uri name or description

                if 'documentRequiredBlock' in response:
                    block = response['documentRequiredBlock']
                    if 'document' in block:
                        response_dict[block._label] = []
                        for row in block['document']:
                            try:
                                if '_uri' in row and 'documentName' in row:
                                    content = "<a href='%s'>%s</a>"
                                    "<div>%s</div>" % (
                                        row._uri, row.documentName,
                                        row.description)
                                    response_dict[block._label].append(content)
                                elif 'description' in row and \
                                    'documentName' in row:
                                    content = "%s<div>%s</div>" % (
                                        row.documentName, row.description)
                                    response_dict[block._label].append(content)
                                elif 'description' in row:
                                    response_dict[block._label].append(
                                        row.description)
                            except AttributeError:
                                pass  # there is no uri name or description

                if 'resultBlock' in response:
                    block = response['resultBlock']
                    if 'result' in block:
                        response_dict[block._label] = [block['result']]

                if 'feeBlock' in response:
                    block = response['feeBlock']
                    if 'fee' in block:
                        response_dict[block._label] = [block['fee']]

                if 'legalRegulationBlock' in response:
                    block = response['legalRegulationBlock']
                    if 'legalRegulation' in block:
                        response_dict[block._label] = []
                        for row in block['legalRegulation']:
                            try:
                                if '_uri' in row and 'documentName' in row:
                                    content = "<a href='%s'>%s</a>"
                                    "<div>%s</div>" % (
                                        row._uri, row.documentName,
                                        row.description)
                                    response_dict[block._label].append(content)
                                elif 'description' in row and \
                                    'documentName' in row:
                                    content = "%s<div>%s</div>" % (
                                        row.documentName, row.description)
                                    response_dict[block._label].append(content)
                                elif 'description' in row:
                                    response_dict[block._label].append(
                                        row.description)
                            except AttributeError:
                                pass  # there is no uri name or description

                if 'documentOtherBlock' in response:
                    block = response['documentOtherBlock']
                    if 'document' in block:
                        response_dict[block._label] = []
                        for row in block['document']:
                            try:
                                content = "<a href='%s'>%s</a>"
                                "<div>%s</div>" % (
                                    row._uri, row.documentName,
                                    row.description)
                                response_dict[block._label].append(content)
                            except AttributeError:
                                pass  # there is no uri name or description

                if 'remarkBlock' in response:
                    block = response['remarkBlock']
                    if 'remark' in block:
                        response_dict[block._label] = [block['remark']]

                if 'approbationBlock' in response:
                    block = response['approbationBlock']
                    if 'approbation' in block:
                        response_dict[block._label] = [block['approbation']]

                if 'contactBlock' in response:
                    block = response['contactBlock']
                    response_dict[block._label] = []
                    if 'contact' in block:
                        for contact in block['contact']:
                            plz = ''
                            for row in contact:
                                if 'content' in row[1] and row[1].content:
                                    if row[0] == 'postalCode':
                                        plz = row[1].content
                                    elif row[0] == 'municipality':
                                        plz += ' %s' % row[1].content
                                        response_dict[block._label].append(plz)
                                    else:
                                        response_dict[block._label].append(
                                            row[1].content)
                            if 'openingHours' in contact and \
                                contact.openingHours:
                                response_dict[block._label].append(
                                    '<br />'.join(contact.openingHours))

                result = {}
                for k, v in response_dict.items():
                    xx = []
                    for row in v:
                        if not row:
                            pass  # ignore
                        elif isinstance(row, str):
                            xx.append(row.decode('utf8'))
                        elif not isinstance(row, unicode):
                            xx.append(unicode(row))
                        else:
                            xx.append(row)
                    if xx:
                        result[k.encode('utf8')] = xx

            except TypeError:
                self.error = True
                return

            # check md5
            md5_hash = md5(str(response)).digest()
            if md5_hash != self.ref_ch_cache['md5']:
                self.config.set_ref_ch_cache(md5_hash, result)
            return result

        return None

    def blocks(self):
        """ Returns the blocks in the correct order.
        """
        return ['Generelle Information', 'Vorbedingungen',
                'Beh\xc3\xb6rdengang',
                'Formular(e)', 'Ben\xc3\xb6tigte Dokumente', 'Ergebnis',
                'Kosten', 'Gesetzliche Grundlagen', 'Andere Dokumente',
                'Bemerkungen', 'Genehmigung', 'Kontakt']

    def get_body(self):
        """
        Gets the details from service and returns it in a dictionary
        """
        response = self.get_response()
        if not response:
            self.error = True
            return {}
        return response
