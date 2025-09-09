import qrcode

# Replace this URL with your hosted app URL
url = "https://streefi.in"  # Or your smart QR redirect link

# Generate QR code
qr_img = qrcode.make(url)

# Save to a file
qr_img.save("smart_qr.png")

print("✅ QR code saved as smart_qr.png")
