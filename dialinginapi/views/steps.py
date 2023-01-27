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
        recipe = request.query_params.get('recipeId', None)
        try:
            if recipe is not None:
                steps_by_recipe = steps.filter(recipe_id = recipe).order_by('order')
                serializer = StepSerializer(steps_by_recipe, many=True)

                return Response(serializer.data)

        except Step.DoesNotExist as ex:

            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        serializer = StepSerializer(steps, many=True)
        return Response(serializer.data)

    def create(self, request):
        """_summary_

        Args:
            request (_type_): _description_
        """
        recipe = Recipe.objects.get(pk = request.data['recipe_id'])
        steps = Step.objects.all()
        recipe_steps = steps.filter(recipe_id_id = recipe)

        if len(recipe_steps) > 0:
            sorted_data = recipe_steps.order_by('order')
            last_order = sorted_data.last()
            step = Step.objects.create(
                description = request.data['description'],
                recipe_id = recipe,
                order = last_order.order + 1
            )
            serializer = StepSerializer(step)
            return Response(serializer.data)
        step = Step.objects.create(
            description = request.data['description'],
            recipe_id = recipe,
            order = 1
        )
        serializer = StepSerializer(step)
        return Response(serializer.data)
    def destroy(self, request,pk):
        """_summary_

        Args:
            request (_type_): _description_
            pk (_type_): _description_
        """
        step = Step.objects.get(pk=pk)
        step.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
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
