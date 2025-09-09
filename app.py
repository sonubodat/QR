from flask import Flask, redirect, request
import os

app = Flask(__name__)

# 🔥 CONFIGURE YOUR LINKS HERE 🔥
IOS_LINK = "https://apps.apple.com/in/app/streefi/id6747432924"  # Replace with your iOS link
ANDROID_LINK = "https://play.google.com/store/apps/details?id=com.streefi.customer&pcampaignid=web_share"  # Replace with your Android link
DESKTOP_LINK = "https://streefi.in"  # Your website for desktop users

def detect_device(user_agent):
    """Simple device detection"""
    if not user_agent:
        return "desktop"
    
    user_agent = user_agent.lower()
    
    if "iphone" in user_agent or "ipad" in user_agent or "ipod" in user_agent:
        return "ios"
    elif "android" in user_agent:
        return "android"
    else:
        return "desktop"

@app.route('/')
def download():
    """Main QR code endpoint - Put this URL in your QR code"""
    user_agent = request.headers.get('User-Agent', '')
    device = detect_device(user_agent)
    
    # Smart redirect based on device
    if device == "ios":
        return redirect(IOS_LINK)
    elif device == "android":
        return redirect(ANDROID_LINK)
    else:
        # Redirect desktop users to your website
        return redirect(DESKTOP_LINK)

@app.route('/health')
def health():
    """Health check"""
    return {"status": "ok"}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=False, host='0.0.0.0', port=port)
