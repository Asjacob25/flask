from . import json as json
from .app import Flask as Flask
from .app import Request as Request
from .app import Response as Response
from .blueprints import Blueprint as Blueprint
from .config import Config as Config
from .ctx import after_this_request as after_this_request
from .ctx import copy_current_request_context as copy_current_request_context
from .ctx import has_app_context as has_app_context
from .ctx import has_request_context as has_request_context
from .globals import current_app as current_app
from .globals import g as g
from .globals import request as request
from .globals import session as session
from .helpers import abort as abort
from .helpers import flash as flash
from .helpers import get_flashed_messages as get_flashed_messages
from .helpers import get_template_attribute as get_template_attribute
from .helpers import make_response as make_response
from .helpers import redirect as redirect
from .helpers import send_file as send_file
from .helpers import send_from_directory as send_from_directory
from .helpers import stream_with_context as stream_with_context
from .helpers import url_for as url_for
from .json import jsonify as jsonify
from .signals import appcontext_popped as appcontext_popped
from .signals import appcontext_pushed as appcontext_pushed
from .signals import appcontext_tearing_down as appcontext_tearing_down
from .signals import before_render_template as before_render_template
from .signals import got_request_exception as got_request_exception
from .signals import message_flashed as message_flashed
from .signals import request_finished as request_finished
from .signals import request_started as request_started
from .signals import request_tearing_down as request_tearing_down
from .signals import template_rendered as template_rendered
from .templating import render_template as render_template
from .templating import render_template_string as render_template_string
from .templating import stream_template as stream_template
from .templating import stream_template_string as stream_template_string

__version__ = "2.3.2.dev"


def __getattr__(name):
    if name == "_app_ctx_stack":
        import warnings
        from .globals import __app_ctx_stack

        warnings.warn(
            "'_app_ctx_stack' is deprecated and will be removed in Flask 2.4.",
            DeprecationWarning,
            stacklevel=2,
        )
        return __app_ctx_stack

    if name == "_request_ctx_stack":
        import warnings
        from .globals import __request_ctx_stack

        warnings.warn(
            "'_request_ctx_stack' is deprecated and will be removed in Flask 2.4.",
            DeprecationWarning,
            stacklevel=2,
        )
        return __request_ctx_stack

    if name == "escape":
        import warnings
        from markupsafe import escape

        warnings.warn(
            "'flask.escape' is deprecated and will be removed in Flask 2.4. Import"
            " 'markupsafe.escape' instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return escape

    if name == "Markup":
        import warnings
        from markupsafe import Markup

        warnings.warn(
            "'flask.Markup' is deprecated and will be removed in Flask 2.4. Import"
            " 'markupsafe.Markup' instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return Markup

    if name == "signals_available":
        import warnings

        warnings.warn(
            "'signals_available' is deprecated and will be removed in Flask 2.4."
            " Signals are always available",
            DeprecationWarning,
            stacklevel=2,
        )
        return True

    raise AttributeError(name)
