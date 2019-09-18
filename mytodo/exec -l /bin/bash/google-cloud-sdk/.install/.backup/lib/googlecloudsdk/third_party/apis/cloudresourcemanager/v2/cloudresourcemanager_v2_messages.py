"""Generated message classes for cloudresourcemanager version v2.

Creates, reads, and updates metadata for Google Cloud Platform resource
containers.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'cloudresourcemanager'


class AuditConfig(_messages.Message):
  r"""Specifies the audit configuration for a service. The configuration
  determines which permission types are logged, and what identities, if any,
  are exempted from logging. An AuditConfig must have one or more
  AuditLogConfigs.  If there are AuditConfigs for both `allServices` and a
  specific service, the union of the two AuditConfigs is used for that
  service: the log_types specified in each AuditConfig are enabled, and the
  exempted_members in each AuditLogConfig are exempted.  Example Policy with
  multiple AuditConfigs:      {       "audit_configs": [         {
  "service": "allServices"           "audit_log_configs": [             {
  "log_type": "DATA_READ",               "exempted_members": [
  "user:jose@example.com"               ]             },             {
  "log_type": "DATA_WRITE",             },             {
  "log_type": "ADMIN_READ",             }           ]         },         {
  "service": "sampleservice.googleapis.com"           "audit_log_configs": [
  {               "log_type": "DATA_READ",             },             {
  "log_type": "DATA_WRITE",               "exempted_members": [
  "user:aliya@example.com"               ]             }           ]         }
  ]     }  For sampleservice, this policy enables DATA_READ, DATA_WRITE and
  ADMIN_READ logging. It also exempts jose@example.com from DATA_READ logging,
  and aliya@example.com from DATA_WRITE logging.

  Fields:
    auditLogConfigs: The configuration for logging of each type of permission.
    service: Specifies a service that will be enabled for audit logging. For
      example, `storage.googleapis.com`, `cloudsql.googleapis.com`.
      `allServices` is a special value that covers all services.
  """

  auditLogConfigs = _messages.MessageField('AuditLogConfig', 1, repeated=True)
  service = _messages.StringField(2)


class AuditLogConfig(_messages.Message):
  r"""Provides the configuration for logging a type of permissions. Example:
  {       "audit_log_configs": [         {           "log_type": "DATA_READ",
  "exempted_members": [             "user:jose@example.com"           ]
  },         {           "log_type": "DATA_WRITE",         }       ]     }
  This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting
  jose@example.com from DATA_READ logging.

  Enums:
    LogTypeValueValuesEnum: The log type that this config enables.

  Fields:
    exemptedMembers: Specifies the identities that do not cause logging for
      this type of permission. Follows the same format of Binding.members.
    logType: The log type that this config enables.
  """

  class LogTypeValueValuesEnum(_messages.Enum):
    r"""The log type that this config enables.

    Values:
      LOG_TYPE_UNSPECIFIED: Default case. Should never be this.
      ADMIN_READ: Admin reads. Example: CloudIAM getIamPolicy
      DATA_WRITE: Data writes. Example: CloudSQL Users create
      DATA_READ: Data reads. Example: CloudSQL Users list
    """
    LOG_TYPE_UNSPECIFIED = 0
    ADMIN_READ = 1
    DATA_WRITE = 2
    DATA_READ = 3

  exemptedMembers = _messages.StringField(1, repeated=True)
  logType = _messages.EnumField('LogTypeValueValuesEnum', 2)


class Binding(_messages.Message):
  r"""Associates `members` with a `role`.

  Fields:
    condition: The condition that is associated with this binding. NOTE: An
      unsatisfied condition will not allow user access via current binding.
      Different bindings, including their conditions, are examined
      independently.
    members: Specifies the identities requesting access for a Cloud Platform
      resource. `members` can have the following values:  * `allUsers`: A
      special identifier that represents anyone who is    on the internet;
      with or without a Google account.  * `allAuthenticatedUsers`: A special
      identifier that represents anyone    who is authenticated with a Google
      account or a service account.  * `user:{emailid}`: An email address that
      represents a specific Google    account. For example,
      `alice@example.com` .   * `serviceAccount:{emailid}`: An email address
      that represents a service    account. For example, `my-other-
      app@appspot.gserviceaccount.com`.  * `group:{emailid}`: An email address
      that represents a Google group.    For example, `admins@example.com`.
      * `domain:{domain}`: The G Suite domain (primary) that represents all
      the    users of that domain. For example, `google.com` or `example.com`.
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`.
  """

  condition = _messages.MessageField('Expr', 1)
  members = _messages.StringField(2, repeated=True)
  role = _messages.StringField(3)


class CloudresourcemanagerFoldersCreateRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersCreateRequest object.

  Fields:
    folder: A Folder resource to be passed as the request body.
    parent: The resource name of the new Folder's parent. Must be of the form
      `folders/{folder_id}` or `organizations/{org_id}`.
  """

  folder = _messages.MessageField('Folder', 1)
  parent = _messages.StringField(2)


class CloudresourcemanagerFoldersDeleteRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersDeleteRequest object.

  Fields:
    foldersId: Part of `name`. the resource name of the Folder to be deleted.
      Must be of the form `folders/{folder_id}`.
  """

  foldersId = _messages.StringField(1, required=True)


class CloudresourcemanagerFoldersGetIamPolicyRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersGetIamPolicyRequest object.

  Fields:
    foldersId: Part of `resource`. REQUIRED: The resource for which the policy
      is being requested. See the operation documentation for the appropriate
      value for this field.
    getIamPolicyRequest: A GetIamPolicyRequest resource to be passed as the
      request body.
  """

  foldersId = _messages.StringField(1, required=True)
  getIamPolicyRequest = _messages.MessageField('GetIamPolicyRequest', 2)


class CloudresourcemanagerFoldersGetRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersGetRequest object.

  Fields:
    foldersId: Part of `name`. The resource name of the Folder to retrieve.
      Must be of the form `folders/{folder_id}`.
  """

  foldersId = _messages.StringField(1, required=True)


class CloudresourcemanagerFoldersListRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersListRequest object.

  Fields:
    pageSize: The maximum number of Folders to return in the response. This
      field is optional.
    pageToken: A pagination token returned from a previous call to
      `ListFolders` that indicates where this listing should continue from.
      This field is optional.
    parent: The resource name of the Organization or Folder whose Folders are
      being listed. Must be of the form `folders/{folder_id}` or
      `organizations/{org_id}`. Access to this method is controlled by
      checking the `resourcemanager.folders.list` permission on the `parent`.
    showDeleted: Controls whether Folders in the DELETE_REQUESTED state should
      be returned. Defaults to false. This field is optional.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3)
  showDeleted = _messages.BooleanField(4)


class CloudresourcemanagerFoldersMoveRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersMoveRequest object.

  Fields:
    foldersId: Part of `name`. The resource name of the Folder to move. Must
      be of the form folders/{folder_id}
    moveFolderRequest: A MoveFolderRequest resource to be passed as the
      request body.
  """

  foldersId = _messages.StringField(1, required=True)
  moveFolderRequest = _messages.MessageField('MoveFolderRequest', 2)


class CloudresourcemanagerFoldersPatchRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersPatchRequest object.

  Fields:
    folder: A Folder resource to be passed as the request body.
    foldersId: Part of `folder.name`. Output only. The resource name of the
      Folder. Its format is `folders/{folder_id}`, for example:
      "folders/1234".
    updateMask: Fields to be updated. Only the `display_name` can be updated.
  """

  folder = _messages.MessageField('Folder', 1)
  foldersId = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class CloudresourcemanagerFoldersSetIamPolicyRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersSetIamPolicyRequest object.

  Fields:
    foldersId: Part of `resource`. REQUIRED: The resource for which the policy
      is being specified. See the operation documentation for the appropriate
      value for this field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  foldersId = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class CloudresourcemanagerFoldersTestIamPermissionsRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersTestIamPermissionsRequest object.

  Fields:
    foldersId: Part of `resource`. REQUIRED: The resource for which the policy
      detail is being requested. See the operation documentation for the
      appropriate value for this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  foldersId = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class CloudresourcemanagerFoldersUndeleteRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersUndeleteRequest object.

  Fields:
    foldersId: Part of `name`. The resource name of the Folder to undelete.
      Must be of the form `folders/{folder_id}`.
    undeleteFolderRequest: A UndeleteFolderRequest resource to be passed as
      the request body.
  """

  foldersId = _messages.StringField(1, required=True)
  undeleteFolderRequest = _messages.MessageField('UndeleteFolderRequest', 2)


class Expr(_messages.Message):
  r"""Represents an expression text. Example:      title: "User account
  presence"     description: "Determines whether the request has a user
  account"     expression: "size(request.user) > 0"

  Fields:
    description: An optional description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.  The application context of the containing message
      determines which well-known feature set of CEL is supported.
    location: An optional string indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: An optional title for the expression, i.e. a short string
      describing its purpose. This can be used e.g. in UIs which allow to
      enter the expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class Folder(_messages.Message):
  r"""A Folder in an Organization's resource hierarchy, used to organize that
  Organization's resources.

  Enums:
    LifecycleStateValueValuesEnum: Output only. The lifecycle state of the
      folder. Updates to the lifecycle_state must be performed via
      DeleteFolder and UndeleteFolder.

  Fields:
    createTime: Output only. Timestamp when the Folder was created. Assigned
      by the server.
    displayName: The folder's display name. A folder's display name must be
      unique amongst its siblings, e.g. no two folders with the same parent
      can share the same display name. The display name must start and end
      with a letter or digit, may contain letters, digits, spaces, hyphens and
      underscores and can be no longer than 30 characters. This is captured by
      the regular expression: [\p{L}\p{N}]([\p{L}\p{N}_-
      ]{0,28}[\p{L}\p{N}])?.
    lifecycleState: Output only. The lifecycle state of the folder. Updates to
      the lifecycle_state must be performed via DeleteFolder and
      UndeleteFolder.
    name: Output only. The resource name of the Folder. Its format is
      `folders/{folder_id}`, for example: "folders/1234".
    parent: The Folder's parent's resource name. Updates to the folder's
      parent must be performed via MoveFolder.
  """

  class LifecycleStateValueValuesEnum(_messages.Enum):
    r"""Output only. The lifecycle state of the folder. Updates to the
    lifecycle_state must be performed via DeleteFolder and UndeleteFolder.

    Values:
      LIFECYCLE_STATE_UNSPECIFIED: Unspecified state.
      ACTIVE: The normal and active state.
      DELETE_REQUESTED: The folder has been marked for deletion by the user.
    """
    LIFECYCLE_STATE_UNSPECIFIED = 0
    ACTIVE = 1
    DELETE_REQUESTED = 2

  createTime = _messages.StringField(1)
  displayName = _messages.StringField(2)
  lifecycleState = _messages.EnumField('LifecycleStateValueValuesEnum', 3)
  name = _messages.StringField(4)
  parent = _messages.StringField(5)


class FolderOperation(_messages.Message):
  r"""Metadata describing a long running folder operation

  Enums:
    OperationTypeValueValuesEnum: The type of this operation.

  Fields:
    destinationParent: The resource name of the folder or organization we are
      either creating the folder under or moving the folder to.
    displayName: The display name of the folder.
    operationType: The type of this operation.
    sourceParent: The resource name of the folder's parent. Only applicable
      when the operation_type is MOVE.
  """

  class OperationTypeValueValuesEnum(_messages.Enum):
    r"""The type of this operation.

    Values:
      OPERATION_TYPE_UNSPECIFIED: Operation type not specified.
      CREATE: A create folder operation.
      MOVE: A move folder operation.
    """
    OPERATION_TYPE_UNSPECIFIED = 0
    CREATE = 1
    MOVE = 2

  destinationParent = _messages.StringField(1)
  displayName = _messages.StringField(2)
  operationType = _messages.EnumField('OperationTypeValueValuesEnum', 3)
  sourceParent = _messages.StringField(4)


class FolderOperationError(_messages.Message):
  r"""A classification of the Folder Operation error.

  Enums:
    ErrorMessageIdValueValuesEnum: The type of operation error experienced.

  Fields:
    errorMessageId: The type of operation error experienced.
  """

  class ErrorMessageIdValueValuesEnum(_messages.Enum):
    r"""The type of operation error experienced.

    Values:
      ERROR_TYPE_UNSPECIFIED: The error type was unrecognized or unspecified.
      ACTIVE_FOLDER_HEIGHT_VIOLATION: The attempted action would violate the
        max folder depth constraint.
      MAX_CHILD_FOLDERS_VIOLATION: The attempted action would violate the max
        child folders constraint.
      FOLDER_NAME_UNIQUENESS_VIOLATION: The attempted action would violate the
        locally-unique folder display_name constraint.
      RESOURCE_DELETED_VIOLATION: The resource being moved has been deleted.
      PARENT_DELETED_VIOLATION: The resource a folder was being added to has
        been deleted.
      CYCLE_INTRODUCED_VIOLATION: The attempted action would introduce cycle
        in resource path.
      FOLDER_BEING_MOVED_VIOLATION: The attempted action would move a folder
        that is already being moved.
      FOLDER_TO_DELETE_NON_EMPTY_VIOLATION: The folder the caller is trying to
        delete contains active resources.
      DELETED_FOLDER_HEIGHT_VIOLATION: The attempted action would violate the
        max deleted folder depth constraint.
    """
    ERROR_TYPE_UNSPECIFIED = 0
    ACTIVE_FOLDER_HEIGHT_VIOLATION = 1
    MAX_CHILD_FOLDERS_VIOLATION = 2
    FOLDER_NAME_UNIQUENESS_VIOLATION = 3
    RESOURCE_DELETED_VIOLATION = 4
    PARENT_DELETED_VIOLATION = 5
    CYCLE_INTRODUCED_VIOLATION = 6
    FOLDER_BEING_MOVED_VIOLATION = 7
    FOLDER_TO_DELETE_NON_EMPTY_VIOLATION = 8
    DELETED_FOLDER_HEIGHT_VIOLATION = 9

  errorMessageId = _messages.EnumField('ErrorMessageIdValueValuesEnum', 1)


class GetIamPolicyRequest(_messages.Message):
  r"""Request message for `GetIamPolicy` method.

  Fields:
    options: OPTIONAL: A `GetPolicyOptions` object for specifying options to
      `GetIamPolicy`. This field is only used by Cloud IAM.
  """

  options = _messages.MessageField('GetPolicyOptions', 1)


class GetPolicyOptions(_messages.Message):
  r"""Encapsulates settings provided to GetIamPolicy.

  Fields:
    requestedPolicyVersion: Optional. The policy format version to be
      returned.  Valid values are 0, 1, and 3. Requests specifying an invalid
      value will be rejected.  Requests for policies with any conditional
      bindings must specify version 3. Policies without any conditional
      bindings may specify any valid value or leave the field unset.
  """

  requestedPolicyVersion = _messages.IntegerField(1, variant=_messages.Variant.INT32)


class ListFoldersResponse(_messages.Message):
  r"""The ListFolders response message.

  Fields:
    folders: A possibly paginated list of Folders that are direct descendants
      of the specified parent resource.
    nextPageToken: A pagination token returned from a previous call to
      `ListFolders` that indicates from where listing should continue. This
      field is optional.
  """

  folders = _messages.MessageField('Folder', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class MoveFolderRequest(_messages.Message):
  r"""The MoveFolder request message.

  Fields:
    destinationParent: The resource name of the Folder or Organization to
      reparent the folder under. Must be of the form `folders/{folder_id}` or
      `organizations/{org_id}`.
  """

  destinationParent = _messages.StringField(1)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should have the format of `operations/some/unique/name`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class Policy(_messages.Message):
  r"""Defines an Identity and Access Management (IAM) policy. It is used to
  specify access control policies for Cloud Platform resources.   A `Policy`
  consists of a list of `bindings`. A `binding` binds a list of `members` to a
  `role`, where the members can be user accounts, Google groups, Google
  domains, and service accounts. A `role` is a named list of permissions
  defined by IAM.  **JSON Example**      {       "bindings": [         {
  "role": "roles/owner",           "members": [
  "user:mike@example.com",             "group:admins@example.com",
  "domain:google.com",             "serviceAccount:my-other-
  app@appspot.gserviceaccount.com"           ]         },         {
  "role": "roles/viewer",           "members": ["user:sean@example.com"]
  }       ]     }  **YAML Example**      bindings:     - members:       -
  user:mike@example.com       - group:admins@example.com       -
  domain:google.com       - serviceAccount:my-other-
  app@appspot.gserviceaccount.com       role: roles/owner     - members:
  - user:sean@example.com       role: roles/viewer   For a description of IAM
  and its features, see the [IAM developer's
  guide](https://cloud.google.com/iam/docs).

  Fields:
    auditConfigs: Specifies cloud audit logging configuration for this policy.
    bindings: Associates a list of `members` to a `role`. `bindings` with no
      members will result in an error.
    etag: `etag` is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the `etag` in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: An `etag` is returned in the response to `getIamPolicy`, and
      systems are expected to put that etag in the request to `setIamPolicy`
      to ensure that their change will be applied to the same version of the
      policy.  If no `etag` is provided in the call to `setIamPolicy`, then
      the existing policy is overwritten.
    version: Specifies the format of the policy.  Valid values are 0, 1, and
      3. Requests specifying an invalid value will be rejected.  Policies with
      any conditional bindings must specify version 3. Policies without any
      conditional bindings may specify any valid value or leave the field
      unset.
  """

  auditConfigs = _messages.MessageField('AuditConfig', 1, repeated=True)
  bindings = _messages.MessageField('Binding', 2, repeated=True)
  etag = _messages.BytesField(3)
  version = _messages.IntegerField(4, variant=_messages.Variant.INT32)


class ProjectCreationStatus(_messages.Message):
  r"""A status object which is used as the `metadata` field for the Operation
  returned by CreateProject. It provides insight for when significant phases
  of Project creation have completed.

  Fields:
    createTime: Creation time of the project creation workflow.
    gettable: True if the project can be retrieved using GetProject. No other
      operations on the project are guaranteed to work until the project
      creation is complete.
    ready: True if the project creation process is complete.
  """

  createTime = _messages.StringField(1)
  gettable = _messages.BooleanField(2)
  ready = _messages.BooleanField(3)


class SearchFoldersRequest(_messages.Message):
  r"""The request message for searching folders.

  Fields:
    pageSize: The maximum number of folders to return in the response. This
      field is optional.
    pageToken: A pagination token returned from a previous call to
      `SearchFolders` that indicates from where search should continue. This
      field is optional.
    query: Search criteria used to select the Folders to return. If no search
      criteria is specified then all accessible folders will be returned.
      Query expressions can be used to restrict results based upon
      displayName, lifecycleState and parent, where the operators `=`, `NOT`,
      `AND` and `OR` can be used along with the suffix wildcard symbol `*`.
      The displayName field in a query expression should use escaped quotes
      for values that include whitespace to prevent unexpected behavior.  Some
      example queries are:  * Query `displayName=Test*` returns Folder
      resources whose display name starts with "Test". * Query
      `lifecycleState=ACTIVE` returns Folder resources with `lifecycleState`
      set to `ACTIVE`. * Query `parent=folders/123` returns Folder resources
      that have `folders/123` as a parent resource. * Query
      `parent=folders/123 AND lifecycleState=ACTIVE` returns active Folder
      resources that have `folders/123` as a parent resource. * Query
      `displayName=\\"Test String\\"` returns Folder resources with display
      names that include both "Test" and "String".
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  query = _messages.StringField(3)


class SearchFoldersResponse(_messages.Message):
  r"""The response message for searching folders.

  Fields:
    folders: A possibly paginated folder search results. the specified parent
      resource.
    nextPageToken: A pagination token returned from a previous call to
      `SearchFolders` that indicates from where searching should continue.
      This field is optional.
  """

  folders = _messages.MessageField('Folder', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class SetIamPolicyRequest(_messages.Message):
  r"""Request message for `SetIamPolicy` method.

  Fields:
    policy: REQUIRED: The complete policy to be applied to the `resource`. The
      size of the policy is limited to a few 10s of KB. An empty policy is a
      valid policy but certain Cloud Platform services (such as Projects)
      might reject them.
    updateMask: OPTIONAL: A FieldMask specifying which fields of the policy to
      modify. Only the fields in the mask will be modified. If no mask is
      provided, the following default mask is used: paths: "bindings, etag"
      This field is only used by Cloud IAM.
  """

  policy = _messages.MessageField('Policy', 1)
  updateMask = _messages.StringField(2)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details.  You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class TestIamPermissionsRequest(_messages.Message):
  r"""Request message for `TestIamPermissions` method.

  Fields:
    permissions: The set of permissions to check for the `resource`.
      Permissions with wildcards (such as '*' or 'storage.*') are not allowed.
      For more information see [IAM
      Overview](https://cloud.google.com/iam/docs/overview#permissions).
  """

  permissions = _messages.StringField(1, repeated=True)


class TestIamPermissionsResponse(_messages.Message):
  r"""Response message for `TestIamPermissions` method.

  Fields:
    permissions: A subset of `TestPermissionsRequest.permissions` that the
      caller is allowed.
  """

  permissions = _messages.StringField(1, repeated=True)


class UndeleteFolderRequest(_messages.Message):
  r"""The UndeleteFolder request message."""


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
