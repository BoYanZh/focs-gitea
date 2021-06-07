# coding: utf-8

# flake8: noqa
"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.14.2+makersmelx+BoYanZh
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from focs_gitea.models.api_error import APIError
from focs_gitea.models.access_token import AccessToken
from focs_gitea.models.add_collaborator_option import AddCollaboratorOption
from focs_gitea.models.add_time_option import AddTimeOption
from focs_gitea.models.annotated_tag import AnnotatedTag
from focs_gitea.models.annotated_tag_object import AnnotatedTagObject
from focs_gitea.models.attachment import Attachment
from focs_gitea.models.branch import Branch
from focs_gitea.models.branch_protection import BranchProtection
from focs_gitea.models.combined_status import CombinedStatus
from focs_gitea.models.comment import Comment
from focs_gitea.models.commit import Commit
from focs_gitea.models.commit_affected_files import CommitAffectedFiles
from focs_gitea.models.commit_date_options import CommitDateOptions
from focs_gitea.models.commit_meta import CommitMeta
from focs_gitea.models.commit_status import CommitStatus
from focs_gitea.models.commit_status_state import CommitStatusState
from focs_gitea.models.commit_user import CommitUser
from focs_gitea.models.contents_response import ContentsResponse
from focs_gitea.models.create_branch_protection_option import CreateBranchProtectionOption
from focs_gitea.models.create_branch_repo_option import CreateBranchRepoOption
from focs_gitea.models.create_email_option import CreateEmailOption
from focs_gitea.models.create_file_options import CreateFileOptions
from focs_gitea.models.create_fork_option import CreateForkOption
from focs_gitea.models.create_gpg_key_option import CreateGPGKeyOption
from focs_gitea.models.create_hook_option import CreateHookOption
from focs_gitea.models.create_hook_option_config import CreateHookOptionConfig
from focs_gitea.models.create_issue_comment_option import CreateIssueCommentOption
from focs_gitea.models.create_issue_option import CreateIssueOption
from focs_gitea.models.create_key_option import CreateKeyOption
from focs_gitea.models.create_label_option import CreateLabelOption
from focs_gitea.models.create_milestone_option import CreateMilestoneOption
from focs_gitea.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from focs_gitea.models.create_org_option import CreateOrgOption
from focs_gitea.models.create_pull_request_option import CreatePullRequestOption
from focs_gitea.models.create_pull_review_comment import CreatePullReviewComment
from focs_gitea.models.create_pull_review_options import CreatePullReviewOptions
from focs_gitea.models.create_release_option import CreateReleaseOption
from focs_gitea.models.create_repo_option import CreateRepoOption
from focs_gitea.models.create_status_option import CreateStatusOption
from focs_gitea.models.create_team_option import CreateTeamOption
from focs_gitea.models.create_user_option import CreateUserOption
from focs_gitea.models.cron import Cron
from focs_gitea.models.delete_email_option import DeleteEmailOption
from focs_gitea.models.delete_file_options import DeleteFileOptions
from focs_gitea.models.deploy_key import DeployKey
from focs_gitea.models.dismiss_pull_review_options import DismissPullReviewOptions
from focs_gitea.models.edit_attachment_options import EditAttachmentOptions
from focs_gitea.models.edit_branch_protection_option import EditBranchProtectionOption
from focs_gitea.models.edit_deadline_option import EditDeadlineOption
from focs_gitea.models.edit_git_hook_option import EditGitHookOption
from focs_gitea.models.edit_hook_option import EditHookOption
from focs_gitea.models.edit_issue_comment_option import EditIssueCommentOption
from focs_gitea.models.edit_issue_option import EditIssueOption
from focs_gitea.models.edit_label_option import EditLabelOption
from focs_gitea.models.edit_milestone_option import EditMilestoneOption
from focs_gitea.models.edit_org_option import EditOrgOption
from focs_gitea.models.edit_pull_request_option import EditPullRequestOption
from focs_gitea.models.edit_reaction_option import EditReactionOption
from focs_gitea.models.edit_release_option import EditReleaseOption
from focs_gitea.models.edit_repo_option import EditRepoOption
from focs_gitea.models.edit_team_option import EditTeamOption
from focs_gitea.models.edit_user_option import EditUserOption
from focs_gitea.models.email import Email
from focs_gitea.models.external_tracker import ExternalTracker
from focs_gitea.models.external_wiki import ExternalWiki
from focs_gitea.models.file_commit_response import FileCommitResponse
from focs_gitea.models.file_delete_response import FileDeleteResponse
from focs_gitea.models.file_links_response import FileLinksResponse
from focs_gitea.models.file_response import FileResponse
from focs_gitea.models.gpg_key import GPGKey
from focs_gitea.models.gpg_key_email import GPGKeyEmail
from focs_gitea.models.general_api_settings import GeneralAPISettings
from focs_gitea.models.general_attachment_settings import GeneralAttachmentSettings
from focs_gitea.models.general_repo_settings import GeneralRepoSettings
from focs_gitea.models.general_ui_settings import GeneralUISettings
from focs_gitea.models.git_blob_response import GitBlobResponse
from focs_gitea.models.git_entry import GitEntry
from focs_gitea.models.git_hook import GitHook
from focs_gitea.models.git_object import GitObject
from focs_gitea.models.git_service_type import GitServiceType
from focs_gitea.models.git_tree_response import GitTreeResponse
from focs_gitea.models.hook import Hook
from focs_gitea.models.identity import Identity
from focs_gitea.models.internal_tracker import InternalTracker
from focs_gitea.models.issue import Issue
from focs_gitea.models.issue_deadline import IssueDeadline
from focs_gitea.models.issue_labels_option import IssueLabelsOption
from focs_gitea.models.issue_template import IssueTemplate
from focs_gitea.models.label import Label
from focs_gitea.models.markdown_option import MarkdownOption
from focs_gitea.models.merge_pull_request_option import MergePullRequestOption
from focs_gitea.models.migrate_repo_form import MigrateRepoForm
from focs_gitea.models.migrate_repo_options import MigrateRepoOptions
from focs_gitea.models.milestone import Milestone
from focs_gitea.models.notification_count import NotificationCount
from focs_gitea.models.notification_subject import NotificationSubject
from focs_gitea.models.notification_thread import NotificationThread
from focs_gitea.models.o_auth2_application import OAuth2Application
from focs_gitea.models.organization import Organization
from focs_gitea.models.pr_branch_info import PRBranchInfo
from focs_gitea.models.payload_commit import PayloadCommit
from focs_gitea.models.payload_commit_verification import PayloadCommitVerification
from focs_gitea.models.payload_user import PayloadUser
from focs_gitea.models.permission import Permission
from focs_gitea.models.public_key import PublicKey
from focs_gitea.models.pull_request import PullRequest
from focs_gitea.models.pull_request_meta import PullRequestMeta
from focs_gitea.models.pull_review import PullReview
from focs_gitea.models.pull_review_comment import PullReviewComment
from focs_gitea.models.pull_review_request_options import PullReviewRequestOptions
from focs_gitea.models.reaction import Reaction
from focs_gitea.models.reference import Reference
from focs_gitea.models.release import Release
from focs_gitea.models.repo_commit import RepoCommit
from focs_gitea.models.repo_topic_options import RepoTopicOptions
from focs_gitea.models.repository import Repository
from focs_gitea.models.repository_meta import RepositoryMeta
from focs_gitea.models.review_state_type import ReviewStateType
from focs_gitea.models.search_results import SearchResults
from focs_gitea.models.server_version import ServerVersion
from focs_gitea.models.state_type import StateType
from focs_gitea.models.stop_watch import StopWatch
from focs_gitea.models.submit_pull_review_options import SubmitPullReviewOptions
from focs_gitea.models.tag import Tag
from focs_gitea.models.team import Team
from focs_gitea.models.time_stamp import TimeStamp
from focs_gitea.models.topic_name import TopicName
from focs_gitea.models.topic_response import TopicResponse
from focs_gitea.models.tracked_time import TrackedTime
from focs_gitea.models.transfer_repo_option import TransferRepoOption
from focs_gitea.models.update_file_options import UpdateFileOptions
from focs_gitea.models.user import User
from focs_gitea.models.user_heatmap_data import UserHeatmapData
from focs_gitea.models.watch_info import WatchInfo
