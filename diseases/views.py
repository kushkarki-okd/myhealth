from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .services import symptoms, predict_diseases

class predictdiseases(APIView):
    renderer_classes=[TemplateHTMLRenderer,JSONRenderer]
    template_name="predict.html"

    def get(self, request):
        
        return Response({"symptoms":symptoms})

    
    def post(self, request):
        selected = request.data.get("symptoms", [])

        if not isinstance(selected, list) or not selected:
            return Response(
                {"error": "Kamti ma ek symptom select garnus."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        valid = [s for s in selected if s in symptoms]
        if not valid:
            return Response(
                {"error": "Invalid symptoms."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        disease, top3 = predict_diseases(valid)

        
        return Response({
            "prediction": disease,
            "top3": [{"disease": d, "probability": p} for d, p in top3],
        })