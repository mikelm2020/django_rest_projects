from rest_framework import serializers

from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("state", "created_date", "modified_date", "deleted_date")

    def validate_measure_unit(self, value):
        if value == "" or value == None:
            raise serializers.ValidationError("Debe ingresar una Unidad de Medida.")
        return value

    def validate_category_product(self, value):
        if value == "" or value == None:
            raise serializers.ValidationError(
                "Debe ingresar una Categoría de Producto."
            )
        return value

    def validate(self, data):
        if "measure_unit" not in data.keys():
            raise serializers.ValidationError(
                {"measure_unit": "Debe ingresar una Unidad de Medida."}
            )

        if "category_product" not in data.keys():
            raise serializers.ValidationError(
                {"category_product": "Debe ingresar una Categoría de Producto."}
            )

        return data

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "description": instance.description,
            "image": instance.image.url if instance.image != "" else "",
            "measure_unit": instance.measure_unit.description
            if instance.measure_unit is not None
            else "",
            "category_product": instance.category_product.description
            if instance.category_product
            else "",
        }
