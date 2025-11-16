from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
from .models import EquipmentDataset
from .serializers import EquipmentDatasetSerializer
from .utils import analyze_csv_file, generate_pdf_report
import tempfile

@api_view(['POST'])
def upload_csv(request):
    if 'file' not in request.FILES:
        return Response({"error": "No file uploaded"}, status=400)

    file = request.FILES['file']
    summary = analyze_csv_file(file)

    entry = EquipmentDataset.objects.create(
        file_name=file.name,
        summary=summary
    )

    return Response(summary)

@api_view(['GET'])
def history(request):
    qs = EquipmentDataset.objects.all().order_by('-uploaded_at')[:5]
    ser = EquipmentDatasetSerializer(qs, many=True)
    return Response(ser.data)

@api_view(['GET'])
def pdf_report(request, pk):
    dataset = EquipmentDataset.objects.get(id=pk)

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    generate_pdf_report(dataset.summary, tmp.name)

    return FileResponse(open(tmp.name, 'rb'), as_attachment=True, filename=f"report_{pk}.pdf")
