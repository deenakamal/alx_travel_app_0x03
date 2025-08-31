from .tasks import send_booking_confirmation_email


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        send_booking_confirmation_email.delay(
            booking.user.email,
            f'Booking ID: {booking.id}, Hotel: {booking.hotel.name}'
        )
