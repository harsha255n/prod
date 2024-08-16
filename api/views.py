from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products, Variants, SubVariants, Stock
from .serializers import ProductSerializer, VariantSerializer, SubVariantSerializer, StockSerializer

class CreateProductView(APIView):
    def post(self, request):
        data = request.data
        product_serializer = ProductSerializer(data=data)
        if product_serializer.is_valid():
            product = product_serializer.save()
            for variant in data.get("variants", []):
                variant_serializer = VariantSerializer(data=variant)
                if variant_serializer.is_valid():
                    variant_serializer.save(product=product)
                    for subvariant in variant.get("subvariants", []):
                        subvariant_serializer = SubVariantSerializer(data=subvariant)
                        if subvariant_serializer.is_valid():
                            subvariant_serializer.save(variant=variant_serializer.instance)
            return Response({"message": "Product created successfully"}, status=201)
        return Response({"error": "Invalid request"}, status=400)
