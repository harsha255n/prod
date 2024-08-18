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
    

class ListProductsView(APIView):
     def get(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class AddStockView(APIView):
    def post(self, request):
        data = request.data
        product_variant_id = data.get("product_variant_id")
        quantity = data.get("quantity")
        if product_variant_id and quantity:
            try:
                product_variant = Variants.objects.get(id=product_variant_id)
                stock = Stock(product_variant=product_variant, quantity=quantity)
                stock.save()
                return Response({"message": "Stock added successfully"}, status=201)
            except Variants.DoesNotExist:
                return Response({"error": "Product variant not found"}, status=404)
        return Response({"error": "Invalid request"}, status=400)

class DeleteProductView(APIView):
    def delete(self, request, product_id):
        try:
            product = Products.objects.get(id=product_id)
            product.delete()
            return Response({"message": "Product deleted successfully"}, status=200)
        except Products.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
