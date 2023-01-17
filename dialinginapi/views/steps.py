"""Module for all methods"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers,status
from dialinginapi.models import Step, Recipe

class StepView(ViewSet):
    """Class creates viewset for Step"""
    def retrieve(self, request, pk):
        """Handles GET requests for single step"""
        try:
            step = Step.objects.get(pk=pk)
            serializer = StepSerializer(step)

            return Response(serializer.data)

        except Step.DoesNotExist as ex:

            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handles GET requests for all steps"""
        steps = Step.objects.all()
        serializer = StepSerializer(steps, many=True)
        recipe = request.query_params.get('recipeId', None)
        try:
            if recipe is not None:
                steps_by_recipe = steps.filter(recipe_id = recipe)
                serializer = StepSerializer(steps_by_recipe, many=True)

                return Response(serializer.data)

        except Step.DoesNotExist as ex:

            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)

class StepSerializer(serializers.ModelSerializer):
    """Serilizer for Method Class"""
    class Meta:
        model = Step
        fields = (
          'id',
          'description',
          'recipe_id',
          'order',
        )
