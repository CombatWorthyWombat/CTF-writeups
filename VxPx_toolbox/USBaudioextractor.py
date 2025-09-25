from scapy.all import rdpcap
import wave
import struct


def extract_audio(pcap_file, in_output_file, out_output_file):
    packets = rdpcap(pcap_file)

    in_audio_data = bytearray()
    out_audio_data = bytearray()

    for packet in packets:
        if 'Raw' in packet:
            raw_data = bytes(packet['Raw'])


            if len(raw_data) == 227 and raw_data[8:10] == b'\xff\xff':
                in_audio_data.extend(raw_data[32:])


            elif len(raw_data) == 277 and raw_data[8:10] == b'\xff\xff':
                out_audio_data.extend(raw_data[32:])

    # Create WAV file for IN packets
    with wave.open(in_output_file, 'wb') as wav_file:
        wav_file.setnchannels(2)
        wav_file.setsampwidth(2)
        wav_file.setframerate(48000)
        wav_file.writeframes(in_audio_data)

    # Create WAV file for OUT packets
    with wave.open(out_output_file, 'wb') as wav_file:
        wav_file.setnchannels(2)
        wav_file.setsampwidth(2)
        wav_file.setframerate(48000)
        wav_file.writeframes(out_audio_data)


# paths and use
pcap_file = 'your PCAP path here'
in_output_file = 'input_audio.wav'
out_output_file = 'output_audio.wav'

extract_audio(pcap_file, in_output_file, out_output_file)
print("extraction finished -> input_audio.wav output_audio.wav")
