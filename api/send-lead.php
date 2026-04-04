<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

// Загружаем конфиг с ключами
$configPath = __DIR__ . '/config.php';
if (!file_exists($configPath)) {
    echo json_encode(['success' => false, 'error' => 'Server configuration error']);
    exit;
}
$config = require $configPath;
$botToken = $config['bot_token'];
$chatId = $config['chat_id'];

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
