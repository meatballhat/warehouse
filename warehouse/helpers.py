# Copyright 2013 Donald Stufft
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
import json
import os.path
import urllib.parse


def url_for(request, endpoint, **values):
    force_external = values.pop("_force_external", False)
    return request.url_adapter.build(
        endpoint, values,
        force_external=force_external,
    )


def gravatar_url(email, size=80):
    if email is None:
        email = ""

    email_hash = hashlib.md5(email.strip().lower().encode("utf8")).hexdigest()

    url = "https://secure.gravatar.com/avatar/{}".format(email_hash)
    params = {
        "size": size,
    }

    return "?".join([url, urllib.parse.urlencode(params)])


def static_url(app, filename):
    """
    static_url('css/bootstrap.css')
    """
    with open(os.path.join(app.static_dir, "assets.json"), "r") as fp:
        assets = json.load(fp)

    return urllib.parse.urljoin(
        app.static_path,
        assets.get(filename, filename),
    )
