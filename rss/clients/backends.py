from typing import Literal, cast, get_args

from transmission_rpc import Client as TransmissionAPIClient
from qbittorrentapi import Client as QbittorrentAPIClient

from rss.clients.exceptions import UnknownTorrentClient
from rss.models import TorrentClient as TorrentClientModel


class TorrentClient:
    def __init__(self, tc_info: TorrentClientModel):
        self.tc_info = tc_info

    def add_torrent(self, torrent, download_dir, paused):
        pass


ProtocolLiteralType = Literal["http", "https"]


def get_protocol_literal(protocol: str) -> ProtocolLiteralType:
    valid_protocols = get_args(ProtocolLiteralType)
    if protocol not in valid_protocols:
        raise Exception(f"Invalid protocol '{protocol}'")
    return cast(ProtocolLiteralType, protocol)


def get_base_path(base_path: str) -> str:
    if base_path.startswith("/"):
        return base_path
    return f"/{base_path}"


class TransmissionClient(TorrentClient):
    def __init__(self, tc_info: TorrentClientModel):
        super().__init__(tc_info)
        base_path = get_base_path(tc_info.base_path)
        self.client = TransmissionAPIClient(
            protocol=get_protocol_literal(tc_info.protocol),
            host=tc_info.host,
            port=int(tc_info.port),
            username=tc_info.username,
            password=tc_info.password,
            path=base_path,
        )

    def add_torrent(self, torrent, download_dir, paused):
        self.client.add_torrent(
            torrent=torrent,
            download_dir=download_dir,
            paused=paused,
        )


class QbittorrentClient(TorrentClient):
    def __init__(self, tc_info: TorrentClientModel):
        super().__init__(tc_info)
        self.tc_info = tc_info
        base_path = get_base_path(tc_info.base_path)
        self.client = QbittorrentAPIClient(
            host=f"{tc_info.protocol}://{tc_info.host}:{tc_info.port}{base_path}",
            username=tc_info.username,
            password=tc_info.password,
        )

    def add_torrent(self, torrent, download_dir, paused):
        self.client.torrents_add(
            urls=torrent,
            save_path=download_dir,
            is_paused=paused,
        )


def get_torrent_client(client: TorrentClientModel) -> TorrentClient:
    if client.client_type == TorrentClientModel.ClientType.TRANSMISSION:
        return TransmissionClient(client)
    elif client.client_type == TorrentClientModel.ClientType.QBITTORRENT:
        return QbittorrentClient(client)

    raise UnknownTorrentClient(f"Unknown torrent client type '{client.client_type}'")
