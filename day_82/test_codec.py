from morse_converter import encode_to_morse, decode_from_morse

def test_morse_encoder_decoder_consistency():
    test_sentence="Hello world, this is a test."
    _, codes = encode_to_morse(test_sentence)
    _, decoded_sentence = decode_from_morse(codes)
    assert test_sentence.lower() == decoded_sentence.lower()

