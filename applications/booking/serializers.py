from rest_framework import serializers

from applications.booking.models import BookingDiagnostic

from applications.booking.utils import check_master_stack, check_date, check_is_master


class BookingDiagnosticSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingDiagnostic
        fields = ('master', 'date', 'time')

    def validate(self, attrs):
        if check_is_master(attrs.get('master')):
            raise serializers.ValidationError('You can book a queue only with the master!')
        if check_date(attrs.get('date')):
            raise serializers.ValidationError('Booking are only possible on weekdays!')
        if check_master_stack(**attrs):
            raise serializers.ValidationError('Time is\'nt available, choose another!')
        return attrs

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['client_id'] = request.user.id
        booking_obj = BookingDiagnostic.objects.create(**validated_data)
        return booking_obj
