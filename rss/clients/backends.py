from transmission_rpc import Client as TransmissionAPIClient
from qbittorrentapi import Client as QbittorrentAPIClient

from rss.clients.exceptions import UnknownTorrentClient
from rss.models import TorrentClient as TorrentClientModel


class TorrentClient:
    @staticmethod
    def from_client_id(client_id: int):
        tc_info = TorrentClientModel.objects.get(id=client_id)

        if tc_info.client_type == TorrentClientModel.ClientType.TRANSMISSION:
            return TransmissionClient(tc_info)
        elif tc_info.client_type == TorrentClientModel.ClientType.QBITTORRENT:
            return QbittorrentClient(tc_info)

        raise UnknownTorrentClient(
            f"torrent client type '{tc_info.client_type}' is unknown to me"
        )

    def add_torrent(self, torrent, download_dir, paused):
        pass


class TransmissionClient(TorrentClient):
    def __init__(self, tc_info):
        self.client = TransmissionAPIClient(
            protocol=tc_info.protocol,
            host=tc_info.host,
            port=tc_info.port,
            username=tc_info.username,
            password=tc_info.password,
            path=tc_info.base_path,
        )

    def add_torrent(self, torrent, download_dir, paused):
        self.client.add_torrent(
            torrent=torrent,
            download_dir=download_dir,
            paused=paused,
        )


class QbittorrentClient(TorrentClient):
    def __init__(self, tc_info: TorrentClientModel):
        self.client = QbittorrentAPIClient(
            host=f"{tc_info.host}:{tc_info.port}",
            username=tc_info.username,
            password=tc_info.password,
        )

    def add_torrent(self, torrent, download_dir, paused):
        self.client.torrents_add(
            urls=torrent,
            save_path=download_dir,
            is_paused=paused,
        )
