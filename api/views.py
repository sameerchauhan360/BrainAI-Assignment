from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.model import predict_mental_health
from .models import AssessmentResponse


@api_view(["POST"])
def predict_mental_health_view(request):
    """
    API view to predict mental health status from questionnaire responses.
    """

    if request.method == "POST":

        responses = request.data.get("responses")

        if len(responses) != 16:
            return Response(
                {"error": "Invalid no. of responses. Expected 16."}, status=400
            )

        prediction = predict_mental_health(responses)

        AssessmentResponse.objects.create(
            responses=responses,
            predicted_condition=prediction,
        )

        return Response(
            {
                "mental_health_status": prediction,
            }
        )
