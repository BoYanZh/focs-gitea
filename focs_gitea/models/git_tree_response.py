# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.14.2+makersmelx+BoYanZh
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from focs_gitea.configuration import Configuration


class GitTreeResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'page': 'int',
        'sha': 'str',
        'total_count': 'int',
        'tree': 'list[GitEntry]',
        'truncated': 'bool',
        'url': 'str'
    }

    attribute_map = {
        'page': 'page',
        'sha': 'sha',
        'total_count': 'total_count',
        'tree': 'tree',
        'truncated': 'truncated',
        'url': 'url'
    }

    def __init__(self, page=None, sha=None, total_count=None, tree=None, truncated=None, url=None, _configuration=None):  # noqa: E501
        """GitTreeResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page = None
        self._sha = None
        self._total_count = None
        self._tree = None
        self._truncated = None
        self._url = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if sha is not None:
            self.sha = sha
        if total_count is not None:
            self.total_count = total_count
        if tree is not None:
            self.tree = tree
        if truncated is not None:
            self.truncated = truncated
        if url is not None:
            self.url = url

    @property
    def page(self):
        """Gets the page of this GitTreeResponse.  # noqa: E501


        :return: The page of this GitTreeResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this GitTreeResponse.


        :param page: The page of this GitTreeResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def sha(self):
        """Gets the sha of this GitTreeResponse.  # noqa: E501


        :return: The sha of this GitTreeResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this GitTreeResponse.


        :param sha: The sha of this GitTreeResponse.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def total_count(self):
        """Gets the total_count of this GitTreeResponse.  # noqa: E501


        :return: The total_count of this GitTreeResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this GitTreeResponse.


        :param total_count: The total_count of this GitTreeResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def tree(self):
        """Gets the tree of this GitTreeResponse.  # noqa: E501


        :return: The tree of this GitTreeResponse.  # noqa: E501
        :rtype: list[GitEntry]
        """
        return self._tree

    @tree.setter
    def tree(self, tree):
        """Sets the tree of this GitTreeResponse.


        :param tree: The tree of this GitTreeResponse.  # noqa: E501
        :type: list[GitEntry]
        """

        self._tree = tree

    @property
    def truncated(self):
        """Gets the truncated of this GitTreeResponse.  # noqa: E501


        :return: The truncated of this GitTreeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._truncated

    @truncated.setter
    def truncated(self, truncated):
        """Sets the truncated of this GitTreeResponse.


        :param truncated: The truncated of this GitTreeResponse.  # noqa: E501
        :type: bool
        """

        self._truncated = truncated

    @property
    def url(self):
        """Gets the url of this GitTreeResponse.  # noqa: E501


        :return: The url of this GitTreeResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GitTreeResponse.


        :param url: The url of this GitTreeResponse.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GitTreeResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GitTreeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GitTreeResponse):
            return True

        return self.to_dict() != other.to_dict()
