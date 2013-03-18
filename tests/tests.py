import keystone_user
import mock
from nose.tools import assert_equal


def setup_foo_tenant():
    keystone = mock.MagicMock()
    tenant = mock.Mock()
    tenant.id = "21b505b9cbf84bdfba60dc08cc2a4b8d"
    tenant.name = "foo"
    tenant.description = "The foo tenant"
    keystone.tenants.list = mock.Mock(return_value=[tenant])
    return keystone


def test_tenant_exists_when_present():
    # Setup
    keystone = setup_foo_tenant()

    # Code under test
    assert keystone_user.tenant_exists(keystone, "foo")


def test_tenant_exists_when_absent():
    # Setup
    keystone = setup_foo_tenant()

    # Code under test
    assert not keystone_user.tenant_exists(keystone, "bar")


def test_ensure_tenant_exists_when_present():
    # Setup
    keystone = setup_foo_tenant()

    # Code under test
    (changed, id) = keystone_user.ensure_tenant_exists(keystone, "foo",
                    "The foo tenant", False)

    # Assertions
    assert not changed
    assert_equal(id, "21b505b9cbf84bdfba60dc08cc2a4b8d")
