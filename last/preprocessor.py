import cv2
import numpy as np
from sklearn.decomposition import PCA

# Extract frames from video
def extract_frames(video_path, num_frames=5):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = max(1, total_frames // num_frames)
    frames = []

    for i in range(num_frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i * frame_interval)
        ret, frame = cap.read()
        if ret:
            resized_frame = cv2.resize(frame, (224, 224))
            frames.append(resized_frame)

    cap.release()
    return frames

# Generate embeddings for frames
def get_frame_embeddings(frames):
    embeddings = []
    for frame in frames:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flattened_frame = gray_frame.flatten()
        embeddings.append(flattened_frame)

    # Apply PCA for dimensionality reduction
    embeddings = np.array(embeddings)
    n_components = min(50, embeddings.shape[0], embeddings.shape[1])
    pca = PCA(n_components=n_components)
    reduced_embeddings = pca.fit_transform(embeddings)
    return reduced_embeddings
