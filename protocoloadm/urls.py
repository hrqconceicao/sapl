from django.conf.urls import include, url
from protocoloadm.views import (AnularProtocoloAdmView,
                                ComprovanteProtocoloView,
                                CriarDocumentoProtocolo,
                                DetailDocumentoAdministrativo,
                                DocumentoAcessorioAdministrativoEditView,
                                DocumentoAcessorioAdministrativoView,
                                PesquisarDocumentoAdministrativo,
                                ProposicaoDetailView, ProposicaoReceberView,
                                ProposicaoView, ProposicoesIncorporadasView,
                                ProposicoesNaoIncorporadasView,
                                ProposicoesNaoRecebidasView,
                                ProtocoloDocumentoView, ProtocoloListView,
                                ProtocoloMateriaView, ProtocoloMostrarView,
                                ProtocoloPesquisaView, TramitacaoAdmDeleteView,
                                TramitacaoAdmEditView,
                                TramitacaoAdmIncluirView, TramitacaoAdmView,
                                documento_acessorio_administrativo_crud,
                                documento_administrativo_crud,
                                protocolo_documento_crud,
                                protocolo_materia_crud,
                                status_tramitacao_administrativo_crud,
                                tipo_documento_administrativo_crud,
                                tramitacao_administrativo_crud)

urlpatterns = [
    url(r'^protocoloadm/docadm/', include(documento_administrativo_crud.urls)),
    url(r'^protocoloadm/tipo-documento-adm/',
        include(tipo_documento_administrativo_crud.urls)),
    url(r'^protocoloadm/doc-acessorio/',
        include(documento_acessorio_administrativo_crud.urls)),
    url(r'^protocoloadm/status-tramitacao-adm/',
        include(status_tramitacao_administrativo_crud.urls)),
    url(r'^protocoloadm/tramitacao-adm/',
        include(tramitacao_administrativo_crud.urls)),
    url(r'^protocoloadm/protocolo-doc/',
        include(protocolo_documento_crud.urls)),
    url(r'^protocoloadm/protocolo-mat/',
        include(protocolo_materia_crud.urls), name='protocolomat'),
    url(r'^protocoloadm/protocolo$',
        ProtocoloPesquisaView.as_view(), name='protocolo'),
    url(r'^protocoloadm/protocolo_list$',
        ProtocoloListView.as_view(), name='protocolo_list'),
    url(r'^protocoloadm/(?P<pk>\d+)/(?P<ano>\d+)/protocolo_mostrar$',
        ProtocoloMostrarView.as_view(), name='protocolo_mostrar'),
    url(r'^protocoloadm/anular-protocolo',
        AnularProtocoloAdmView.as_view(), name='anular_protocolo'),
    url(r'^protocoloadm/protocolar-doc',
        ProtocoloDocumentoView.as_view(), name='protocolar_doc'),
    url(r'^protocoloadm/protocolar-mat',
        ProtocoloMateriaView.as_view(), name='protocolar_mat'),
    url(r'^protocoloadm/pesq-doc-adm',
        PesquisarDocumentoAdministrativo.as_view(), name='pesq_doc_adm'),
    url(r'^protocoloadm/doc-adm/(?P<pk>\d+)$',
        DetailDocumentoAdministrativo.as_view(), name='detail_doc_adm'),
    url(r'^protocoloadm/doc-ace-adm/(?P<pk>\d+)',
        DocumentoAcessorioAdministrativoView.as_view(), name='doc_ace_adm'),
    url(r'^protocoloadm/doc-ace-adm/edit/(?P<pk>\d+)/(?P<ano>\d+)',
        DocumentoAcessorioAdministrativoEditView.as_view(),
        name='doc_ace_adm_edit'),

    url(r'^protocoloadm/(?P<pk>\d+)/tramitacao$',
        TramitacaoAdmView.as_view(), name='tramitacao_adm'),
    url(r'^protocoloadm/(?P<pk>\d+)/tramitacao_incluir',
        TramitacaoAdmIncluirView.as_view(), name='tramitacao_incluir'),
    url(r'^protocoloadm/(?P<pk>\d+)/tramitacao_edit',
        TramitacaoAdmEditView.as_view(), name='tramitacao_edit'),
    url(r'^protocoloadm/(?P<pk>\d+)/tramitacao_delete/(?P<oid>\d+)',
        TramitacaoAdmDeleteView.as_view(), name='tramitacao_delete'),

    url(r'^protocoloadm/(?P<pk>\d+)/(?P<ano>\d+)/comprovante$',
        ComprovanteProtocoloView.as_view(), name='comprovante_protocolo'),
    url(r'^protocoloadm/(?P<pk>\d+)/(?P<ano>\d+)/criar_documento$',
        CriarDocumentoProtocolo.as_view(), name='criar_documento'),


    # TODO: move to Proposicoes app
    url(r'^proposicoes$',
        ProposicaoView.as_view(), name='proposicao'),
    url(r'^proposicoes/proposicao-receber',
        ProposicaoReceberView.as_view(), name='proposicao_receber'),
    url(r'^proposicoes/proposicoes-naorecebidas',
        ProposicoesNaoRecebidasView.as_view(),
        name='proposicoes_naorecebidas'),
    url(r'^proposicoes/proposicoes-naoincorporadas',
        ProposicoesNaoIncorporadasView.as_view(),
        name='proposicoes_naoincorporadas'),
    url(r'^proposicoes/proposicoes-incorporadas',
        ProposicoesIncorporadasView.as_view(),
        name='proposicoes_incorporadas'),
    url(r'^proposicoes/(?P<pk>\d+)/proposicao',
        ProposicaoDetailView.as_view(), name='proposicao_view'),
]
