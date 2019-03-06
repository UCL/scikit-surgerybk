
def test_TestServer(setup_server, bk_medical_data_source_worker, socket_var):
    test_message = 'Test message'
    sent_message = bk_medical_data_source_worker.generate_command_message(test_message)
    bk_medical_data_source_worker.connect_to_host(address=socket_var["TCP_IP"],
                                                  port=socket_var["TCP_PORT"])
    sentOK = bk_medical_data_source_worker.send_command_message(
                                           message=test_message)

    assert sentOK == True
    receiveOK = bk_medical_data_source_worker.receive_response_message(
                                  expected_size=len(sent_message))
    assert receiveOK == True
    print("Received data in test: {:} \n".format(
             bk_medical_data_source_worker.data))
    assert bk_medical_data_source_worker.data.decode() == sent_message

def test_stop_streaming(setup_server, bk_medical_data_source_worker, socket_var):
    bk_medical_data_source_worker.connect_to_host(address=socket_var["TCP_IP"],
                                                  port=socket_var["TCP_PORT"])
    bk_medical_data_source_worker.stop_streaming()
    assert bk_medical_data_source_worker.is_streaming == False
    assert bk_medical_data_source_worker.request_stop_streaming == False
    print("Received data in test: {:} \n".format(
             bk_medical_data_source_worker.data))

def test_start_streaming(setup_server, bk_medical_data_source_worker, socket_var):
    bk_medical_data_source_worker.connect_to_host(address=socket_var["TCP_IP"],
                                                  port=socket_var["TCP_PORT"])
    bk_medical_data_source_worker.start_streaming()
    assert bk_medical_data_source_worker.is_streaming == True
    assert bk_medical_data_source_worker.request_stop_streaming == False
    print("Received data in test: {:} \n".format(
             bk_medical_data_source_worker.data))

def test_request_stop(setup_server, bk_medical_data_source_worker, socket_var):
    bk_medical_data_source_worker.connect_to_host(address=socket_var["TCP_IP"],
                                                  port=socket_var["TCP_PORT"])
    bk_medical_data_source_worker.request_stop()
    assert bk_medical_data_source_worker.request_stop_streaming == True
