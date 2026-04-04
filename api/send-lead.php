<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

// Настоящий токен и ID чата скрыты на сервере
$botToken = '8778679367:AAHzAsbzsV34Zt3YRXq4Cbn6W9rLH66n-PI';
$chatId = '5930269100';

// Читаем входящий JSON
$inputRaw = file_get_contents("php://input");
$input = json_decode($inputRaw, true);

if (!$input) {
    echo json_encode(['success' => false, 'error' => 'No data']);
    exit;
}

$text = $input['text'] ?? '';

if (empty($text)) {
    echo json_encode(['success' => false, 'error' => 'Empty text']);
    exit;
}

// Отправляем в Telegram
$url = "https://api.telegram.org/bot{$botToken}/sendMessage";
$data = [
    'chat_id' => $chatId,
    'text' => $text,
];

$options = [
    'http' => [
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query($data),
    ],
];
$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);

if ($result === FALSE) {
    echo json_encode(['success' => false, 'error' => 'Telegram API error']);
} else {
    echo json_encode(['success' => true]);
}
?>
