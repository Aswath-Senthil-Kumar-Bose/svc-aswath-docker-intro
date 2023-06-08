from ..app import app

def test_root():
    """
    Tests that a cow is in fact being returned on the / endpoint.
    """
    client = app.test_client()
    response = client.get("/")
    a_cow = "\n".join([
      "     \   ^__^",
      "      \  (oo)\_______",
      "         (__)\       )\/\\",
      "           ||----w |",
      "           ||     ||"
    ]).encode('utf-8')

    assert a_cow in response.data.encode('utf-8')
