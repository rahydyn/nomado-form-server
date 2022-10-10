import json
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import FormSerializer
from .models import Form
from users.models import User

from .retrieve import retrieve_response, retrieve_content

##
from rest_framework.views import APIView
from rest_framework.response import Response

from api.mixins import ApiErrorsMixin, ApiAuthMixin, PublicApiMixin

from auth.services import jwt_login, google_validate_id_token

# from users.services import user_get_or_create
# from users.selectors import user_get_me
##

class FormListApi(ApiAuthMixin, ApiErrorsMixin, generics.ListAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = (AllowAny, )


# class FormInitApi(PublicApiMixin, ApiErrorsMixin, APIView):
class FormInitApi(PublicApiMixin, ApiErrorsMixin, generics.CreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        print(request.body)
        reqData = json.loads(request.body)
        formId = reqData["formId"]
        userId = reqData["userId"]
        email = reqData["email"]
        user = User.objects.filter(email=email).first()
        access_token = user.access_token
        refresh_token = user.refresh_token

        response_data = retrieve_content(form_id=formId, access_token=access_token, refresh_token=refresh_token)
        print(response_data)
        form = Form(title=response_data["info"]["documentTitle"], user=email, userId=userId, formId=formId)
        form.full_clean()
        form.save()

        response = Response(data=response_data)
        # response = jwt_login(response=response, user=user)

        return response


class FormDetailApi(generics.RetrieveAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = (AllowAny, )


{
    'formId': '1ooXsTF6Wysaw4KI2HfPxRczKE0rSlYPo8o7_RGQZqTk',
    'info': {
        'documentTitle': '無題のフォーム'
        },
    'revisionId': '00000003',
    'responderUri': 'https://docs.google.com/forms/d/e/1FAIpQLSdHP2hGn8fwD6jIf4ZSiwNBA5H-ufN2q-8pIIPtT3s5pPCSaQ/viewform',
    'items': [
        {
            'itemId': '020777b4',
            'title': '無題の質問',
            'questionItem': {
                'question': {
                    'questionId': '72a9b5b7',
                    'choiceQuestion': {
                        'type': 'RADIO',
                        'options': [
                            {
                                'value': 'オプション 1'
                            }
                        ]
                    }
                }
            }
        }
    ]
}