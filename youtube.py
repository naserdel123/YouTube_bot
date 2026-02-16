import yt_dlp
import re

async def search_youtube(query: str, max_results: int = 5):
    """البحث في يوتيوب باستخدام yt-dlp (بدون API)"""
    
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': False,
    }
    
    search_query = f"ytsearch{max_results}:{query}"
    
    try:
        # استخدام run_in_executor لأن yt_dlp synchronous
        import asyncio
        loop = asyncio.get_event_loop()
        
        def extract():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(search_query, download=False)
        
        info = await loop.run_in_executor(None, extract)
        
        results = []
        for entry in info.get('entries', []):
            results.append({
                'id': entry.get('id'),
                'title': entry.get('title', 'بدون عنوان'),
                'channel': entry.get('uploader', 'غير معروف'),
                'duration': format_duration(entry.get('duration', 0)),
                'views': entry.get('view_count', 0),
                'thumbnail': entry.get('thumbnail', ''),
                'url': f"https://youtube.com/watch?v={entry.get('id')}"
            })
        
        return results
        
    except Exception as e:
        print(f"Error searching YouTube: {e}")
        return []

def format_duration(seconds: int) -> str:
    """تحويل الثواني إلى صيغة مقروءة"""
    if not seconds:
        return "غير معروف"
    
    minutes = seconds // 60
    secs = seconds % 60
    
    if minutes >= 60:
        hours = minutes // 60
        minutes = minutes % 60
        return f"{hours}:{minutes:02d}:{secs:02d}"
    
    return f"{minutes}:{secs:02d}"
    