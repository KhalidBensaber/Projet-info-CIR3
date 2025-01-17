from django.shortcuts import render
from .models import TelemetryLog
from django.db.models import Avg, Count  # Import the required aggregate functions
from django.http import JsonResponse

def telemetry_dashboard(request):
    logs = TelemetryLog.objects.all()
    total_requests = TelemetryLog.objects.count()
    avg_response_time = TelemetryLog.objects.aggregate(Avg('response_time'))['response_time__avg']
    status_counts = TelemetryLog.objects.values('status_code').annotate(count=Count('status_code'))

    return render(request, 'telemetry_dashboard.html', {
        'logs': logs,
        'total_requests': total_requests,
        'avg_response_time': avg_response_time,
        'status_counts': status_counts,
    })
    
    

def telemetry_api(request):
    total_requests = TelemetryLog.objects.count()
    avg_response_time = TelemetryLog.objects.aggregate(Avg('response_time'))['response_time__avg']
    status_counts = list(TelemetryLog.objects.values('status_code').annotate(count=Count('status_code')))

    return JsonResponse({
        "total_requests": total_requests,
        "avg_response_time": avg_response_time,
        "status_counts": status_counts,
    })

