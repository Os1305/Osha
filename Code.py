# Base class for people in the delivery system
class Person:
    def __init__(self, id, name, phoneNumber, email):
        self.id = id
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email

    # Getter methods
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phoneNumber

    def getEmail(self):
        return self.email

    # Setter methods
    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def setEmail(self, email):
        self.email = email

# Class representing a customer who places delivery orders
class Customer(Person):
    def __init__(self, id, name, phoneNumber, email, address, customerId):
        super().__init__(id, name, phoneNumber, email)
        self.address = address
        self.customerId = customerId

    # Getter methods
    def getAddress(self):
        return self.address

    def getCustomerId(self):
        return self.customerId

    # Setter methods
    def setAddress(self, address):
        self.address = address

    def setCustomerId(self, customerId):
        self.customerId = customerId

    def placeOrder(self):
        pass

# Class representing a delivery staff member
class DeliveryStaff(Person):
    def __init__(self, id, name, phoneNumber, email, staffId, vehicleDetails):
        super().__init__(id, name, phoneNumber, email)
        self.staffId = staffId
        self.vehicleDetails = vehicleDetails
        self.isAvailable = True

    # Getter methods
    def getStaffId(self):
        return self.staffId

    def getVehicleDetails(self):
        return self.vehicleDetails

    def isAvailable(self):
        return self.isAvailable

    # Setter methods
    def setStaffId(self, staffId):
        self.staffId = staffId

    def setVehicleDetails(self, vehicleDetails):
        self.vehicleDetails = vehicleDetails

    def setAvailable(self, available):
        self.isAvailable = available

    def assignDelivery(self, order):
        pass

    def completeDelivery(self, order):
        pass

# Class representing a delivery order
class DeliveryOrder:
    def __init__(self, orderId, pickupAddress, deliveryAddress, orderDate, packageDetails):
        self.orderId = orderId
        self.pickupAddress = pickupAddress
        self.deliveryAddress = deliveryAddress
        self.orderDate = orderDate
        self.status = "Pending"
        self.deliveryFee = 0.0
        self.packageDetails = packageDetails

    # Getter methods
    def getOrderId(self):
        return self.orderId

    def getPickupAddress(self):
        return self.pickupAddress

    def getDeliveryAddress(self):
        return self.deliveryAddress

    def getOrderDate(self):
        return self.orderDate

    def getStatus(self):
        return self.status

    def getDeliveryFee(self):
        return self.deliveryFee

    def getPackageDetails(self):
        return self.packageDetails

    # Setter methods
    def setOrderId(self, orderId):
        self.orderId = orderId

    def setPickupAddress(self, pickupAddress):
        self.pickupAddress = pickupAddress

    def setDeliveryAddress(self, deliveryAddress):
        self.deliveryAddress = deliveryAddress

    def setOrderDate(self, orderDate):
        self.orderDate = orderDate

    def setStatus(self, status):
        self.status = status

    def setDeliveryFee(self, deliveryFee):
        self.deliveryFee = deliveryFee

    def setPackageDetails(self, packageDetails):
        self.packageDetails = packageDetails

    def calculateDeliveryFee(self):
        pass

#Class representing a delivery note document
class DeliveryNote:
    def __init__(self, noteId, generatedDate):
        self.noteId = noteId
        self.generatedDate = generatedDate
        self.signatureRequired = "Yes"
        self.specialInstructions = ""

    # Getter methods
    def getNoteId(self):
        return self.noteId

    def getGeneratedDate(self):
        return self.generatedDate

    def getSignatureRequired(self):
        return self.signatureRequired

    def getSpecialInstructions(self):
        return self.specialInstructions

    # Setter methods
    def setNoteId(self, noteId):
        self.noteId = noteId

    def setGeneratedDate(self, generatedDate):
        self.generatedDate = generatedDate

    def setSignatureRequired(self, required):
        self.signatureRequired = required

    def setSpecialInstructions(self, instructions):
        self.specialInstructions = instructions

    def printDeliveryNote(self):
        pass

# Class for handling payment for delivery orders
class Payment:
    # Initialize a Payment object
    def __init__(self, paymentId, amount, paymentMethod):
        self.paymentId = paymentId
        self.amount = amount
        self.paymentMethod = paymentMethod
        self.paymentStatus = "Pending"

    # Getter methods
    def getPaymentId(self):
        return self.paymentId

    def getAmount(self):
        return self.amount

    def getPaymentMethod(self):
        return self.paymentMethod

    def getPaymentStatus(self):
        return self.paymentStatus

    # Setter methods
    def setPaymentId(self, paymentId):
        self.paymentId = paymentId

    def setAmount(self, amount):
        self.amount = amount

    def setPaymentMethod(self, method):
        self.paymentMethod = method

    def setPaymentStatus(self, status):
        self.paymentStatus = status

    def processPayment(self):
        pass


def generateSampleDeliveryNote():
    # Create a customer
    customer = Customer(
        id=1,
        name="John Smith",
        phoneNumber="555-123-4567",
        email="john.smith@example.com",
        address="123 Main St, Anytown, AN 12345",
        customerId="CUST1001"
    )

    # Create a delivery order
    order = DeliveryOrder(
        orderId=5001,
        pickupAddress="456 Warehouse Ave, Anytown, AN 12346",
        deliveryAddress="789 Residential Blvd, Anytown, AN 12347",
        orderDate="2025-02-26",
        packageDetails="1 Large Box, Electronics, Fragile"
    )

    # Set delivery fee
    order.setDeliveryFee(15.99)

    # Create a delivery staff
    staff = DeliveryStaff(
        id=2,
        name="Michael Johnson",
        phoneNumber="555-987-6543",
        email="michael.j@deliveryco.com",
        staffId="STAFF301",
        vehicleDetails="White Van - License: XYZ-123"
    )

    # Create a delivery note
    note = DeliveryNote(
        noteId=7001,
        generatedDate="2025-02-26"
    )

    # Set special instructions
    note.setSpecialInstructions("Please leave at front door if no answer")

    # Display the delivery note information
    print("=" * 50)
    print("DELIVERY NOTE")
    print("=" * 50)
    print("Note ID:", note.getNoteId())
    print("Date:", note.getGeneratedDate())
    print("-" * 50)
    print("CUSTOMER INFORMATION:")
    print("Name:", customer.getName())
    print("Phone:", customer.getPhoneNumber())
    print("Email:", customer.getEmail())
    print("-" * 50)
    print("ORDER DETAILS:")
    print("Order ID:", order.getOrderId())
    print("Order Date:", order.getOrderDate())
    print("Pickup Address:", order.getPickupAddress())
    print("Delivery Address:", order.getDeliveryAddress())
    print("Package Details:", order.getPackageDetails())
    print("Delivery Fee: $", order.getDeliveryFee())
    print("-" * 50)
    print("DELIVERY STAFF:")
    print("Name:", staff.getName())
    print("Contact:", staff.getPhoneNumber())
    print("Vehicle:", staff.getVehicleDetails())
    print("-" * 50)
    print("Signature Required:", note.getSignatureRequired())
    print("Special Instructions:", note.getSpecialInstructions())
    print("=" * 50)


# Call the function to generate and display a sample delivery note
if __name__ == "__main__":
    generateSampleDeliveryNote()