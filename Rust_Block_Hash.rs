use sha2::{Sha256, Digest};
use std::time::{SystemTime, UNIX_EPOCH};

pub struct RustBlock {
    index: u64,
    previous_hash: String,
    timestamp: u64,
    data: String,
    nonce: u64,
}

impl RustBlock {
    pub fn new(index: u64, previous_hash: String, data: String) -> Self {
        let timestamp = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs();
        RustBlock {
            index,
            previous_hash,
            timestamp,
            data,
            nonce: 0,
        }
    }

    pub fn compute_hash(&self) -> String {
        let input = format!(
            "{}{}{}{}{}",
            self.index, self.previous_hash, self.timestamp, self.data, self.nonce
        );
        let mut hasher = Sha256::new();
        hasher.update(input.as_bytes());
        let result = hasher.finalize();
        format!("{:x}", result)
    }
}
