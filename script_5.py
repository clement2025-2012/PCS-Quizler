# Create the final ZIP file
zip_filename = "PCS-Academy-Quiz-App-Final.zip"

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Add all files from the project directory
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arc_name = os.path.relpath(file_path, project_dir)
            zipf.write(file_path, arc_name)
            print(f"Added to ZIP: {arc_name}")

print(f"\n✅ Successfully created ZIP file: {zip_filename}")
print(f"📦 ZIP file size: {os.path.getsize(zip_filename) / (1024*1024):.2f} MB")

# List ZIP contents
print("\n📋 ZIP Contents:")
with zipfile.ZipFile(zip_filename, 'r') as zipf:
    for info in zipf.filelist:
        print(f"  📄 {info.filename} ({info.file_size} bytes)")

print("\n🎯 Deployment Instructions:")
print("1. Download the ZIP file")
print("2. Extract it to your local machine")
print("3. Upload to Render, Netlify, or any static hosting platform")
print("4. For Render: Set build command to 'npm run build' and publish directory to './'")
print("5. Your PCS Academy Quiz App will be live and ready for AdSense approval!")

print(f"\n📁 ZIP file created: {zip_filename}")