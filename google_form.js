function onSubmit(e) {
  const payload = {
    timestamp: new Date().toISOString(),
    responses: e.namedValues
  };

  const options = {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };

  const webhookUrl = "SAMPLE_ENDPOINT"; 
  const response = UrlFetchApp.fetch(webhookUrl, options);

  if (response.getResponseCode() !== 200) {
    console.error("Error:", response.getContentText());
  }
}