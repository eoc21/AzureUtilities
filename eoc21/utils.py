"""
Simple utils module for basic routines to
work with containers and block blob storage
"""
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings

__author__ = 'edwardcannon'


class AzureUtilities(object):
    """
    Basic skeleton class to work with block blob
    storage on Azure
    """
    def __init__(self, account_name,
                 key):
        self.block_blob_service = BlockBlobService(account_name,
                                                   key)
        self.container_names = []

    def create_container(self, container_name, public_access):
        """
        Creates a container
        :param container_name:
        :return:
        """
        if public_access:
            self.block_blob_service.create_container(container_name,
                                                     public_access=PublicAccess.Container)
            self.container_names.append(container_name)
        else:
            self.block_blob_service.create_container(container_name)
            self.container_names.append(container_name)

    def create_blob(self, container_name,
                    blob_name, upload_file,
                    file_type):
        """
        Creates a blob on specified Azure account
        :param container_name: Container name
        :param blob_name: Desired blob name
        :param upload_file: File to upload to blob
        :param file_type: Input file type
        :return:
        """
        self.block_blob_service.create_blob_from_path(container_name,
                                                      blob_name,
                                                      upload_file,
                                                      content_settings=ContentSettings(content_type=file_type))

    def download_single_file(self,
                             container_name,
                             blob_name,
                             output_file):
        """
        Downloads a specific file from a blob and container
        :param container_name: Container
        :param blob_name: Blob
        :param output_file: Requested output file name
        :return:
        """

        self.block_blob_service.get_blob_to_path(container_name,
                                                 blob_name,
                                                 output_file)

if __name__ == '__main__':
    az_util = AzureUtilities(account_name='N/A',
                             key='N/A')
    az_util.download_single_file('N/A', 'N/A', 'N/A')
